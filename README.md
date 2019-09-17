# Python module with helpful data

Here you can find many functions and classes that you can use in your future work.

## Files
The main file (must be present for the folder to be considered a module)
> \_\_init\_\_.py

Input/output console operations and options
> console.py

Write test0() or test11() or something similar to test some commands
> examples.py

Alternative for included "math" library
> nomath.py

## Examples code
```
import mit

li = mit.read('Enter some numbers')
m = mit.nomath.find_max(li)

if m > 10:
   mit.draw('Hello, World!', mit.Colors.bg.green, mit.Colors.bold)
else:
   mit.draw('Hello, World!', mit.Colors.fg.purple, mit.Colors.underline)
```

## see you soon! ^^
