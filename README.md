Item Catalog App
======================

This is a python application to display items per category. Users can login using a third party login (Google Plus). Authorized users can create, edit and delete items they created.

Installation and Required Packages
----------------------------
1- Install python
The program is written in python3.
You can find the installation file in the python download webpage.

https://www.python.org/downloads/

2- Install Flask
	pip install Flask

3- Install SQLAlqhemy
	pip install sqlalchemy

4- install Pillow package for image handling
	pip install Pillow


Database:
----------------------------
the database used in this code is sqlite database. to insatll the database.
Please run below in the terminal:
 - python catalogdb_setup.py
 - python seeder.py


Running the application
----------------------------
to run the program, navigate to the folder then run the following command in the terminal.

Python application.py

In the browser navigate to localhost:5000/
This should bring you to the main page which displays all categories with a link to view the items within.

Initially there will be a login button where user can login using google plus.

Unauthenticated users can view the catalog only.

Once logged in, user can naviagte to below:
1- My account:
   Displays user info taken from her google account.
2- Add Item button displays under each category:
   She can add item to any category

3- In the item details page:
 delete and edit buttons are active if the user is logged in and she is the creator for that item. The same buttons will deactivated otherwise.

Deleteing an Item:
-----------------------------
 	each item has a status field in the database. This field either A for active items or X for non active ones. This means when the user delets an item it becomes inactive in the database (status = 'X') but the record is not deleted for the same. The same will not be displayed to the user in the app front end.


Image Handling:
-----------------------------
Item details includes adding a picture which is saved in the database and the file system as well. The app generates a random name then it saves it to the item table and the file system. If an image is not provided while creating the item, a default image will be given. If the user updates the image for any item, the old image is automatically deleted from the file system. 

Deleting an item dosn't delete its image from the file system since the record only gets deactivated.

Securing the pages:
------------------------------
To protect the items from unauthorized access, the app checks for user login and redirects the user to the login page if authenticated.


JSON End points:
-----------------------
1- Entire Catalog
http://localhost:5000/catalog/JSON
This will provide a json for the entire catalog, category wise

2- Categor Items
/catalog/<string:category_name>/Category/JSON
ex:
/catalog/Soccer/Category/JSON
This provides a json data for all items in a given category 

3- Specific Item
/catalog/<string:catgeory_name>/<string:item_name>/item/JSON
ex: 
/catalog/Soccer/Ball/item/JSON
This provides a json data for a given item
