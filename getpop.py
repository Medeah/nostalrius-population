from cfscrape import create_scraper
from server import app, get_db
from bs4 import BeautifulSoup
from time import time

scraper = create_scraper() # returns a requests.Session object
r = scraper.get("https://en.nostalrius.org/")

soup = BeautifulSoup(r.content, 'html.parser')
orange = soup.find_all("span", class_="orange")
pvp = int(orange[4].text)
pve = int(orange[8].text)

with app.app_context():
    c = get_db()
    row = (pve, pvp)

    # Insert a row of data
    c.execute("INSERT INTO series VALUES (strftime('%s', 'now')*1000,?,?)", row)

    # Save (commit) the changes
    c.commit()
    print("Inserted %s" % str(row))
