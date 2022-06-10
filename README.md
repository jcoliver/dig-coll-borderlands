# Borderlands newspaper data mining

This repository hosts Jupyter Notebooks introducing text data mining with 
Python on the newspaper collection. The work is part two projects:

+ _Using Newspapers as Data for Collaborative Pedagogy: A Multidisciplinary 
Interrogation of the Borderlands in Undergraduate Classrooms_, funded in part 
by the Mellon Foundation through the 
[Collections as Data](https://collectionsasdata.github.io/part2whole/) program. 
More information about the project is available found at 
[https://libguides.library.arizona.edu/newspapers-as-data](https://libguides.library.arizona.edu/newspapers-as-data).
+ _Reporting on Race and Ethnicity in the Borderlands (1882-1924): A 
Data-Driven Digital Storytelling Hub_, funded by the Mellon Foundation through 
the [Digital Borderlands](http://borderlands.digitalscholarship.library.arizona.edu/)
program.

If you are looking for an introduction explaining the concept of text data 
mining, check out the StoryMap at [https://storymaps.arcgis.com/stories/cd7e273c42cd4ab6b6ce3fa89c13132c](https://storymaps.arcgis.com/stories/cd7e273c42cd4ab6b6ce3fa89c13132c).

The scripts responsible for downloading and assembling daily volumes are 
available in a separate repository, at 
[https://github.com/jcoliver/borderlands-newspapers](https://github.com/jcoliver/borderlands-newspapers).

## The work focuses on the following titles:
+ _Arizona Citizen_, one of Arizona's earliest newspapers, published in Tucson
+ _Arizona Post_, a Tucson newspaper by and for the Jewish community
+ _Arizona Sun_, an African American newspaper published in Phoenix
+ _Apache Sentinel_, published by African American soldiers stationed at Fort 
Huachuca
+ _Bisbee Daily Review_, a newspaper published in Bisbee, a mining town at that 
time
+ _Border Vidette_, a newspaper published in Nogales, Arizona, on the border 
with Nogales, Mexico
+ _Phoenix Tribune_, the first African American newspaper published in Arizona
+ _El Fronterizo_, a weekly Tucson Spanish-language paper
+ _El Mosquito_, a Tucson paper including local news and news from Mexico
+ _El Sol_, a Spanish-language, Mexican American newspaper published in Phoenix
+ _El Tucsonense_, a Spanish-language, Mexican American newspaper published in 
Tucson
+ _The Daily Morning Oasis_, a daily English paper from Nogales, Arizona
+ _The Oasis_, an English-language paper published in Nogales, Arizona
+ _The Weekly Orb_, a weekly paper from Bisbee, Arizona
+ _Tucson Citizen_, a continuation of the Tucson newspaper, _Arizona Citizen_

The text for most of these newspapers is available at 
[Chronicling America](https://chroniclingamerica.loc.gov/newspapers/). 
Downloads of the texts used the API, documented at 
[https://chroniclingamerica.loc.gov/about/api/](https://chroniclingamerica.loc.gov/about/api/).
The entire data set is available from the UArizona Research Data Repository at
[https://doi.org/10.25422/azu.data.12735992.v3](https://doi.org/10.25422/azu.data.12735992.v3).

## Text data mining lessons
Lessons for using these data in text data mining are available in Jupyter 
Notebooks. All lessons are licensed under a 
[CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/legalcode) 2020 
by Jeffrey C. Oliver.

| Name | Launch | Description |
|:-----|:------:|:------------|
| Introduction to text mining (short) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jcoliver/dig-coll-borderlands/main?filepath=Text-Mining-Short.ipynb) | A brief lesson introducing relative word frequencies and visual display of word use over time. Includes a subset of the titles (three) for the three year period 1917-1919. |
| Introduction to text mining (long)  | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jcoliver/dig-coll-borderlands/main?filepath=Text-Mining-Long.ipynb) | An extended version of the short lesson, above. Time to complete the lesson is approximately two hours |
| Text mining template | [![Binder](https://notebooks.gesis.org/binder/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/jcoliver/dig-coll-borderlands/main?filepath=Text-Mining-Template.ipynb) | A relatively lightweight notebook to explore text mining analyses on the full data set of eight titles. |
