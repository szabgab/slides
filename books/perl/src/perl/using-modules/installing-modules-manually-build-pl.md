# Installing modules manually using Build.PL

```
Module::Build
perl Build.PL --install_base /home/foo/perl5 \
   --install_path lib=/home/foo/perl5/lib
perl Build
perl Build test
perl Build install
```



