__doc__ = """
Hencoder - A text based encoder based on Hauffman encoding
=====================================================================

Hencoder is a simple encoder based on greedy algorithim [Hauffman encoding](https://en.wikipedia.org/wiki/Huffman_coding).

This package can be used to:
* Encode any text files to binary
* Decode any encoded file to original content

"""

# Let users know if they're missing any of our hard dependencies
hard_dependencies = ("queue", "collections")
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(f"{dependency}: {e}")

if missing_dependencies:
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(missing_dependencies)
    )
del hard_dependencies, dependency, missing_dependencies


from .main.api import (
    encode, 
    decode
    )
