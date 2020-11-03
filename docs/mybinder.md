# Running notebooks on MyBinder

## Kernel dies on file download in Text-Mining-Template

As of 2020-10-20, kernel dies when trying to download the archive from the
UA data repository. Memory (2048) maxes out and kernel dies. Confirmed that
this notebook worked fine as recently at 2020-10-15

Possible issues:

1. Something changed on UA repository when it "went live" ca. 2020-10-19
    + Test by downloading file from somewhere else (of similar size) (same as
      test for 2)
2. Got lucky on early tries and had more RAM to play with on MyBinder
    + Test by attempting to download a similar-sized file.
    + A 1.2 GB file on Zenodo: https://zenodo.org/record/2597595/files/bio_answerfinder_data.zip?download=1
    + Result: **kernel died as RAM maxed out**
3. Unknown

## Try alternatives to MyBinder

+ https://notebooks.gesis.org/binder/ Seems to work. RAM is much higher (8GB),
    and notebook
+ Google Colaboratory is another option, although it has a different interface
    than standard Jupyter Notebooks https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb