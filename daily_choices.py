import os
import sys


def q7():
    print("Wil je dit programma opnieuw starten? (y / n)")
    dontclose = input()
    if(dontclose == "y"):
        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
    elif(dontclose == "n"):
        sys.exit()
    else:
        print("Typ alstublieft 'y' of 'n' in.")

def q1():
    print("Het is een gloednieuwe minecraft wereld. Je start in de wereld zonder items. Wat doe je als eerst?")
    print("")
    print(" A. Je breekt wat bomen om hout te krijgen voor tools.")
    print(" B. Je begint met een huis te maken zo snel als je kan.")
    print(" C. Je wacht tot het avond is om mobs te gaan vechten.")
    a1 = input(" Kies 'A', 'B' of 'C' >>>>> ")
    if (a1 == "A"):
        print("")
        print("Je breekt een paar bomen en krijgt veel hout. Je gebruikt het om een pickaxe mee te maken en daarmee stone tools en cobblestone te krijgen.")
        print("")
    elif (a1 == "B"):
        print("")
        print("Je begint met dirt bij elkaar te verzamelen en kapt een paar bomen voor wat houten tools om zo snel mogelijk een veilig huis te kunnen maken.")
        print("")
    elif (a1 == "C"):
        print("")
        print("Je kiest om te wachten tot het nacht word zodat mobs spawnen. Wanneer het avond was werd je gedood door de meerdere mobs die waren gespawnt omdat je geen items had. Probeer Opnieuw.")
        print("")
        q7()
    else:
        print("")
        print("Kies alstublieft A, B of C.")
        print("")
        q1()
q1()

def q2():
    print("Je was door de avond gekomen met gemak. Maar nu is er een nieuwe probleem... Voedsel! Hoe wil je aan voedsel komen?")
    print("")
    print(" A. Eet de Rotten Flesh van de zombies die je hebt gekilled.")
    print(" B. Je start een farm met de Seeds die je krijgt van gras.")
    print(" C. Je zoekt naar Animals.")
    a2 = input(" Kies 'A', 'B' of 'C' >>>>> ")
    if (a2 == "A"):
        print("")
        print("Je besloot Rotten Flesh te eten. Je krijgt het hunger effect en voor dat je een oplossing kon vinden ging je dood door de honger. Probeer opnieuw")
        print("")
        q7()
    elif (a2 == "B"):
        print("")
        print("Je begint met gras te breken om seeds te krijgen en maakt een farm bij het water. Het duurde een tijdje tot het voledig gegroeid was maar je kon er gemakkelijk mee door met bread. Tijdens je zoektocht vond je ook wat Melons en besloot die aan je farm toe te voegen.")
        print("")
    elif (a2 == "C"):
        print("")
        print("Je ging op jacht naar Animals. Je vond een boel koeien en schapen. Beide handig voor meer dan alleen voedsel. Met de Leather kon je wat armor maken en met de wol kon je een bed maken om door de nachten te komen. Nadat je het vlees gekookt had had je meer dan genoeg voor een paar dagen.")
        print("")
    else:
        print("")
        print("Kies alstublieft A, B of C")
        print("")
        q2()
q2()

def q3():
    print("Je zit diep in een underground mine, op zoek naar iron en hopelijk andere handige ores. Bij nu was het al bijna avond. Niet handig voor wanneer je weer boven gronds komt... maar je zag een boel Iron Ore voor je. Wat zou je het beste kunnen doen?")
    print("")
    print(" A. Je pakt de iron en gaat snel weer naar boven.")
    print(" B. Je pakt de iron en gaat verder.")
    print(" C. Je laat de iron voor morgen.")
    a3 = input(" Kies 'A', 'B' of 'C' >>>>> ")
    if (a3 == "A"):
        print("")
        print("Je mined de Iron Ores zo snel als je kan en build weer terug naar boven naar veiligheid. Je was net op tijd binnen voor dat de mobs begonnen te spawnen.")
        print("")
    elif (a3 == "B"):
        print("")
        print("Je mined de Iron Ore en gaat door met zoeken voor Iron en andere ores. Er waren zoveel mobs in de mines dat je moest terugtrekken met laag HP. Maar het moment dat je bovengronds kwam werd je gedood door de mobs die waren gespawnt omdat het avond was. Probeer opnieuw.")
        print("")
        q7()
    elif (a3 == "C"):
        print("")
        print("Je laat de Iron Ore liggen en build omhoog. Je had meer dan genoeg tijd om naar binnen te gaan gelukkig. Volgende dag ga je weer terug de mine in en haal je de Iron Ore op.")
        print("")
    else:
        print("")
        print("Kies alstublieft A, B of C.")
        print("")
        q3()
q3()

def q5():
    print("Nadat je voledig Iron Armor en tools hebt gemaakt was het tijd om naar de Nether te gaan. Maar hoe ga je de portal maken?")
    print("")
    print(" A. Je zoekt naar diamonds om een diamond pickaxe mee te maken zodat je obsidian kan breken en de portal mee maken.")
    print(" B. Je probeert een speedrun trucje om de portal te maken.")
    print(" C. Je zoekt naar een gebroken Nether portal en maakt de ontbrekende obsidian blokken met water en lava.")
    a5 = input(" Kies 'A', 'B' of 'C' >>>>> ")
    if (a5 == "A"):
        print("")
        print("Je gaat de mines in en zoekt naar diamond. Na een tijdje vondt je 3 diamonds en maakte er een diamond pickaxe mee om obsidian te breken en de portal te bouwen. Na dat je dat hebt gedaan stapte je naar binnen. De Nether in.")
        print("")
        print("Volgende Hoofdstuk: The Nether.")
        print("")
        print("Einde van Hoofdstuk 1.")
        print("")
        print("Druk op ENTER om programma af te sluiten.")
        dontclose0 = input()
    elif (a5 == "B"):
        print("")
        print("Je probeert een trucje wat je op internet hebt gezien van Minecraft speedrunners. Ze plaatsen blokken, water en lava op de juiste plekjes om heel makkelijk en snel een portal te maken. Je probeerde het een paar keer zelf maar het ging vaak mis. Je besloot om op te zoeken hoe het moet en na een guide was het gelukt. Na dat stapte je de portan in. De Nether in.")
        print("")
        print("Volgende Hoofdstuk: The Nether.")
        print("")
        print("Einde van Hoofdstuk 1.")
        print("")
        print("Druk op ENTER om programma af te sluiten.")
        dontclose1 = input()

    elif (a5 == "C"):
        print("")
        print("Je besluit om te zoeken bovengronds naar gebroken portal structures die spawnen in elke biome. Na veel moeite had je er 2 kunnen vinden. De eerste ging fout met hoe je de obsidian plaatste maar de tweede ging goed. Nadat je de portal hebt gehersteld stapje je naar binnen. De Nether in.")
        print("")
        print("Volgende Hoofdstuk: The Nether.")
        print("")
        print("Einde van Hoofdstuk 1.")
        print("")
        print("Druk op ENTER om programma af te sluiten.")
        dontclose2 = input()
    else:
        print("")
        print("Kies alstublieft A, B of C.")
        print("")
        q5()
q5()
