# FastAPI - Path containing a directory path


{% embed include file="src/examples/fastapi/path-of-path/main.py" %}

```
http://localhost:8000/shallow/a.txt    works
http://localhost:8000/shallow/a/b.txt  not found

http://localhost:8000/deep/a.txt       works
http://localhost:8000/deep/a/b.txt     works
```


