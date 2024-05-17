#int
x=46
type(x)

#float
x=10.3
type(x)

#complex
x=2j+1
type(x)

# string
x="hello ai era"
type(x)

name = "John"

long_string = """uzun string ifadelerini bu şekilde üçer tırnak arasına yazabiliriz
örneğin şuan olduğu gibi
Veri Yapıları: Hızlı Özet"""

name[0]

name[0:2]

long_string[0:10]

long_string

"veri" in long_string #büyük harf küçük harf duyarlılığı

"Veri" in long_string

#boolean
True
False
type(True)

##### LİSTE
x=["btc","eth","xpr"]
type(x)

#sözlük
x={"name":"Peter","Age": 36}
type(x)

#tupple
x=("python","ml","ds")
type(x)

#set
x={"python","ml","ds"}
type(x)

# NOT: Liste, tupple, set ve dictionary veri yapıları aynı zamanda python collections (Arrays) olarak geçer.

#VERİ YAPILARI METHODLARI

dir(str) #stringlerle kullanılabilecek methodları verir

type(name)

type(len)

len(name)

len("hidayetfurkanözer")

"miuul".upper()
"MIUUL".lower()

#replace : değiştirir

hi = "Hello AI Era"
hi.replace("l","p")

#split : böler

"Hello AI Era".split()   #boşlukları böldü

#sprip : kırpar

" ofofo ".strip() #boşlukları kırptı
"ofofo".strip("o") #baş ve sondaki "o" ları kırptı

#capitalize : ilk harfi büyütür
"furkan".capitalize()

dir(str)

"furkan".startswith("f")







