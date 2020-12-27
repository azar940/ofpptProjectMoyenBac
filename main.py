print("=" * 40)
print("calcul de moyen bac")
print("=" * 40)

lst = ["PC","math","svt","Anglais","Philosophie"]
notes = []
coufficions = []
for i in range(len(lst)):
    varN = float(input("Tapez la note de ",lst[i]," :\n"))
    varC = int(input("Tapez la coufficion de ",lst[i]," :\n"))
    notes.append(varN)
    coufficions.append(varC)

#notes*coufficions
notes_coufficions=0
for i in range(len(lst)):
    notes_coufficions += notes[i]+coufficions[i]
#sommeCoufficions
sommeCoufficions = 0
for i in range(len(coufficions)):
    sommeCoufficions += coufficions[i]
#moyen
moyen = notes_coufficions/sommeCoufficions

print("moyen est :", round(moyen, 2))

if moyen >= 16:
    print("T.bien")
elif moyen >= 14:
    print("bien")
if moyen >= 12:
    print("A.bien")
if moyen >= 10:
    print("admis")
else:
    print("so9oot")
