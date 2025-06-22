from cs50 import SQL
import sys
import re

# Sqlite file link for shows.db
dbFile = SQL("sqlite:///shows.db")

def main():
    user_want = input("Actor/Actress: ").rstrip().title()

    if re.search(r"[a-zA-Z]\ [a-zA-Z]", user_want):
        searchForShows(user_want)
    else:
        sys.exit("Couldn't find actor/actress shows")

def searchForShows(name):
    # Query for sqlite to grab the shows from the name of the actor/actress. WORKS ONLY FOR "shows.db" IN THIS SOURCE.
    rows = dbFile.execute("SELECT title, year, episodes FROM shows WHERE id IN (SELECT show_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name = (?))) ORDER BY(year)", name)

    # Print if the actor doesn't exist 
    if not rows:
        print(f"'{name}' couldn't be found in the database")

    for row in rows:
        print(f"{row['year']}: {row['title']} - Ep: {row['episodes']}")

if __name__ == "__main__":
    main()

