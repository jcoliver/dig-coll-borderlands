# Collections as Data

This repository hosts Python code for downloading and analyzing scanned OCR text from a collection of southwestern U.S. borderlands newspapers. It also includes Jupyter Notebooks introducing text data mining with Python on the newspaper collection. The work is part of the project _Using Newspapers as Data for Collaborative Pedagogy: A Multidisciplinary Interrogation of the Borderlands in Undergraduate Classrooms_, funded in part by the Mellon Foundation through the [Collections as Data](https://collectionsasdata.github.io/part2whole/) program. More information about the project is available found at [https://libguides.library.arizona.edu/newspapers-as-data](https://libguides.library.arizona.edu/newspapers-as-data).

If you are looking for an introduction explaining the concept of text data mining, check out the StoryMap at [https://storymaps.arcgis.com/stories/cd7e273c42cd4ab6b6ce3fa89c13132c](https://storymaps.arcgis.com/stories/cd7e273c42cd4ab6b6ce3fa89c13132c).

## The work focuses on the following titles:
+ _Arizona Post_, a Tucson newspaper by and for the Jewish community
+ _Arizona Sun_, an African American newspaper published in Phoenix
+ _Apache Sentinel_, published by African American soldiers stationed at Fort Huachuca
+ _Bisbee Daily Review_, a newspaper published in Bisbee, a mining town at that time
+ _Border Vidette_, a newspaper published in Nogales, Arizona, on the border with Nogales, Mexico
+ _Phoenix Tribune_, the first African American newspaper published in Arizona
+ _El Sol_, a Spanish-language, Mexican American newspaper published in Phoenix
+ _El Tucsonense_, a Spanish-language, Mexican American newspaper published in Tucson

The text for these newspapers is available at [Chronicling America](https://chroniclingamerica.loc.gov/newspapers/). Downloads of the texts used the API, documented at [https://chroniclingamerica.loc.gov/about/api/](https://chroniclingamerica.loc.gov/about/api/).

## Text data mining lessons
Lessons for using these data in text data mining are available in Jupyter Notebooks:

| Name | Launch | Description |
|:-----|:------:|:------------|
| Introduction to text mining (short) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jcoliver/dig-coll-borderlands/master?filepath=Text-Mining-Short.ipynb) | A brief lesson introducing relative word frequencies and visual display of word use over time. Includes a subset of the titles (three) for the three year period 1917-1919. |
| Introduction to text mining (long)  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jcoliver/dig-coll-borderlands/master?filepath=Text-Mining-Long.ipynb) | An extended version of the short lesson, above. Time to complete the lesson is approximately two hours |
| Text mining template | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jcoliver/dig-coll-borderlands/master?filepath=Text-Mining-Template.ipynb) | A relatively lightweight notebook to explore text mining analyses on the full data set of eight titles. |

## Data preparation scripts
1. download-pages.py: Download files via the Chronicling America API. Pages are in the "pages" folder within an individual title's folder. For example, pages for _El Tucsonense_ are downloaded to 'el-tucsonense/pages'. File names reflect the date, in YYYYMMDD, and the page number; e.g. page 2 of _El Tucsonense_'s paper from January 3, 1925 is stored as 19250103-2.txt.
2. assemble-volumes.py: Assemble text file for a single day's newspaper by concatenating all individual pages for a particular day/title combination. The text for each day's paper is stored in the 'volumes' folder for each title. For example, the text for the January 3, 1925 issue of _El Tucsonense_ is located in data/el-tucsonense/volumes/19250103.txt.
3. retrieve-complete.py and retrieve-complete.sh: Python and bash scripts for downloading full data set from the University of Arizona Research Data Repository. These scripts download the archive file from the data repository and extract the contents to data/complete. Both scripts accomplish the same thing, they differ only in language used.