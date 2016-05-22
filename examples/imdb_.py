import sys
import re
# Import the IMDbPY package.
try:
    import imdb
except ImportError:
    print 'You need to install the IMDbPY package!'
    sys.exit(1)

# search movie by name using API
title = "Love Actually"
i = imdb.IMDb()
results = i.search_movie(title)
for movie in results:
    print movie.getID() + ": " + movie['long imdb title']

# read from list file soundtrack(local database)
# print all movie titles in the file (too many..)
f = open('../datasets/imdb/soundtracks.list', 'r')
st = f.read()
pattern = re.compile('\n#(.*?).\(')
items = re.findall(pattern, st)
for item in items:
    print item
f.close()