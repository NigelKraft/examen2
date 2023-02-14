lijst = ["hey","hoi","hallo"]

def nieuw_woord():
    woord = input("Geef de het woord dat u wil toevoegen in:")
    lijst.append(woord)
    print("Het nieuwe woord zin in de lijst!")
    print(lijst)

def delete_woord():
    index = int(input("het woord op welke index wilt u verwijderen:"))
    lijst.pop(index)
    print(lijst)

def lijst_naar_dic():
    print("The original list is : " + str(lijst))
    K = "W"
    res = dict.fromkeys(lijst, K)
    res = {key: K + key for key in res}
    print("The constructed Dictionary : ", res)

#invoer#
def gebruikers_invoer():
    invoer = input("geef je keuze in")
    return invoer
#invoer#

def keuzes():
    print("1: voeg een woord toe")
    print("2: verwijder een woord")
    print("3: zet de lijst om naar een dictionary")
    invoer = gebruikers_invoer()
    while not invoer == "stop":
        if invoer == "1":
            nieuw_woord()
        elif invoer == "2":
            delete_woord()
        elif invoer == "3":
            lijst_naar_dic()
        else:
            print("Foutieve invoer")
        invoer = gebruikers_invoer()
    quit("Het programma word gestopt")

keuzes()