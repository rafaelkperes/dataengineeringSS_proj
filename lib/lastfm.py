import pdb
import pandas as pd
import requests
import xml.etree.ElementTree as ET

class LastFM:
    baseurl = 'http://ws.audioscrobbler.com/2.0/?'
    def __init__(self, apikey = 'b863970e9ba9d8391a162cae75ce422b', XML = True): # XML false will return JSON search - other methods may not work
        self.url = self.baseurl + 'api_key=' + apikey
        if (not XML):
            self.url += '&format=JSON'

    def artistInfo(self, artistname):
        searchurl = self.url + '&method=artist.getinfo&artist=' + artistname
        response = requests.get(searchurl)
        root = ET.fromstring(response.content)

        if root.find('error') is not None:
            error = root.find('error').get('code')
            if error == '6':
                raise ValueError('Artist not found.')
            else:
                raise Exception('Error %s when search artist %s' % (error, artistname))
        elif root.find('artist') is not None:
            artist = root.find('artist')
            name = artist.find('name').text
            stats = artist.find('stats')
            playcount = stats.find('playcount').text
            listeners = stats.find('listeners').text
            #print ('%s: %d listeners and %.3d plays.' % (name, int(listeners), int(playcount)))
            artist_info = {}
            artist_info['name'] = name
            artist_info['playcount'] = playcount
            artist_info['listeners'] = listeners
            return artist_info
        else:
            raise Exception('Unknown error when search artist %s' % artistname) # what to do? - should never happen


if __name__ == "__main__":
    lastfm = LastFM()

    try:    
        artist = lastfm.artistInfo('Cher')
        print (artist)
    except ValueError as err:
        print(err)

    try:
        artist = lastfm.artistInfo('blind guardian')
        print ('Blind Guardian play count: ' + artist['playcount'])
    except ValueError as err:
        print(err)

    try:
        artist = lastfm.artistInfo('ASDASDDQWEDFGVD')
        print (artist)
    except ValueError as err:
        print(err)
