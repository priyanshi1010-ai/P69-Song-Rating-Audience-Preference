P69 - SONG RATING & AUDIENCE PREFERENCE ANALYSIS
=================================================

1. PROJECT OVERVIEW
-------------------
This project is a Python-based Song Rating and Audience
Preference Analysis System.

The application allows users to enter song ratings and
analyze audience preferences based on songs, artists,
genres and playlists.

The project uses Tkinter for the graphical user interface,
Pandas and NumPy for data analysis, Matplotlib for
visualization and CSV files for persistent storage.


2. OBJECTIVES
-------------
- Record audience song ratings.
- Store rating data permanently.
- Display stored rating records.
- Delete selected records.
- Calculate overall rating statistics.
- Identify the highest and lowest rated songs.
- Identify the preferred genre.
- Identify the top-rated artist.
- Display graphical analysis.
- Validate user input.
- Handle runtime and file-related errors.


3. TECHNOLOGIES USED
--------------------
Python
Tkinter
Pandas
NumPy
Matplotlib
CSV File Handling


4. PROJECT FILES
----------------

main.py
    Main application and Tkinter GUI.

data_manager.py
    Handles CSV file storage, loading, adding
    and deleting records.

analysis.py
    Performs Pandas and NumPy data analysis.

charts.py
    Creates Matplotlib charts.

test_project.py
    Contains automated test cases.

ratings.csv
    Stores project data permanently.

requirements.txt
    Contains required Python libraries.


5. FEATURES
-----------

- Add song rating
- View all ratings
- Delete rating
- Persistent CSV storage
- Overall average rating
- Highest-rated song
- Lowest-rated song
- Preferred genre
- Top artist
- Song rating chart
- Genre preference chart
- Input validation
- Exception handling
- Pandas analysis
- NumPy calculations
- Tkinter GUI
- Automated testing


6. HOW TO RUN
-------------

Step 1:
Install Python 3.

Step 2:
Open Command Prompt in the project folder.

Step 3:
Install required packages:

    pip install -r requirements.txt

Step 4:
Run the application:

    python main.py


7. HOW TO RUN TESTS
-------------------

Run:

    python -m unittest test_project.py


8. DATA STORAGE
---------------

The application stores all ratings in:

    ratings.csv

The file is automatically created if it does not exist.


9. ANALYSIS
-----------

The project calculates:

- Total ratings
- Number of unique songs
- Number of audience members
- Number of artists
- Number of genres
- Average rating
- Highest rating
- Lowest rating
- Highest-rated song
- Lowest-rated song
- Preferred genre
- Top artist


10. VISUALIZATION
-----------------

The project provides:

1. Average Rating by Song
2. Audience Preference by Genre


11. VALIDATION
--------------

The application validates:

- Empty fields
- Invalid rating values
- Rating range from 1 to 5
- Invalid text input
- Missing record selection


12. ERROR HANDLING
------------------

Exception handling is used for:

- Invalid user input
- CSV errors
- File errors
- Data conversion errors
- Chart errors


13. TESTING
-----------

Automated test cases are provided in:

    test_project.py

The tests verify:

- CSV data loading
- Required columns
- Rating range
- Numeric rating values
- Data loading functionality


14. CONCLUSION
--------------

The project provides a complete Python-based system
for recording song ratings and analyzing audience
preferences using data processing, visualization,
file handling and a graphical user interface.