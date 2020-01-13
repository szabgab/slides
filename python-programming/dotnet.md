# Python .NET
{id: dotnet}

## IronPython
{id: ironpython}

Python running on the [DLR](https://docs.microsoft.com/en-us/dotnet/framework/reflection-and-codedom/dynamic-language-runtime-overview)
that is on top of the [CLR](https://docs.microsoft.com/en-us/dotnet/standard/clr) of Microsoft.

* [IronPython](https://ironpython.net/
* [GitHub](https://github.com/IronLanguages/ironpython2)
* Only supports Python 2

* [Iron Python 3](https://github.com/IronLanguages/ironpython3)
* Not ready for production

## Use .NET libraries from Python
{id: dotnet-from-python}
{i: pythonnet}
{i: csc}
{i: nuget}
{i: Roslyn}

* [pythonnet](http://pythonnet.github.io/)
* [pythonnet source code](https://github.com/pythonnet/pythonnet)

```
pip install pythonnet
```

The latest Visual Studio is supposed to include [Nuget](https://www.nuget.org/), but if you don't have it, you can download it from [Nuget downloads](https://www.nuget.org/downloads)

Make sure `nuget.exe` is somewhere in your PATH:

For example I've created `C:\Bin`, put the nuget.exe in this directory and added `C:\Bin` to the `PATH`.

Then install the compilers using nuget install Microsoft.Net.Compilers as suggested on [Roslyn](https://github.com/dotnet/roslyn)
This created the `Microsoft.Net.Compilers.3.4.0` directory in my home directory

Make sure `csc.exe` is somewhere in your PATH or use the full path to it:

"\Users\Gabor Szabo\Microsoft.Net.Compilers.3.4.0\tools\csc.exe" /t:library MyMath.cs

## Python and .NET console
{id: python-and-dotnet-console}

![](examples/dotnet/net_console.py)

```
python net_console.py
```


## Python and .NET examples
{id: python-and-dotnet}

![](examples/dotnet/math/MyMath.cs)
![](examples/dotnet/math/myapp.py)

```
csc /t:library MyMath.cs
python myapp.py
```

C:\Windows\Microsoft.NET\Framework\v4.0.30319\
C:\Program Files\dotnet\

## Exercise Python and .NET
{id: exercise-python-and-dotnet}

* Take a .NET class that you would like to use, try that.

