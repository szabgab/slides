# Java Installation


* JRE
* JDK
* java
* javac


There are several implementation of Java, one currently controlled by Oracle and it can be downloaded from Oracle.com
but as far as I know there are various problematic licensing restrictions.
A better choice is to download the Open JDK.


* [Java Download Open JDK](https://openjdk.java.net/)


On MS Windows install it by unipping the .zip file and then configuring the PATH to include the bin/ directory.



Before we even write a line of code we would like to make sure that both the java compiler and the java runtime is
accessible for us. So we open a command line window or a Power Shell window and we type in javac --version
and java --version respectively.


On MS Windows

```
> javac --version
javac 14.0.2
```

```
> java --version
openjdk 14.0.2 2020-07-14
OpenJDK Runtime Environment (build 14.0.2+12-46)
OpenJDK 64-Bit Server VM (build 14.0.2+12-46, mixed mode, sharing)
```


