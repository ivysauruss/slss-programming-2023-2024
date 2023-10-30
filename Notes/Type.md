In Python, data can be grouped into categories called Types. 

| Name    | Example   |
| ---     | ---           |
| string or `str` | `"hello world!"`|
|`list`           | `[1, 2, 3, 4, 5]` |
| boolean or `bool`| `True` `False`    |
| integer or `int` | `1 -10 1205` |
| `float`          | `1.2 -432.21 1.0` | 

An example showing the use of these names: 

```python
favourite_food = "bibimbap"
my_age = 16
my_age_float = 16.0
```

# Converting Types 

There are some **special functions** built into Python that helps to convert data from one type to another. 

```python
intro_string = "My age is"
my_age = 16

# Recall 

"My name is" + "Jim"                   # "My name isJim"
"My name is" + " Jim"                  # "My name is Jim"
intro_string + my_age                  # This is going to BREAK
```