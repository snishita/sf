# Wire simulator

The simulator runs on AGX Dynamics and is therefore available only to those who have a license to use this software.

## Tested Environment
- Windows 10
- Visual Studio
- AGX Dynamics 2.26.1.0

## How to use the provided file?
First of all, you should watch the movie of "demonstration of the string figure simulation at README.md in the parent directory.

The provided file is a rewritten version of "tutorial_wireWindAndWater.cpp" provided in the AGX Dynamics tutorial folder. Users of this file should replace it with the file of the same name provided in the tutorial folder.

When this file is run, the input prompt for path data file appears first. You can specify the file name by its absolute path. Relative paths can also be used to specify a file name, but the hard-coded path string must be changed in that case.

- line 392: the path for input file
- line 264: the path for output file (describe below) 

After input of the path data, you input a finger movement code. Then, wire simulation will start.

During simulation, it accepts input of the following keys on the keyboard:
- the cursor right key moves the cylinders so that they split to the left or right.
- the cursor left key moves the cylinders so that they  approache from the left and right.
- the cursor moves the cylinders so that they are divided into left, right, up, and down sections. This move is usually performed at the final step of the string figure.
- The right shift key terminates the simulation and prompts to output path data.

You can specify the output file name by its absolute path. Relative paths can also be used to specify a file name, but you need to change the source code (see above).