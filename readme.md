Check Dependencies:
```
  node --version
  python3 --version
  sqlite3 --version
```
Install and run:
```
pip install -r requirements.txt
python3 createdb.py
python3 getpop.py # get data from nostalrius website
python3 server.py #debug
gunicorn -w 4 -b 127.0.0.1:5000 server:app #
```

Setup cronjob:
```
*/15 * *   *   *     cd ~/nostalrius-population && python3 getpop.py
```
