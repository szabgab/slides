# Jupyter notebooks
{id: jupyter}

## What is Jupyter Notebook?
{id: what-is-jupyter}

* [Jupyter](https://jupyter.org/)

* A web-based interactive development environment

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

## Jupyter New notebook
{id: jupyter-new-notebook}

* Create new notebook (New / Python 3)
* It is called "Untitled" - Rename it
* Type in some code `x = 2`
* Modes: Blue - command mode, Green - edit mode
* Enter - Switch to edit mode (or newline if already in edit mode)
* ESC - Switch to command mode
* Ctrl-Enter - excuted current code
* Clear Cell data before saving
* Button h for help
* Buttons A, B
* ...
* Quit - shut down the notebook server.

## Jupyter Notebook file format
{id: jupyter-notebook-file-format}

* Jupyter file format (show the file) JSON
* Download file as Python (.py)

## Jupyter notebook Intellisense (TAB completition)
{id: jupyter-notebook-intellisense}

* Just press TAB


## Jupyter add
{id: jupyter-simple-add}

* Open an existing notebook: `examples/jupyter/add.ipynb`


## Planets
{id: planets-csv}

* The Planets example we saw in the Pandas chapter

* `examples/jupyter/planets.csv`
* `examples/jupyter/planets.ipynb`


## Jupyter StackOverflow
{id: jupyter-stackoverflow}

* Download a dataset from the [Stack Overflow survey](https://insights.stackoverflow.com/survey).
* unzip the file. Feel free to remove the `__MACOSX/` directory if it is included.

* `examples/jupyter/SO/so.ipynb`
* `examples/jupyter/SO/selected-rows.ipynb`
* `examples/jupyter/SO/selected-columns.ipynb`



## Use SciPy image
{id: use-scipy-image}

* `scipy_image.ipynb`

## Create Random image
{id: create-random-image}

* `create_random_image.ipynb`

## Load image using OpenCV
{id: load-image-using-opencv}

* [opencv](https://opencv.org/)
* [opencv-python](https://pypi.org/project/opencv-python/)

* `load_image_using_opencv`

## IPy Widgets
{id: ipywidgets}
{i: ipywidgets}

* [Interact](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)
* [Widget list](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html)

* `ipywidgets.ipynb`

## Genes using Jupyter
{id: genes-using-jupyter}

```
jupyter notebook genes.ipynb
```

## Jupyter Notebook and Markdown
{id: jupyter-notebook-markdown}

* `markdown.ipynb`
* [Jupyter Markdown](https://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Working%20With%20Markdown%20Cells.html(
* [Original Markdown](https://daringfireball.net/projects/markdown/syntax)
* [Markdown](https://en.wikipedia.org/wiki/Markdown)

## Latex in Jupyter Notebook
{id: {jupyter-notebook-latex}

* `latex.ipynb`
* [Latex symbols](https://en.wikipedia.org/wiki/Wikipedia:LaTeX_symbols)

## More Jupyter examples
{id: jupyter-examples}

* `generate.ipynb` Generate a single Pandas DataFrame
* `salary_generate.ipynb`
* `salary.ipynb`
* `temperatures.ipynb`
* `weather.ipynb`
* `numpy_matrix.ipynb`
* `seaborn_tips.ipynb`

## Jupyter Notebook: run on other port
{id: jupyter-notebook-on-other-ports}

```
jupyter notebook --port 8080
```

## Jupyter Notebook: public IP
{id: jupyter-notebook-public-ip}

```
jupyter notebook --ip 192.168.1.10
```


## Other Jupyter Notebook Kernels
{id: other-jupyter-notebook-kernels}

[Jupyter Kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)

## Jupyter Notebook convert to other format (nbconvert)
{id: jupyter-notebook-convert-to-other-format}
{i: nbconvert}

```
jupyter nbconvert try.ipynb --to HTML
jupyter nbconvert try.ipynb --to PDF    (needs also pandoc)
```

## Jupyter Notebook extensions
{id: jupyter-notebook-extensions}

```
pip install jupyter_contrib_nbextensions
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user
```

* Scratchpad
* Variable Inspector

