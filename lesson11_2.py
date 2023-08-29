import random
def getScore():
    score=[]
    for i in range(5):
        score.append(random.randint(50,100))
    return score

def get_name(number):
    with open("names.txt",encoding="utf-8",newline='') as file:
        names_str=file.read()
        names_list=names_str.split(sep="\n")
        name=random.choices(names_list,k=number)
    return name

number = int(input("請輸入學生數:"))
name = get_name(number)
student=[]
for i in range(number):
    score=getScore()
    score=[name[i]]+score
    student.append(score)
print(student)