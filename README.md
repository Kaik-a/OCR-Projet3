# OCR-Projet3 - Help MacGyver to escape !

In this game, you control MacGyver who is trapped in a maze. He must collect three items to tinker something which can help him asleep the guardian protecting the exit. 

## Prerequisites
* Download this repository
* You must have python3 installed on your computer, otherwise you can follow the guides on python's website https://www.python.org/downloads/
* You should have pip installed with python3 if not, you can follow the guide 
there https://pip.pypa.io/en/stable/installing/
* Set your current directory in the project:
```cd path/to/folder/downloaded```
* run on your console/terminal the following command: 
```pip install -r requirements.txt```
* Export your PYTHONPATH
	in Windows:```set PYTHONPATH=.```
	in MacOS/Linux:```export PYTHONPATH=.```
* Everything should be ok to play now !

## Launch the game
* In your console/terminal run 
```python3 main/main.py```

## Commands
For this game, you can just use the directionals arrows to move MacGyver throughout the maze.

## Program design
* directory main : contains main.py where we can find the main() function 
* directory model : game's classes
* directory ressources: game's ressources (pictures, maze plain file)
* directory tests : tests
* directory view : contains file related to game's display
* file config.py : constants of the game
## Tests
All the tests have been realized with pytest. You can install it with the following command ```pip install -U pytest```. When it's done, you can launch test using ```pytest path/to/test/file.py```

## Author 
**Mehdi Bichari** - [GitHub Repo](https://github.com/Kaik-a/)

## Acknowledgements 
I want to make a special thank to Julien Jacquelinet who helped me all along this project and all the openclassrooms community !
