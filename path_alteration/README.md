# Path alteration

- modifyPath.py: a script to perform the path alteration
- simple_viewer.py: scripts to visualize path data

## Requirement:
- ANTLR4
- Python3
    - VPython
    - antlr4-python3-runtime

## How to use them

First of all, you should watch the movie of "demonstration of the string figure simulation at README.md in the parent directory.

To alter a given path data, specify one of the following two types of arguments.
```
Usage: 
    python modifyPath.py <original path filename> <altered path filename>
    python modifyPath.py <original path filename> <altered path filename> <packed path filename> <finger-string extended path filename>
```

The second type is used for The second type is used to learn about the process of executing the path alteration.

The `<original path file>` is input for the script, and the script outputs the other files.

After executing the script, enter the finger movement code. Note that if the fingers specified by the code have no noose, or if the finger string is not detected correctly, the code cannot be executed and an error will occur.

The `packed path filename` as the output of the script is an input of the following wire simulation.


