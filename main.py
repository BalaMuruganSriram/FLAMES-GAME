from collections import  Counter

def Commonchars(string1,string2):
    dict1 = Counter(string1)
    dict2 = Counter(string2)
    dictcommonchars = dict1 & dict2
    intx = len(dictcommonchars)
    return intx

def Remove(removestring, n):
    removedstring = removestring[0:n-1]+removestring[n:len(removestring)]
    return  removedstring




print("--Welcome to FLAMES relationship calculator--")
name1 = input("Enter Name 1 :")
name2 = input("Enter Name 2 :")
name1.lower()
name2.lower()
Commonchars(name1, name2)

intp = len(name1)
intq = len(name2)
intr = Commonchars(name1 , name2)
totalpqr = intp + intq - (2*intr)
z = totalpqr


flamestr = "FLAMES"

y1 = z % 6
if y1 == 0:
    flamestr = Remove(flamestr, 6)
    y2 = 6
else:
    flamestr = Remove(flamestr, y1)



y2 = ((z-(6-y1)) % 5)
if y2 == 0:
    y2 = 5
    flamestr = Remove(flamestr, 5)
else:
    flamestr = Remove(flamestr, y2)



y3 = (z-(5-y2)) % 4
if y3 == 0:
    y3 = 4
    flamestr = Remove(flamestr, 4)
else:
    flamestr = Remove(flamestr, y3)



y4 = (z-(4-y3)) % 3
if y4 == 0:
    y4 = 3
    flamestr = Remove(flamestr, 3)
else:
    flamestr = Remove(flamestr, y4)


y5 = (z-(3-y4)) % 2
if y5 == 0:
    y5 = 2
    flamestr = Remove(flamestr, 2)
else:
    flamestr = Remove(flamestr, y5)

if flamestr == "F":
    print("Your relationship will be maintained as friendship")
elif flamestr == "L":
    print("Your relationship will end in love")
elif flamestr == "A":
    print("Your relationship can be an Affection towards each other")
elif flamestr == "M":
    print("Your relation can end in Marriage")
elif flamestr == "E":
    print("Be Careful! There is risk of your relationship become hostile.")
elif flamestr == "S":
    print("I guess you both are siblings")
else:
    print("Unexpected error")

print("Thank you")















