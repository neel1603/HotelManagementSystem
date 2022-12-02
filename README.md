# HotelManagementSystem

This was a GUI based (tkinter) Database Management System (SQLite3) built using
python. It serves various functions such as storing the details for owners,
customers, bill payments, employee details, etc. Various DBMS constraints were
also used to build this system, as different levels of privileges for different
users using the system. Hence data retrieval and storing capabilities differ in
the case of customers, owners and employees.

Here for our restaurant we have maintained four positions and different rights for accessing database pertaining to their roles i.e.

	Admin    (Mode = 1)

	Owner    (Mode = 2)

	Employee (Mode = 3)

	Customer (Mode = 4)
        
Initially we are providing Authentication form i.e. to login or sign-in concurrently collecting the mode.

As per the mode selected access to data accordingly will be granted.

E.g.
If admin gets logged in then admin has the rights to Insert, Delete, Update as well as to View the database but if any customer or employee gets logged in then 
they can simply view their own details and the rest is hidden for them.

We have created GUI using tkinter in order to provide functionalities.

