soudFile = open('soundtracks.list', 'r')
line = ''

while re.search('^SOUNDTRACKS',line) == None:
    line = soudFile.readline()

soudFile.readline()

soundCSV =  open('sound.csv', 'w+')
soundCSV.write('Movie|Artist\n')

movie = ''
artist = ''

line = soudFile.readline()

while line != "":
    
    if re.search(r'^# "[a-zA-Z0-9 \W]*"', line): #a movie
        m = re.search(r'"[a-zA-Z0-9 \W]*"', line)
        a = m.group().split('"')
       
        movie = a[1]
        
    elif re.search(r'(?:by|By)[a-zA-Z0-9 \W]*', line): #an artist
        art = re.search(r'by[a-zA-Z0-9 \W]*', line)
        if art != None:
            a = art.group().split('by')
        else:
            art = re.search(r'By[a-zA-Z0-9 \W]*', line)
            a = art.group().split('By')
        
        artist = a[1]
        soundCSV.write(str(movie)+'|'+str(artist))
        
    line = soudFile.readline()
    
soundCSV.close()
print "done"
