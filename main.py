from prettytable import PrettyTable
gidsen = {1: {"naam": "Jaap",
             "leeftijd": 25,
             "geslacht": "man",
             "loon": 2500,
             "steden": ["Amsterdam", "Rotterdam", "Den Haag"]},
           2: {"naam": "Max",
             "leeftijd": 28,
             "geslacht": "man",
             "loon": 3000,
             "steden": ["Utrecht", "Groningen", "Maastricht"]},
           3: {"naam": "Sandrien",
             "leeftijd": 24,
             "geslacht": "vrouw",
             "loon": 2000,
             "steden": ["Eindhoven", "Amsterdam", "Tilburg"]},
           4: {"naam": "Anna",
             "leeftijd": 23,
             "geslacht": "vrouw",
             "loon": 2500,
             "steden": ["Maastricht", "Apeldoorn", "Zwolle"]},
           5: {"naam": "Kay",
             "leeftijd": 29,
             "geslacht": "man",
             "loon": 3500,
             "steden": ["Enschede", "Haarlem", "Arnhem"]}}

admin = {"admin1": {"gebruikersnaam":"admin1", "wachtwoord":"admineen"}}

#invoer#
def gebruikers_invoer():
    invoer = input("geef je keuze in")
    return invoer
#invoer#

#functies
def gidsen_pretty_table(gidsen):
    gidsen_pretty_table = PrettyTable(["Id","Naam", "Leeftijd", "Geslacht", "Loon", "Steden"])
    for key, value in gidsen.items():
        gidsen_pretty_table.add_row([key, value['naam'], value['leeftijd'], value['geslacht'], value['loon'], value['steden']])
    print(gidsen_pretty_table)

def geslacht_gidsen(gidsen):
  mannen = []
  vrouwen = []
  for gids in gidsen.values():
    if gids["geslacht"] == "man":
      mannen.append(gids["naam"])
    else:
      vrouwen.append(gids["naam"])
  print("mannen:",mannen)
  print("vrouwen:",vrouwen)

def tonen_gids_per_stad():
  stad = input("Op welke stad wilt u filteren.")
  gidsen_stad = []
  for gids in gidsen.values():
    if stad in gids["steden"]:
      gidsen_stad.append(gids)
  print(gidsen_stad)

def verdiensten_per_maand(gidsen):
    minimum = int(input("geef de minimun verdiensten in"))
    for gids in gidsen.values():
        if gids["loon"] >= minimum:
            print(gids["naam"],"verdient",gids["loon"])

def stad_gidsen():
    geslacht = input("Op welk geslacht wilt u filteren")
    stad = input("op welke stad wilt u filteren")
    resultaat = []
    for gids in gidsen.values():
        if gids["geslacht"] == geslacht and stad in gids["steden"]:
            resultaat.append(gids)
    print(resultaat)
#functies

#admin functies
def nieuwe_gids():
    naam = input("Geef de naam van de gids:")
    leeftijd = int(input("Geef de leeftijd van de gids:"))
    geslacht = input("Geef het geslacht van de gids (man/vrouw):")
    loon =  int(input("Geef het loon van de gids:"))
    steden = []
    gidsen[len(gidsen) + 1] = {"naam": naam, "leeftijd": leeftijd, "geslacht": geslacht, "loon": loon, "steden": steden}

    print("De nieuwe gids is toegevoegd aan de lijst!")
    gidsen_pretty_table(gidsen)

def stad_toevoegen():
  stad = input("Geef de naam van de stad die je aan de gids wil toevoegen: ")
  persoon = int(input("Geef het nummer van de gids waaraan je een stad wil toevoegen: "))
  gidsen[persoon]["steden"].append(stad)
  print("De stad is toegevoegd.")
  gidsen_pretty_table(gidsen)


def verwijder_een_gids(gidsen):
    id = int(input("Geef de id van de gids die je wilt verwijderen: "))
    del gidsen[id]
    print("Gids met id",id,"is succesvol verwijderd")
    gidsen_pretty_table(gidsen)

def voeg_een_stad_toe_iedereen():
    stad = input("welke stad wilt u toevoegen")
    for gids in gidsen.values():
        gids['steden'].append(stad)
    print(gidsen)
    gidsen_pretty_table(gidsen)

def verander_admin_wachtwoord(admin):
    gebruikersnaam = input("gebruikersnaam:")
    oudwachtwoord = input("oud wachtwoord:")
    nieuwwachtwoord = input("nieuw wachtwoord:")
    nieuwwachtwoord2 = input("bevestig nieuw wachtwoord:")

    if gebruikersnaam in admin and admin[gebruikersnaam]["wachtwoord"] == oudwachtwoord and nieuwwachtwoord == nieuwwachtwoord2:
        admin[gebruikersnaam]["wachtwoord"] = nieuwwachtwoord
        print("wachtwoord gewijzigd")
        print(admin)
    else:
        print("wachtwoord kon niet gewijzigd worden")


#menu
def menu():
    print("1: toon alle mannen/vrouwen gidsen.")
    print("2: toon alle gidsen die een bepaalde stad gidsen.")
    print("3: toon iedereen die meer verdient dan x per maand.")
    print("4: toon alle mannen of vrouwen die een stad gidsen.")
    invoer = gebruikers_invoer()
    while not invoer == "stop":
        if invoer == "1":
            geslacht_gidsen(gidsen)
        elif invoer == "2":
            tonen_gids_per_stad()
        elif invoer == "3":
            verdiensten_per_maand(gidsen)
        elif invoer == "4":
            stad_gidsen()
        else:
            print("foutieve invoer")
        invoer = gebruikers_invoer()
    keuzes()
#menu

#admin menu
def admin_menu():
    print("========Admin========")
    gebruikersnaam = input("Gebruikersnaam:")
    wachtwoord = input("Wachtwoord: ")
    if gebruikersnaam in admin and admin[gebruikersnaam]["wachtwoord"] == wachtwoord:
        print("1: Voeg een gids toe.")
        print("2: Voeg een stad toe aan een gids.")
        print("3: Verwijder een gids. ")
        print("4: Voeg een stad toe voor elke gids")
        print("5: Verander het wachtwoord van een admin")
        invoer = gebruikers_invoer()
        while not invoer == "stop":
            if invoer == "1":
                nieuwe_gids()
            elif invoer == "2":
                stad_toevoegen()
            elif invoer == "3":
                verwijder_een_gids(gidsen)
            elif invoer == "4":
                voeg_een_stad_toe_iedereen()
            elif invoer == "5":
                verander_admin_wachtwoord(admin)
            else:
                print("foutieve invoer")
            invoer = gebruikers_invoer()
        keuzes()
    else:
        print("De ingevoerde gegevens kloppen niet")
        keuzes()
#admin menu

#keuzes
def keuzes():
    print("1: Toon alle gidsen")
    print("2: Toon alle filters")
    print("3: Admin login")
    invoer = gebruikers_invoer()
    while not invoer == "stop":
        if invoer == "1":
            gidsen_pretty_table(gidsen)
        elif invoer == "2":
            menu()
        elif invoer == "3":
            admin_menu()
        else:
            print("Foutieve invoer")
        invoer = gebruikers_invoer()
    quit("Het programma word gestopt")
#keuzes

keuzes()