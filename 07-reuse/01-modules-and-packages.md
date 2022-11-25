# Modules and Reusing Code

## Modules

Every python file you write can be imported into other python files.

For example, imagine you have one python file named `greetings.py` with the following functions in it:

```python
def say_hi():
    print("hello!!")

def say_bye():
    print("bye!")
```

We can import this code into any other python file using the `import` statement, followed by the name of the file (minus the extension). Let's say we have a `main.py`. Inside we can write:

```python
import greetings
```

We can then call code from the `greetings` file with the name of the file, a dot, and then the function to run:

```python
import greetings

greetings.say_hi()
greetings.say_bye()
```

## Command line programs

Notice that our `greetings` file only has functions in it. If we run the file with python nothing will happen because we have defined functions but not called them. It's frequently the case that you might want to have a file that can be imported into other files as a module, but also run on its own. To do this in python we add a special `if` statement at the bottom of the file.

```python
def say_hi():
    print("hello!!")

def say_bye():
    print("bye!")

if __name__ == "__main__":
    say_hi()
```

The `__name__` variable is a special built-in python variable whose value will change based on if the file is being run directly (`python greetings.py`) or imported. If the file is run directly, `__name__` will contain the name of the file. If the file is imported, `__name__` will contain the string `__main__`. 

### Command line arguments

If you're making a command line program, you may want to be able to parse options and arguments. The built-in `argparse` module can help you do this:

```python
import argparse

def revolt(total_times):
    print("revolution " * total_times)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Revolution sayer')

    parser.add_argument("--total", type=int, help="How many times?", default=10)

    args = parser.parse_args()
    
    revolt(args.total)
```

(another funny example):

```python
from subprocess import run


def send_message(message, number):
    args = [
        "osascript",
        "-e",
        f'tell application "Messages" to send "{message}" to buddy "{number}"',
    ]
    run(args)
```

### Running a program at regular intervals

On mac and linux you can run a command at regular intervals using `crontab`

List current jobs:

```
crontab -l
```

Add a job:

```
crontab -e
```

instructions here: https://crontab.guru/


### Distributing your library or command line program

After you've made a library or command line tool you may wish to share it on python's package index: pypi. To do so, follow [this guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/). 

It can be somewhat confusing to do it on your own. Two tools that can help are [hatch](https://hatch.pypa.io/latest/) and [poetry](https://python-poetry.org/) 

#### Poetry

Let's make a simple python project using poetry:

```
poetry new revolution
```

```
poetry add PACKAGE
```


```toml
[tool.poetry.scripts]
revolution = "printrevolution:main"
```

```
poetry build
```

```
poetry publish
```

