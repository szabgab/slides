# Changing @INC - Relative PATH

```
Directory layout

  script/app.pl
  lib/My/Module.pm
```


```
# relative path
use FindBin;
use File::Spec;
use lib File::Spec->catfile($FindBin::Bin, '..', 'lib');
```


```
# relative path
use File::Spec;
use File::Basename;
use lib File::Spec->catfile(
            File::Basename::dirname(File::Spec->rel2abs($0)),
            '..',
            'lib');
```



