import os
import traceback

from ase_syntax import ase_file


class ParsingError(ValueError):
    pass


def parse(path):
    with open(path, "rb") as fh:
	    data = fh.read()
    try:
        return ase_file.parse(data)
    except Exception as err:
        traceback.print_exc()
        raise ParsingError(err)

