# Hotel Management

This is a basic Hotel Management System built using Python and SQLite for a simple backend. It allows basic operations like managing room bookings, guest check-in/check-out, and viewing the availability of rooms. This is a minimal version of a hotel management application for learning and development purposes.

<h1>Features</h1>

<h3>Room Booking:</h3> Allows guests to book rooms for specific dates.

<h3>Check-In/Check-Out:</h3> Manage guest check-in and check-out.

<h3>Room Availability:</h3> Check available rooms based on dates.

<h3>Guest Management:</h3> Store basic guest information like name and contact details.

<h3>Simple Console Interface:</h3> This version uses a command-line interface.

<h1>Technologies Used</h1>

<h3>Backend:</h3> Python 

<h3>Database:</h3> SQLite (lightweight database for simplicity)

<h1>Installation Prerequisites</h1>

Ensure you have the following installed on your local machine:

- Python 3.x 

- SQLite 

<h2>Steps to Install</h2>

<h4>Clone the repository:</h4>

'''git clone https://github.com/yourusername/hotel-management-python.git'''


<h4>Install Python dependencies:</h4>
You can just navigate to the project directory and install the required Python packages.

'''cd hotel-management-python
pip install -r requirements.txt  # If using Flask, or install necessary libraries like Flask'''


<h4>Database Setup:</h4>
The system uses SQLite for storing data. A simple schema is provided in database_setup.py.

<h4>To set up the database:</h4>

'''python database_setup.py'''


This will create the database (hotel_management.db) and the required tables.

Run the application:
Once everything is set up, run the main Python script to start the system.

'''python app.py'''


The application should now be running locally. You can interact with it through the command line interface.

<h1>Main Features</h1>

<h3>Room Booking:</h3>

Enter the room number, guest name, check-in, and check-out dates.

The system will check availability and book the room if available.

<h3>Check-In/Check-Out:</h3>

Admin can mark a guest as checked in or checked out by providing the guest ID.

<h3>View Available Rooms:</h3>

Admin can see which rooms are available based on selected dates.

