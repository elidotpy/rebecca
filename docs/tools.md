# Tools

Tools are the things Rebecca can do.

All tools are defined in `"./rebecca_tools.py"`

# How to create your own tool?

First, you need to declare a function with the name of the tool. Let's say we want to make a function named "meow"

```python
def meow():
```

and we want to give it the argument "times", so it prints meow {times} times.

```python
def meow(times):
```

Now, we need to hint the type of the argument. This is necessary, so the AI doesn't breaks, or try to use a different type than you intended to. In this case, it is an integer. You can also add a `return type hint`, but it isn't really necessary.

```python
def meow(times:int):
```

Okay, now, it needs a docstring, so the AI knows what it does.

```python
def meow(times:int):
    """
        Outputs the word "meow" {times} times.
    """
```

then, we can finally write the content of the function.

```python
def meow(times:int):
    """
        Outputs the word "meow" {times} times.
    """
    return "meow " * times
```

Finally, we need to make the AI know that the tool exists.
To do that, just add an item to the "tools" list, defined on the bottom of this file.

```python
tools = [tool1, tool2, meow]
```

(tool1 and tool2 are for purely showcasing purposes.)

Congratulations, You just made your own tool, and the AI is able to use it!

# How to remove tools?

Remove the tool's name from the `tools` list on the end of the file.
For example, you want to remove "tool2"
```python
tools = [tool1, tool3] # it was [tool1, tool2, tool3]
```

Now rebecca can't use the tool anymore.