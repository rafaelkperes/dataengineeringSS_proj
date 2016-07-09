# parser ACTORS to ACTORS.CSV and MOVIES.CSV
# using actors.list from imdb/interfaces

actors_file = open('actors.list', 'r')
line = ""

# goes to the begin of the actors list
while re.search('^THE ACTORS LIST',line) == None:
    line = actors_file.readline()
#jump 4 rows
actors_file.readline()
actors_file.readline()
actors_file.readline()
actors_file.readline()

#opens the CSV files
actorCSV = open('actors.csv', 'w+')
actorCSV.write('Id|FirstName|LastName\n')

movieCSV = open('movies.csv', "w+")
movieCSV.write('Id|Name|Year\n')

actor_movieCSV = open('actors_movies.csv', "w+")
actor_movieCSV.write('IdActor|IdMovie\n')

#start building actors structure actors[list of actor]::movie[actor_name, movies]
idActor = 0
idMovie = 0

actors = []
movie = []
movies = []
line = actors_file.readline()


while line != "": 
    if re.search(r'^[a-zA-Z0-9\$](.*?)[	]', line): #an actor
            
        name = re.search(r'^(.*?)[	]', line)
        movie = re.search(r'[	][a-zA-Z0-9 \W]*',line)
        year = re.search(r'\([0-9?]*\)',line)
        #print name.group()
        a = name.group().strip()
        #a = a.split(',')
        
        actorCSV.write(str(idActor)+'|'+str(a)+'\n')
        
        if year:
            movieCSV.write(str(idMovie)+'|'+str(movie.group().strip())+'|'+str(year.group())+'\n')
            
        else:
            movieCSV.write(str(idMovie)+'|'+str(movie.group().strip())+'|null\n')
            
        
        actor_movieCSV.write(str(idActor)+'|'+str(idMovie)+'\n')
        idActor = idActor + 1
        idMovie = idMovie + 1
        
    elif re.search(r'^[a-zA-Z0-9\$](.*?)[	]', line): #a movie from a actor
        if a != -1:
            movie = re.search(r'[	][a-zA-Z0-9 \W]*',line)
            year = re.search(r'\([0-9?]*\)',line)
            if year:
                movieCSV.write(str(idMovie)+'|'+str(movie.group().strip())+'|'+str(year.group())+'\n')
                
            else:
                movieCSV.write(str(idMovie)+'|'+str(movie.group().strip())+'|null\n')
                
                    
            actor_movieCSV.write(str(idActor)+'|'+str(idMovie)+'\n')
            idMovie = idMovie + 1
            
            
    line = actors_file.readline()

actorCSV.close()
movieCSV.close()
actor_movieCSV.close()

print "done";
