import re
with open('11ex.txt',encoding='utf-8') as file:
   a=file.read()
userid=re.findall(r'User \d+',a)
errorline=re.findall( r".*\bERROR \b.*",a)
error_users=re.findall(r"ERROR User \d+",a)
print(userid)
print(errorline)
print(error_users)