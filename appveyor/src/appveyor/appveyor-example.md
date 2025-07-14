# Appveyor Example


* [codeandtalk](https://github.com/szabgab/codeandtalk.com/)

```
build: false

environment:
  matrix:
    - PYTHON: "C:\\Python34"
      PYTHON_VERSION: "3.4.1"
      PYTHON_ARCH: "32"

    - PYTHON: "C:\\Python36"
      PYTHON_VERSION: "3.6.3"
      PYTHON_ARCH: "32"
init:
  - "ECHO %PYTHON% %PYTHON_VERSION% %PYTHON_ARCH%"

install:
  - "%PYTHON%/Scripts/pip.exe install pytest"
  - "%PYTHON%/Scripts/pip.exe install ."

test_script:
- "%PYTHON%/Scripts/pytest.exe"
```


