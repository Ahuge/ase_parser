# ase_parser
[Adobe Swatch Exchange](https://www.lifewire.com/ase-file-2619688) file format parser written using the python [construct library](https://construct.readthedocs.io/en/latest/).

## Usage:
This is no setup much like a library, instead as a code snippet that you can grab.  
View the file `test.py` to see it's usage.

```python
import os

from ase_parse import parse

myfile = "theme.ase"
struct = parse(myfile)

print(struct)
```

## Dependencies:
 - construct  
    `pip install construct`
