angry_avengers='dr.bruce banner aka the hulk'.rsplit('aka')
print(angry_avengers)
bii_avengers='gro...at'.rsplit('. ')
print(bii_avengers)
bii_avengers='rocket\ttracoon'.rsplit()
print(bii_avengers)
rii_avengers='rocket\t\tracoon'.rsplit()
print(rii_avengers)
gotg_avengers ='rocket\n\nracoon'.splitlines(True)
print(gotg_avengers)
avengers=b'tony,steve,bruce'
print(avengers)
print(type(avengers))
avengers=b'gro\xddt'
print(avengers[3])
print(chr(92))
avengers=rb'gro\xddt'
print(avengers[3])
print(chr(92))
