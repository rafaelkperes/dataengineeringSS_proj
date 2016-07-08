#Parser Movie Plot
plotfile = open('plot.list', 'r')
line = ""

# goes to the begin of the actors list
while re.search('^PLOT SUMMARIES LIST',line) == None:
    line = plotfile.readline()
#jump 2 rows
plotfile.readline()
plotfile.readline()

plotCSV = open('plot.csv', 'w+')
plotCSV.write('MovieName|Plot\n')

line = plotfile.readline()
i = 0;
while line != "": 
    if re.search(r'^[MV:][a-zA-Z0-9 \W]*', line):
        if i != 0:
            plotCSV.write(str(plot)+'\n')
        i = i + 1
        
        movie = re.search(r'[ ][a-zA-Z0-9 \W]*', line)
        plotCSV.write(str(movie.group().strip())+'|')
        plot = ''
        
    elif re.search(r'^[PL: ][a-zA-Z0-9 \W]*', line):
        p = re.search(r'[ ][a-zA-Z0-9 \W]*', line)
        plot = plot + ' '+ str(p.group().strip())
    line = plotfile.readline()
plotCSV.close()
print "done"
