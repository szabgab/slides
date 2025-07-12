# PyPI

[PyPI](https://pypi.org/) is the central registry of all the 3rd party Python libraries. When you use `pip` or any other tool to install a dependency, by default they consult the API of PyPI to get the distribution and all of its dependencies.

When people release a new version of their Python package they upload it to PyPI.

So when people talk about contributing to Python they usually talk about improving one of the packages and uploading it to PyPI, but who maintains PyPI? Can one contribute to it?

If you visit [PyPI](https://pypi.org/) and scroll to the bottom you can see that it is available in a number of languages including Hebrew, which indicates it should also support RTL (Right-to-left) rendering. Those translations need maintenance and more translations could be added.

Also at the bottom of the page I found a link to the [warehouse](https://github.com/pypi/warehouse) in the  [GitHub organization of PyPI](https://github.com/pypi).
That organization has a number of other projects in it as well, but looking at the warehouse one can see that there are 75 open pull-requests and 441 open issues.
There are certainly things to do.

One of the nice things about working on a project like PyPI itself is that you can also get involved in the operation aspect of a real high-load system. It is not like contributing to a framework which might be important and satisfying, but quite distant from the operations.

