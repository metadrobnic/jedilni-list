print("Dnevni meni")

jedilni_list = []

while True:
    answer =raw_input("Bi rad dodal novo jed? da/ne")
    if answer == "da":
        jed = raw_input("Dodaj jed: " )
        cena = raw_input("Napisi ceno: ")
        jedilni_list.append([jed, cena])
    if answer == "ne":
        break

print("Danasnji meni:")

for i in jedilni_list:
    print("* " + i[0] + ": " +  i[1] )


moj_fajl = open("meni.txt", "w+")

moj_fajl.write("Danasnji meni:\n")

for i in jedilni_list:
    moj_fajl.write("* " + i[0] + ": " +  i[1] + "\n")

moj_fajl.close()