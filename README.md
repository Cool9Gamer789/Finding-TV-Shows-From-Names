# 🎬 Actor/Actress TV Show Lookup

## 📦 Requirements
```
pip install cs50
```
## Required Files:
* shows.db: This SQLite database must be present in the same directory. It's provided in the CS50 SQL notes

## 🛠️ How It Works
* This script queries the shows.db database for TV shows where the specified actor/actress has appeared, and lists them in order by year.

## 🚀 How to Run
1. Make sure shows.db is in the same directory as the script.
2. Run the script:
```
py show.py
```
3. When prompted, enter the full name of the actor or actress (e.g., Steve Carell or Jennifer Aniston).
4. The script will return a list of shows they've appeared in, ordered by year.

## ❗ Error Handling
* If the name is not found, the script will let you know:
```
'John Doe' couldn't be found in the database
```
* If input doesn't match the expected full name format (e.g., just "Steve" or "Carell"), it will exit:
```
Couldn't find actor/actress shows
```
