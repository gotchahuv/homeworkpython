print('Номер 21')
import re
print('Введите логин')
log=input()
def is_valid_login(login):
    pat=r"[a-zA-Z][a-zA-Z0-9_]{3,15}"
    if re.fullmatch(pat,login):
        return True
    else:
        return False

print(is_valid_login(log))