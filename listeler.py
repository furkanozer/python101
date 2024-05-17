#####################################################
############### LİSTELER(List) ######################
#####################################################

notes = [1,2,3,4]
type(notes)
names=["a","b","v","d"]
not_nam= [1,2,3,"a","b",True,[1,2,3]]

not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]

notes[0]

notes[0] = 99

notes

not_nam[0:4]

#Liste Methodları

dir(notes)  #append önemli

len(notes)
len(not_nam)

#append : eleman ekler

notes.append(100)
notes

#pop: indexe göre eleman siler

notes.pop(0)
notes

#insert: indexe ekler
notes.insert(2,99)
notes

#####################################################
################## #SÖZLÜK  #########################
#####################################################
#key-value

dictionary = {"REG" : "Regression",
              "LOG": "Logistic Regression",
              "CART":"Classification and Reg"}
dictionary["REG"]

dictionary1 = {"REG" : ["RMSE",10],
              "LOG": ["MSE",20],
              "CART":["SSE",30]}

dictionary1["CART"][1]

#KEY SORGULAMA

"REG" in dictionary1

"YSA" in dictionary1

dictionary1.get("REG")

#VALUE DEĞİŞTİRMEK

dictionary1["REG"] = ["YSA",10]
dictionary1

#TÜM KEY VE VALUE'LARA ERİŞMEK
dictionary1.keys()
dictionary1.values()

#TÜM ÇİFTLERİ TUPLE HALİNDE LİSTEYE ÇEVİRME
dictionary1.items()

#KEY VE VALUE DEĞERLERİNİ GÜNCELLEMEK
dictionary1.update({"RF":10}) #yazdığımız key olmadığı için ekledi
dictionary1.update({"REG":12}) #aynı key olduğu için update etti
dictionary1

#####################################################
##### DEMET (TUPLE) LİSENİN DEĞİŞTİRİLEMEZ HALİ #####
#####################################################

t=("john","mark",1,2)
type(t)
t[0]
t[0:3]

t[0]=99 #değiştirilemez
t=list(t)
type(t)
t[0]=99
t #ancak liste haline getirilip değiştirilir. (TUPLE DEĞİŞTİRİLEMEDİĞİ İÇİN DAHA GÜVENLİDİR BAZEN KULLANMAK GEREKBİLİR)

##################################################### DEĞİŞTİRİLEBİLİR
###########  SET KÜME İŞLEMLERİ  ################### SIRASIZ + EŞSİZ
##################################################### KAPSAYICI

set1 = set([1,3,5])
set2 = set([1,2,3])

#differance :iki kümenin farkı

set1.difference(set2)  #set1 ' de olup set2 ' de olmayanlar

set2.difference(set1)  #set2 ' de olup set1 'de olmayanlar

## symetric differance : iki kümede de birbirlerine göre olmayanları verir

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

# İnersection: İki Kümenin Kesişimi
set1.intersection(set2)
set2.intersection(set1)

set1 & set2  #intersection gibi davranıp kesişimi getiir
set1 - set2  #differance gibi davranır

# union:  iki kümenin birleşimi
set1.union(set2)
set2.union(set1)

set3=set([8,9,7])
set4=set([5,6,7,8,9,10])
# isdisjoint : iki kümenin birleşimi boş mu?
set3.isdisjoint(set4)
set4.isdisjoint(set3)

# issubset : bir kümde diğer kümenin altkümesi mi?
set3.issubset(set4)
set4.issubset(set3)

# issuperset : bir küme diğer kümeyi kapsıyor mu?
set3.issuperset(set4)
set4.issuperset(set3)


