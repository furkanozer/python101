##################################
#### FONKSİYONLAR
#### KOŞULLAR
#### DÖNGÜLER
#### COMPREHENSIONS
##################################

#########  FONKSİYON OKURYAZARLIĞI  #########
?print # = help(print)
print("a","b" )
print("a","b", sep="__" )

######## FONKSİYON TANIMLAMA  ########
#def fonk tanımlamaya yarar

def calculate(x):
    print(x*2)

calculate(5)
#### İKİ ARGÜMANLI/PARAMETRELİ BİR FONKSİYON TANIMLAYALIM
def summer(arg1 , arg2):
    print(arg1+arg2)

summer(7,8)

############ DOCSTRİNG #################
def summer(arg1 , arg2):
    """
    Sum of two numbers

    Parameters
    ----------
    arg1: int, float
    arg2: int, float

    Returns:
         int,float

    Examples:



    """

summer()

########## FONKSİYONLARIN STATEMENT/BODY BÖLÜMÜ #############

# def function_name(parameters/arguments):
#     statements (function body)

def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")

say_hi("denemelere_devam")

def multiplication(a,b):
    c =  a * b
    print(c)

multiplication(10,9)


#girilen değerleri bir liste içinde saklayacak fonksiyon
list_store = []

def add_element(a,b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1,8)
add_element(18,8)
add_element(180,10)

###############   ÖN TANIIMLI ARGÜMANLAR/PARAMETRELER(DEFAULT PARAMETERS/ARG) ##################

def divide(a,b):
    print(a/b)

divide(1,2)

def divide(a,b=1):
    print(a/b)

divide(10)

def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")

say_hi()
say_hi("merhaba")

############ NE ZAMAN FONKSİYON YAZMA İHTİYACIMIZ OLUR   ################

## warm, moisture,charge

(56+15) / 80
(17+45) / 70
(52+45) / 80

##  DRY
def calculate(warm, moisture, charge):
    print((warm+moisture)/charge)

calculate(98,17,78)

###### RETURN: FONKSİYON ÇIKTILARINI GİRDİ OLARAK KULLANMAK

calculate(98,17,78) * 10

type(calculate(98,17,78))

def calculate(warm, moisture, charge):
    return (warm+moisture)/charge

calculate(98,17,78) * 10

a = calculate(98,17,78)

def calculate(warm, moisture, charge):
    warm = warm*2
    moisture=moisture*2
    charge=charge*2
    output=(warm+moisture)/charge
    return warm,moisture,charge,output

calculate(98,12,78)

warm,moisture,charge,output = calculate(98,12,78)  #hepisini ayrı ayrı çağırabiliriz

########## FONKSİYON İÇERİSİNDEN FONKSİYON ÇAĞIRMAK ##############

def calculate(warm, moisture, charge):
    return int((warm+moisture)/charge)  # float değil de int olmasını istedik


calculate(90,12,12) * 10


def standardization(a , p):
    return a*10/100*p*p

standardization(45,1)

def all_calculation(warm,moisture,charge,p):
    a = calculate(warm,moisture,charge)
    b= standardization(a,p)
    print(b*10)

all_calculation(1,3,5,12)

def all_calculation(warm,moisture,charge,a,p):
    print(calculate(warm,moisture,charge))
    b= standardization(a,p)
    print(b*10)


all_calculation(1,3,5,19, 12)

##########  LOCAL VE GLOBAL DEĞİŞKENLER ###############3
list_store=[1,2]

def add_element(a,b):
    c = a * b
    list_store.append(c)
    print(c, list_store)

add_element(1,9)












