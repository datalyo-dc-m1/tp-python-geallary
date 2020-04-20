"""
t = [1, 2, 3, 4, 5]
a = t[0] + t[3]
b = t[-1]
c = t[3:]
a = a + t[-2]

print(type (t))
print(a)

alphabet = ["a", "b", "c", "d", "e"]

print(alphabet[-3:])


liste = [1, 4, 1, 2, 1, 5, 3, 1, 12]

while liste.count(1) > 0:
  liste.remove(1)

print(liste)

liste.sort()

print(liste)
"""

grades = [8,12,15,6,10,19,18,7,13,15,8,15,17,13,12,15,16,9,10,3,19,20,15]

print("Maximum ", grades[0], "Minimum ", grades[len(grades)-1])
print("Minimum ", min(grades), "Maximum ", max(grades))
print(max(grades)-min(grades))
print(sum(grades)/len(grades))
print(len(grades))

grades.append(14)
grades[5]=13

grades.sort()

print(grades)

cpt = 0
for i in grades:
    if grades[i] > 10:
        cpt = cpt + 1
print(cpt, "élèves ont validé la matière")

