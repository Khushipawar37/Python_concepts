a = int(input("Enter your age: "))

if(a >= 18):
    print("Adult")

elif(a < 0):
    print("Invalid age")
else:
    print("Not an adult")

print("Program ends")

for i in range(1,6):
    print(i)

j = 0

while(j < 5):
    print(j)
    j +=1

for i in range(0,40,4):
    print(i)

s = "Khushi"
for i in (s):
    print(i)

for i in range(100):
    if(i == 12):
        break
    print(i)

for i in range(10):
    if( i == 3 or i == 7):
        continue
    print(i)