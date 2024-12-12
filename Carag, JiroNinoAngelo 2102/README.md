
# BooKeep: Library Manager

BooKeep: Library manager is a system that will help libraries to manage the books inside it. It will ensure that libraries can efficiently manage the books being added, the books being borrowed, and keep records of the borrowed books.

The application utilized the programming language Python, and used different libraries and modules in order to make it functional and to have a working graphical user interface. It also used MySQL as a database to store the records and data inputs.


## Objective 

The project aims to lessen the time of managing records of libraries, knowing that managing the books shelf by shelf could be a hassle for people, and it could consume so much time. If 
the system can reduce at least an hour of the librarian on managing the library, it could be a big help for them, for the time spared could be used for other works, like cleaning shelves and such.

## Python Libraries Implemented

`Python tkinter` - The module for Tkinter was imported into the program, used for the basic Graphical User Interface. Python Tkinter lets the programmer use different commands in order to 
create an interactive feature on the system, wherein users can see for themselves what the program does and can also manipulate the program by inputting some data and storing them. 

`MySQL Connector` - This module will help the program to establish a connection between MySQL 
database and Python programming language. After connecting to a MySQL database, the program will have commands that can be used to manipulate and store data. The python program can also inherit MySQL commands, so that the system can be used and reused because there is a storage for data. 

`Pillow` - Python Imaging Library or PIL is a python module that is used to add support for 
opening, manipulating and integrating different images into the program. This module can 
be used when the developer wants to insert images so that the GUI is visually appealing to 
the users.
## SDGs 

There are some SDGs from the 17 sustainable development goals are reflected in the system BooKeep: Library Manager. SDGs helps innovation to be helpful to the society and be sustainable. Some of these are the following: 

1. Quality Education - libraries are essential for students especially on higher forms of education, and helping libraries be more efficient can help its effectiveness and students can utilize the library more because it has a better system, which is a faster way for it to be utilized. 

2. Industry, Innovation, and Infrastructure- systems like these could help on mobilizing industries because small scale changes on smaller systems could give big impact, like improving the library system, it can help not only students, but also people in the industry to research efficiently because it is less hassle for them to learn more through the books in the library.

3. Responsible Consumption and Production- promoting libraries using systems like these helps people become responsible consumers because instead of buying books, reading it for once, and for it only to end up on their shelves because they’re done reading it, they can just borrow books, and return it after reading. This way, we can lessen the production of books, because producing things that are used only for once could lead to other problems. 
## Instructions

1. The user can choose if they will use the application as an admin or as user.
2. If the `admin` button is clicked, it will ask the user for the amdin password, which is by default `123`. Then the admin window will pop-up after inputting the password.
3. There are five buttons to choose from on the admin page. First is the add book, which is used to add books into the library. Second is remove book, where the admin can remove book using the book id assigned. Third is the view book, where the admin can see all the books in the library. Fourth one is view borrow records, where the admin can see all the records of the borrowers from the day the application was implemented. Lastly, the view borrowed books, where the admin can see all the books being borrowed as of the moment.
4. If the user clicks `User` on the homepage or main menu, they'll see 3 main buttons which have different functions. The first one is borrow book, where users will input their name, the id of the book they wish to borrow, and the dates of when the books was borrowed and date when they wish to return the book. The second function is to return book. Lastly, the view available books, where the users can see what books could be borrowed by the time they are using the system.