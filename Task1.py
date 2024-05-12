#MainFlow Task1 - Create a List Set & Dictionary

#List - A collectible datatype which can store homogenous datatype and is mutable in nature.
name = "Katsu"
a = list(name)
print(a)

b = [1,2,3,4,5,6,7,8]
print(b)

c = []
c[0] = 1
c[1] = 2
c[2] = 3
c[0] = 00

d.copy(c)
c.append(4)
c.pop(2)
print(c)
print(d)

#Set - Set is also a collectible datatype which stores only unique data and filters out repetetive data.

s = (1,1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9)
print(s)

s.add(10)
s.add(1)
s1.copy(s)
s.clear()
s.discard(1)

print(s1)

#Dictionary - Dictioanry is a collectible datatype whih stores the values in the key value pairs, its a type of hash table.
#In Dictionary Data is Mutable but the size is immutable.
#We cant fetch values by calling the index in dictionaries.


d1 = {"a":1, "b":2, "c":3, "d":4}
d2.copy(d1)

d1[a] = 01
d1.get(a)
d1.keys()
d1.values()
d1.items()

print(d1)
print(d2)






