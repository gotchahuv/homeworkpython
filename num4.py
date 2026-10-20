import csv
print('номер 4')
with open('exlub4.csv','r', encoding='utf-8') as csvfile:
    read=csv.DictReader(csvfile)
    with open('exlub4n.csv','w',encoding='utf-8',newline='') as red2:
        wr=csv.DictWriter(red2, fieldnames=read.fieldnames)
        wr.writeheader()
        for i in read:
            if float(i['price'])>100:
                wr.writerow(i)
with open('exlub4n.csv', encoding='utf-8') as csvfile:
    reader=csv.DictReader(csvfile)
    for i in reader:
        print(i)