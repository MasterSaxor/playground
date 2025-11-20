def add(a, b):
    """
    >>> add(5, 3)
    8

    >>> add(200, 100)
    300

    >>> add("hi", 5)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 2, in add
    TypeError: can only concatenate str (not int") to str

    """
    return a + b
