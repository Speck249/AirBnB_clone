# AirBnB Clone :house_with_garden:
---
![AirBnB Logo](/assets/AirBnB_logo.png "AirBnB Logo")
---
## Project Description
This focus of this project is building a copy of the official AirBnB website.
Implmented in four phases, the first ('AirBnB clone') focuses on building a powerful 
storage system along with a console for interacting with the web app. 

THE COMMAND INTERPRETER:
Developed using the Python Cmd module, the command interpreter is a simple line-oriented
CLI that functions as a basic Shell for manipulating data without a visual interface and 
capable of these commands- Create | Show | Count | Update | Destroy.

## Console Usage
Clone this repository & proceed to run the console:
-- git clone https://github.com/.../AirBnB_clone.git

Here's what you'll find in the repo:

|           Modules                 |                       Description                            |
|-----------------------------------|:-------------------------------------------------------------|
| console.py                        | Contains entry point of the command interpreter              |
| models/amenity.py                 | Handles amenity objects.                                     |
| models/base_models.py             | Parent class defines all common attr/methods for subclasses. |
| models/city.py                    | Handles city objects.                                        |
| models/place.py                   | Handles place objects.                                       |
| models/state.py                   | Handles state objects.                                       |
| models/review.py                  | Handles review objects.                                      |
| models/user.py                    | Handles user objects.                                        |
| models/engine/file_storage.py     | Serializes/deserializes instances to & from JSON file.       |
| tests/test_models/                | Contains all test cases for all classes.                     |
| test_models/test_amenity.py       | Unit test suite for amenity subclass.                        |
| test_models/test_base_class.py    | Unit test suite for base class.                              |
| test_models/test_city.py          | Unit test suite for city subclass.                           |
| test_models/test_place.py         | Unit test suite for place subclass.                          |
| test_models/test_state.py         | Unit test suite for state subclass.                          |
| test_models/test_review.py        | Unit test suite for review subclass.                         |
| test_models/test_user.py          | Unit test suite for user subclass.                           |
| test_models/test_file_storage.py  | Unit test suite for user subclass.                           |


**HOW IT WORKS**: 
After running the console module (console.py), the user will gain access to the command interpreter
either in **Interactive** or **Non-Interactive** mode. In interactive mode, the user will encounter a prompt - (hbnb)
indicating the shell program is ready to accept input. In this case, the user is expected to insert the correct
command which will invoke some action to be executed. Note that a new prompt will appear to accept user input until
the program is terminated. 

In non-interactive mode, there won't be any prompt to interact with. Instead, the user will
pipe in his/her input and won't be prompted for a new input until another command is piped into program execution.
For clear depiction of both modes, please refer to the 'Test' section of this file.  

**Interactive mode**
```
~/ALX-C#11/AirBnB_clone$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

```
**Non-interactive mode**
```
~/ALX-C#11/AirBnB_clone$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help quit
Quit command to exit the program

(hbnb) quit

```
Here are the commands of the command interpreter:

|  **Methods** |          **Description**                            |
|--------------|:----------------------------------------------------|
| **create**   | Create new instances of a given class.              |
| **show**     | Prints string representation of an instance.        |
| **count**    | Retrieves the number of instance of a given class.  |
| **all**      | Prints all string representation of all instances.  | 
| **update**   | Updates an instance.                                |    
| **destroy**  | Deletes an instance.                                |
| **help**     | Returns information of a given command.             |
| **EOF/quit** | Exits the program                                   |

## Tests
**unittest**
```
~/ALX-C#11/AirBnB_clone$ python3 -m unittest discover tests
......................................................................................
----------------------------------------------------------------------
Ran 86 tests in 0.872s

OK
```
---
## Authors
Jeffrey Kirigo | jeffreykirigo75@gmail.com <br>
Rediet Kifle | redietkfle@gmail.com
