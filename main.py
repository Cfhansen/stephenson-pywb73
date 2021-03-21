###solution to problem 73 from ben stephenson's "the python workbook".

import re

mystr = str(input('Enter a phrase:'))

mystr = mystr.lower()
mystr = re.sub(' ','',mystr)
mystr = re.sub(',','',mystr)
mystr = re.sub('/.','',mystr)
mystr = re.sub('/','',mystr)
mystr = re.sub('-','',mystr)
mystr = re.sub('/?','',mystr)
mystr = re.sub('!','',mystr)

print(mystr == mystr[::-1])
