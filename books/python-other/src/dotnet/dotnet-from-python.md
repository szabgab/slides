# Use .NET libraries from Python

* pythonnet
* csc
* nuget
* Roslyn

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


