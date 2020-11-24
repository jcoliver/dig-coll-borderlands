# Additional data from CONTENTdm

There are additional data for _El Tucsonense_ hosted on the library's CONTENTdm
site. Specifically at

https://content.library.arizona.edu/digital/collection/p16127coll3/search
or
https://content.library.arizona.edu/digital/collection/p16127coll3

There is an API for CONTENTdm, although still working out functionality. Some
documentation can be found at https://www.oclc.org/support/services/contentdm/help/customizing-website-help/other-customizations/contentdm-api-reference.en.html

Several references include specifying a port, but then this page https://help.oclc.org/Metadata_Services/CONTENTdm/Advanced_website_customization/API_Reference/CONTENTdm_API
has the following example:

https://sandbox.contentdm.oclc.org/digital/bl/dmwebservices/index.php?q=dmGetCollectionList/json

Applying this to UAL:

https://content.library.arizona.edu/digital/bl/dmwebservices/index.php?q=dmGetCollectionList/json

This works. We see the collection list

## Let's try to get the collection. From API documentation:

http://CdmServer.com:port/dmwebservices/index.php?q=dmGetCollectionArchivalInfo/alias/format

    alias is a collection alias
    format is either xml or json

The collection alias is p16127coll3 (theoretically), so for JSON format:
https://content.library.arizona.edu/digital/bl/dmwebservices/index.php?q=dmGetCollectionArchivalInfo/p16127coll3/json
Hmm...nothing there. Tried for another alias ("asd"), but also got no results.

The collection level query
https://content.library.arizona.edu/digital/bl/dmwebservices/index.php?q=dmGetCollectionFieldInfo/p16127coll3/json

Returns a JSON, but all the fields are empty or "blank"

## Try an item-level query

https://content.library.arizona.edu/digital/bl/dmwebservices/index.php?q=dmGetItemInfo/alias/pointer/format
+ alias is a collection alias
+ pointer is the pointer to the item for which you want metadata
+ format is either xml or json

https://content.library.arizona.edu/digital/bl/dmwebservices/index.php?q=dmGetItemInfo/p16127coll3/23622/json
This _did_ work.

What about asking if there is OCR text?
https://content.library.arizona.edu/digital/bl/dmwebservices/index.php?q=dmItemHasOCRText/p16127coll3/23622/json
Works, but returns false.

## There is also a separate set of four API options, including a getfile:

/utils/getfile/collection/alias/id/pointer/filename/name
+ alias is the collection alias
+ pointer is the pointer to the item in the collection
+ name is the file name to use when saving the file

https://content.library.arizona.edu/utils/getfile/collection/p16127coll3/id/23622/filename/testpage.xml

That gave an XML which listed all pages for that day. Maybe the pageptr field is useful?
<?xml version="1.0"?>
<cpd>
  <type>Document</type>
  <page>
    <pagetitle>Page 1</pagetitle>
    <pagefile>23617.jp2</pagefile>
    <pageptr>23616</pageptr>
  </page>
  ...
</cpd>

https://content.library.arizona.edu/utils/getfile/collection/p16127coll3/id/23616/filename/testpage.xml

This is an XML (4 MB), which might be the image. If not, funky encoding.

## Aha! We can get a json with the text in a field "fullte" with
https://content.library.arizona.edu/digital/bl/dmwebservices/index.php?q=dmGetItemInfo/p16127coll3/23616/json

It is that "23616" id that I pulled out of the XML from the GetFile call.

But how do we get a list of all those pages (or at least the item id for each day)? Inquiry sent to OCLC 2020-09-23.

## Try dmQuery?

http://CdmServer.com:port/dmwebservices/index.php?q=dmQuery/alias/searchstrings/fields/sortby/maxrecs/start/suppress/docptr/suggest/facets/showunpub/denormalizeFacets/format

Try:

alias : p16127coll3
searchstrings : 0
fields : identi!title
sortby : identi
maxrecs : 1024
start : 1
suppress : 1
docptr :
suggest : 0
facets : 0
showunpub : 0
denormalizeFacets : 1
format : json

https://content.library.arizona.edu/digital/bl/dmwebservices/index.php?q=dmQuery/p16127coll3/0/identi!title/identi/1024/1/1//0/0/0/1/json

This works. 1024 records (0-1023, out of a total of 3679) are returned in a json with two top-level elements, pager and records:

+ pager
    + start "1"
    + maxrecs "1024"
    + total 3679
+ records
    + 0
        + collection "/p16127coll3"
        + pointer 6237
        + filetype "cpd"
        + parentobject -1
        + identi "sn95060694"
        + title "El Tucsonense, 1952-08-08"
        + find "6238.cpd"
    + 1
        + collection "/p16127coll3"
        + pointer 6621
        + filetype "cpd"
        + parentobject -1
        + identi "sn95060694"
        + title "El Tucsonense, 1953-04-21"
        + find "6622.cpd"

Taking the first value from the pointer element, we can try to get the item info:

https://content.library.arizona.edu/digital/bl/dmwebservices/index.php?q=dmGetItemInfo/p16127coll3/6237/json

But these are records for an individual day's paper (not individual pages).

The getfile utility provides a list of all pages:
https://content.library.arizona.edu/utils/getfile/collection/p16127coll3/id/6237/filename/testpage.xml

<cpd>
  <type>Document</type>
    <page>
      <pagetitle>Page 1</pagetitle>
      <pagefile>6234.jp2</pagefile>
      <pageptr>6233</pageptr>
    </page>
    <page>
        ....
    </page>
</cpd>

And from there, there are four pages, with pageptr values 6233-6236. We can then get text for page 1 via:

https://content.library.arizona.edu/digital/bl/dmwebservices/index.php?q=dmGetItemInfo/p16127coll3/6233/json

So, we would need to
+ first get the total number of items (a day's paper) in the collection.
+ run a series of queries to get the pointer values for all the records