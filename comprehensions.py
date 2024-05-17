############# COMPREHENSIONS #############

########## LIST COMPREHENSIONS



"""
#### ESKİ YÖNTEM
salaries = [1000,2000,3000,4000,5000]
def new_salary(x):
    return x * 20 / 100 + x

new_salary()
null_list = []
for i in salaries:
    null_list.append((new_salary(i)))

for i in salaries:
    if i >3000:
        null_list.append(new_salary(i))
    else:
        null_list.append(new_salary(i*2))
"""

[salary * 2 for salary in salaries]
[salary * 2 for salary in salaries if salary <3000]  ## EĞER sadece if kullanılıyorsa if en sağa yazılır ama else ile birlikte kullanılacaksa for döngüsü sağa geçer
[salary * 2  if salary <3000 else salary * 0 for salary in salaries]
[new_salary(salary * 2)  if salary <3000 else (salary * 0.2) for salary in salaries]

students=["John","Mark","Vanessa", "Mariam"]
students_no = ["John","Vanessa"]
[student.lower() if student in students_no else student.upper() for student in students]


##################### DİCT COMPREHENSIONS
dictionary = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4 }

dictionary.keys()
dictionary.values()
dictionary.items()

{k : v ** 2 for (k,v) in dictionary.items()}
{k.upper() : v for (k,v) in dictionary.items()}

########### UYGULAMA MÜLAKAT SORUSU
# AMAÇ : ÇİFT SAYILARIN KARESİ ALINARAK BİR SÖZLÜĞE EKLENMELİDİR

numbers = range(10)







##################################################################
################# LİST DİCT COMPREHENSIONS  ######################
######################  UYGULAMALARI  ############################

#### VERİ SETİNDEKİ DEĞİŞKEN İSİMLERİNİ DEĞİŞTİRMEK

import seaborn as sns

df = sns.load_dataset("car_crashes")
df

df.head()

df.columns

for col in df.columns:
    print(col.upper())























