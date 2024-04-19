# PyFIDE: FIDE Chess Data Scraper

PyFIDE is a Python tool designed to scrape data from the FIDE (Fédération Internationale des Échecs) chess website. It provides functionalities to gather information about players, their ratings, and gaming statistics from the FIDE database.

## Features

* **Player Data Extraction** : Retrieve player information including name, country, Elo rating, and birth year.
* **FIDE ID Retrieval** : Obtain FIDE IDs associated with players.
* **Rating History** : Access historical ratings of players across different time periods.
* **Different Game Formats** : Get ratings for classical, rapid, and blitz chess formats.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/jasnain-singh/PyFIDE.git
   ```
2. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Import the `FideInfo` class from `pyfide.py`:

   ```
   from pyfide import FideInfo
   ```
2. Instantiate the `FideInfo` class:

   ```
   fi = FideInfo()
   ```
3. Utilize the available methods to scrape data:

   ```
   # Get top players
   top_players = fi.getTop(max=100)

   # Update top 100 players list
   updated_players_list = fi.updateTop100()

   #Get FIDE IDs for players
   fide_ids_df = fi.getFideIds()

   #Update FIDE IDs
   updated_fide_ids = fi.updateFideId()

   #Get FIDE ID for a specific player
   fide_id = fi.getFideId(name="Carlsen, Magnus") # Name needs to be matching their FIDE Profile name

   #Get all ratings for a player
   all_ratings = fi.getAllRatings(name="Carlsen, Magnus")

   #Get classical ratings for a player
   classical_ratings = fi.classical(name="Carlsen, Magnus")

   #Get rapid ratings for a player
   rapid_ratings = fi.rapid(name="Carlsen, Magnus")

   #Get blitz ratings for a player
   blitz_ratings = fi.blitz(name="Carlsen, Magnus")
   ```

## Contributors

* [Jasnain Singh](https://github.com/jasnain-singh)

## License

This project is licensed under the MIT License - see the [LICENSE]() file for details.

---

Feel free to customize the sections and details according to your preferences and project specifics!
