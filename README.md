# AirBnB_clone
PROJECT DESCRIPTION
This repository contains the initial stage my student project to build the
AirBnB website clone.
At this stage I am implementing a backend interface, or Console, to manage
program data.
Console commands allow the user to CREATE, UPDATE, and DESTROY objects,
as well as manage file storage. Using a system of JSON
serialization/deserialization, storage is persistent between sessions.

COMMAND INTERPRETER
The command interpreter is the core of the application. It is responsible for
accepting and parsing user input, and executing the corresponding actions.

STARTING THE COMMAND INTERPRETER
To start the command interpreter run the following command in your
terminal: $ ./console.py

Once the console is running you can enter commands to manipulate objects
in the database using the following basic commands:
## Commands

- `create <class>`: Creates a new instance of the specified class.
- `show <class> <id>`: Shows the string representation of an instance.
- `destroy <class> <id>`: Deletes an instance.
- `all [<class>]`: Lists all instances of the specified class, or all instances if no class is specified.
- `update <class> <id> <attribute> <value>`: Updates the specified attribute of an instance.


EXAMPLES Example 0: Create an object Usage: create Basemodel
creating folders
$ ./console.py
(hbnb) create BaseModel
12345678-1234-1234-1234-123456789abc
(hbnb) show BaseModel 12345678-1234-1234-1234-123456789abc
[BaseModel] (12345678-1234-1234-1234-123456789abc) {'id': '12345678-1234-1234-1234-123456789abc', ...}
(hbnb) all BaseModel
["[BaseModel] (12345678-1234-1234-1234-123456789abc) {...}"]
(hbnb) destroy BaseModel 12345678-1234-1234-1234-123456789abc
(hbnb) quit
$