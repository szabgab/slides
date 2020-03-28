# Windows cmd
{id: windows-cmd}

## Configuration - Properties
{id: configuration}

* Font: change font type and size
* Layout: Window Size and Screen Buffer Size
* Colors: Background/Text,  RGB 0-255

* Font: Consolas 16
* Layout: Window Size: 103x27
* Layout: Screen Buffer Size: 103x9001
* Colors: Screen Background: 12-12-12
* Colors: Screen Text: 118-118-118


## File system
{id: file-system}
{i: pwd}
{i: cd}
{i: %CD%}

Show current directory (like pwd)

```
echo %CD%
cd
```

Change directory (folder)

```
cd some\other\place
cd ..
```

Show content of directory (folder)

```
dir
```

Show content of file

```
type FILENAME
```


```
echo
redirection with >  and >>
cls
```

## pushd - podd
{id: pushd-popd}
{i: pushd}
{i: popd}

```
pushd some\other\place
popd
```

## Directory
{id: directory}
{i: del}
{i: mkdir}
{i: rmdir}

```
del             (delete file)
mkdir           (make directory)
rmdir           (remove directory)
```

## File Globbing
{id: file-globbing}
{i: dir}
{i: ren}

```
dir *.txt
ren       (rename, move)
```
## ERRORLEVEL
{id: errorlevel}
{i: ERRORLEVEL}

```
dir
echo %ERRORLEVEL%
0

dir nosuch
echo %ERRORLEVEL%
1
```

