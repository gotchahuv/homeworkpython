import json
print('номер 5')
with open('students.json', encoding='utf-8') as file:
    studys=json.load(file)
for study in studys:
    if study["score"]>=60:
        study["passed"]=1
best=max(studys, key=lambda studys: studys["score"])
result={'best':best,
        'guys':studys}
with open('res_stud.json','w',encoding="utf-8") as file:
    json.dump(result,file,ensure_ascii=False,indent=4)
with open('res_stud.json',"r",encoding="utf-8") as file:
    a=json.load(file)
    print(a)