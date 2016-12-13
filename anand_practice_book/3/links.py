import sys
import re
import urllib
f=urllib.urlopen(sys.argv[1])
b=f.read()
list=re.findall(r'htt.+://[\w]+.+"',b)
for i in list:
	print i[:-1]
