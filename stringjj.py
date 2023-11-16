string="be a programer"
str1=string.zfill(19)
print(str1)
s1="be a programmer"
len(s1)
num='-182'
print(num.zfill(4))

string="text"
left_jusitified=string.ljust(25,'*')
print(left_jusitified)

name="   nidhi"
str1=name.lstrip()
print(name)
print(str1)


name="nidhi  "
str1=name.rstrip()
print(name)
print(str1)


name="   nidhi  "
str1=name.strip()
print(name)
print(str1)

str="ws cube tech"
x=str.split()
print(x)
str="i am the best in my career because i am nidhi"
x=str.partition("the")
print(x)

str=" i am best nidhi sahu"
x=str.rpartition("and")
print(x)

richest_avengers='tony@ironman'.partition('@')
print(richest_avengers)

richest_avengers='tony@ironman'.rpartition('@')
print(richest_avengers)
angry_avenger='dr.bruce banner aka the hulk'.rsplit()
print(angry_avenger)


