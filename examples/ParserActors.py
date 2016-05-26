import sys
import re

# parser ACTORS to xml
# using actors.list from imdb/interfaces
# It creates the following xml structure (without identation):
#<actors>
#   <actor>
#       <name>..</name>
#       <movies>
#           <movie>
#               <name>..</name>
#               <year>..</year>
#           </movie>
#           <movie> .. </movie>
#       </movies>
#   </actor>
#   <actor> ... </actor>
#</actors>


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

#opens a xml file
xml = open('actors.xml', 'w+')
xml.write('<?xml version="1.0" encoding="UTF-8"?>')
xml.write('<actors>')

#start building actors structure actors[list of actor]::actor[name, movies]
a = -1
Actors = []
line = actors_file.readline()
while line != "": 
    if line[:1] == '$': #an actor
        if a >= 0:
            xml.write('</movies></actor>')
        a = a + 1
        m = 0
        
        actor = re.search(r'^\$[a-zA-Z0-9]*[ ]*,[ ]*[a-zA-Z0-9]*', line)
        name = actor.group()[1:].split(',')
        name = name[1].strip()+' '+name[0].strip()
        xml.write('<actor><name>'+name.strip()+'</name>')
        
        movie = re.search(r'[	](.*?)[ ]\([0-9]*\?*\)',line)
        aux = movie.group().strip()
        aux = aux.split('(')
        aux[0] = aux[0].strip(' ')
        aux[0] = aux[0].strip('"')
        aux[1] = aux[1].strip(')')
        xml.write('<movies><movie><name>'+aux[0]+'</name><year>'+aux[1]+'</year></movie>')
        
    else:
        movie = re.search(r'[	](.*?)[ ]\([0-9]*\?*\)',line)
        if movie != None:
            aux = movie.group().strip()
            aux = aux.split('(')
            aux[0] = aux[0].strip(' ')
            aux[0] = aux[0].strip('"')
            aux[1] = aux[1].strip(')')
            xml.write('<movie><name>'+aux[0]+'</name><year>'+aux[1]+'</year></movie>')
    line = actors_file.readline()
    
print "done"
xml.write('</movies></actor></actors>')
actors_file.close()
xml.close()
