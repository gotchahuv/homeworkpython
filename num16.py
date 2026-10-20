print('Номер 16')
import re
stats = {"INFO": 0, "WARNING": 0, "ERROR": 0}
error_users = set()
with open('logs.txt',encoding='utf-8') as file:
    for line in file:
        a=re.search(r'(INFO|WARNING|ERROR)',line)
        stats[a.group()]+=1
        if a.group() == 'ERROR':
            user=re.search(r"User \d+",line)
            error_users.add(user.group())
for a in stats:
    print(a,stats[a])
print(sorted(error_users))