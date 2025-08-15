listt = ["Khushi", 59, 37.3, "Harsh"]

print(listt[0])
listt[0] = 9
print(listt[0])

listt.append(34)
print(listt)
listt.insert(3,89)
print(listt)


tuplee = (87, "khushi", False, 89 ,32 , 89)

print(tuplee)
print(type(tuplee))

print(tuplee.count(89))



dicti = {
    "a" : 99,
    "b" : 87,
    "c" : 100,
}

print(dicti, type(dicti))
print(dicti.items())
print(dicti.keys())

dicti.update({"a" : 30,"d": 55})
print(dicti)


e = set()

sett = {1,2,2,2,3,3,4,5}
print(sett)
sett.add(7)
print(sett)

s1 = {1,2,3,4,5}
s2 = (4,5,6,7)

print(s1.union(s2))
print(s1.intersection(s2))