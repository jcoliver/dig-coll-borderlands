# Collections as Data
## Planning for python lessons

An example question of what a disciplinary scholar would be interested in doing in the classroom: I would like to track the difference in sentiment for the month prior and the month after the Bisbee deportation that occurred on July 12, 1917. i.e. sentiment analysis for June 1917, July 1917, and August 1917. Do this for 2+ newspapers and draw comparisons. Do sentiment analysis, word frequency analysis, and most specialized words.

Data will come from UAL Special Collections OCR of borderlands newspapers, focusing on two timeframes:

+ 1915-1922
    + El Tucsonense, a Spanish-language, Mexican American newspaper published in Tucson
    + Bisbee Daily Review, a newspaper published in Bisbee, a mining town at that time
    + Border Vidette, a newspaper published in Nogales, Arizona, on the border with Nogales, Mexico
    + Phoenix Tribune, the first African American newspaper published in Arizona
+ 1941-1959
    + El Tucsonense, a Spanish-language, Mexican American newspaper published in Tucson
    + El Sol, a Spanish-language, Mexican American newspaper published in Phoenix
    + Arizona Sun, an African American newspaper published in Phoenix
    + Apache Sentinel, published by African American soldiers stationed at Fort Huachuca

The Spanish language titles are largely available at [http://www.library.arizona.edu/contentdm/mmap/](http://www.library.arizona.edu/contentdm/mmap/). However downloading text is a bit cumbersome. As individual pages of issues are shown, and only PDFs are available for download (not text).

English language titles are hosted by [Chronicling America](https://chroniclingamerica.loc.gov/newspapers/).
2016-04-05 of _Bisbee Daily Review_ is at [https://chroniclingamerica.loc.gov/lccn/sn84024827/1916-04-05/ed-1/seq-4/ocr/](https://chroniclingamerica.loc.gov/lccn/sn84024827/1916-04-05/ed-1/seq-4/ocr/). A text file should be available at [https://chroniclingamerica.loc.gov/lccn/sn84024827/1916-04-05/ed-1/seq-4/ocr.txt](https://chroniclingamerica.loc.gov/lccn/sn84024827/1916-04-05/ed-1/seq-4/ocr.txt), but as of 2019-10-15, this was unavailable (as was the XML version). A copy of the text is saved in data/bisbee-daily-review.

## Pressure points
+ Getting data in computable format. If APIs are out there it would make things a lot easier.
+ Installing NLTK for python is a little screwy.
+ Downloading stopwords from NLTK may require some attention

**Note** installing the natural language toolkit (nltk) for python took a little wrangling, most likely due to incorrect installation of pip. To get it installed, use:

`python -m pip install nltk`

from the terminal. nltk documentation suggests `pip install nltk`, but this throws an error "ImportError: cannot import name 'main'". See [https://github.com/pypa/pip/issues/5599](https://github.com/pypa/pip/issues/5599) for discussion and debugging.