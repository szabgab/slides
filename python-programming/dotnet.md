# Python .NET
{id: dotnet}

## IronPython
{id: ironpython}

* [IronPython](https://ironpython.net/
* [GitHub](https://github.com/IronLanguages/ironpython2)
* Only supports Python 2

* [Iron Python 3](https://github.com/IronLanguages/ironpython3)
* Not ready for production

## Use .NET libraries from Python
{id: dotnet-from-python}


https://github.com/pythonnet/pythonnet

pip install pythonnet

http://pythonnet.github.io/

C:\Windows\Microsoft.NET\Framework\v4.0.30319\
C:\Program Files\dotnet\

The latest Visual Studio is supposed to come with Nuget, but if you don't have it, you can download it from https://www.nuget.org/downloads

Put the executable somewhere in your PATH

For example I've created c:\Bin, put the nuget.exe in this directory and added C:\Bin to the PATH.

Then install the compilers using nuget install Microsoft.Net.Compilers as suggested on https://github.com/dotnet/roslyn
This created the
Microsoft.Net.Compilers.3.4.0
directory in my home directory

"\Users\Gabor Szabo\Microsoft.Net.Compilers.3.4.0\tools\csc.exe" /t:library MyMath.cs

## Add Integers
{id: add-integers}

![](examples/dotnet/math/MyMath.cs)
![](examples/dotnet/math/myapp.py)

```
css /t:library MyMath.cs
python myapp.py
```

## Python from .NET
{id: python-from-dotnet}


