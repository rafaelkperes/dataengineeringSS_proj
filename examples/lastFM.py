import requests
import xml.etree.ElementTree as xmlTree

artistname = 'Norah Jones'
url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=' \
      + artistname + '&api_key=b863970e9ba9d8391a162cae75ce422b' #&format=json'

response = requests.get(url)

if str(response) == '<Response [200]>':
    root = xmlTree.fromstringlist(response.content)
    ar = root.find('artist')
    print ar.find('name').text
    stats = ar.find('stats')
    print 'listners: ' + stats.find('listeners').text
    print 'playcounts: ' + stats.find('playcount').text
else:
    print 'no such musician in lastFM'