# Jupyter notebooks
{id: jupyter}


## Jupyter on Windows
{id: run-jupyter-windows}


On Windows install [Anaconda](https://www.anaconda.com/distribution/)
and then you'll be able to run Jupyter notebook from the start menu.


Alternatively:

```
pip install jupyter
```

## Jupyter on Linux and OSX
{id: run-jupyter-linux}

Install

For Linux and OSX I recommend using **virtualenv** and installing with **pip**.

```
virtualenv -p python3 ~/venv3
source ~/venv3/bin/activate
pip install jupyter
```

Run

```
cd examples/jupyter/
jupyter notebook
```

* Your browser should open. If not, there is a link in the terminal.


## Jupyter add
{id: jupyter-simple-add}


* Open an existing notebook (ipynb file). e.g examples/jupyter/add.ipynb
* Create new notebook.
* File - Save As
* ...
* Quit - shut down the notebook server.



```
def add(x, y):
    return x+y

add(2,3)
```


## Planets
{id: planets-csv}

![](examples/jupyter/planets.csv)


## Jupyter StackOverflow
{id: jupyter-stackoverflow}

* Download the latest dataset from the [survey](https://insights.stackoverflow.com/survey).
* unzip the file. Feel free to remove the __MACOSX/ directory.

![](examples/jupyter/stack_overflow.py)


## Jupyter notebook Intellisense (TAB completition)
{id: jupyter-notebook-intellisense}


```
%config IPCompleter.greedy=True
```


## Jupyter examples
{id: jupyter-examples}


```

examples/jupyter/planets.csv

examples/jupyter/planets.ipynb

examples/jupyter/numpy_matrix.ipynb

examples/jupyter/seaborn_tips.ipynb
```

## IPy Widgets
{id: ipywidgets}
{i: ipywidgets}

* [Interact](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)
* [Widget list](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html)

## Genes using Jupyter
{id: genes-using-jupyter}

```
cd examples/pandas/
jupyter notebook genes.ipynb
```


