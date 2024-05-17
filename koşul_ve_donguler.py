############### KOŞULLAR ##############

###  TRUE FALSE

1==1
1==2

#if
if 1==1:
    print("something")

if 1==2:
    print("something")

number = 10

if number == 10 :
    print("number is 10")

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(12)

def number_check(number):
    if number > 10:
        print("Number is bigger than 10")
    elif number == 10:
        print("Number is 10")
    else:
        print("Number less than 10")

number_check(10)

#########################################
##########  DÖNGÜLER (LOOPS) ###########
#######################################

students=["John","Mark","Vanessa", "Mariam"]

students[0]
students[1]
students[2]

for i in students:
    print(i.upper())

salaries = [1000,2000,3000,4000,5000]

for salary in salaries:
    # zamlısalary + salary * 20 / 100
    print(salary*20/100+salary)

def new_salary(salary,addition):
    addition_salary = ((salary*addition)/100) + salary
    return(int((addition_salary)))

new_salary(6000,25)

for salary in salaries:
    print(new_salary(salary,10))

salaries2 = [10700,25000,30400,40300,50200]

for salary in salaries2:
    print(int((new_salary(salary,15))))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary,10))
    else:
        print(new_salary(salary,20))

##################### UYGULAMA MÜLAKAT SORUSU ##########################
########################################################################

range(len(string))

range(0,5)
range(5)

def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()

    print(new_string)


alternating("mİuul")


############# BREAK &&&& CONTİNUE &&&& WHİLE #####################

salaries = [1000,2000,3000,4000,5000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)

for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

## while
number = 1
while number<5:
    print(number)
    number+=1

############## ENUMARATE : OTOMATİK COUNTER/INDEXER İLE FOR LOOP ########

students = ['John', 'Mark', 'Vanessa', 'Mariam']

for student in students:
    print(student)

for index, student in enumerate(students , 1):
    print(index,student)

A = []
B = []

for index, student in enumerate(students):
    if index %2 ==0:
        A.append(student)
    else:
        B.append(student)
    print(A,B)

##################################### divide_students fonk yazınız
######## MÜLAKAT SORUSU ############# çift indexte yer alanları bir listeye tek indexte olanları başka listeye alınız
##################################### fakat iki listeyi tek liste olarak return olsun


students = ['John', 'Mark', 'Vanessa', 'Mariam']

""""###farklı yolu
def divade_students(students):
    groups = [[],[]]
    for index, student in enumerate(students):
        if index % 2 ==0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups
"""

A = []
B = []
def divade_students(students):
    for index, student in enumerate(students):
        if index % 2 ==0:
            A.append(student)
        else:
            B.append(student)
    return(A,B)


divade_students(students)

############################################################
#### ALTERNATİG FONKSİYONUNUN ENUMARATE İLE YAZILMASI  #####
############################################################
def alternating_with_enumarate(string):
    new_string = ""
    for index, letter in enumerate(string):
        if index % 2 ==0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumarate("hidayetfurkanozer")

############## ZİP ##########################   ********** önemli olabilir***********

students = ['John', 'Mark', 'Vanessa', 'Mariam']

departments = ["mathematics","statistics","physics","astronomy"]

ages = [23,30,26,22]

list(zip(students,departments,ages))

#############################################################
########### LAMBDA , MAP , FİLTER , REDUCE ##################

new_sum = lambda a, b : a+b  #fonksiyon tanımlamaya yarar kullan at fonksiyon
new_sum(4,5)

#   map
salaries = [1000,2000,3000,4000,5000]
def new_salary(x):
    return x * 20 / 100 + x
new_salary(1000)

for i in salaries:
    print(new_salary(i))

list(map(new_salary,salaries)) #for yerine kullanıldı

list(map(lambda x : x*20/100+x,salaries)) #lambda fonksiyon yerine kullanıldı

list(map(lambda x: x**2 , salaries))

# filter  ##çok önemli değil
list_store = [1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x % 2 == 0, list_store)) #filter sorgu yapar burada 2 ye bölümünden kalan sıfır mı diye sorar

# reduce ##çok önemli değil
from functools import reduce
list_store1 =[1,2,3,4]
reduce(lambda a,b: a+b, list_store1)

