# Jupyter notebooks
{id: jupyter}

## What is Jupyter Notebook?
{id: what-is-jupyter}

* [Jupyter](https://jupyter.org/)

* A web-based interactive development environment

## Jupyter on Windows
{id: run-jupyter-windows}

If you use [Anaconda](https://www.anaconda.com/distribution/) it already comes with Jupyter notebook.
On Windows you can run it from the start menu.


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
* Execute code
* Show content of variables
* import modules
* Quit - shut down the notebook server.

* Number is the execution order Out[] refers to the number of the cell for this this the output.


## Jupyter Notebook file format
{id: jupyter-notebook-file-format}

* Jupyter file format (show the file) JSON
* Download file as Python (.py)

## Jupyter notebook edit and command mode
{id: jupyter-edit-and-command-mode}



* Modes: Blue - command mode, Green - edit mode
* Enter - Switch to edit mode (or newline if already in edit mode)
* ESC - Switch to command mode
* Ctrl-Enter - execute current cell
* Shift-Enter - execute current cell

* Clear Cell data before saving
* Button h for help
* Button A - add cell Above current cell
* Button B - add cell Below current cell
* dd  - delete current cell
* ...


## Jupyter notebook Intellisense (TAB completition)
{id: jupyter-notebook-intellisense}

* Just press TAB for word completition and method suggestions

## Jupyter add
{id: jupyter-simple-add}

* Open an existing notebook: `add.ipynb`


## Planets
{id: planets-csv}

* The Planets example we saw in the Pandas chapter

* `planets.csv`
* `planets.ipynb`


## Jupyter input
{id: jupyter-input}

```
name = input("Name: ")
```

## File chooser
{id: jupyter-filechooser}

* Avoid hard-coded pathes
* `FileChooser.ipynb`

## IPy Widgets
{id: ipywidgets}
{i: ipywidgets}

* [Interact](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)
* [Widget list](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html)

* `ipywidgets.ipynb`

## Jupyter Notebook and Markdown
{id: jupyter-notebook-markdown}

* `markdown.ipynb`
* [Jupyter Markdown](https://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Working%20With%20Markdown%20Cells.html)
* [Original Markdown](https://daringfireball.net/projects/markdown/syntax)
* [Markdown](https://en.wikipedia.org/wiki/Markdown)

## Latex in Jupyter Notebook
{id: jupyter-notebook-latex}

* To insert complex formulas.
* `latex.ipynb`
* [Latex symbols](https://en.wikipedia.org/wiki/Wikipedia:LaTeX_symbols)


## Jupyter StackOverflow
{id: jupyter-stackoverflow}

* Download a dataset from the [Stack Overflow survey](https://insights.stackoverflow.com/survey).
* unzip the file. Feel free to remove the `__MACOSX/` directory if it is included.

* `SO/so.ipynb`
* `SO/selected-rows.ipynb`
* `SO/selected-columns.ipynb`


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

## Genes using Jupyter
{id: genes-using-jupyter}

```
jupyter notebook genes.ipynb
```

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

## Jupyter notebook Checkpoints
{id: jupyter-notebook-checkpoints}

* A very simple, one-level version control.
* I would not rely on it as it is now. Use a real VCS. (e.g. git)

