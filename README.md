# Collections as Data

This repository hosts Python code for downloading and analyzing scanned OCR text from Arizona newspapers. The work is part of the project _Using Newspapers as Data for Collaborative Pedagogy: A Multidisciplinary Interrogation of the Borderlands in Undergraduate Classrooms_, funded in part by the Mellon Foundation through the [Collections as Data](https://collectionsasdata.github.io/part2whole/) program.

## The work focuses on the following titles:
+ Arizona Sun, an African American newspaper published in Phoenix
+ Apache Sentinel, published by African American soldiers stationed at Fort Huachuca
+ Bisbee Daily Review, a newspaper published in Bisbee, a mining town at that time
+ Border Vidette, a newspaper published in Nogales, Arizona, on the border with Nogales, Mexico
+ Phoenix Tribune, the first African American newspaper published in Arizona
+ El Sol, a Spanish-language, Mexican American newspaper published in Phoenix
+ El Tucsonense, a Spanish-language, Mexican American newspaper published in Tucson

The text for these newspapers is available at [Chronicling America](https://chroniclingamerica.loc.gov/newspapers/). Downloads of the texts used the API, documented at [https://chroniclingamerica.loc.gov/about/api/](https://chroniclingamerica.loc.gov/about/api/).

## Data preparation
1. Titles and associated metadata are found in data/titles.csv
2. Text files of individual pages are downloaded via download-pages.py. Pages are downloaded to a folder called 'pages' in the data folder for the appropriate title. For example, pages for _El Tucsonense_ are downloaded to 'data/el-tucsonense/pages'. File names reflect the date, in YYYYMMDD, and the page number; e.g. page 2 of _El Tucsonense_'s paper from January 3, 1925 is stored as 19250103-2.txt.
3. Volumes, i.e. a single day's newspaper, are assembled into a single text file from pages by assemble-volumes.py. The text for each day's paper is stored in the 'volumes' folder for each title. The text for the January 3, 1925 issue of _El Tucsonense_ is located in data/el-tucsonense/volumes/19250103.txt.

## Pressure points
+ Installing additional packages for Python may require some finesse. This depends largely on how `pip` is installed on your machine. For example, if things are as they should be, the NLTK for Python package can be installed via `pip install nltk`. If, however, this results in an error, it is likely due to a non-standard `pip` installation (see [https://github.com/pypa/pip/issues/5599](https://github.com/pypa/pip/issues/5599) for a lengthy discussion on `pip` and possible debugging solutions). The workaround is to instead use `python -m pip install nltk`.
+ When preparing to use the NLTK for Python, the corpora with stopwords needs to be downloaded only once. That is, the script setup.py need be run only once.