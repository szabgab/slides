# Dart using vim

* vim


Syntax highlighting with [Dart vim plugin](https://github.com/dart-lang/dart-vim-plugin)


```
cd ~/
$ git clone https://github.com/dart-lang/dart-vim-plugin
ln -s ~/dart-vim-plugin/syntax/dart.vim ~/.vim/syntax/
```


And include the following lines in ~/.vimrc



```
" automatic Dart file type detection
au BufRead,BufNewFile *.dart set filetype=dart
```


