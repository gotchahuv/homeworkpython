print('Номер 18')
import re
import logging
import json
logging.basicConfig(level=logging.INFO, filename="py_log.log",format="%(asctime)s %(levelname)s %(message)s")
mets={}
urls={}
error=0
c=0
pat=r"\S+\S+ (\d{1,3}(?:\.\d{1,3}){3}) ([A-Z]+) (\S+) (\d{3})"
try:
    logging.info('Нач обр')
    print('Нач')
    with open('access.log',encoding='utf-8') as file:
        for line in file:
            a=re.search(pat,line)
            if a is None:
                logging.warning('Некорректно')
                continue
            ip=a.group(1)
            met=a.group(2)
            url=a.group(3)
            stat=int(a.group(4))
            mets[met]=mets.get(met,0)+1
            urls[url]=urls.get(url,0)+1
            c+=1
            if 400<=stat<500:
                error+=1
    url1=max(urls,key=urls.get)
    res={'Count':c,'Metod':mets,'Error':error,'Url':url1}
    with open('res18.json','w',encoding='utf-8') as file:
        json.dump(res,file,ensure_ascii=False,indent=4)
    logging.info('end')
    print('Конец')
    with open('res18.json', encoding='utf-8') as file:
        a = json.load(file)
    print(a)

except (OSError, UnicodeError) as e:
    logging.error(e)
    print('Mistake')