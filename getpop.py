from cfscrape import create_scraper
from server import app, get_db
from bs4 import BeautifulSoup

scraper = create_scraper() # returns a requests.Session object
r = scraper.get("https://en.nostalrius.org/")

soup = BeautifulSoup(r.content, 'html.parser')

blocks = soup.find_all("div", class_="block")
pvpblock = blocks[3].find_all("span")
pveblock = blocks[4].find_all("span")

if pvpblock[0].text == "Online":
    pvp = int(pvpblock[4].text)
else:
    pvp = 0

if pveblock[0].text == "Online":
    pve = int(pveblock[4].text)
else:
    pve = 0

with app.app_context():
    c = get_db()
    row = (pve, pvp)

    # Insert a row of data
    c.execute("INSERT INTO series VALUES (strftime('%s', 'now')*1000,?,?)", row)

    # Save (commit) the changes
    c.commit()
    print("Inserted %s" % str(row))
