from datetime import *

date=(datetime.now().strftime("%d/%m/%Y"))
print(date)

file=open("index.html","a")
file.write("\nLast update: "+date)
file.close()
