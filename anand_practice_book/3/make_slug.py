import re
a=re.findall(r'(\w+)',"  ---hello---world  hai")
b='-'.join(a)
print b
