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

5- install oauth2client for google login
You might need to install the above package.
	pip3 install --upgrade oauth2client

Database:
----------------------------
the database used in this code is sqlite database. to insatll the database.
Please run below in the terminal:
 - python catalogdb_setup.py
 - python seeder.py


Running the application
----------------------------
to run the program, clone the entire project folder then navigate to the folder then run the following command in the terminal.

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
 delete and edit buttons are active if the user is logged in and she is the creator for that item. The same buttons will be deactivated otherwise.


Image Handling:
-----------------------------
Item details includes adding a picture which is saved in the database and the file system as well. The app generates a random name then it saves it to the item table and the file system. If an image is not provided while creating the item, a default image will be given. If the user updates the image for any item, the old image is automatically deleted from the file system.

Deleting an item deletes its image from the file system after deleting the item as well.

Securing the pages:
------------------------------
To protect the items from unauthorized access, the app checks for user login and redirects the user to the login page if not authenticated.
When the user attempts to delete or edit an item for which she is not authorized to do so, the app checks if the user id matches the user id of the item being maniplulated and if they don't macth the user is redrected back to the itm details page.


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
