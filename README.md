PROJECT DESCRIPTION
This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

COMMAND INTERPRETER
The command interpreter is the core of the application. It is responsible for accepting and parsing user input, and executing the corresponding actions.

HOW TO START IT
To start the command interpreter run the followin command in your terminal:
$ ./console.py

HOW TO USE IT
Once the console is running you can enter commands to manipulate objects in the database using the following basic syntax:
<command> <class> <id> <attributes>
where:
  command   : Such as create, show, destroy, all, update
  class     :Describing name of the class objects you want to manage
  id        :ID of the object
  attributes:Attributes  you want to create or update
  
EXAMPLES
Example 0: Create an object
Usage: create <class_name>

(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
Example 1: Show an object
Usage: show <class_name> <_id>

(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  

Example 2: Destroy an object
Usage: destroy <class_name> <_id>

(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   

Example 3: Update an object
Usage: update <class_name> <_id>

(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
