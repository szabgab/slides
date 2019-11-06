# Getting Started with Data Science for non-programmers
{id: index}

## Data Science
{id: data-science}

![Data Science](img/data-science.png)

* [source](https://towardsdatascience.com/introduction-to-statistics-e9d72d818745)

## Main subjects
{id: main-subjects}

* Data Analyzis
* Data Science
* Machine Learning
* Deep Learning
* AI (Artificial Intelligence)
* Big Data

## Self introduction
{id: self-introduction}

* [Gábor Szabó](https://www.linkedin.com/in/szabgab/) @szabgab
* Helps organizations improve their development by creating faster feedback loops

* [Training courses](https://hostlocal.com/)
* [Code Maven Workshops](https://workshops.code-maven.com/)

* [Code Maven in English](https://code-maven.com/)
* [Code Maven in Hebrew](https://he.code-maven.com/)

* [Code Mavens Meetup group](https://www.meetup.com/Code-Mavens/)


## Overview of this material
{id: overview}

* Install Tools (Python, Jupyter Notebook, NumPy, Pandas, Matplotlib, and Seaborn).
* **Data Source:** Read in some CSV file (and maybe also a JSON file).
* Make some simple filtering and transformation on the data.
* Create some simple graphs.
* Create some understanding of the data.

## Tools
{id: tools}

* [Anaconda distribution](https://www.anaconda.com/distribution/)

* [Python](https://www.python.org/)
* [Jupyter notebook](https://jupyter.org/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)

## Visualization
{id: visualization}

* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Plotly](https://plot.ly/)
* [Bokeh](https://docs.bokeh.org/)

## Install Python on Windows
{id: install-python-windows}

* [Anaconda](https://www.anaconda.com/distribution/)
* Download, install, accept the defaults (except: add Anaconda to PATH)

## Install Python on Linux
{id: install-python-linux}

Use the terminal

```
$ which python3

$ sudo apt-get install python3
$ sudo yum install python3

$ sudo apt-get install virtualenv
$ sudo yum install virtualenv
```

## Install Python Mac OSX
{id: install-python-mac-osx}

Use the terminal.

Install [Homebrew](https://brew.sh/) if you don't have it yet.

```
$ which python3

$ brew install python3
$ brew install virtualenv
```

## Install Jupyter notebook and Python modules on Linux and OSX
{id: install-jupyter}

```
$ virtualenv -p python3 ~/venv3
$ source ~/venv3/bin/activate
$ pip install jupyter pandas seaborn
```

## Install Python modules on Windows (Anaconda)
{id: install-in-anaconda}

* Open the "Anaconda Prompt"
* Type in `conda list seaborn` to see if seaborn is already installed
* (it will show something like this, if it is installed):

```
# packages in environment at C:\ProgramData\Anaconda3:
#
# Name                    Version                   Build  Channel
seaborn                   0.9.0                    py37_0
```

* Install `seaborn` by typing `conda install seaborn`

* If all else fails you can also try `pip install seaborn`


## Start Jupyter notebook
{id: start-jupyter-notebook}

* Windows: Anaconda Jupyter notebook
* Linux, OSX: `$ jupyter notebook`

## Reading CSV file (Planets)
{id: planets}

* [planets.csv](https://github.com/szabgab/slides/blob/main/python/examples/jupyter/planets.csv)
* [planets.ipynb](https://github.com/szabgab/slides/blob/main/python/examples/jupyter/planets.ipynb)

## Exercise 1
{id: exercise-1}

* Download the planets.csv file and follow the steps above

* Download another CSV file and analyze that.
    * [UN](http://data.un.org/)

## Seaborn
{id: seaborn}

* [examples/seaborn_tips.ipynb](https://github.com/szabgab/slides/blob/main/python/examples/jupyter/seaborn_tips.ipynb)

![](examples/seaborn/tips.py)


## Temperatures
{id: temperatures}

* [temperatures.csv](https://github.com/szabgab/slides/blob/main/python/examples/jupyter/temperatures.csv)
* [temperatures.ipynb](https://github.com/szabgab/slides/blob/main/python/examples/jupyter/temperatures.ipynb)


## Stack Overflow survey
{id: stack-overflow}

* [Stack Overflow survey](https://insights.stackoverflow.com/survey)
* [so.ipynb](https://github.com/szabgab/slides/blob/main/python/examples/jupyter/SO/so.ipynb)
* selected-columns.ipynb
* selected-rows.ipynb
* show.ipynb


## Other Materials
{id: other-materials}

* [DataCamp](https://www.datacamp.com/)
* [Machine Learning at Coursera](https://www.coursera.org/learn/machine-learning)
* [Machine Learning in Hebrew](https://machinelearning.co.il/581/machine-learning-beginners-guide/)
* [Books](https://machinelearning.co.il/306/machinelearningbooks/)
* [Courses](https://machinelearning.co.il/102/machinelearningcourses/)
* [Tips about courses](https://machinelearning.co.il/2424/4coursetips/)
* [On Facebook](https://www.facebook.com/groups/543283492502370/permalink/989056861258362/)

## Data Sources (Competitions)
{id: data-sources}

* [Kaggle](https://www.kaggle.com/)
* [Driven Data](https://www.drivendata.org/)
* [CrowdAnalytix community](https://www.crowdanalytix.com/community)
* [InnoCentive](https://www.innocentive.com/our-solvers/)
* [TunedIT](http://tunedit.org/challenges)
* [CodaLab](https://competitions.codalab.org/)
* [Anlytics Vidhya](https://datahack.analyticsvidhya.com/)
* [CorwdAI](https://www.crowdai.org/challenges)
* [NumerAI](https://numer.ai/)

* [Source](https://towardsdatascience.com/top-competitive-data-science-platforms-other-than-kaggle-2995e9dad93c)

## Thank You
{id: thank-you}

* [Gábor Szabó on LinkedIn](https://www.linkedin.com/in/szabgab/) @szabgab

* [Training courses](https://hostlocal.com/)
* [Code Maven Workshops](https://workshops.code-maven.com/)

* [Code Mavens Meetup group](https://www.meetup.com/Code-Mavens/)

