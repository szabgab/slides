# Reading the .env environment file in Python

* `.env` file in the same folder where the program is.

{% embed include file="src/examples/os/.env)

{% embed include file="src/examples/os/show_env.py" %}

```
pip install python-dotenv
```

```
python examples/os/read_env.py
SOME_THING=other python examples/os/read_env.py
```


