from functools import lru_cache

import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

# referencia sobre o DictReader:
# https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
# https://docs.python.org/3/library/csv.html
