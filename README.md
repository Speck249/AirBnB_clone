# AirBnB Clone :house_with_garden:
---
![AirBnB Logo](/assets/AirBnB_logo.png "AirBnB Logo")
---
## Project Description
The AirBnB project is geared towards building a copy of the official AirBnB website.
Implmented in four phases, the first ('AirBnB clone') focuses on building a powerful 
storage system along with a console. 

The Command Interpreter:
Developed using the Python Cmd module, the command interpreter is a simple line-oriented
CLI that acts mostly like a basic Shell for manipulating data without a visual interface.
It is capable of five primary commands - Create | Show | Count | Update | Destroy.
## Console Usage
Clone this repository & proceed to run the console:
-- git clone https://github.com/.../AirBnB_clone.git

Here's what you'll find in the repo:
|           Modules                 |                       Description                           |
| ----------------------------------|------------------------------------------------------------:|
| console.py                        | contains entry point of the command interpreter             |
| models/amenity.py                 | Handles amenity objects.                                    |
| base_models.py                    | Parent class defines all common attr/methods for subclasses.|
| city.py                           | Handles city objects.                                       |
| place.py                          | Handles place objects.                                      |
| state.py                          | Handles state objects.                                      |
| review.py                         | Handles review objects.                                     |
| user.py                           | Handles user objects.                                       |
| engine/file_storage.py            | Serializes/deserializes instances to & from JSON file.      |
| tests/test_models/test_amenity.py | Unit test suite for amenity subclass.                       |
| test_base_class.py                | Unit test suite for base class.                             |
| test_city.py                      | Unit test suite for city subclass.                          |
| test_place.py                     | Unit test suite for place subclass.                         |
| test_state.py                     | Unit test suite for state subclass.                         |
| test_review.py                    | Unit test suite for review subclass.                        |
| test_user.py                      | Unit test suite for user subclass.                          |
| test_file_storage.py              | Unit test suite for user subclass.                          |

And these are the commands of the command interpreter:
|   Methods  |             Description                            |
| -----------|---------------------------------------------------:|
| create     | Create new instances of a given class.             |
| show       | Prints string representation of an instance.       |
| count      | Retrieves the number of instance of a given class. |
| all        | Prints all string representation of all instances. | 
| update     | Updates an instance.                               |    
| destroy    | Deletes an instance.                               |
| help       | Returns information of a given command.            |
| EOF/quit   | Exits the program                                  |
## Tests
---
## Authors
Jeffrey Kirigo - jeffreykirigo75@gmail.com
Rediet Kifle - redietkfle@gmail.com
