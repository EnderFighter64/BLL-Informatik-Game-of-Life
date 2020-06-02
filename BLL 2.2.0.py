from tkinter import *
from random import randint
# Sollte das Programm nicht funktioneren, dann probieren Sie bitte aus, Zeilen 2553, 2609 und 3152 oder 3248 zu entfernen.
# Der Spieler interagiert mit einer Zelle. Dies wird hier verarbeitet.
def ZelleFarbwechselAllgemein(Zellfarbe, PositionAlpha):
    global Position
    Position = PositionAlpha
    # Währenddessen die KI am Zug ist oder wenn die Runde beendet worden ist, dann soll sich nichts mehr ändert.
    if ZelleFarbwechselAktiviert == True: 
        global ResetZelle
        global ResetZelleFarbe
        if ResetZelle[0] == Position[0] and ResetZelle[1] == Position[1]:
            # Der Zug des Spielers wird rückgängig gemacht, wenn der Spieler eine Zelle anklickt, die er zuvor erschaffen oder getötet hat.
            if ResetZelleFarbe == 'red':
                Zellfarbe = 'red'
            if ResetZelleFarbe == 'blue':
                Zellfarbe = 'blue'
            if ResetZelleFarbe == 'black':
                Zellfarbe = 'black'
            Reset()
        else:
            global PositionsVermerkZweiZwei
            global PositionsVermerkZweiDrei
            global SpielerZugTyp
            global SpielerAmZug
            global Farbe
            global ZugBeendet
            global FarbaendrungDurchWechsel
            global Farbaenderung
            # Bei dem Erschaffen einer neuen Zelle wurde eine Zelle, die als erstes geopfert wurde, erneut angeklickt.
            if Position[0] == PositionsVermerkZweiZwei[0] and Position[1] == PositionsVermerkZweiZwei[1]:
                if not PositionsVermerkZweiZwei[2] == 0:
                    # Die Zelle wird nicht mehr geopfert.
                    FarbaendrungDurchWechsel = True
                    SpielerZugTyp = SpielerZugTyp - 1
                    PositionsVermerkZweiZwei = [-1, -1, 0]
                    ZugBeendet = False
                    if not PositionsVermerkZweiDrei[2] == 0:
                        # Wurde eine zweite Zelle schon geopfert, dann ist es nun die erste Zelle, die opfert wurde.
                        PositionsVermerkZweiZwei[0] = PositionsVermerkZweiDrei[0]
                        PositionsVermerkZweiZwei[1] = PositionsVermerkZweiDrei[1]
                        PositionsVermerkZweiZwei[2] = PositionsVermerkZweiDrei[2]
                        PositionsVermerkZweiDrei = [-1, -1, 0]
                        # Die Zelle, die ans Leben kommt, ändert seine Farbe.
                        if SpielerAmZug == 1:
                            Farbaenderung[2] = 'orange'
                        else:
                            Farbaenderung[2] = 'lightblue'
                    else:
                        Farbaenderung[2] = 'white'
            elif Position[0] == PositionsVermerkZweiDrei[0] and Position[1] == PositionsVermerkZweiDrei[1]:                
                # Bei dem Erschaffen einer neuen Zelle wurde die Zelle, die als zweites geopfert wurde, erneut angeklickt.
                if not PositionsVermerkZweiDrei[2] == 0:
                    # Die Zelle wird nicht mehr geopfert
                    FarbaendrungDurchWechsel = True
                    SpielerZugTyp = SpielerZugTyp - 1
                    ZugBeendet = False
                    if SpielerAmZug == 1:
                        Farbaenderung[2] = 'orange'
                    else:
                        Farbaenderung[2] = 'lightblue'
                    PositionsVermerkZweiDrei = [0, 0, 0]
            else:
                global ButtonAendern
                # Im Tutorialmodus ändern sich die Zellen auf eine andere Art und Weise.
                if ButtonAendern == True:   
                    # Tote Zellen werden lebendig und nehmen die Farbe des 1. Spielers an.
                    if Zellfarbe == 'black':
                        Zellfarbe = 'red'
                    # Lebendige Zellen des 1. Spielers werden zu lebendigen Zellen des 2. Spielers.
                    elif Zellfarbe == 'red':
                        Zellfarbe = 'blue'
                    # Lebendige Zellen des 2. Spielers sterben.
                    elif Zellfarbe == 'blue':
                        Zellfarbe = 'black'
                else:
                    if SpielerZugTyp < 2:
                        if not Zellfarbe == 'black':
                            # Eine Zelle wird getötet
                            # Falls eine Zelle vorher getötet wurde, kommt sie wieder ans Leben. Die Speicherung aus dem PositionsVermerkEins wird geladen.
                            Farbe[PositionsVermerkEins[0]][PositionsVermerkEins[1]] = PositionsVermerkEins[2]
                            PositionsVermerkEins[0] = Position[0]
                            PositionsVermerkEins[1] = Position[1]
                            PositionsVermerkEins[2] = Zellfarbe
                            ZugBeendet = True
                            global NeuGenerierung
                            NeuGenerierung = True
                            SpielerZugTyp = 1
                            global ResetbuttonSpawnbar
                            ResetbuttonSpawnbar = True
                            ResetZelle = [PositionsVermerkEins[0], PositionsVermerkEins[1]]
                            # Die vom Spieler getötete Zelle wird in PositionsVermerkEins gespeichert.
                            if Zellfarbe == 'red':
                                ResetZelleFarbe = 'red'
                            if Zellfarbe == 'blue':
                                ResetZelleFarbe = 'blue'
                            # Die Zelle wird getötet
                            Zellfarbe = 'black'
                        else:
                            # Eine neue Zelle wird geboren, ohne dass eine bisher getötet wurde.
                            ZelleZumLebenBringenNrEins(Zellfarbe)
                    else:
                        # Eine Zelle wird zum Leben gebracht und der Spieler klickt eine andere Zelle an.
                        ZelleZumLebenBringen(Zellfarbe)
            Fenster.quit()
    return(Zellfarbe)

def ZelleZumLebenBringenNrEins(Zellfarbe):
    # Eine Zelle wird geboren, ohne dass eine getötet wurde
    global SpielerZugTyp
    global ResetZelle
    global ResetZelleFarbe
    global Farbe
    global Position
    if SpielerZugTyp == 1:
        Reset()
    SpielerZugTyp = 2
    global ResetbuttonSpawnbar
    ResetbuttonSpawnbar = True
    global PositionsVermerkZweiEins
    # Position der Zelle wird in PositionsVermerkZweiEins gespeichert.
    PositionsVermerkZweiEins[0] = Position[0]
    PositionsVermerkZweiEins[1] = Position[1]
    PositionsVermerkZweiEins[2] = 'black'
    Farbe[Position[0]][Position[1]] = 'red'
    global Farbaenderung
    # Die neu erschaffene Zelle wird weiß gemacht.
    Farbaenderung[0] = Position[0]
    Farbaenderung[1] = Position[1]
    Farbaenderung[2] = 'white'
    ResetZelle = [Position[0], Position[1]]
    ResetZelleFarbe = 'black'
    

def ZelleZumLebenBringen(Zellfarbe): 
    # Eine Zelle wird zum Leben gebracht und der Spieler klickt eine andere Zelle an.
    global SpielerAmZug
    global Farbe
    global Position
    global PositionsVermerkZweiZwei
    global PositionsVermerkZweiDrei
    global SpielerZugTyp
    if SpielerAmZug == 1:
        Spieler = 'red'
    else:
        Spieler = 'blue'
    # Der Spieler klickt eine schwarze Zelle an. Diese Zelle ist jetzt die Zelle, die zum Leben gebracht wird.
    if Farbe[Position[0]][Position[1]] == 'black':
        WeissAenderungZulassen = True
        if not PositionsVermerkZweiZwei[2] == 0:
            if PositionsVermerkZweiZwei[0] == Position[0] and PositionsVermerkZweiZwei[1] == Position[1]:
                WeissAenderungZulassen = False
            if not PositionsVermerkZweiDrei[2] == 0:
                if PositionsVermerkZweiDrei[0] == Position[0] and PositionsVermerkZweiDrei[1] == Position[1]:
                    WeissAenderungZulassen = False
        if WeissAenderungZulassen == True:
            WeissAenderung()
    # Der Spieler hat bereits eine Zelle geopfert und opfert nun eine Zweite. Der Zug kann nun beendet werden.
    if SpielerZugTyp == 3:
        if Farbe[Position[0]][Position[1]] == Spieler:
            SpielerZugTyp = 4
            global ZugBeendet
            ZugBeendet = True
            PositionsVermerkZweiDrei[0] = Position[0]
            PositionsVermerkZweiDrei[1] = Position[1]
            PositionsVermerkZweiDrei[2] = Spieler
            if SpielerAmZug == 1:
                Farbaenderung[2] = 'red'
            else:
                Farbaenderung[2] = 'blue'
    # Der Spieler hat noch keine Zelle geopfert und opfert jetzt die Erste.
    if SpielerZugTyp == 2:
        if Farbe[Position[0]][Position[1]] == Spieler:
            SpielerZugTyp = 3
            PositionsVermerkZweiZwei[0] = Position[0]
            PositionsVermerkZweiZwei[1] = Position[1]
            PositionsVermerkZweiZwei[2] = Spieler
            if SpielerAmZug == 1:
                Farbaenderung[2] = 'orange'
            else:
                Farbaenderung[2] = 'lightblue'
    
def WeissAenderung():
    # Der Spieler möchte eine andere Zelle zum Leben bringen.
    global PositionsVermerkZweiEins
    global Position
    global Farbe
    global VerschiebungvonWeiss
    global Farbentfernung
    global ResetZelle
    ResetZelle = [Position[0], Position[1]]
    Farbentfernung[0] = PositionsVermerkZweiEins[0]
    Farbentfernung[1] = PositionsVermerkZweiEins[1]
    VerschiebungvonWeiss = True
    PositionsVermerkZweiEins[0] = Position[0]
    PositionsVermerkZweiEins[1] = Position[1]
    global Farbaenderung
    Farbaenderung[0] = Position[0]
    Farbaenderung[1] = Position[1]    

def FarbaenderungDavor():
    # Sorgt dafür, dass neu erschaffene Zellen ihre jeweilige Farbe erhalten.
    global Farbaenderung
    global Farbe
    global SpielerAmZug
    if SpielerAmZug == 1:
        Spieler = 'red'
    else:
        Spieler = 'blue'
    FarbManipulation = Farbe[:]
    FarbManipulation[Farbaenderung[0]][Farbaenderung[1]] = Spieler
    FarbeSup=Generation(FarbManipulation)
    if not FarbeSup == 'black':
        global xManipulation
        xManipulation = [Farbaenderung[0],Farbaenderung[1],FarbeSup[Farbaenderung[0]][Farbaenderung[1]]]
    if not Farbaenderung[2] == 0:
        Farbe[Farbaenderung[0]][Farbaenderung[1]] = Farbaenderung[2]
        
def FarbaenderungDanach():
    # Verhindert, dass dem Benutzer mehr neu erschaffene Zellen angezeigt werden als es sollte.
    global Farbaenderung
    global Farbentfernung
    if not Farbaenderung[2] == 0:
        Farbe[Farbaenderung[0]][Farbaenderung[1]] = 'black'
    if not Farbentfernung[0] == -1:
        Farbe[Farbentfernung[0]][Farbentfernung[1]] = 'black'
        
def NextGen():
    # Der Spieler hat auf den Button "Zug Beenden" geklickt.
    global ZugBeendet
    if ZugBeendet == True:
        global NochImZug
        NochImZug = False
        Fenster.quit()
        
def Reset():
    # Hier wird der Zug des Spielers rückgängig gemacht. Alle vorherigen Aktionen werden zurückgesetzt.
    global NeuGenerierung
    global SpielerZugTyp
    global PositionsVermerkEins
    global PositionsVermerkZweiEins
    global PositionsVermerkZweiZwei
    global PositionsVermerkZweiDrei
    global Farbe
    global FarbeAAVermerk
    global SpielerAmZug
    # Die Zelle, die der Spieler getötet hat, kommt ans Leben.
    if not PositionsVermerkEins[2] == 0:
        Farbe[PositionsVermerkEins[0]][PositionsVermerkEins[1]] = PositionsVermerkEins[2]
        PositionsVermerkEins = [-1, -2, 0]
    # Die Zelle, die der Spieler ans Leben gebracht hat, wird getötet.
    if not PositionsVermerkZweiEins[2] == 0:
        Farbe[PositionsVermerkZweiEins[0]][PositionsVermerkZweiEins[1]] = 'black'
    PositionsVermerkZweiEins = [-1, -1, 0]
    # Die Zelle, die der Spieler für das Erschaffen einer anderen Zelle als erstes geopfert hat, wird wieder ans Leben gebracht.
    if not PositionsVermerkZweiZwei[2] == 0:
        if SpielerAmZug == 1:
            Farbe[PositionsVermerkZweiZwei[0]][PositionsVermerkZweiZwei[1]] = 'red'
        else:
            Farbe[PositionsVermerkZweiZwei[0]][PositionsVermerkZweiZwei[1]] = 'blue'
    PositionsVermerkZweiZwei = [-1, -1, 0]
    # Die Zelle ,die der Spieler für das Erschaffen einer anderen Zelle als zweites geopfert hat, wird wieder ans Leben gebracht.
    if not PositionsVermerkZweiDrei[2] == 0:
        if SpielerAmZug == 1:
            Farbe[PositionsVermerkZweiDrei[0]][PositionsVermerkZweiDrei[1]] = 'red'
        else:
            Farbe[PositionsVermerkZweiDrei[0]][PositionsVermerkZweiDrei[1]] = 'blue'
    PositionsVermerkDreiDrei = [-1, -1, 0]
    SpielerZugTyp = 0
    NeuGenerierung = True
    global ZugBeendet
    ZugBeendet = False
    global ResetbuttonSpawnbar
    ResetbuttonSpawnbar = False
    global ResetZelle
    ResetZelle = [-1, -1]
    Fenster.quit()
    global Farbaenderung
    Farbaenderung = [-1, -2, 0]
    global Farbentfernung
    Farbentfernung = [-1, -1]

# Hier wird ermittelt, wie viele Zellen von Spieler 1 noch vorhanden sind.
def RotErmittlung():
    global Farbe
    global SpielBrettLaenge
    RoteZellen = 0
    Index = 0
    while Index < SpielBrettLaenge:
        SupIndex = 0
        while SupIndex < SpielBrettLaenge:
            if Farbe[Index][SupIndex] == 'red':
                RoteZellen = RoteZellen + 1
            SupIndex = SupIndex + 1
        Index = Index + 1
    return(RoteZellen)

# Hier wird ermittelt, wie viele Zellen von Spieler 2 noch vorhanden sind.
def BlauErmittlung():
    global Farbe
    global SpielBrettLaenge
    BlaueZellen = 0
    Index = 0
    while Index < SpielBrettLaenge:
        SupIndex = 0
        while SupIndex < SpielBrettLaenge:
            if Farbe[Index][SupIndex] == 'blue':
                BlaueZellen = BlaueZellen + 1
            SupIndex = SupIndex + 1
        Index = Index + 1
    return(BlaueZellen)
    
# Hier wird das entsprechende Menu generiert , wenn der Spieler am Zug ist.
def Spielerzug():
    # Wichtige Variablen werden generiert.
    global SpielerFarbe
    global NochImZug
    global ErstmaligeGenerierung
    global NeuGenerierung
    global PositionsVermerk
    global ZugBeendenButton
    global RueckgaengigButton
    global ZugBeendet
    global SpielerAmZug
    global Farbe
    global SpielBrettLaenge
    ZugBeendet = False
    global ResetbuttonSpawnbar
    global SpielerZugTyp
    global PositionsVermerkZweiDrei
    ResetbuttonSpawnbar = False
    NochImZug = True
    ErstmaligeGenerierung = True
    NeuGenerierung = False
    global VerschiebungvonWeiss
    VerschiebungvonWeiss = False
    global FarbaendrungDurchWechsel
    FarbaendrungDurchWechsel = False
    while NochImZug == True:
        # Der Spieler verweilt so lange in dieser while-Schleife, bis er seinen Zug beendet.
        if ErstmaligeGenerierung == True:
            AnzahlRoterZellen=RotErmittlung()
            AnzahlBlauerZellen=BlauErmittlung()
            # Die Label, die dem Benutzer mitteilt, wie viele Zellen von den beiden Spielern noch am Leben sind, werden generiert.
            if SpielerFarbe[0] == 'red':
                RotLabelText = 'Anzahl roter Zellen: ' + str(AnzahlRoterZellen)
            if SpielerFarbe[0] == 'blue':
                RotLabelText = 'Anzahl blauer Zellen: ' + str(AnzahlRoterZellen)
            if SpielerFarbe[0] == 'yellow':
                RotLabelText = 'Anzahl gelber Zellen: ' + str(AnzahlRoterZellen)
            if SpielerFarbe[0] == 'green':
                RotLabelText = 'Anzahl grüner Zellen: ' + str(AnzahlRoterZellen)
            if SpielerFarbe[1] == 'red':
                BlauLabelText = 'Anzahl roter Zellen: ' + str(AnzahlBlauerZellen)
            if SpielerFarbe[1] == 'blue':
                BlauLabelText = 'Anzahl blauer Zellen: ' + str(AnzahlBlauerZellen)
            if SpielerFarbe[1] == 'yellow':
                BlauLabelText = 'Anzahl gelber Zellen: ' + str(AnzahlBlauerZellen)
            if SpielerFarbe[1] == 'green':
                BlauLabelText = 'Anzahl grüner Zellen: ' + str(AnzahlBlauerZellen)
            RotLabelFarbe = SpielerFarbe[0]
            if RotLabelFarbe == 'yellow':
                RotLabelFarbe = '#968A08'
            BlauLabelFarbe = SpielerFarbe[1]
            if BlauLabelFarbe == 'yellow':
                BlauLabelFarbe = '#968A08'
            RotLabel = Label(Fenster, fg=RotLabelFarbe, text=RotLabelText)
            BlauLabel = Label(Fenster, fg=BlauLabelFarbe, text=BlauLabelText)
            RotLabel.config(font=('Black_Arial', 17))
            BlauLabel.config(font=('Black_Arial', 17))
            RotLabel.place(x=777, y=150)
            BlauLabel.place(x=777, y=190)
            ErstmaligeGenerierung = False
        # Das Label, welches dem Benutzer mitteilt, welcher Spieler gerade am Zug ist, wird generiert.
        if SpielerAmZug == 1:
            # Spieler 1 ist am Zug.
            DieserSpielerIstAmZugFarbe = SpielerFarbe[0]
            if DieserSpielerIstAmZugFarbe == 'yellow':
                DieserSpielerIstAmZugFarbe = '#968A08'
            DieserSpielerIstAmZug = Label(Fenster, text='Spieler 1 ist am Zug', fg=DieserSpielerIstAmZugFarbe)
            DieserSpielerIstAmZug.config(font=('Black_Arial', 20))
            DieserSpielerIstAmZug.place(x=767, y=40)
        else:
            # Spieler 2 ist am Zug.
            DieserSpielerIstAmZugFarbe = SpielerFarbe[1]
            if DieserSpielerIstAmZugFarbe == 'yellow':
                DieserSpielerIstAmZugFarbe = '#968A08'
            DieserSpielerIstAmZug = Label(Fenster, text='Spieler 2 ist am Zug', fg=DieserSpielerIstAmZugFarbe)
            DieserSpielerIstAmZug.config(font=('Black_Arial', 20))
            DieserSpielerIstAmZug.place(x=767, y=40)
        # Der "Rückgängig machen" Knopf wird generiert.
        RueckgaengigButton = Button(Fenster, bg='grey', text='Rückgängig machen', command=Reset, fg='black')
        RueckgaengigButton.config(font=('Black_Arial', 17))
        if ResetbuttonSpawnbar == True:
            # Der "Rückgängig machen" Knopf wird platziert, wenn der Spieler bereits eine Aktion vorgenommen hat.
            RueckgaengigButton.place(x=785, y=330)
        # Der "Zug Beenden" Knopf wird generiert.
        ZugBeendenButton = Button(Fenster, bg='lightgrey', text='Zug Beenden', command=NextGen, fg='black')
        ZugBeendenButton.config(font=('Black_Arial', 20))
        if ZugBeendet == True:
            # Der "Zug Beenden" Knopf wird platziert, wenn der Zug beendet werden kann.
            ZugBeendenButton.place(x=800, y=250)
        if SpielerZugTyp == 2:
            PositionsVermerkZweiDrei = [-1, -1, 0]
        if not PositionsVermerkZweiZwei[2] == 0:
            if SpielerZugTyp > 1:
                Farbe[PositionsVermerkZweiZwei[0]][PositionsVermerkZweiZwei[1]] = 'black'
        if not PositionsVermerkZweiDrei[2] == 0:
            if SpielerZugTyp > 2:
                Farbe[PositionsVermerkZweiDrei[0]][PositionsVermerkZweiDrei[1]] = 'black'
        FarbaenderungDavor()
        ButtonsSpawner()
        Fenster.mainloop()
        # Hier hat der Spieler seine Aktion schon gemacht.
        global Position
        if FarbaendrungDurchWechsel == True:
            FarbaendrungDurchWechsel = False
            if SpielerAmZug == 1:
                Farbe[Position[0]][Position[1]] = 'red'
            else:
                Farbe[Position[0]][Position[1]] = 'blue'
        if VerschiebungvonWeiss == True:
            VerschiebungvonWeiss = False
            Farbe[Position[0]][Position[1]] = 'red'
        FarbaenderungDanach()
        DieserSpielerIstAmZug.destroy()
        ZugBeendenButton.destroy()
        RueckgaengigButton.destroy()
    # Der Spieler hat seinen Zug beendet.
    RotLabel.destroy()
    BlauLabel.destroy()
    global ImSpiel
    if ImSpiel == True:
        if SpielerZugTyp == 4:
            if SpielerAmZug == 1:
                Spieler = 'red'
            else:
                Spieler = 'blue'
            Farbe[PositionsVermerkZweiEins[0]][PositionsVermerkZweiEins[1]] = Spieler
        # Es wird gezählt, wie viele lebenden Zellen jeder Spieler noch hat.
        AnzahlRoterZellen=RotErmittlung()
        AnzahlBlauerZellen=BlauErmittlung()
        Farbe=Generation(Farbe)
        if SpielerAmZug == 1:
            SpielerAmZug = 2
        else:
            SpielerAmZug = 1
        ZugBeendenButton.destroy()
        RueckgaengigButton.destroy()
        Gewinncheck()
    
def Gewinncheck():
    # Hier wird überprüft, ob ein Spieler schon gewonnen hat.
    global ImSpiel
    global GewinnerLabel
    global SpielerFarbe
    AnzahlRoterZellen=RotErmittlung()
    AnzahlBlauerZellen=BlauErmittlung()
    if AnzahlRoterZellen == 0:
        # Spieler 1 hat keine lebenden Zellen mehr.
        if AnzahlBlauerZellen == 0:
            # Spieler 2 hat auch keine lebenden Zellen mehr. Es ist ein Unendschieden. Das entsprechene Label wird generiert.
            ImSpiel = False
            GewinnerLabel = Label(Fenster, text='Unentschieden!')
            GewinnerLabel.config(font=('Black_Arial', 20), fg='black')
            GewinnerLabel.place(x=794, y=210)
        else:
            # Spieler 2 hat noch Zellen. Spieler 2 gewinnt. Das entsprechene Label wird generiert.
            ImSpiel = False
            if SpielerFarbe[1] == 'red':
                GewinnerLabelText = 'Rot hat gewonnen'
            if SpielerFarbe[1] == 'blue':
                GewinnerLabelText = 'Blau hat gewonnen'
            if SpielerFarbe[1] == 'yellow':
                GewinnerLabelText = 'Gelb hat gewonnen'
            if SpielerFarbe[1] == 'green':
                GewinnerLabelText = 'Grün hat gewonnen'
            GewinnerLabelFarbe = SpielerFarbe[1]
            if GewinnerLabelFarbe == 'yellow':
                GewinnerLabelFarbe = '#968A08'
            GewinnerLabel = Label(Fenster, text=GewinnerLabelText)
            GewinnerLabel.config(font=('Black_Arial', 20), fg=GewinnerLabelFarbe)
            GewinnerLabel.place(x=772, y=210)
    else:
        if AnzahlBlauerZellen == 0:
            # Spieler 2 hat keine Zellen mehr und Spieler 1 hat noch Zellen. Spieler 1 gewinnt. Das entsprechene Label wird generiert.
            ImSpiel = False
            if SpielerFarbe[0] == 'red':
                GewinnerLabelText = 'Rot hat gewonnen'
            if SpielerFarbe[0] == 'blue':
                GewinnerLabelText = 'Blau hat gewonnen'
            if SpielerFarbe[0] == 'yellow':
                GewinnerLabelText = 'Gelb hat gewonnen'
            if SpielerFarbe[0] == 'green':
                GewinnerLabelText = 'Grün hat gewonnen'
            GewinnerLabelFarbe = SpielerFarbe[0]
            if GewinnerLabelFarbe == 'yellow':
                GewinnerLabelFarbe = '#968A08'
            GewinnerLabel = Label(Fenster, text=GewinnerLabelText)
            GewinnerLabel.config(font=('Black_Arial', 20), fg=GewinnerLabelFarbe)
            GewinnerLabel.place(x=779, y=210)
        
# Wenn der Spieler eine Zelle anklickt, dann wird das hier erfasst und der Befehl wird zu Zeile 5 weitergeleitet.  
def ZelleAAFarbwechsel():
    Position = [0, 0]
    Farbe[0][0]=ZelleFarbwechselAllgemein(Farbe[0][0], Position)
def ZelleABFarbwechsel():
    Position = [0, 1]
    Farbe[0][1]=ZelleFarbwechselAllgemein(Farbe[0][1], Position)
def ZelleACFarbwechsel():
    Position = [0, 2]
    Farbe[0][2]=ZelleFarbwechselAllgemein(Farbe[0][2], Position)
def ZelleADFarbwechsel():
    Position = [0, 3]
    Farbe[0][3]=ZelleFarbwechselAllgemein(Farbe[0][3], Position)
def ZelleAEFarbwechsel():
    Position = [0, 4]
    Farbe[0][4]=ZelleFarbwechselAllgemein(Farbe[0][4], Position)
def ZelleAFFarbwechsel():
    Position = [0, 5]
    Farbe[0][5]=ZelleFarbwechselAllgemein(Farbe[0][5], Position)
def ZelleAGFarbwechsel():
    Position = [0, 6]
    Farbe[0][6]=ZelleFarbwechselAllgemein(Farbe[0][6], Position)
def ZelleAHFarbwechsel():
    Position = [0, 7]
    Farbe[0][7]=ZelleFarbwechselAllgemein(Farbe[0][7], Position)
def ZelleBAFarbwechsel():
    Position = [1, 0]
    Farbe[1][0]=ZelleFarbwechselAllgemein(Farbe[1][0], Position)
def ZelleBBFarbwechsel():
    Position = [1, 1]
    Farbe[1][1]=ZelleFarbwechselAllgemein(Farbe[1][1], Position)
def ZelleBCFarbwechsel():
    Position = [1, 2]
    Farbe[1][2]=ZelleFarbwechselAllgemein(Farbe[1][2], Position)
def ZelleBDFarbwechsel():
    Position = [1, 3]
    Farbe[1][3]=ZelleFarbwechselAllgemein(Farbe[1][3], Position)
def ZelleBEFarbwechsel():
    Position = [1, 4]
    Farbe[1][4]=ZelleFarbwechselAllgemein(Farbe[1][4], Position)
def ZelleBFFarbwechsel():
    Position = [1, 5]
    Farbe[1][5]=ZelleFarbwechselAllgemein(Farbe[1][5], Position)
def ZelleBGFarbwechsel():
    Position = [1, 6]
    Farbe[1][6]=ZelleFarbwechselAllgemein(Farbe[1][6], Position)
def ZelleBHFarbwechsel():
    Position = [1, 7]
    Farbe[1][7]=ZelleFarbwechselAllgemein(Farbe[1][7], Position)
def ZelleCAFarbwechsel():
    Position = [2, 0]
    Farbe[2][0]=ZelleFarbwechselAllgemein(Farbe[2][0], Position)
def ZelleCBFarbwechsel():
    Position = [2, 1]
    Farbe[2][1]=ZelleFarbwechselAllgemein(Farbe[2][1], Position)
def ZelleCCFarbwechsel():
    Position = [2, 2]
    Farbe[2][2]=ZelleFarbwechselAllgemein(Farbe[2][2], Position)
def ZelleCDFarbwechsel():
    Position = [2, 3]
    Farbe[2][3]=ZelleFarbwechselAllgemein(Farbe[2][3], Position)
def ZelleCEFarbwechsel():
    Position = [2, 4]
    Farbe[2][4]=ZelleFarbwechselAllgemein(Farbe[2][4], Position)
def ZelleCFFarbwechsel():
    Position = [2, 5]
    Farbe[2][5]=ZelleFarbwechselAllgemein(Farbe[2][5], Position)
def ZelleCGFarbwechsel():
    Position = [2, 6]
    Farbe[2][6]=ZelleFarbwechselAllgemein(Farbe[2][6], Position)
def ZelleCHFarbwechsel():
    Position = [2, 7]
    Farbe[2][7]=ZelleFarbwechselAllgemein(Farbe[2][7], Position)
def ZelleDAFarbwechsel():
    Position = [3, 0]
    Farbe[3][0]=ZelleFarbwechselAllgemein(Farbe[3][0], Position)
def ZelleDBFarbwechsel():
    Position = [3, 1]
    Farbe[3][1]=ZelleFarbwechselAllgemein(Farbe[3][1], Position)
def ZelleDCFarbwechsel():
    Position = [3, 2]
    Farbe[3][2]=ZelleFarbwechselAllgemein(Farbe[3][2], Position)
def ZelleDDFarbwechsel():
    Position = [3, 3]
    Farbe[3][3]=ZelleFarbwechselAllgemein(Farbe[3][3], Position)
def ZelleDEFarbwechsel():
    Position = [3, 4]
    Farbe[3][4]=ZelleFarbwechselAllgemein(Farbe[3][4], Position)
def ZelleDFFarbwechsel():
    Position = [3, 5]
    Farbe[3][5]=ZelleFarbwechselAllgemein(Farbe[3][5], Position)
def ZelleDGFarbwechsel():
    Position = [3, 6]
    Farbe[3][6]=ZelleFarbwechselAllgemein(Farbe[3][6], Position)
def ZelleDHFarbwechsel():
    Position = [3, 7]
    Farbe[3][7]=ZelleFarbwechselAllgemein(Farbe[3][7], Position)
def ZelleEAFarbwechsel():
    Position = [4, 0]
    Farbe[4][0]=ZelleFarbwechselAllgemein(Farbe[4][0], Position)
def ZelleEBFarbwechsel():
    Position = [4, 1]
    Farbe[4][1]=ZelleFarbwechselAllgemein(Farbe[4][1], Position)
def ZelleECFarbwechsel():
    Position = [4, 2]
    Farbe[4][2]=ZelleFarbwechselAllgemein(Farbe[4][2], Position)
def ZelleEDFarbwechsel():
    Position = [4, 3]
    Farbe[4][3]=ZelleFarbwechselAllgemein(Farbe[4][3], Position)
def ZelleEEFarbwechsel():
    Position = [4, 4]
    Farbe[4][4]=ZelleFarbwechselAllgemein(Farbe[4][4], Position)
def ZelleEFFarbwechsel():
    Position = [4, 5]
    Farbe[4][5]=ZelleFarbwechselAllgemein(Farbe[4][5], Position)
def ZelleEGFarbwechsel():
    Position = [4, 6]
    Farbe[4][6]=ZelleFarbwechselAllgemein(Farbe[4][6], Position)
def ZelleEHFarbwechsel():
    Position = [4, 7]
    Farbe[4][7]=ZelleFarbwechselAllgemein(Farbe[4][7], Position)
def ZelleFAFarbwechsel():
    Position = [5, 0]
    Farbe[5][0]=ZelleFarbwechselAllgemein(Farbe[5][0], Position)
def ZelleFBFarbwechsel():
    Position = [5, 1]
    Farbe[5][1]=ZelleFarbwechselAllgemein(Farbe[5][1], Position)
def ZelleFCFarbwechsel():
    Position = [5, 2]
    Farbe[5][2]=ZelleFarbwechselAllgemein(Farbe[5][2], Position)
def ZelleFDFarbwechsel():
    Position = [5, 3]
    Farbe[5][3]=ZelleFarbwechselAllgemein(Farbe[5][3], Position)
def ZelleFEFarbwechsel():
    Position = [5, 4]
    Farbe[5][4]=ZelleFarbwechselAllgemein(Farbe[5][4], Position)
def ZelleFFFarbwechsel():
    Position = [5, 5]
    Farbe[5][5]=ZelleFarbwechselAllgemein(Farbe[5][5], Position)
def ZelleFGFarbwechsel():
    Position = [5, 6]
    Farbe[5][6]=ZelleFarbwechselAllgemein(Farbe[5][6], Position)
def ZelleFHFarbwechsel():
    Position = [5, 7]
    Farbe[5][7]=ZelleFarbwechselAllgemein(Farbe[5][7], Position)
def ZelleGAFarbwechsel():
    Position = [6, 0]
    Farbe[6][0]=ZelleFarbwechselAllgemein(Farbe[6][0], Position)
def ZelleGBFarbwechsel():
    Position = [6, 1]
    Farbe[6][1]=ZelleFarbwechselAllgemein(Farbe[6][1], Position)
def ZelleGCFarbwechsel():
    Position = [6, 2]
    Farbe[6][2]=ZelleFarbwechselAllgemein(Farbe[6][2], Position)
def ZelleGDFarbwechsel():
    Position = [6, 3]
    Farbe[6][3]=ZelleFarbwechselAllgemein(Farbe[6][3], Position)
def ZelleGEFarbwechsel():
    Position = [6, 4]
    Farbe[6][4]=ZelleFarbwechselAllgemein(Farbe[6][4], Position)
def ZelleGFFarbwechsel():
    Position = [6, 5]
    Farbe[6][5]=ZelleFarbwechselAllgemein(Farbe[6][5], Position)
def ZelleGGFarbwechsel():
    Position = [6, 6]
    Farbe[6][6]=ZelleFarbwechselAllgemein(Farbe[6][6], Position)
def ZelleGHFarbwechsel():
    Position = [6, 7]
    Farbe[6][7]=ZelleFarbwechselAllgemein(Farbe[6][7], Position)
def ZelleHAFarbwechsel():
    Position = [7, 0]
    Farbe[7][0]=ZelleFarbwechselAllgemein(Farbe[7][0], Position)
def ZelleHBFarbwechsel():
    Position = [7, 1]
    Farbe[7][1]=ZelleFarbwechselAllgemein(Farbe[7][1], Position)
def ZelleHCFarbwechsel():
    Position = [7, 2]
    Farbe[7][2]=ZelleFarbwechselAllgemein(Farbe[7][2], Position)
def ZelleHDFarbwechsel():
    Position = [7, 3]
    Farbe[7][3]=ZelleFarbwechselAllgemein(Farbe[7][3], Position)
def ZelleHEFarbwechsel():
    Position = [7, 4]
    Farbe[7][4]=ZelleFarbwechselAllgemein(Farbe[7][4], Position)
def ZelleHFFarbwechsel():
    Position = [7, 5]
    Farbe[7][5]=ZelleFarbwechselAllgemein(Farbe[7][5], Position)
def ZelleHGFarbwechsel():
    Position = [7, 6]
    Farbe[7][6]=ZelleFarbwechselAllgemein(Farbe[7][6], Position)
def ZelleHHFarbwechsel():
    Position = [7, 7]
    Farbe[7][7]=ZelleFarbwechselAllgemein(Farbe[7][7], Position)
def ZelleAIFarbwechsel():
    Position = [0, 8]
    Farbe[0][8]=ZelleFarbwechselAllgemein(Farbe[0][8], Position)
def ZelleAJFarbwechsel():
    Position = [0, 9]
    Farbe[0][9]=ZelleFarbwechselAllgemein(Farbe[0][9], Position)
def ZelleBIFarbwechsel():
    Position = [1, 8]
    Farbe[1][8]=ZelleFarbwechselAllgemein(Farbe[1][8], Position)
def ZelleBJFarbwechsel():
    Position = [1, 9]
    Farbe[1][9]=ZelleFarbwechselAllgemein(Farbe[1][9], Position)
def ZelleCIFarbwechsel():
    Position = [2, 8]
    Farbe[2][8]=ZelleFarbwechselAllgemein(Farbe[2][8], Position)
def ZelleCJFarbwechsel():
    Position = [2, 9]
    Farbe[2][9]=ZelleFarbwechselAllgemein(Farbe[2][9], Position)
def ZelleDIFarbwechsel():
    Position = [3, 8]
    Farbe[3][8]=ZelleFarbwechselAllgemein(Farbe[3][8], Position)
def ZelleDJFarbwechsel():
    Position = [3, 9]
    Farbe[3][9]=ZelleFarbwechselAllgemein(Farbe[3][9], Position)
def ZelleEIFarbwechsel():
    Position = [4, 8]
    Farbe[4][8]=ZelleFarbwechselAllgemein(Farbe[4][8], Position)
def ZelleEJFarbwechsel():
    Position = [4, 9]
    Farbe[4][9]=ZelleFarbwechselAllgemein(Farbe[4][9], Position)
def ZelleFIFarbwechsel():
    Position = [5, 8]
    Farbe[5][8]=ZelleFarbwechselAllgemein(Farbe[5][8], Position)
def ZelleFJFarbwechsel():
    Position = [5, 9]
    Farbe[5][9]=ZelleFarbwechselAllgemein(Farbe[5][9], Position)
def ZelleGIFarbwechsel():
    Position = [6, 8]
    Farbe[6][8]=ZelleFarbwechselAllgemein(Farbe[6][8], Position)
def ZelleGJFarbwechsel():
    Position = [6, 9]
    Farbe[6][9]=ZelleFarbwechselAllgemein(Farbe[6][9], Position)
def ZelleHIFarbwechsel():
    Position = [7, 8]
    Farbe[7][8]=ZelleFarbwechselAllgemein(Farbe[7][8], Position)
def ZelleHJFarbwechsel():
    Position = [7, 9]
    Farbe[7][9]=ZelleFarbwechselAllgemein(Farbe[7][9], Position)
def ZelleIAFarbwechsel():
    Position = [8, 0]
    Farbe[8][0]=ZelleFarbwechselAllgemein(Farbe[8][0], Position)
def ZelleIBFarbwechsel():
    Position = [8, 1]
    Farbe[8][1]=ZelleFarbwechselAllgemein(Farbe[8][1], Position)
def ZelleICFarbwechsel():
    Position = [8, 2]
    Farbe[8][2]=ZelleFarbwechselAllgemein(Farbe[8][2], Position)
def ZelleIDFarbwechsel():
    Position = [8, 3]
    Farbe[8][3]=ZelleFarbwechselAllgemein(Farbe[8][3], Position)
def ZelleIEFarbwechsel():
    Position = [8, 4]
    Farbe[8][4]=ZelleFarbwechselAllgemein(Farbe[8][4], Position)
def ZelleIFFarbwechsel():
    Position = [8, 5]
    Farbe[8][5]=ZelleFarbwechselAllgemein(Farbe[8][5], Position)
def ZelleIGFarbwechsel():
    Position = [8, 6]
    Farbe[8][6]=ZelleFarbwechselAllgemein(Farbe[8][6], Position)
def ZelleIHFarbwechsel():
    Position = [8, 7]
    Farbe[8][7]=ZelleFarbwechselAllgemein(Farbe[8][7], Position)
def ZelleIIFarbwechsel():
    Position = [8, 8]
    Farbe[8][8]=ZelleFarbwechselAllgemein(Farbe[8][8], Position)
def ZelleIJFarbwechsel():
    Position = [8, 9]
    Farbe[8][9]=ZelleFarbwechselAllgemein(Farbe[8][9], Position)
def ZelleJAFarbwechsel():
    Position = [9, 0]
    Farbe[9][0]=ZelleFarbwechselAllgemein(Farbe[9][0], Position)
def ZelleJBFarbwechsel():
    Position = [9, 1]
    Farbe[9][1]=ZelleFarbwechselAllgemein(Farbe[9][1], Position)
def ZelleJCFarbwechsel():
    Position = [9, 2]
    Farbe[9][2]=ZelleFarbwechselAllgemein(Farbe[9][2], Position)
def ZelleJDFarbwechsel():
    Position = [9, 3]
    Farbe[9][3]=ZelleFarbwechselAllgemein(Farbe[9][3], Position)
def ZelleJEFarbwechsel():
    Position = [9, 4]
    Farbe[9][4]=ZelleFarbwechselAllgemein(Farbe[9][4], Position)
def ZelleJFFarbwechsel():
    Position = [9, 5]
    Farbe[9][5]=ZelleFarbwechselAllgemein(Farbe[9][5], Position)
def ZelleJGFarbwechsel():
    Position = [9, 6]
    Farbe[9][6]=ZelleFarbwechselAllgemein(Farbe[9][6], Position)
def ZelleJHFarbwechsel():
    Position = [9, 7]
    Farbe[9][7]=ZelleFarbwechselAllgemein(Farbe[9][7], Position)
def ZelleJIFarbwechsel():
    Position = [9, 8]
    Farbe[9][8]=ZelleFarbwechselAllgemein(Farbe[9][8], Position)
def ZelleJJFarbwechsel():
    Position = [9, 9]
    Farbe[9][9]=ZelleFarbwechselAllgemein(Farbe[9][9], Position)
def ZelleAKFarbwechsel():
    Position = [0, 10]
    Farbe[0][10]=ZelleFarbwechselAllgemein(Farbe[0][10], Position)
def ZelleALFarbwechsel():
    Position = [0, 11]
    Farbe[0][11]=ZelleFarbwechselAllgemein(Farbe[0][11], Position)
def ZelleBKFarbwechsel():
    Position = [1, 10]
    Farbe[1][10]=ZelleFarbwechselAllgemein(Farbe[1][10], Position)
def ZelleBLFarbwechsel():
    Position = [1, 11]
    Farbe[1][11]=ZelleFarbwechselAllgemein(Farbe[1][11], Position)
def ZelleCKFarbwechsel():
    Position = [2, 10]
    Farbe[2][10]=ZelleFarbwechselAllgemein(Farbe[2][10], Position)
def ZelleCLFarbwechsel():
    Position = [2, 11]
    Farbe[2][11]=ZelleFarbwechselAllgemein(Farbe[2][11], Position)
def ZelleDKFarbwechsel():
    Position = [3, 10]
    Farbe[3][10]=ZelleFarbwechselAllgemein(Farbe[3][10], Position)
def ZelleDLFarbwechsel():
    Position = [3, 11]
    Farbe[3][11]=ZelleFarbwechselAllgemein(Farbe[3][11], Position)
def ZelleEKFarbwechsel():
    Position = [4, 10]
    Farbe[4][10]=ZelleFarbwechselAllgemein(Farbe[4][10], Position)
def ZelleELFarbwechsel():
    Position = [4, 11]
    Farbe[4][11]=ZelleFarbwechselAllgemein(Farbe[4][11], Position)
def ZelleFKFarbwechsel():
    Position = [5, 10]
    Farbe[5][10]=ZelleFarbwechselAllgemein(Farbe[5][10], Position)
def ZelleFLFarbwechsel():
    Position = [5, 11]
    Farbe[5][11]=ZelleFarbwechselAllgemein(Farbe[5][11], Position)
def ZelleGKFarbwechsel():
    Position = [6, 10]
    Farbe[6][10]=ZelleFarbwechselAllgemein(Farbe[6][10], Position)
def ZelleGLFarbwechsel():
    Position = [6, 11]
    Farbe[6][11]=ZelleFarbwechselAllgemein(Farbe[6][11], Position)
def ZelleHKFarbwechsel():
    Position = [7, 10]
    Farbe[7][10]=ZelleFarbwechselAllgemein(Farbe[7][10], Position)
def ZelleHLFarbwechsel():
    Position = [7, 11]
    Farbe[7][11]=ZelleFarbwechselAllgemein(Farbe[7][11], Position)
def ZelleIKFarbwechsel():
    Position = [8, 10]
    Farbe[8][10]=ZelleFarbwechselAllgemein(Farbe[8][10], Position)
def ZelleILFarbwechsel():
    Position = [8, 11]
    Farbe[8][11]=ZelleFarbwechselAllgemein(Farbe[8][11], Position)
def ZelleJKFarbwechsel():
    Position = [9, 10]
    Farbe[9][10]=ZelleFarbwechselAllgemein(Farbe[9][10], Position)
def ZelleJLFarbwechsel():
    Position = [9, 11]
    Farbe[9][11]=ZelleFarbwechselAllgemein(Farbe[9][11], Position)
def ZelleKKFarbwechsel():
    Position = [10, 10]
    Farbe[10][10]=ZelleFarbwechselAllgemein(Farbe[10][10], Position)
def ZelleKLFarbwechsel():
    Position = [10, 11]
    Farbe[10][11]=ZelleFarbwechselAllgemein(Farbe[10][11], Position)
def ZelleLKFarbwechsel():
    Position = [11, 10]
    Farbe[11][10]=ZelleFarbwechselAllgemein(Farbe[11][10], Position)
def ZelleLLFarbwechsel():
    Position = [11, 11]
    Farbe[11][11]=ZelleFarbwechselAllgemein(Farbe[11][11], Position)
def ZelleKAFarbwechsel():
    Position = [10, 0]
    Farbe[10][0]=ZelleFarbwechselAllgemein(Farbe[10][0], Position)
def ZelleLAFarbwechsel():
    Position = [11, 0]
    Farbe[11][0]=ZelleFarbwechselAllgemein(Farbe[11][0], Position)
def ZelleKBFarbwechsel():
    Position = [10, 1]
    Farbe[10][1]=ZelleFarbwechselAllgemein(Farbe[10][1], Position)
def ZelleLBFarbwechsel():
    Position = [11, 1]
    Farbe[11][1]=ZelleFarbwechselAllgemein(Farbe[11][1], Position)
def ZelleKCFarbwechsel():
    Position = [10, 2]
    Farbe[10][2]=ZelleFarbwechselAllgemein(Farbe[10][2], Position)
def ZelleLCFarbwechsel():
    Position = [11, 2]
    Farbe[11][2]=ZelleFarbwechselAllgemein(Farbe[11][2], Position)
def ZelleKDFarbwechsel():
    Position = [10, 3]
    Farbe[10][3]=ZelleFarbwechselAllgemein(Farbe[10][3], Position)
def ZelleLDFarbwechsel():
    Position = [11, 3]
    Farbe[11][3]=ZelleFarbwechselAllgemein(Farbe[11][3], Position)
def ZelleKEFarbwechsel():
    Position = [10, 4]
    Farbe[10][4]=ZelleFarbwechselAllgemein(Farbe[10][4], Position)
def ZelleLEFarbwechsel():
    Position = [11, 4]
    Farbe[11][4]=ZelleFarbwechselAllgemein(Farbe[11][4], Position)
def ZelleKFFarbwechsel():
    Position = [10, 5]
    Farbe[10][5]=ZelleFarbwechselAllgemein(Farbe[10][5], Position)
def ZelleLFFarbwechsel():
    Position = [11, 5]
    Farbe[11][5]=ZelleFarbwechselAllgemein(Farbe[11][5], Position)
def ZelleKGFarbwechsel():
    Position = [10, 6]
    Farbe[10][6]=ZelleFarbwechselAllgemein(Farbe[10][6], Position)
def ZelleLGFarbwechsel():
    Position = [11, 6]
    Farbe[11][6]=ZelleFarbwechselAllgemein(Farbe[11][6], Position)
def ZelleKHFarbwechsel():
    Position = [10, 7]
    Farbe[10][7]=ZelleFarbwechselAllgemein(Farbe[10][7], Position)
def ZelleLHFarbwechsel():
    global Position
    Position = [11, 7]
    Farbe[11][7]=ZelleFarbwechselAllgemein(Farbe[11][7], Position)
def ZelleKIFarbwechsel():
    Position = [10, 8]
    Farbe[10][8]=ZelleFarbwechselAllgemein(Farbe[10][8], Position)
def ZelleLIFarbwechsel():
    Position = [11, 8]
    Farbe[11][8]=ZelleFarbwechselAllgemein(Farbe[11][8], Position)
def ZelleKJFarbwechsel():
    Position = [10, 9]
    Farbe[10][9]=ZelleFarbwechselAllgemein(Farbe[10][9], Position)
def ZelleLJFarbwechsel():
    Position = [11, 9]
    Farbe[11][9]=ZelleFarbwechselAllgemein(Farbe[11][9], Position)
def ZelleAMFarbwechsel():
    Position = [0, 12]
    Farbe[0][12]=ZelleFarbwechselAllgemein(Farbe[0][12], Position)
def ZelleANFarbwechsel():
    Position = [0, 13]
    Farbe[0][13]=ZelleFarbwechselAllgemein(Farbe[0][13], Position)
def ZelleBMFarbwechsel():
    Position = [1, 12]
    Farbe[1][12]=ZelleFarbwechselAllgemein(Farbe[1][12], Position)
def ZelleBNFarbwechsel():
    Position = [1, 13]
    Farbe[1][13]=ZelleFarbwechselAllgemein(Farbe[1][13], Position)
def ZelleCMFarbwechsel():
    Position = [2, 12]
    Farbe[2][12]=ZelleFarbwechselAllgemein(Farbe[2][12], Position)
def ZelleCNFarbwechsel():
    Position = [2, 13]
    Farbe[2][13]=ZelleFarbwechselAllgemein(Farbe[2][13], Position)
def ZelleDMFarbwechsel():
    Position = [3, 12]
    Farbe[3][12]=ZelleFarbwechselAllgemein(Farbe[3][12], Position)
def ZelleDNFarbwechsel():
    Position = [3, 13]
    Farbe[3][13]=ZelleFarbwechselAllgemein(Farbe[3][13], Position)
def ZelleEMFarbwechsel():
    Position = [4, 12]
    Farbe[4][12]=ZelleFarbwechselAllgemein(Farbe[4][12], Position)
def ZelleENFarbwechsel():
    Position = [4, 13]
    Farbe[4][13]=ZelleFarbwechselAllgemein(Farbe[4][13], Position)
def ZelleFMFarbwechsel():
    Position = [5, 12]
    Farbe[5][12]=ZelleFarbwechselAllgemein(Farbe[5][12], Position)
def ZelleFNFarbwechsel():
    Position = [5, 13]
    Farbe[5][13]=ZelleFarbwechselAllgemein(Farbe[5][13], Position)
def ZelleGMFarbwechsel():
    Position = [6, 12]
    Farbe[6][12]=ZelleFarbwechselAllgemein(Farbe[6][12], Position)
def ZelleGNFarbwechsel():
    Position = [6, 13]
    Farbe[6][13]=ZelleFarbwechselAllgemein(Farbe[6][13], Position)
def ZelleHMFarbwechsel():
    Position = [7, 12]
    Farbe[7][12]=ZelleFarbwechselAllgemein(Farbe[7][12], Position)
def ZelleHNFarbwechsel():
    Position = [7, 13]
    Farbe[7][13]=ZelleFarbwechselAllgemein(Farbe[7][13], Position)
def ZelleIMFarbwechsel():
    Position = [8, 12]
    Farbe[8][12]=ZelleFarbwechselAllgemein(Farbe[8][12], Position)
def ZelleINFarbwechsel():
    Position = [8, 13]
    Farbe[8][13]=ZelleFarbwechselAllgemein(Farbe[8][13], Position)
def ZelleJMFarbwechsel():
    Position = [9, 12]
    Farbe[9][12]=ZelleFarbwechselAllgemein(Farbe[9][12], Position)
def ZelleJNFarbwechsel():
    Position = [9, 13]
    Farbe[9][13]=ZelleFarbwechselAllgemein(Farbe[9][13], Position)
def ZelleKMFarbwechsel():
    Position = [10, 12]
    Farbe[10][12]=ZelleFarbwechselAllgemein(Farbe[10][12], Position)
def ZelleKNFarbwechsel():
    Position = [10, 13]
    Farbe[10][13]=ZelleFarbwechselAllgemein(Farbe[10][13], Position)
def ZelleLMFarbwechsel():
    Position = [11, 12]
    Farbe[11][12]=ZelleFarbwechselAllgemein(Farbe[11][12], Position)
def ZelleLNFarbwechsel():
    Position = [11, 13]
    Farbe[11][13]=ZelleFarbwechselAllgemein(Farbe[11][13], Position)
def ZelleMMFarbwechsel():
    Position = [12, 12]
    Farbe[12][12]=ZelleFarbwechselAllgemein(Farbe[12][12], Position)
def ZelleMNFarbwechsel():
    Position = [12, 13]
    Farbe[12][13]=ZelleFarbwechselAllgemein(Farbe[12][13], Position)
def ZelleNMFarbwechsel():
    Position = [13, 12]
    Farbe[13][12]=ZelleFarbwechselAllgemein(Farbe[13][12], Position)
def ZelleNNFarbwechsel():
    Position = [13, 13]
    Farbe[13][13]=ZelleFarbwechselAllgemein(Farbe[13][13], Position)
def ZelleMAFarbwechsel():
    Position = [12, 0]
    Farbe[12][0]=ZelleFarbwechselAllgemein(Farbe[12][0], Position)
def ZelleNAFarbwechsel():
    Position = [13, 0]
    Farbe[13][0]=ZelleFarbwechselAllgemein(Farbe[13][0], Position)
def ZelleMBFarbwechsel():
    Position = [12, 1]
    Farbe[12][1]=ZelleFarbwechselAllgemein(Farbe[12][1], Position)
def ZelleNBFarbwechsel():
    Position = [13, 1]
    Farbe[13][1]=ZelleFarbwechselAllgemein(Farbe[13][1], Position)
def ZelleMCFarbwechsel():
    Position = [12, 2]
    Farbe[12][2]=ZelleFarbwechselAllgemein(Farbe[12][2], Position)
def ZelleNCFarbwechsel():
    Position = [13, 2]
    Farbe[13][2]=ZelleFarbwechselAllgemein(Farbe[13][2], Position)
def ZelleMDFarbwechsel():
    Position = [12, 3]
    Farbe[12][3]=ZelleFarbwechselAllgemein(Farbe[12][3], Position)
def ZelleNDFarbwechsel():
    Position = [13, 3]
    Farbe[13][3]=ZelleFarbwechselAllgemein(Farbe[13][3], Position)
def ZelleMEFarbwechsel():
    Position = [12, 4]
    Farbe[12][4]=ZelleFarbwechselAllgemein(Farbe[12][4], Position)
def ZelleNEFarbwechsel():
    Position = [13, 4]
    Farbe[13][4]=ZelleFarbwechselAllgemein(Farbe[13][4], Position)
def ZelleMFFarbwechsel():
    Position = [12, 5]
    Farbe[12][5]=ZelleFarbwechselAllgemein(Farbe[12][5], Position)
def ZelleNFFarbwechsel():
    Position = [13, 5]
    Farbe[13][5]=ZelleFarbwechselAllgemein(Farbe[13][5], Position)
def ZelleMGFarbwechsel():
    Position = [12, 6]
    Farbe[12][6]=ZelleFarbwechselAllgemein(Farbe[12][6], Position)
def ZelleNGFarbwechsel():
    Position = [13, 6]
    Farbe[13][6]=ZelleFarbwechselAllgemein(Farbe[13][6], Position)
def ZelleMHFarbwechsel():
    Position = [12, 7]
    Farbe[12][7]=ZelleFarbwechselAllgemein(Farbe[12][7], Position)
def ZelleNHFarbwechsel():
    Position = [13, 7]
    Farbe[13][7]=ZelleFarbwechselAllgemein(Farbe[13][7], Position)
def ZelleMIFarbwechsel():
    Position = [12, 8]
    Farbe[12][8]=ZelleFarbwechselAllgemein(Farbe[12][8], Position)
def ZelleNIFarbwechsel():
    Position = [13, 8]
    Farbe[13][8]=ZelleFarbwechselAllgemein(Farbe[13][8], Position)
def ZelleMJFarbwechsel():
    Position = [12, 9]
    Farbe[12][9]=ZelleFarbwechselAllgemein(Farbe[12][9], Position)
def ZelleNJFarbwechsel():
    Position = [13, 9]
    Farbe[13][9]=ZelleFarbwechselAllgemein(Farbe[13][9], Position)
def ZelleMKFarbwechsel():
    Position = [12, 10]
    Farbe[12][10]=ZelleFarbwechselAllgemein(Farbe[12][10], Position)
def ZelleNKFarbwechsel():
    Position = [13, 10]
    Farbe[13][10]=ZelleFarbwechselAllgemein(Farbe[13][10], Position)
def ZelleMLFarbwechsel():
    Position = [12, 11]
    Farbe[12][11]=ZelleFarbwechselAllgemein(Farbe[12][11], Position)
def ZelleNLFarbwechsel():
    Position = [13, 11]
    Farbe[13][11]=ZelleFarbwechselAllgemein(Farbe[13][11], Position)
def ZelleAOFarbwechsel():
    Position = [0, 14]
    Farbe[0][14]=ZelleFarbwechselAllgemein(Farbe[0][14], Position)
def ZelleAPFarbwechsel():
    Position = [0, 15]
    Farbe[0][15]=ZelleFarbwechselAllgemein(Farbe[0][15], Position)
def ZelleBOFarbwechsel():
    Position = [1, 14]
    Farbe[1][14]=ZelleFarbwechselAllgemein(Farbe[1][14], Position)
def ZelleBPFarbwechsel():
    Position = [1, 15]
    Farbe[1][15]=ZelleFarbwechselAllgemein(Farbe[1][15], Position)
def ZelleCOFarbwechsel():
    Position = [2, 14]
    Farbe[2][14]=ZelleFarbwechselAllgemein(Farbe[2][14], Position)
def ZelleCPFarbwechsel():
    Position = [2, 15]
    Farbe[2][15]=ZelleFarbwechselAllgemein(Farbe[2][15], Position)
def ZelleDOFarbwechsel():
    Position = [3, 14]
    Farbe[3][14]=ZelleFarbwechselAllgemein(Farbe[3][14], Position)
def ZelleDPFarbwechsel():
    Position = [3, 15]
    Farbe[3][15]=ZelleFarbwechselAllgemein(Farbe[3][15], Position)
def ZelleEOFarbwechsel():
    Position = [4, 14]
    Farbe[4][14]=ZelleFarbwechselAllgemein(Farbe[4][14], Position)
def ZelleEPFarbwechsel():
    Position = [4, 15]
    Farbe[4][15]=ZelleFarbwechselAllgemein(Farbe[4][15], Position)
def ZelleFOFarbwechsel():
    Position = [5, 14]
    Farbe[5][14]=ZelleFarbwechselAllgemein(Farbe[5][14], Position)
def ZelleFPFarbwechsel():
    Position = [5, 15]
    Farbe[5][15]=ZelleFarbwechselAllgemein(Farbe[5][15], Position)
def ZelleGOFarbwechsel():
    Position = [6, 14]
    Farbe[6][14]=ZelleFarbwechselAllgemein(Farbe[6][14], Position)
def ZelleGPFarbwechsel():
    Position = [6, 15]
    Farbe[6][15]=ZelleFarbwechselAllgemein(Farbe[6][15], Position)
def ZelleHOFarbwechsel():
    Position = [7, 14]
    Farbe[7][14]=ZelleFarbwechselAllgemein(Farbe[7][14], Position)
def ZelleHPFarbwechsel():
    Position = [7, 15]
    Farbe[7][15]=ZelleFarbwechselAllgemein(Farbe[7][15], Position)
def ZelleIOFarbwechsel():
    Position = [8, 14]
    Farbe[8][14]=ZelleFarbwechselAllgemein(Farbe[8][14], Position)
def ZelleIPFarbwechsel():
    Position = [8, 15]
    Farbe[8][15]=ZelleFarbwechselAllgemein(Farbe[8][15], Position)
def ZelleJOFarbwechsel():
    Position = [9, 14]
    Farbe[9][14]=ZelleFarbwechselAllgemein(Farbe[9][14], Position)
def ZelleJPFarbwechsel():
    Position = [9, 15]
    Farbe[9][15]=ZelleFarbwechselAllgemein(Farbe[9][15], Position)
def ZelleKOFarbwechsel():
    Position = [10, 14]
    Farbe[10][14]=ZelleFarbwechselAllgemein(Farbe[10][14], Position)
def ZelleKPFarbwechsel():
    Position = [10, 15]
    Farbe[10][15]=ZelleFarbwechselAllgemein(Farbe[10][15], Position)
def ZelleLOFarbwechsel():
    Position = [11, 14]
    Farbe[11][14]=ZelleFarbwechselAllgemein(Farbe[11][14], Position)
def ZelleLPFarbwechsel():
    Position = [11, 15]
    Farbe[11][15]=ZelleFarbwechselAllgemein(Farbe[11][15], Position)
def ZelleMOFarbwechsel():
    Position = [12, 14]
    Farbe[12][14]=ZelleFarbwechselAllgemein(Farbe[12][14], Position)
def ZelleMPFarbwechsel():
    Position = [12, 15]
    Farbe[12][15]=ZelleFarbwechselAllgemein(Farbe[12][15], Position)
def ZelleNOFarbwechsel():
    Position = [13, 14]
    Farbe[13][14]=ZelleFarbwechselAllgemein(Farbe[13][14], Position)
def ZelleNPFarbwechsel():
    Position = [13, 15]
    Farbe[13][15]=ZelleFarbwechselAllgemein(Farbe[13][15], Position)
def ZelleOOFarbwechsel():
    Position = [14, 14]
    Farbe[14][14]=ZelleFarbwechselAllgemein(Farbe[14][14], Position)
def ZelleOPFarbwechsel():
    Position = [14, 15]
    Farbe[14][15]=ZelleFarbwechselAllgemein(Farbe[14][15], Position)
def ZellePOFarbwechsel():
    Position = [15, 14]
    Farbe[15][14]=ZelleFarbwechselAllgemein(Farbe[15][14], Position)
def ZellePPFarbwechsel():
    Position = [15, 15]
    Farbe[15][15]=ZelleFarbwechselAllgemein(Farbe[15][15], Position)
def ZelleOAFarbwechsel():
    Position = [14, 0]
    Farbe[14][0]=ZelleFarbwechselAllgemein(Farbe[14][0], Position)
def ZellePAFarbwechsel():
    Position = [15, 0]
    Farbe[15][0]=ZelleFarbwechselAllgemein(Farbe[15][0], Position)
def ZelleOBFarbwechsel():
    Position = [14, 1]
    Farbe[14][1]=ZelleFarbwechselAllgemein(Farbe[14][1], Position)
def ZellePBFarbwechsel():
    Position = [15, 1]
    Farbe[15][1]=ZelleFarbwechselAllgemein(Farbe[15][1], Position)
def ZelleOCFarbwechsel():
    Position = [14, 2]
    Farbe[14][2]=ZelleFarbwechselAllgemein(Farbe[14][2], Position)
def ZellePCFarbwechsel():
    Position = [15, 2]
    Farbe[15][2]=ZelleFarbwechselAllgemein(Farbe[15][2], Position)
def ZelleODFarbwechsel():
    Position = [14, 3]
    Farbe[14][3]=ZelleFarbwechselAllgemein(Farbe[14][3], Position)
def ZellePDFarbwechsel():
    Position = [15, 3]
    Farbe[15][3]=ZelleFarbwechselAllgemein(Farbe[15][3], Position)
def ZelleOEFarbwechsel():
    Position = [14, 4]
    Farbe[14][4]=ZelleFarbwechselAllgemein(Farbe[14][4], Position)
def ZellePEFarbwechsel():
    Position = [15, 4]
    Farbe[15][4]=ZelleFarbwechselAllgemein(Farbe[15][4], Position)
def ZelleOFFarbwechsel():
    Position = [14, 5]
    Farbe[14][5]=ZelleFarbwechselAllgemein(Farbe[14][5], Position)
def ZellePFFarbwechsel():
    Position = [15, 5]
    Farbe[15][5]=ZelleFarbwechselAllgemein(Farbe[15][5], Position)
def ZelleOGFarbwechsel():
    Position = [14, 6]
    Farbe[14][6]=ZelleFarbwechselAllgemein(Farbe[14][6], Position)
def ZellePGFarbwechsel():
    Position = [15, 6]
    Farbe[15][6]=ZelleFarbwechselAllgemein(Farbe[15][6], Position)
def ZelleOHFarbwechsel():
    Position = [14, 7]
    Farbe[14][7]=ZelleFarbwechselAllgemein(Farbe[14][7], Position)
def ZellePHFarbwechsel():
    Position = [15, 7]
    Farbe[15][7]=ZelleFarbwechselAllgemein(Farbe[15][7], Position)
def ZelleOIFarbwechsel():
    Position = [14, 8]
    Farbe[14][8]=ZelleFarbwechselAllgemein(Farbe[14][8], Position)
def ZellePIFarbwechsel():
    Position = [15, 8]
    Farbe[15][8]=ZelleFarbwechselAllgemein(Farbe[15][8], Position)
def ZelleOJFarbwechsel():
    Position = [14, 9]
    Farbe[14][9]=ZelleFarbwechselAllgemein(Farbe[14][9], Position)
def ZellePJFarbwechsel():
    Position = [15, 9]
    Farbe[15][9]=ZelleFarbwechselAllgemein(Farbe[15][9], Position)
def ZelleOKFarbwechsel():
    Position = [14, 10]
    Farbe[14][10]=ZelleFarbwechselAllgemein(Farbe[14][10], Position)
def ZellePKFarbwechsel():
    Position = [15, 10]
    Farbe[15][10]=ZelleFarbwechselAllgemein(Farbe[15][10], Position)
def ZelleOLFarbwechsel():
    Position = [14, 11]
    Farbe[14][11]=ZelleFarbwechselAllgemein(Farbe[14][11], Position)
def ZellePLFarbwechsel():
    Position = [15, 11]
    Farbe[15][11]=ZelleFarbwechselAllgemein(Farbe[15][11], Position)
def ZelleOMFarbwechsel():
    Position = [14, 12]
    Farbe[14][12]=ZelleFarbwechselAllgemein(Farbe[14][12], Position)
def ZellePMFarbwechsel():
    Position = [15, 12]
    Farbe[15][12]=ZelleFarbwechselAllgemein(Farbe[15][12], Position)
def ZelleONFarbwechsel():
    Position = [14, 13]
    Farbe[14][13]=ZelleFarbwechselAllgemein(Farbe[14][13], Position)
def ZellePNFarbwechsel():
    Position = [15, 13]
    Farbe[15][13]=ZelleFarbwechselAllgemein(Farbe[15][13], Position) 
    
# Die Farben der Zellen werden in so einer Art und Weise verändert, dass eine Generation reibungslos berechnet werden kann.
def GenerationKorrektur(FarbeAlt):
    global GenerationVerschiebung
    GenerationVerschiebung = []
    global SpielBrettLaenge
    global SpielerAmZug
    Index = 0
    while Index < SpielBrettLaenge:
        SupIndex = 0
        while SupIndex < SpielBrettLaenge:
            # graue Zellen werden schwarz
            if FarbeAlt[Index][SupIndex] == 'grey':
                FarbeAlt[Index][SupIndex] = 'black'
                GenerationVerschiebung.append([Index, SupIndex, 'grey'])
            # orangene Zellen werden rot
            if FarbeAlt[Index][SupIndex] == 'orange':
                FarbeAlt[Index][SupIndex] = 'red'
                GenerationVerschiebung.append([Index, SupIndex, 'orange'])
            # hellblaue Zellen werden blau
            if FarbeAlt[Index][SupIndex] == 'lightblue':
                FarbeAlt[Index][SupIndex] = 'blue'
                GenerationVerschiebung.append([Index, SupIndex, 'lightblue'])
            if FarbeAlt[Index][SupIndex] == 'white':
                # weiße Zellen werden rot
                if SpielerAmZug == 1:
                    FarbeAlt[Index][SupIndex] = 'red'
                    GenerationVerschiebung.append([Index, SupIndex, 'white'])
                # weiße Zellen werden blau
                else:
                    FarbeAlt[Index][SupIndex] = 'blue'
                    GenerationVerschiebung.append([Index, SupIndex, 'white'])
            SupIndex = SupIndex + 1
        Index = Index + 1
    return(FarbeAlt)

# Die Generation nach jeden Zug wird hier ermittelt.
def Generation(FarbeAlt):
    FarbeAlt=GenerationKorrektur(FarbeAlt)
    global SpielBrettLaenge
    global ComputerStaerke
    global SpielerAmZug
    global SpielerZugTyp
    FarbeNeu = ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black']
    Index = 0
    # Jede Zelle wird angesteuert.
    while Index < SpielBrettLaenge:
        SupIndex = 0
        while SupIndex < SpielBrettLaenge:
            Zaehlung = 8
            Rot = 0
            IndexSup = -1
            # Jede Nachbarzelle der Zelle wird angesteuert.
            while IndexSup < 2:
                SupIndexSup = -1
                while SupIndexSup < 2:
                    if SupIndexSup == 0 and IndexSup == 0:
                        NutzloseVariable = 'Ich bin sinnfrei'
                    else:
                        if FarbeAlt[Index + IndexSup][SupIndex + SupIndexSup] == 'black':    
                            Zaehlung = Zaehlung - 1
                        if FarbeAlt[Index + IndexSup][SupIndex + SupIndexSup] == 'red':
                            Rot = Rot + 1
                    SupIndexSup = SupIndexSup + 1
                IndexSup = IndexSup + 1
            if FarbeAlt[Index][SupIndex] == 'black':
                if Zaehlung == 3:
                    # Tote Zellen werden zu Lebenden, wenn sie 3 Nachbarzellen haben.
                    if Rot > 1:
                        FarbeNeu[Index][SupIndex] = 'red'
                    else:
                        FarbeNeu[Index][SupIndex] = 'blue'
            if FarbeAlt[Index][SupIndex] == 'red':
                # Lebende Zellen überleben, wenn sie 2 oder 3 Nachbarzellen haben.
                if Zaehlung == 2 or Zaehlung == 3:
                    FarbeNeu[Index][SupIndex] = 'red'
            if FarbeAlt[Index][SupIndex] == 'blue':
                if Zaehlung == 2 or Zaehlung == 3:
                    FarbeNeu[Index][SupIndex] = 'blue'
            SupIndex = SupIndex + 1
        Index = Index + 1
    FarbeAlt=GenerationAntiKorrektur(FarbeAlt)
    return(FarbeNeu)
    
# Die orangenen, hellblauen, etc. Zellen, die zu rot, blau oder schwarz konvertiert worden sind, werden zu orange, hellblau, grau, etc. zurückkonvertiert.
def GenerationAntiKorrektur(FarbeAlt):
    global GenerationVerschiebung
    Index = 0
    while Index < len(GenerationVerschiebung):
        FarbeAlt[GenerationVerschiebung[Index][0]][GenerationVerschiebung[Index][1]] = GenerationVerschiebung[Index][2]
        Index = Index + 1
    return(FarbeAlt)
    
def GenerationTriggerer():
    # Eine Generation soll stattfinden.
    global Farbe
    Farbe=Generation(Farbe)
    Fenster.quit()

def GleichePunktfarbe(Farbe):
    # Nach jeder Runde hat jedes X die Farbe der jeweiligen Zelle.
    global SpielBrettLaenge
    Index = 0
    Punktfarbe = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'], ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
    while Index < SpielBrettLaenge:
        SupIndex = 0
        while SupIndex < SpielBrettLaenge:
            Punktfarbe[Index][SupIndex] = Farbe[Index][SupIndex]
            SupIndex = SupIndex + 1
        Index = Index + 1
    return(Punktfarbe)

def ButtonsErstgenerierung():
    # Wenn das Spiel gestartet wird, dann werden hier alle Zellen generiert.
    global ZurueckButton
    ZurueckButton = Button(Fenster, text='Zurück zum Hauptmenu', bg='grey', command=AntiDebug)
    ZurueckButton.config(font=('Arial', 18))
    ZurueckButton.place(x=757, y=670)
    global Zelle
    Zelle = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    Index = 0
    while Index < 16:
        SupIndex = 0
        while SupIndex < 15:
            Zelle[Index].append(0)
            SupIndex = SupIndex + 1
        Index = Index + 1
    global SpielBrettLaenge
    # Diese Zellen werden immer generiert.
    Zelle[0][0] = Button(Fenster, command=ZelleAAFarbwechsel)
    Zelle[0][1] = Button(Fenster, command=ZelleABFarbwechsel)
    Zelle[0][2] = Button(Fenster, command=ZelleACFarbwechsel)
    Zelle[0][3] = Button(Fenster, command=ZelleADFarbwechsel)
    Zelle[0][4] = Button(Fenster, command=ZelleAEFarbwechsel)
    Zelle[0][5] = Button(Fenster, command=ZelleAFFarbwechsel)
    Zelle[0][6] = Button(Fenster, command=ZelleAGFarbwechsel)
    Zelle[0][7] = Button(Fenster, command=ZelleAHFarbwechsel)
    Zelle[1][0] = Button(Fenster, command=ZelleBAFarbwechsel)
    Zelle[1][1] = Button(Fenster, command=ZelleBBFarbwechsel)
    Zelle[1][2] = Button(Fenster, command=ZelleBCFarbwechsel)
    Zelle[1][3] = Button(Fenster, command=ZelleBDFarbwechsel)
    Zelle[1][4] = Button(Fenster, command=ZelleBEFarbwechsel)
    Zelle[1][5] = Button(Fenster, command=ZelleBFFarbwechsel)
    Zelle[1][6] = Button(Fenster, command=ZelleBGFarbwechsel)
    Zelle[1][7] = Button(Fenster, command=ZelleBHFarbwechsel)
    Zelle[2][0] = Button(Fenster, command=ZelleCAFarbwechsel)
    Zelle[2][1] = Button(Fenster, command=ZelleCBFarbwechsel)
    Zelle[2][2] = Button(Fenster, command=ZelleCCFarbwechsel)
    Zelle[2][3] = Button(Fenster, command=ZelleCDFarbwechsel)
    Zelle[2][4] = Button(Fenster, command=ZelleCEFarbwechsel)
    Zelle[2][5] = Button(Fenster, command=ZelleCFFarbwechsel)
    Zelle[2][6] = Button(Fenster, command=ZelleCGFarbwechsel)
    Zelle[2][7] = Button(Fenster, command=ZelleCHFarbwechsel)
    Zelle[3][0] = Button(Fenster, command=ZelleDAFarbwechsel)
    Zelle[3][1] = Button(Fenster, command=ZelleDBFarbwechsel)
    Zelle[3][2] = Button(Fenster, command=ZelleDCFarbwechsel)
    Zelle[3][3] = Button(Fenster, command=ZelleDDFarbwechsel)
    Zelle[3][4] = Button(Fenster, command=ZelleDEFarbwechsel)
    Zelle[3][5] = Button(Fenster, command=ZelleDFFarbwechsel)
    Zelle[3][6] = Button(Fenster, command=ZelleDGFarbwechsel)
    Zelle[3][7] = Button(Fenster, command=ZelleDHFarbwechsel)
    Zelle[4][0] = Button(Fenster, command=ZelleEAFarbwechsel)
    Zelle[4][1] = Button(Fenster, command=ZelleEBFarbwechsel)
    Zelle[4][2] = Button(Fenster, command=ZelleECFarbwechsel)
    Zelle[4][3] = Button(Fenster, command=ZelleEDFarbwechsel)
    Zelle[4][4] = Button(Fenster, command=ZelleEEFarbwechsel)
    Zelle[4][5] = Button(Fenster, command=ZelleEFFarbwechsel)
    Zelle[4][6] = Button(Fenster, command=ZelleEGFarbwechsel)
    Zelle[4][7] = Button(Fenster, command=ZelleEHFarbwechsel)
    Zelle[5][0] = Button(Fenster, command=ZelleFAFarbwechsel)
    Zelle[5][1] = Button(Fenster, command=ZelleFBFarbwechsel)
    Zelle[5][2] = Button(Fenster, command=ZelleFCFarbwechsel)
    Zelle[5][3] = Button(Fenster, command=ZelleFDFarbwechsel)
    Zelle[5][4] = Button(Fenster, command=ZelleFEFarbwechsel)
    Zelle[5][5] = Button(Fenster, command=ZelleFFFarbwechsel)
    Zelle[5][6] = Button(Fenster, command=ZelleFGFarbwechsel)
    Zelle[5][7] = Button(Fenster, command=ZelleFHFarbwechsel)
    Zelle[6][0] = Button(Fenster, command=ZelleGAFarbwechsel)
    Zelle[6][1] = Button(Fenster, command=ZelleGBFarbwechsel)
    Zelle[6][2] = Button(Fenster, command=ZelleGCFarbwechsel)
    Zelle[6][3] = Button(Fenster, command=ZelleGDFarbwechsel)
    Zelle[6][4] = Button(Fenster, command=ZelleGEFarbwechsel)
    Zelle[6][5] = Button(Fenster, command=ZelleGFFarbwechsel)
    Zelle[6][6] = Button(Fenster, command=ZelleGGFarbwechsel)
    Zelle[6][7] = Button(Fenster, command=ZelleGHFarbwechsel)
    Zelle[7][0] = Button(Fenster, command=ZelleHAFarbwechsel)
    Zelle[7][1] = Button(Fenster, command=ZelleHBFarbwechsel)
    Zelle[7][2] = Button(Fenster, command=ZelleHCFarbwechsel)
    Zelle[7][3] = Button(Fenster, command=ZelleHDFarbwechsel)
    Zelle[7][4] = Button(Fenster, command=ZelleHEFarbwechsel)
    Zelle[7][5] = Button(Fenster, command=ZelleHFFarbwechsel)
    Zelle[7][6] = Button(Fenster, command=ZelleHGFarbwechsel)
    Zelle[7][7] = Button(Fenster, command=ZelleHHFarbwechsel)
    if SpielBrettLaenge > 8:
        # Nur bei der Spielbrettgröße von 10x10 oder größer werden diese Zellen generiert.
        Zelle[0][8] = Button(Fenster, command=ZelleAIFarbwechsel)
        Zelle[0][9] = Button(Fenster, command=ZelleAJFarbwechsel)
        Zelle[1][8] = Button(Fenster, command=ZelleBIFarbwechsel)
        Zelle[1][9] = Button(Fenster, command=ZelleBJFarbwechsel)
        Zelle[2][8] = Button(Fenster, command=ZelleCIFarbwechsel)
        Zelle[2][9] = Button(Fenster, command=ZelleCJFarbwechsel)
        Zelle[3][8] = Button(Fenster, command=ZelleDIFarbwechsel)
        Zelle[3][9] = Button(Fenster, command=ZelleDJFarbwechsel)
        Zelle[4][8] = Button(Fenster, command=ZelleEIFarbwechsel)
        Zelle[4][9] = Button(Fenster, command=ZelleEJFarbwechsel)
        Zelle[5][8] = Button(Fenster, command=ZelleFIFarbwechsel)
        Zelle[5][9] = Button(Fenster, command=ZelleFJFarbwechsel)
        Zelle[6][8] = Button(Fenster, command=ZelleGIFarbwechsel)
        Zelle[6][9] = Button(Fenster, command=ZelleGJFarbwechsel)
        Zelle[7][8] = Button(Fenster, command=ZelleHIFarbwechsel)
        Zelle[7][9] = Button(Fenster, command=ZelleHJFarbwechsel)
        Zelle[8][8] = Button(Fenster, command=ZelleIIFarbwechsel)
        Zelle[8][9] = Button(Fenster, command=ZelleIJFarbwechsel)
        Zelle[9][8] = Button(Fenster, command=ZelleJIFarbwechsel)
        Zelle[9][9] = Button(Fenster, command=ZelleJJFarbwechsel)
        Zelle[8][0] = Button(Fenster, command=ZelleIAFarbwechsel)
        Zelle[9][0] = Button(Fenster, command=ZelleJAFarbwechsel)
        Zelle[8][1] = Button(Fenster, command=ZelleIBFarbwechsel)
        Zelle[9][1] = Button(Fenster, command=ZelleJBFarbwechsel)
        Zelle[8][2] = Button(Fenster, command=ZelleICFarbwechsel)
        Zelle[9][2] = Button(Fenster, command=ZelleJCFarbwechsel)
        Zelle[8][3] = Button(Fenster, command=ZelleIDFarbwechsel)
        Zelle[9][3] = Button(Fenster, command=ZelleJDFarbwechsel)
        Zelle[8][4] = Button(Fenster, command=ZelleIEFarbwechsel)
        Zelle[9][4] = Button(Fenster, command=ZelleJEFarbwechsel)
        Zelle[8][5] = Button(Fenster, command=ZelleIFFarbwechsel)
        Zelle[9][5] = Button(Fenster, command=ZelleJFFarbwechsel)
        Zelle[8][6] = Button(Fenster, command=ZelleIGFarbwechsel)
        Zelle[9][6] = Button(Fenster, command=ZelleJGFarbwechsel)
        Zelle[8][7] = Button(Fenster, command=ZelleIHFarbwechsel)
        Zelle[9][7] = Button(Fenster, command=ZelleJHFarbwechsel)
    if SpielBrettLaenge > 10:
        # Nur bei der Spielbrettgröße von 12x12 oder größer werden diese Zellen generiert.
        Zelle[0][10] = Button(Fenster, command=ZelleAKFarbwechsel)
        Zelle[0][11] = Button(Fenster, command=ZelleALFarbwechsel)
        Zelle[1][10] = Button(Fenster, command=ZelleBKFarbwechsel)
        Zelle[1][11] = Button(Fenster, command=ZelleBLFarbwechsel)
        Zelle[2][10] = Button(Fenster, command=ZelleCKFarbwechsel)
        Zelle[2][11] = Button(Fenster, command=ZelleCLFarbwechsel)
        Zelle[3][10] = Button(Fenster, command=ZelleDKFarbwechsel)
        Zelle[3][11] = Button(Fenster, command=ZelleDLFarbwechsel)
        Zelle[4][10] = Button(Fenster, command=ZelleEKFarbwechsel)
        Zelle[4][11] = Button(Fenster, command=ZelleELFarbwechsel)
        Zelle[5][10] = Button(Fenster, command=ZelleFKFarbwechsel)
        Zelle[5][11] = Button(Fenster, command=ZelleFLFarbwechsel)
        Zelle[6][10] = Button(Fenster, command=ZelleGKFarbwechsel)
        Zelle[6][11] = Button(Fenster, command=ZelleGLFarbwechsel)
        Zelle[7][10] = Button(Fenster, command=ZelleHKFarbwechsel)
        Zelle[7][11] = Button(Fenster, command=ZelleHLFarbwechsel)
        Zelle[8][10] = Button(Fenster, command=ZelleIKFarbwechsel)
        Zelle[8][11] = Button(Fenster, command=ZelleILFarbwechsel)
        Zelle[9][10] = Button(Fenster, command=ZelleJKFarbwechsel)
        Zelle[9][11] = Button(Fenster, command=ZelleJLFarbwechsel)
        Zelle[10][10] = Button(Fenster, command=ZelleKKFarbwechsel)
        Zelle[10][11] = Button(Fenster, command=ZelleKLFarbwechsel)
        Zelle[11][10] = Button(Fenster, command=ZelleLKFarbwechsel)
        Zelle[11][11] = Button(Fenster, command=ZelleLLFarbwechsel)
        Zelle[10][0] = Button(Fenster, command=ZelleKAFarbwechsel)
        Zelle[11][0] = Button(Fenster, command=ZelleLAFarbwechsel)
        Zelle[10][1] = Button(Fenster, command=ZelleKBFarbwechsel)
        Zelle[11][1] = Button(Fenster, command=ZelleLBFarbwechsel)
        Zelle[10][2] = Button(Fenster, command=ZelleKCFarbwechsel)
        Zelle[11][2] = Button(Fenster, command=ZelleLCFarbwechsel)
        Zelle[10][3] = Button(Fenster, command=ZelleKDFarbwechsel)
        Zelle[11][3] = Button(Fenster, command=ZelleLDFarbwechsel)
        Zelle[10][4] = Button(Fenster, command=ZelleKEFarbwechsel)
        Zelle[11][4] = Button(Fenster, command=ZelleLEFarbwechsel)
        Zelle[10][5] = Button(Fenster, command=ZelleKFFarbwechsel)
        Zelle[11][5] = Button(Fenster, command=ZelleLFFarbwechsel)
        Zelle[10][6] = Button(Fenster, command=ZelleKGFarbwechsel)
        Zelle[11][6] = Button(Fenster, command=ZelleLGFarbwechsel)
        Zelle[10][7] = Button(Fenster, command=ZelleKHFarbwechsel)
        Zelle[11][7] = Button(Fenster, command=ZelleLHFarbwechsel)
        Zelle[10][8] = Button(Fenster, command=ZelleKIFarbwechsel)
        Zelle[11][8] = Button(Fenster, command=ZelleLIFarbwechsel)
        Zelle[10][9] = Button(Fenster, command=ZelleKJFarbwechsel)
        Zelle[11][9] = Button(Fenster, command=ZelleLJFarbwechsel)
    if SpielBrettLaenge > 12:
        # Nur bei der Spielbrettgröße von 14x14 oder 16x16 werden diese Zellen generiert.
        Zelle[0][12] = Button(Fenster, command=ZelleAMFarbwechsel)
        Zelle[0][13] = Button(Fenster, command=ZelleANFarbwechsel)
        Zelle[1][12] = Button(Fenster, command=ZelleBMFarbwechsel)
        Zelle[1][13] = Button(Fenster, command=ZelleBNFarbwechsel)
        Zelle[2][12] = Button(Fenster, command=ZelleCMFarbwechsel)
        Zelle[2][13] = Button(Fenster, command=ZelleCNFarbwechsel)
        Zelle[3][12] = Button(Fenster, command=ZelleDMFarbwechsel)
        Zelle[3][13] = Button(Fenster, command=ZelleDNFarbwechsel)
        Zelle[4][12] = Button(Fenster, command=ZelleEMFarbwechsel)
        Zelle[4][13] = Button(Fenster, command=ZelleENFarbwechsel)
        Zelle[5][12] = Button(Fenster, command=ZelleFMFarbwechsel)
        Zelle[5][13] = Button(Fenster, command=ZelleFNFarbwechsel)
        Zelle[6][12] = Button(Fenster, command=ZelleGMFarbwechsel)
        Zelle[6][13] = Button(Fenster, command=ZelleGNFarbwechsel)
        Zelle[7][12] = Button(Fenster, command=ZelleHMFarbwechsel)
        Zelle[7][13] = Button(Fenster, command=ZelleHNFarbwechsel)
        Zelle[8][12] = Button(Fenster, command=ZelleIMFarbwechsel)
        Zelle[8][13] = Button(Fenster, command=ZelleINFarbwechsel)
        Zelle[9][12] = Button(Fenster, command=ZelleJMFarbwechsel)
        Zelle[9][13] = Button(Fenster, command=ZelleJNFarbwechsel)
        Zelle[10][12] = Button(Fenster, command=ZelleKMFarbwechsel)
        Zelle[10][13] = Button(Fenster, command=ZelleKNFarbwechsel)
        Zelle[11][12] = Button(Fenster, command=ZelleLMFarbwechsel)
        Zelle[11][13] = Button(Fenster, command=ZelleLNFarbwechsel)
        Zelle[12][12] = Button(Fenster, command=ZelleMMFarbwechsel)
        Zelle[12][13] = Button(Fenster, command=ZelleMNFarbwechsel)
        Zelle[13][12] = Button(Fenster, command=ZelleNMFarbwechsel)
        Zelle[13][13] = Button(Fenster, command=ZelleNNFarbwechsel)
        Zelle[12][0] = Button(Fenster, command=ZelleMAFarbwechsel)
        Zelle[13][0] = Button(Fenster, command=ZelleNAFarbwechsel)
        Zelle[12][1] = Button(Fenster, command=ZelleMBFarbwechsel)
        Zelle[13][1] = Button(Fenster, command=ZelleNBFarbwechsel)
        Zelle[12][2] = Button(Fenster, command=ZelleMCFarbwechsel)
        Zelle[13][2] = Button(Fenster, command=ZelleNCFarbwechsel)
        Zelle[12][3] = Button(Fenster, command=ZelleMDFarbwechsel)
        Zelle[13][3] = Button(Fenster, command=ZelleNDFarbwechsel)
        Zelle[12][4] = Button(Fenster, command=ZelleMEFarbwechsel)
        Zelle[13][4] = Button(Fenster, command=ZelleNEFarbwechsel)
        Zelle[12][5] = Button(Fenster, command=ZelleMFFarbwechsel)
        Zelle[13][5] = Button(Fenster, command=ZelleNFFarbwechsel)
        Zelle[12][6] = Button(Fenster, command=ZelleMGFarbwechsel)
        Zelle[13][6] = Button(Fenster, command=ZelleNGFarbwechsel)
        Zelle[12][7] = Button(Fenster, command=ZelleMHFarbwechsel)
        Zelle[13][7] = Button(Fenster, command=ZelleNHFarbwechsel)
        Zelle[12][8] = Button(Fenster, command=ZelleMIFarbwechsel)
        Zelle[13][8] = Button(Fenster, command=ZelleNIFarbwechsel)
        Zelle[12][9] = Button(Fenster, command=ZelleMJFarbwechsel)
        Zelle[13][9] = Button(Fenster, command=ZelleNJFarbwechsel)
        Zelle[12][10] = Button(Fenster, command=ZelleMKFarbwechsel)
        Zelle[13][10] = Button(Fenster, command=ZelleNKFarbwechsel)
        Zelle[12][11] = Button(Fenster, command=ZelleMLFarbwechsel)
        Zelle[13][11] = Button(Fenster, command=ZelleNLFarbwechsel)
    if SpielBrettLaenge > 14:
        # Nur bei der Spielbrettgröße von 16x16 werden diese Zellen generiert.
        Zelle[0][14] = Button(Fenster, command=ZelleAOFarbwechsel)
        Zelle[0][15] = Button(Fenster, command=ZelleAPFarbwechsel)
        Zelle[1][14] = Button(Fenster, command=ZelleBOFarbwechsel)
        Zelle[1][15] = Button(Fenster, command=ZelleBPFarbwechsel)
        Zelle[2][14] = Button(Fenster, command=ZelleCOFarbwechsel)
        Zelle[2][15] = Button(Fenster, command=ZelleCPFarbwechsel)
        Zelle[3][14] = Button(Fenster, command=ZelleDOFarbwechsel)
        Zelle[3][15] = Button(Fenster, command=ZelleDPFarbwechsel)
        Zelle[4][14] = Button(Fenster, command=ZelleEOFarbwechsel)
        Zelle[4][15] = Button(Fenster, command=ZelleEPFarbwechsel)
        Zelle[5][14] = Button(Fenster, command=ZelleFOFarbwechsel)
        Zelle[5][15] = Button(Fenster, command=ZelleFPFarbwechsel)
        Zelle[6][14] = Button(Fenster, command=ZelleGOFarbwechsel)
        Zelle[6][15] = Button(Fenster, command=ZelleGPFarbwechsel)
        Zelle[7][14] = Button(Fenster, command=ZelleHOFarbwechsel)
        Zelle[7][15] = Button(Fenster, command=ZelleHPFarbwechsel)
        Zelle[8][14] = Button(Fenster, command=ZelleIOFarbwechsel)
        Zelle[8][15] = Button(Fenster, command=ZelleIPFarbwechsel)
        Zelle[9][14] = Button(Fenster, command=ZelleJOFarbwechsel)
        Zelle[9][15] = Button(Fenster, command=ZelleJPFarbwechsel)
        Zelle[10][14] = Button(Fenster, command=ZelleKOFarbwechsel)
        Zelle[10][15] = Button(Fenster, command=ZelleKPFarbwechsel)
        Zelle[11][14] = Button(Fenster, command=ZelleLOFarbwechsel)
        Zelle[11][15] = Button(Fenster, command=ZelleLPFarbwechsel)
        Zelle[12][14] = Button(Fenster, command=ZelleMOFarbwechsel)
        Zelle[12][15] = Button(Fenster, command=ZelleMPFarbwechsel)
        Zelle[13][14] = Button(Fenster, command=ZelleNOFarbwechsel)
        Zelle[13][15] = Button(Fenster, command=ZelleNPFarbwechsel)
        Zelle[14][14] = Button(Fenster, command=ZelleOOFarbwechsel)
        Zelle[14][15] = Button(Fenster, command=ZelleOPFarbwechsel)
        Zelle[15][14] = Button(Fenster, command=ZellePOFarbwechsel)
        Zelle[15][15] = Button(Fenster, command=ZellePPFarbwechsel)
        Zelle[14][0] = Button(Fenster, command=ZelleOAFarbwechsel)
        Zelle[15][0] = Button(Fenster, command=ZellePAFarbwechsel)
        Zelle[14][1] = Button(Fenster, command=ZelleOBFarbwechsel)
        Zelle[15][1] = Button(Fenster, command=ZellePBFarbwechsel)
        Zelle[14][2] = Button(Fenster, command=ZelleOCFarbwechsel)
        Zelle[15][2] = Button(Fenster, command=ZellePCFarbwechsel)
        Zelle[14][3] = Button(Fenster, command=ZelleODFarbwechsel)
        Zelle[15][3] = Button(Fenster, command=ZellePDFarbwechsel)
        Zelle[14][4] = Button(Fenster, command=ZelleOEFarbwechsel)
        Zelle[15][4] = Button(Fenster, command=ZellePEFarbwechsel)
        Zelle[14][5] = Button(Fenster, command=ZelleOFFarbwechsel)
        Zelle[15][5] = Button(Fenster, command=ZellePFFarbwechsel)
        Zelle[14][6] = Button(Fenster, command=ZelleOGFarbwechsel)
        Zelle[15][6] = Button(Fenster, command=ZellePGFarbwechsel)
        Zelle[14][7] = Button(Fenster, command=ZelleOHFarbwechsel)
        Zelle[15][7] = Button(Fenster, command=ZellePHFarbwechsel)
        Zelle[14][8] = Button(Fenster, command=ZelleOIFarbwechsel)
        Zelle[15][8] = Button(Fenster, command=ZellePIFarbwechsel)
        Zelle[14][9] = Button(Fenster, command=ZelleOJFarbwechsel)
        Zelle[15][9] = Button(Fenster, command=ZellePJFarbwechsel)
        Zelle[14][10] = Button(Fenster, command=ZelleOKFarbwechsel)
        Zelle[15][10] = Button(Fenster, command=ZellePKFarbwechsel)
        Zelle[14][11] = Button(Fenster, command=ZelleOLFarbwechsel)
        Zelle[15][11] = Button(Fenster, command=ZellePLFarbwechsel)
        Zelle[14][12] = Button(Fenster, command=ZelleOMFarbwechsel)
        Zelle[15][12] = Button(Fenster, command=ZellePMFarbwechsel)
        Zelle[14][13] = Button(Fenster, command=ZelleONFarbwechsel)
        Zelle[15][13] = Button(Fenster, command=ZellePNFarbwechsel)
    Index = 0
    while Index < SpielBrettLaenge:
        SupIndex = 0
        # Berechnung, wo die Zellen platziert werden müssen
        if SpielBrettLaenge == 8:
            Zentrierung = 180
        if SpielBrettLaenge == 10:
            Zentrierung = 135
        if SpielBrettLaenge == 12:
            Zentrierung = 90
        if SpielBrettLaenge == 14:
            Zentrierung = 45
        if SpielBrettLaenge == 16:
            Zentrierung = 0
        # Die Zellen werden platziert.
        while SupIndex < SpielBrettLaenge:
            Zelle[Index][SupIndex].place(x=45*SupIndex+5+Zentrierung, y=45*Index+5+Zentrierung, width=44, height=44)
            SupIndex = SupIndex + 1
        Index = Index + 1

# sorgt dafür, dass die Zellen korrekt angezeigt werden
def ButtonsSpawner():   
    global Farbe
    global ZelleFarbwechselAktiviert
    global SpielerZugTyp
    global SpielBrettLaenge
    if ZelleFarbwechselAktiviert == True:
        # Das X in jeder Zelle erhält seine richtige Farbe. Es wird hierfür eine weitere Generation berechnet.
        Punktfarbe=Generation(Farbe)
    else:
        # Das X in der Mitte bekommt die gleiche Farbe wie die Zelle.
        Punktfarbe=GleichePunktfarbe(Farbe)
    global PositionsVermerkZweiZwei
    global PositionsVermerkZweiDrei
    global Annulieren
    if Annulieren == False:
        if SpielerZugTyp < 3:
            PositionsVermerkZweiZwei = [-1, -1, 0]
            PositionsVermerkZweiDrei = [-1, -1, 0]
        if not PositionsVermerkZweiZwei[2] == 0:
            Farbe[PositionsVermerkZweiZwei[0]][PositionsVermerkZweiZwei[1]] = 'grey'
        if not PositionsVermerkZweiDrei[2] == 0:
            Farbe[PositionsVermerkZweiDrei[0]][PositionsVermerkZweiDrei[1]] = 'grey'
    Index = 0
    # Hat der Spieler im Hauptmenu eine andere Farbe für die Zellen ausgewählt als die in der Standarteinstellung, dann wird hier die Farbe entsprechend geändert.
    Farbe,Punktfarbe=FarbkonvertierungHin(Farbe,Punktfarbe)
    # Die Zellen erhalten ihre korrekte Farbe
    while Index < SpielBrettLaenge:
        SupIndex = 0
        while SupIndex < SpielBrettLaenge:
            Zelle[Index][SupIndex].config(text='x', fg=Punktfarbe[Index][SupIndex], bg=Farbe[Index][SupIndex], font=('Black_Arial', 25))
            SupIndex = SupIndex + 1
        Index = Index + 1
    # Die Farben der Zelle, die bei der "FarbkonvertierungHin" geändert worden sind, werden hier wieder ihre ursprüngliche Farbe annehmen.
    Farbe,Punktfarbe=FarbkonvertierungRueck(Farbe,Punktfarbe)
    if not PositionsVermerkZweiZwei[2] == 0:
        Farbe[PositionsVermerkZweiZwei[0]][PositionsVermerkZweiZwei[1]] = 'black'
    if not PositionsVermerkZweiDrei[2] == 0:
        Farbe[PositionsVermerkZweiDrei[0]][PositionsVermerkZweiDrei[1]] = 'black'

def FarbkonvertierungHin(Farbe, Punktfarbe):
    # Hat der Spieler im Hauptmenu eine andere Farbe für die Zellen ausgewählt als die in der Standarteinstellung, dann wird hier die Farbe entsprechend geändert.
    global SpielerFarbe
    FarbeNeu = ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black']
    PunktfarbeNeu = ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black']
    Index = 0
    while Index < 16:
        SupIndex = 0
        while SupIndex < 16:
            if SpielerFarbe[0] == 'red':
                if Farbe[Index][SupIndex] == 'red':
                    FarbeNeu[Index][SupIndex] = 'red'
                if Farbe[Index][SupIndex] == 'orange':
                    FarbeNeu[Index][SupIndex] = 'orange'
            if SpielerFarbe[0] == 'blue':
                if Farbe[Index][SupIndex] == 'red':
                    FarbeNeu[Index][SupIndex] = 'blue'
                if Farbe[Index][SupIndex] == 'orange':
                    FarbeNeu[Index][SupIndex] = 'lightblue'
            if SpielerFarbe[0] == 'yellow':
                if Farbe[Index][SupIndex] == 'red':
                    FarbeNeu[Index][SupIndex] = 'yellow'
                if Farbe[Index][SupIndex] == 'orange':
                    FarbeNeu[Index][SupIndex] = 'lightyellow'
            if SpielerFarbe[0] == 'green':
                if Farbe[Index][SupIndex] == 'red':
                    FarbeNeu[Index][SupIndex] = 'green'
                if Farbe[Index][SupIndex] == 'orange':
                    FarbeNeu[Index][SupIndex] = 'lightgreen'
            SupIndex = SupIndex + 1
        Index = Index + 1
    Index = 0
    while Index < 16:
        SupIndex = 0
        while SupIndex < 16:
            if SpielerFarbe[1] == 'red':
                if Farbe[Index][SupIndex] == 'blue':
                    FarbeNeu[Index][SupIndex] = 'red'
                if Farbe[Index][SupIndex] == 'lightblue':
                    FarbeNeu[Index][SupIndex] = 'orange'
            if SpielerFarbe[1] == 'blue':
                if Farbe[Index][SupIndex] == 'blue':
                    FarbeNeu[Index][SupIndex] = 'blue'
                if Farbe[Index][SupIndex] == 'lightblue':
                    FarbeNeu[Index][SupIndex] = 'lightblue'
            if SpielerFarbe[1] == 'yellow':
                if Farbe[Index][SupIndex] == 'blue':
                    FarbeNeu[Index][SupIndex] = 'yellow'
                if Farbe[Index][SupIndex] == 'lightblue':
                    FarbeNeu[Index][SupIndex] = 'lightyellow'
            if SpielerFarbe[1] == 'green':
                if Farbe[Index][SupIndex] == 'blue':
                    FarbeNeu[Index][SupIndex] = 'green'
                if Farbe[Index][SupIndex] == 'lightblue':
                    FarbeNeu[Index][SupIndex] = 'lightgreen'
            SupIndex = SupIndex + 1
        Index = Index + 1
    Index = 0
    while Index < 16:
        SupIndex = 0
        while SupIndex < 16:
            if SpielerFarbe[0] == 'red':
                if Punktfarbe[Index][SupIndex] == 'red':
                    PunktfarbeNeu[Index][SupIndex] = 'red'
            if SpielerFarbe[0] == 'blue':
                if Punktfarbe[Index][SupIndex] == 'red':
                    PunktfarbeNeu[Index][SupIndex] = 'blue'
            if SpielerFarbe[0] == 'yellow':
                if Punktfarbe[Index][SupIndex] == 'red':
                    PunktfarbeNeu[Index][SupIndex] = 'yellow'
            if SpielerFarbe[0] == 'green':
                if Punktfarbe[Index][SupIndex] == 'red':
                    PunktfarbeNeu[Index][SupIndex] = 'green'
            SupIndex = SupIndex + 1
        Index = Index + 1
    Index = 0
    while Index < 16:
        SupIndex = 0
        while SupIndex < 16:
            if SpielerFarbe[1] == 'blue':
                if Punktfarbe[Index][SupIndex] == 'blue':
                    PunktfarbeNeu[Index][SupIndex] = 'blue'
            if SpielerFarbe[1] == 'red':
                if Punktfarbe[Index][SupIndex] == 'blue':
                    PunktfarbeNeu[Index][SupIndex] = 'red'
            if SpielerFarbe[1] == 'yellow':
                if Punktfarbe[Index][SupIndex] == 'blue':
                    PunktfarbeNeu[Index][SupIndex] = 'yellow'
            if SpielerFarbe[1] == 'green':
                if Punktfarbe[Index][SupIndex] == 'blue':
                    PunktfarbeNeu[Index][SupIndex] = 'green'
            SupIndex = SupIndex + 1
        Index = Index + 1
    Index = 0
    while Index < 16:
        SupIndex = 0
        while SupIndex < 16:
            if Farbe[Index][SupIndex] == 'grey':
                FarbeNeu[Index][SupIndex] = 'grey'
            if Farbe[Index][SupIndex] == 'white':
                FarbeNeu[Index][SupIndex] = 'white'
            SupIndex = SupIndex + 1
        Index = Index + 1
    return(FarbeNeu, PunktfarbeNeu)   
    
# Die Farben der Zelle, die bei der "FarbkonvertierungHin" geändert worden sind, werden hier wieder ihre ursprüngliche Farbe annehmen.
def FarbkonvertierungRueck(Farbe,Punktfarbe):
    global SpielerFarbe
    FarbeNeu = ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black']
    PunktfarbeNeu = ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black']
    Index = 0
    while Index < 16:
        SupIndex = 0
        while SupIndex < 16:
            if SpielerFarbe[0] == 'red':
                if Farbe[Index][SupIndex] == 'red':
                    FarbeNeu[Index][SupIndex] = 'red'
                if Farbe[Index][SupIndex] == 'orange':
                    FarbeNeu[Index][SupIndex] = 'orange'
            if SpielerFarbe[0] == 'blue':
                if Farbe[Index][SupIndex] == 'blue':
                    FarbeNeu[Index][SupIndex] = 'red'
                if Farbe[Index][SupIndex] == 'lightblue':
                    FarbeNeu[Index][SupIndex] = 'orange'
            if SpielerFarbe[0] == 'yellow':
                if Farbe[Index][SupIndex] == 'yellow':
                    FarbeNeu[Index][SupIndex] = 'red'
                if Farbe[Index][SupIndex] == 'lightyellow':
                    FarbeNeu[Index][SupIndex] = 'orange'
            if SpielerFarbe[0] == 'green':
                if Farbe[Index][SupIndex] == 'green':
                    FarbeNeu[Index][SupIndex] = 'red'
                if Farbe[Index][SupIndex] == 'lightgreen':
                    FarbeNeu[Index][SupIndex] = 'orange'
            SupIndex = SupIndex + 1
        Index = Index + 1
    Index = 0
    while Index < 16:
        SupIndex = 0
        while SupIndex < 16:
            if SpielerFarbe[1] == 'red':
                if Farbe[Index][SupIndex] == 'red':
                    FarbeNeu[Index][SupIndex] = 'blue'
                if Farbe[Index][SupIndex] == 'orange':
                    FarbeNeu[Index][SupIndex] = 'lightblue'
            if SpielerFarbe[1] == 'blue':
                if Farbe[Index][SupIndex] == 'blue':
                    FarbeNeu[Index][SupIndex] = 'blue'
                if Farbe[Index][SupIndex] == 'lightblue':
                    FarbeNeu[Index][SupIndex] = 'lightblue'
            if SpielerFarbe[1] == 'yellow':
                if Farbe[Index][SupIndex] == 'yellow':
                    FarbeNeu[Index][SupIndex] = 'blue'
                if Farbe[Index][SupIndex] == 'lightyellow':
                    FarbeNeu[Index][SupIndex] = 'lightblue'
            if SpielerFarbe[1] == 'green':
                if Farbe[Index][SupIndex] == 'green':
                    FarbeNeu[Index][SupIndex] = 'blue'
                if Farbe[Index][SupIndex] == 'lightgreen':
                    FarbeNeu[Index][SupIndex] = 'lightblue'
            SupIndex = SupIndex + 1
        Index = Index + 1
    Index = 0
    while Index < 16:
        SupIndex = 0
        while SupIndex < 16:
            if SpielerFarbe[0] == 'red':
                if Punktfarbe[Index][SupIndex] == 'red':
                    PunktfarbeNeu[Index][SupIndex] = 'red'
            if SpielerFarbe[0] == 'blue':
                if Punktfarbe[Index][SupIndex] == 'blue':
                    PunktfarbeNeu[Index][SupIndex] = 'red'
            if SpielerFarbe[0] == 'yellow':
                if Punktfarbe[Index][SupIndex] == 'yellow':
                    PunktfarbeNeu[Index][SupIndex] = 'red'
            if SpielerFarbe[0] == 'green':
                if Punktfarbe[Index][SupIndex] == 'green':
                    PunktfarbeNeu[Index][SupIndex] = 'red'
            SupIndex = SupIndex + 1
        Index = Index + 1
    Index = 0
    while Index < 16:
        SupIndex = 0
        while SupIndex < 16:
            if SpielerFarbe[1] == 'blue':
                if Punktfarbe[Index][SupIndex] == 'blue':
                    PunktfarbeNeu[Index][SupIndex] = 'blue'
            if SpielerFarbe[1] == 'red':
                if Punktfarbe[Index][SupIndex] == 'red':
                    PunktfarbeNeu[Index][SupIndex] = 'blue'
            if SpielerFarbe[1] == 'yellow':
                if Punktfarbe[Index][SupIndex] == 'yellow':
                    PunktfarbeNeu[Index][SupIndex] = 'blue'
            if SpielerFarbe[1] == 'green':
                if Punktfarbe[Index][SupIndex] == 'blue':
                    PunktfarbeNeu[Index][SupIndex] = 'blue'
            SupIndex = SupIndex + 1
        Index = Index + 1
    Index = 0
    while Index < 16:
        SupIndex = 0
        while SupIndex < 16:
            if Farbe[Index][SupIndex] == 'grey':
                FarbeNeu[Index][SupIndex] = 'grey'
            if Farbe[Index][SupIndex] == 'white':
                FarbeNeu[Index][SupIndex] = 'white'
            SupIndex = SupIndex + 1
        Index = Index + 1
    return(FarbeNeu, PunktfarbeNeu)
    
def ButtonDeSpawner():
    # Die Zellen und der "Zurück zum Hauptmenu" Button werden gelöscht.
    global SpielBrettLaenge
    ZurueckButton.destroy()
    Index = 0
    while Index < SpielBrettLaenge:
        SupIndex = 0
        while SupIndex < SpielBrettLaenge:
            Zelle[Index][SupIndex].destroy()
            SupIndex = SupIndex + 1
        Index = Index + 1
        

def ZellenLoeschen():
    # Alle Zellen werden getötet.
    global Farbe
    Farbe = ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black']
    Fenster.quit()
    
def AntiDebug():
    # Der Benutzer hat den Button "Zurück zum Hauptmenu" angeklickt.
    global DebugWiederholung
    global ImSpiel
    DebugWiederholung = False
    ImSpiel = False
    global NochImZug
    NochImZug = False
    global NochmalSpielen
    NochmalSpielen = False
    ZellenLoeschen()

def DebugModusStarten():
    # Der Benutzer hat den Button "Game of Life ausprobieren" im Hauptmenu angeklickt.
    global DebugModusStarter
    DebugModusStarter = True
    global MenuLoop
    MenuLoop = False
    Fenster.quit()

def Debug():
    # Der Benutzer startet den "Game of Life" Modus.
    global DebugWiederholung
    DebugWiederholung = True
    global ButtonAendern
    ButtonAendern = True
    global ResetZelle
    ResetZelle = [-1, -1]
    global SpielerZugTyp
    SpielerZugTyp = -1
    global GenerationButton
    global ZellenLoeschButton
    global KIMoveButton
    while DebugWiederholung == True:
        # Der Benutzer befindet sich im "Game of Life" Modus so lange, bis er ihn beendet.
        ButtonsSpawner()
        GenerationButton = Button(Fenster, text='Nächste Generation', bg='grey', command=GenerationTriggerer)
        GenerationButton.config(font=('Arial', 19))
        GenerationButton.place(x=770,y=266)
        ZellenLoeschButton = Button(Fenster, text='Alle Zellen töten', bg='lightgrey', command=ZellenLoeschen)
        ZellenLoeschButton.config(font=('Arial', 17))
        ZellenLoeschButton.place(x=800,y=340)
        KlugeKIMoveButton = Button(Fenster, text='kluge KI Zug', bg='lightgrey', fg='black', command=ComputerZugKlug)
        KlugeKIMoveButton.config(font=('Arial', 17))
        #KlugeKIMoveButton.place(x=815, y=195) # entfernen um ein Debug-Feature zu nutzen, welches nicht im fertigen Spiel vorhanden ist.
        DummeKIMoveButton = Button(Fenster, text='dumme KI Zug', bg='lightgrey', fg='black',command=ComputerZugDumm)
        DummeKIMoveButton.config(font=('Arial', 17))
        #DummeKIMoveButton.place(x=805, y=125) # entfernen um ein Debug-Feature zu nutzen, welches nicht im fertigen Spiel vorhanden ist.
        Fenster.mainloop()
        ZellenLoeschButton.destroy()
        GenerationButton.destroy()
        KlugeKIMoveButton.destroy()
        DummeKIMoveButton.destroy()

def RotKillCheck(Farbe):
    # Es wird überprüft, ob alle Zellen von Spieler 1 tot sind.
    global SpielBrettLaenge
    Index = 0
    Rotzaehlung = 0
    Gekillt = False
    while Index < SpielBrettLaenge:
        SupIndex = 0
        while SupIndex < SpielBrettLaenge:
            if Farbe[Index][SupIndex] == 'red':
                Rotzaehlung = Rotzaehlung + 1
            SupIndex = SupIndex + 1
        Index = Index + 1
    if Rotzaehlung == 0:
        Gekillt = True
    return(Gekillt)

def BlauKillCheck(Farbe):
    # Es wird überprüft, ob alle Zellen von Spieler 2 tot sind.
    global SpielBrettLaenge
    Index = 0
    Blauzaehlung = 0
    Gekillt = False
    while Index < SpielBrettLaenge:
        SupIndex = 0
        while SupIndex < SpielBrettLaenge:
            if Farbe[Index][SupIndex] == 'blue':
                Blauzaehlung = Blauzaehlung + 1
            SupIndex = SupIndex + 1
        Index = Index + 1
    if Blauzaehlung == 0:
        Gekillt = True
    return(Gekillt)

# Unbenutztes Feature: Der Benutzer aktiviert die dumme KI im "Game of Life" Modus.
def ComputerZugDumm():
    global ComputerStaerke
    global SpielerAmZug
    ComputerStaerke = 1
    SpielerAmZug = 2
    ComputerZug()
    
# Unbenutztes Feature: Der Benutzer aktiviert die kluge KI im "Game of Life" Modus.
def ComputerZugKlug():
    global ComputerStaerke
    global SpielerAmZug
    ComputerStaerke = 2
    SpielerAmZug = 2
    ComputerZug()

# Der Compter macht seinen Zug. (Teil 1) ComputerStaerke 1 = dumme KI -- ComputerStaerke 2 = kluge KI
def ComputerZug():
    global ComputerStaerke
    global ComputerStaerkeEins
    global ComputerStaerkeHier
    global SpielerAmZug
    # Ermitteln der Computerstaerke
    if SpielerAmZug == 2:
        if ComputerStaerke == 1:
            ComputerStaerkeHier = 1
        else:
            ComputerStaerkeHier = 2
    else: 
        if ComputerStaerkeEins == 1:
            ComputerStaerkeHier = 1
        else:
            ComputerStaerkeHier = 2
    global Farbe
    global ComputerZugSchritt
    global Chance
    # Hier wird die Chance ermittelt, dass die dumme KI einen besseren Zug wirklich auch als den besseren deklariert. Je mehr eigene Zellen am Leben sind, desto unwahrscheinlicher ist es.
    if SpielerAmZug == 2:
        Chance=BlauErmittlung()
    else:
        Chance=RotErmittlung()
    Chance = Chance // 2 + 1
    ComputerZugSchritt = 1
    # Vorbereitung für die nächsten Schrite, indem erforderliche Variablen generiert werden.
    BesteZelle = [-1, -1, -1, -1, -1, -1, -1]
    BesteEigeneZelle = [-1, -1, -1]
    BesteEigeneZelleZwei = [-1, -1, -1]
    global SpielBrettLaenge
    ErstesMal = True
    EigeneFarbeWichtig = 2
    Index = 0
    # Jede Zelle wird einzelnt getötet, wenn sie am Leben ist.
    while Index < SpielBrettLaenge:
        SupIndex = 0
        while SupIndex < SpielBrettLaenge:
            if not Farbe[Index][SupIndex] == 'black':
                if SpielerAmZug == 2:
                    if Farbe[Index][SupIndex] == 'blue':
                        BlaueZelle = True
                    else:
                        BlaueZelle = False
                else:
                    if Farbe[Index][SupIndex] == 'red':
                        BlaueZelle = True
                    else:
                        BlaueZelle = False
                FarbeZurueck = Farbe[Index][SupIndex]
                Farbe[Index][SupIndex] = 'black'
                # Es wird eine Generation berechnet.
                FarbeTest=Generation(Farbe)
                # Wenn nach einer Generation alle gegnerischen Zellen tot sind und mindestens eine eigene Zelle noch am Leben ist, dann deklariert die kluge KI diesen Zug als den aller besten Zug.
                if SpielerAmZug == 2:
                    Gekillt=RotKillCheck(FarbeTest)
                else:
                    Gekillt=BlauKillCheck(FarbeTest)
                if Gekillt == True:
                    if SpielerAmZug == 2:
                        Gekillt=BlauKillCheck(FarbeTest)
                    else:
                        Gekillt=RotKillCheck(FarbeTest)
                    if Gekillt == False:
                        if ComputerStaerkeHier == 2:
                            BesteZelle[0] = Index
                            BesteZelle[1] = SupIndex
                            BesteZelle[2] = 999
                # Eine zweite Generation wird berechnet.
                FarbeTest=Generation(FarbeTest)
                # Es wird ermittelt, wie viele eigene Zellen am Leben sind im Verhältnis zu wie viele gegnerische Zellen am Leben sind. (Score = Anzahl eigener Zellen minus Anzahl gegnerischer Zellen)
                Score=ScoreCheck(FarbeTest)
                # Wenn es die erste Zelle ist, die überprüft wird, dann ist das für die KI der beste Zug bislang.
                if ErstesMal == True:
                    BesteZelle[0] = Index
                    BesteZelle[1] = SupIndex
                    BesteZelle[2] = Score
                    ErstesMal = False
                else:
                    # Die kluge KI überprüft, ob durch diesen Zug alle gegnerischen Zellen tot sind und ob noch mindestens eine eigene Zelle am Leben ist.  Ist dies der Fall, dann deklariert die kluge KI diesen Zug als den Besten, es sei denn, es gibt noch einen Zug, welcher alle gegnerischen Zellen nach nur einer Generation tötet.
                    if Score > BesteZelle[2]:
                        Gekillt=BlauKillCheck(FarbeTest)
                        if Gekillt == False:
                            Gekillt=RotKillCheck(FarbeTest)
                            if Gekillt == True:
                                if ComputerStaerke == 2:
                                    Score = 998
                            DiesMachen = True
                            # Ist es die dumme KI, dann wird anhand der Wahrscheinlichkeit von vorhin ausgelost, ob die KI diesen Zug wirklich als den Besseren deklariert.
                            if ComputerStaerke == 1:
                                Zug = randint(1, Chance)
                                if not Zug == 1:
                                    DiesMachen = False
                            if DiesMachen == True:
                                # Ist dieser Zug besser als die vorherigen, dann deklariert die KI diesen Zug als den bislang Besten.
                                BesteZelle[0] = Index
                                BesteZelle[1] = SupIndex
                                BesteZelle[2] = Score
                        elif ComputerStaerkeHier == 1:
                            # Die dumme KI entscheidet anhand der vorhin ermittelten Wahrscheinlichkeit, ob die KI diesen Zug wirklich als den Besseren deklariert.
                            DiesMachen = True
                            if ComputerStaerkeHier == 1:
                                Zug = randint(1, Chance)
                                if Zug == 1:
                                    DiesMachen = False
                            if DiesMachen == True:
                                BesteZelle[0] = Index
                                BesteZelle[1] = SupIndex
                                BesteZelle[2] = Score
                # Unabhängig vom vorherigen Schritt ermittelt hier die KI nochmal die besten 2 eigene Zellen, welche den höchsten Score haben. Das Verfahren läuft ähnlich ab wie vorhin.
                if BlaueZelle == True:
                    if EigeneFarbeWichtig == 2: 
                        # Die erste eigene Zelle wird immer als die bisher Beste deklariert.
                        BesteEigeneZelle[0] = Index
                        BesteEigeneZelle[1] = SupIndex
                        BesteEigeneZelle[2] = Score
                        EigeneFarbeWichtig = 1
                    elif EigeneFarbeWichtig == 1:
                        if Score > BesteEigeneZelle[2]:
                            # Die zweite eigene Zelle hat einen höheren Score wie die Erste und wird als die Beste deklariert und die andere Zelle als die Zweitbeste.
                            BesteEigeneZelleZwei[0] = BesteEigeneZelle[0]
                            BesteEigeneZelleZwei[1] = BesteEigeneZelle[1]
                            BesteEigeneZelleZwei[2] = BesteEigeneZelle[2]
                            BesteEigeneZelle[0] = Index
                            BesteEigeneZelle[1] = SupIndex
                            BesteEigeneZelle[2] = Score
                        else:
                            # Die zweite eigene Zelle hat einen höheren Score wie die Erste und wird als die Zweitbeste deklariert.
                            BesteEigeneZelleZwei[0] = Index
                            BesteEigeneZelleZwei[1] = SupIndex
                            BesteEigeneZelleZwei[2] = Score
                    else:
                        # Ab hier wurden schon 2 eigene Zellen überprüft
                        if Score > BesteEigeneZelleZwei[2]:
                            if Score > BesteEigeneZelle[2]:
                                # Mit einer gewissen Wahrscheinlichkeit deklariert die dumme KI Zellen mit einem höheren Score nicht als bessere Zellen.
                                DiesMachen = True
                                if ComputerStaerkeHier == 1:
                                    Zug = randint(1, Chance)
                                    if not Zug == 1:
                                        DiesMachen = False
                                if DiesMachen == True:
                                    # Der Score ist der bislang höchste und die KI deklariert diese Zelle als die bislang beste und die Zelle, die vorhin die Beste war als die Zweitbeste.
                                    BesteEigeneZelleZwei[0] = BesteEigeneZelle[0]
                                    BesteEigeneZelleZwei[1] = BesteEigeneZelle[1]
                                    BesteEigeneZelleZwei[2] = BesteEigeneZelle[2]
                                    BesteEigeneZelle[0] = Index
                                    BesteEigeneZelle[1] = SupIndex
                                    BesteEigeneZelle[2] = Score
                            else:
                                # Mit einer gewissen Wahrscheinlichkeit deklariert die dumme KI Zellen mit einem höheren Score nicht als bessere Zellen.
                                DiesMachen = True
                                if ComputerStaerkeHier == 1:
                                    Zug = randint(1, Chance)
                                    if not Zug == 1:
                                        DiesMachen = False
                                if DiesMachen == True:
                                    # Der Score ist der Zweithöchste und die KI deklariert diese Zelle als die bislang Zweitbeste.
                                    BesteEigeneZelleZwei[0] = Index
                                    BesteEigeneZelleZwei[1] = SupIndex
                                    BesteEigeneZelleZwei[2] = Score
                Farbe[Index][SupIndex] = FarbeZurueck
            SupIndex = SupIndex + 1
        Index = Index + 1
    if SpielerAmZug == 2:
        Blau=BlauErmittlung()
    else:
        Blau=RotErmittlung()
    if Blau > 1:
         # Wenn mindesten 2 eigene Zellen leben, dann ermittelt die KI nach einem potentiellen besseren Zug, indem sie auch eigene Zellen erschaffen lässt.
        ComputerZugTeilZwei(BesteZelle, BesteEigeneZelle, BesteEigeneZelleZwei)
    else:
        # Wenn nur noch eine eigene Zelle am Leben ist, dann wählt die KI den bislang besten Zug aus.
        ComputerZugErgebnis(BesteZelle)

# Der Compter macht seinen Zug. (Teil 2)
def ComputerZugTeilZwei(BesteZelle, BesteEigeneZelle, BesteEigeneZelleZwei):
    global SpielerAmZug
    global Chance
    global ComputerStaerkeHier
    global ComputerZugSchritt
    ComputerZugSchritt = 2
    global Farbe
    global SpielBrettLaenge
    # Die besten 2 eigene Zellen werden vorübergehend getötet.
    Farbe[BesteEigeneZelle[0]][BesteEigeneZelle[1]] = 'black'
    Farbe[BesteEigeneZelleZwei[0]][BesteEigeneZelleZwei[1]] = 'black'
    Index = 0
    # Jede Zelle wird einzelnt zum Leben gebracht, wenn sie tot ist.
    while Index < SpielBrettLaenge:
        SupIndex = 0
        while SupIndex < SpielBrettLaenge:
            if Farbe[Index][SupIndex] == 'black':
                # Die Farbe der Zelle entspricht der eigenen Farbe.
                if SpielerAmZug == 2:
                    Farbe[Index][SupIndex] = 'blue'
                else:
                    Farbe[Index][SupIndex] = 'red'
                # Es wird eine Generation gemacht.
                FarbeTest=Generation(Farbe)
                # Es wird überprüft, ob durch diesen Zug alle gegnerischen Zellen tot sind und ob noch mindestens eine eigene Zelle am Leben ist. Wenn ja, dann wählt die kluge KI diesen Zug als den aller Besten aus.
                if SpielerAmZug == 2:
                    Gekillt=RotKillCheck(FarbeTest)
                else:
                    Gekillt=BlauKillCheck(FarbeTest)
                if Gekillt == True:
                    if SpielerAmZug == 2:
                        Gekillt=BlauKillCheck(FarbeTest)
                    else:
                        Gekillt=RotKillCheck(FarbeTest)
                    if Gekillt == False:
                        if ComputerStaerkeHier == 2:
                            BesteZelle[0] = BesteEigeneZelle[0]
                            BesteZelle[1] = BesteEigeneZelle[1]
                            BesteZelle[2] = 999
                            BesteZelle[3] = BesteEigeneZelleZwei[0]
                            BesteZelle[4] = BesteEigeneZelleZwei[1]
                            BesteZelle[5] = Index
                            BesteZelle[6] = SupIndex
                # Es wird eine weitere Generation gemacht.
                FarbeTest=Generation(FarbeTest)
                # Es wird ermittelt, wie viele eigene Zellen am Leben sind im Verhältnis zu wie viele gegnerische Zellen am Leben sind. (Score = Anzahl eigener Zellen minus Anzahl gegnerischer Zellen)
                Score=ScoreCheck(FarbeTest)
                if Score > BesteZelle[2]:
                    # Ist dieser Zug besser als alle anderen zuvor, dann deklariert die KI diesen Zug als den bisher Besten.
                    if SpielerAmZug == 2:
                        Gekillt=BlauKillCheck(FarbeTest)
                    else:
                        Gekillt=RotKillCheck(FarbeTest)
                    # Die kluge KI überprüft, ob durch diesen Zug alle gegnerischen Zellen tot sind und ob noch mindestens eine eigene Zelle am Leben ist. Ist dies der Fall, dann deklariert die kluge KI diesen Zug als den Besten, es sei denn, es gibt noch einen Zug, welcher alle gegnerischen Zellen nach nur einer Generation tötet.
                    if Gekillt == False:
                        if SpielerAmZug == 2:
                            Gekillt=RotKillCheck(FarbeTest)
                        else:
                            Gekillt=BlauKillCheck(FarbeTest)
                        if Gekillt == True:
                            if ComputerStaerke == 2:
                                Score = 998
                        DiesMachen = True
                        if ComputerStaerkeHier == 1:
                            Zug = randint(1, Chance * 2)
                            if not Zug == 1:
                                DiesMachen = False
                        if DiesMachen == True:
                            # Ist dieser Zug besser als die vorherigen, dann deklariert die KI diesen Zug als den bislang Besten.
                            BesteZelle[0] = BesteEigeneZelle[0]
                            BesteZelle[1] = BesteEigeneZelle[1]
                            BesteZelle[2] = Score
                            BesteZelle[3] = BesteEigeneZelleZwei[0]
                            BesteZelle[4] = BesteEigeneZelleZwei[1]
                            BesteZelle[5] = Index
                            BesteZelle[6] = SupIndex
                    elif ComputerStaerkeHier == 1:
                        # Gilt nur für die dumme KI: Ist dieser Zug besser als die vorherigen, dann deklariert die KI diesen Zug als den bislang Besten, wenn der Zufall so will.
                        DiesMachen = True
                        if ComputerStaerkeHier == 1:
                            Zug = randint(1, Chance * 2)
                            if not Zug == 1:
                                DiesMachen = False
                        if DiesMachen == True:
                            BesteZelle[0] = BesteEigeneZelle[0]
                            BesteZelle[1] = BesteEigeneZelle[1]
                            BesteZelle[2] = Score
                            BesteZelle[3] = BesteEigeneZelleZwei[0]
                            BesteZelle[4] = BesteEigeneZelleZwei[1]
                            BesteZelle[5] = Index
                            BesteZelle[6] = SupIndex
                Farbe[Index][SupIndex] = 'black'                   
            SupIndex = SupIndex + 1
        Index = Index + 1           
    # Die vorhin getöteten Zellen kommen wieder an Leben mit der selben Farbe die zuvor.
    if SpielerAmZug == 2:
        Farbe[BesteEigeneZelle[0]][BesteEigeneZelle[1]] = 'blue'
        Farbe[BesteEigeneZelleZwei[0]][BesteEigeneZelleZwei[1]] = 'blue'
    else:
        Farbe[BesteEigeneZelle[0]][BesteEigeneZelle[1]] = 'red'
        Farbe[BesteEigeneZelleZwei[0]][BesteEigeneZelleZwei[1]] = 'red'
    # Die KI tat nur eine Entscheidung getroffen, welchen Zug sie nimmt.
    ComputerZugErgebnis(BesteZelle)
    
# Die KI hat nun erfolgreich ihen Zug ermittelt und führt ihn nun aus.
def ComputerZugErgebnis(BesteZelle):
    global SpielerFarbe
    global Farbe
    global GenerationButton
    global ZellenLoeschButton
    global KIMoveButton
    global ZelleFarbwechselAktiviert
    global SpielerAmZug
    global SpielerZugTyp
    SpielerZugTyp = -1
    global PunktfarbenAussnahme
    # DebugWiederholung ist immer False. Dies ist ein Debug-Feature, welches nicht mehr im fertigen Spiel vorhanden ist.
    if DebugWiederholung == False:
        # Von der KI getötete Zellen erscheinen grau und von der KI erschaffene Zellen erscheinen weiß.
        FarbeErinnerung = Farbe[BesteZelle[0]][BesteZelle[1]]
        Farbe[BesteZelle[0]][BesteZelle[1]] = 'grey'
        if BesteZelle[3] > -1:
            Farbe[BesteZelle[3]][BesteZelle[4]] = 'grey'
            Farbe[BesteZelle[5]][BesteZelle[6]] = 'white'
        # Ermittlung, wie viele Zellen jeder Spieler noch hat.
        AnzahlRoterZellen=RotErmittlung()
        AnzahlBlauerZellen=BlauErmittlung()
        if BesteZelle[3] > -1:
            if SpielerAmZug == 1:
                AnzahlRoterZellen = AnzahlRoterZellen + 2
            else:
                AnzahlBlauerZellen = AnzahlBlauerZellen + 2
        else:
            if FarbeErinnerung == 'red':
                AnzahlRoterZellen = AnzahlRoterZellen + 1
            else:
                AnzahlBlauerZellen = AnzahlBlauerZellen + 1
        # Das Label, welches dem Benutzer anzeigt, wie viele Zellen von jedem Spieler noch am Leben sind.
        if SpielerFarbe[0] == 'red':
            RotLabelText = 'Anzahl roter Zellen: ' + str(AnzahlRoterZellen)
        if SpielerFarbe[0] == 'blue':
            RotLabelText = 'Anzahl blauer Zellen: ' + str(AnzahlRoterZellen)
        if SpielerFarbe[0] == 'yellow':
            RotLabelText = 'Anzahl gelber Zellen: ' + str(AnzahlRoterZellen)
        if SpielerFarbe[0] == 'green':
            RotLabelText = 'Anzahl grüner Zellen: ' + str(AnzahlRoterZellen)
        if SpielerFarbe[1] == 'red':
            BlauLabelText = 'Anzahl roter Zellen: ' + str(AnzahlBlauerZellen)
        if SpielerFarbe[1] == 'blue':
            BlauLabelText = 'Anzahl blauer Zellen: ' + str(AnzahlBlauerZellen)
        if SpielerFarbe[1] == 'yellow':
            BlauLabelText = 'Anzahl gelber Zellen: ' + str(AnzahlBlauerZellen)
        if SpielerFarbe[1] == 'green':
            BlauLabelText = 'Anzahl grüner Zellen: ' + str(AnzahlBlauerZellen)
        RotLabelFarbe = SpielerFarbe[0]
        if RotLabelFarbe == 'yellow':
            RotLabelFarbe = '#968A08'
        BlauLabelFarbe = SpielerFarbe[1]
        if BlauLabelFarbe == 'yellow':
            BlauLabelFarbe = '#968A08'
        RotLabel = Label(Fenster, fg=RotLabelFarbe, text=RotLabelText)
        BlauLabel = Label(Fenster, fg=BlauLabelFarbe, text=BlauLabelText)
        RotLabel.config(font=('Black_Arial', 17))
        BlauLabel.config(font=('Black_Arial', 17))
        RotLabel.place(x=785, y=150)
        BlauLabel.place(x=785, y=190)
        # Generierung des "Die KI ist am Zug" Labels.
        if SpielerAmZug == 2:
            DieserSpielerIstAmZugFarbe = SpielerFarbe[1]
            if DieserSpielerIstAmZugFarbe == 'yellow':
                DieserSpielerIstAmZugFarbe = '#968A08'
            DieserSpielerIstAmZug = Label(Fenster, text='Die KI ist am Zug', fg=DieserSpielerIstAmZugFarbe)
        else:
            DieserSpielerIstAmZugFarbe = SpielerFarbe[0]
            if DieserSpielerIstAmZugFarbe == 'yellow':
                DieserSpielerIstAmZugFarbe = '#968A08'
            DieserSpielerIstAmZug = Label(Fenster, text='Die KI ist am Zug', fg=DieserSpielerIstAmZugFarbe)
        DieserSpielerIstAmZug.config(font=('Black_Arial', 20))
        DieserSpielerIstAmZug.place(x=790, y=40)
        # Die Zellen werden auf der GUI korrekt angezeigt.
        PunktfarbenAussnahme = True
        ButtonsSpawner()
        PunktfarbenAussnahme = False
    Farbe[BesteZelle[0]][BesteZelle[1]] = 'black'
    # Die Zellen erhalten nun ihre korrekte Farbe.
    if BesteZelle[3] > -1:
        Farbe[BesteZelle[3]][BesteZelle[4]] = 'black'
        if SpielerAmZug == 2:
            Farbe[BesteZelle[5]][BesteZelle[6]] = 'blue'
        else:
            Farbe[BesteZelle[5]][BesteZelle[6]] = 'red'
    # DebugWiederholung ist immer False. Dies ist ein Debug-Feature, welches nicht im fertigen Spiel mehr vorhanden ist.
    if DebugWiederholung == True:
        ButtonsSpawner()
    else:
        # Generierung des "Weiter" Buttons
        KIMoveWeiterButton = Button(Fenster, bg='lightgrey', fg='black', text='Weiter', command=KIMoveWeiter)
        KIMoveWeiterButton.config(font=('Arial', 20))
        KIMoveWeiterButton.place(x=842, y=250)
        ZelleFarbwechselAktiviert = False
        # Das Spiel wartet so lange, bis der Benutzer auf den "Weiter" Button geklickt hat.
        Fenster.mainloop()
        # Es wird eine Generation gemacht.
        Farbe=Generation(Farbe)
        # Die Labels und Buttons, die vorhin generiert worden sind, werden gelöscht.
        ZelleFarbwechselAktiviert = True
        KIMoveWeiterButton.destroy()
        if SpielerAmZug == 2:
            SpielerAmZug = 1
        else:
            SpielerAmZug = 2
        RotLabel.destroy()
        BlauLabel.destroy()
        DieserSpielerIstAmZug.destroy()

# Der Benutzer den "Weiter" Knopf gedrückt.
def KIMoveWeiter():
    Fenster.quit()

# Es wird ermittelt, wie viele Zellen des 1. Spielers im Verhältnis zu der Anzahl der Zellen des 2. Spielers am Leben sind.
def ScoreCheck(Farbetest):
    global SpielBrettLaenge
    global SpielerAmZug
    Index = 0
    Score = 0
    while Index < SpielBrettLaenge:
        SupIndex = 0
        while SupIndex < SpielBrettLaenge:
            if Farbetest[Index][SupIndex] == 'blue':
                if SpielerAmZug == 2:
                    Score = Score + 1
                else:
                    Score = Score - 1
            if Farbetest[Index][SupIndex] == 'red':
                if SpielerAmZug == 1:
                    Score = Score + 1
                else:
                    Score = Score - 1
            SupIndex = SupIndex + 1
        Index = Index + 1
    return(Score)
        
# Die Zellen am Anfang des Spiels werden hier generiert. (Schritt 2 -> Punktspiegelung und Farbänderung der Zellen von Schritt 1)
def Punktspiegelung(Farbe, Lang, Halblang):
    Index = 0
    while Index < Halblang:
        SupIndex = 0
        while SupIndex < Lang:
            if Farbe[Index][SupIndex] == 'red':
                FarbeUmgekehrt = 'blue'
            if Farbe[Index][SupIndex] == 'blue':
                FarbeUmgekehrt = 'red'
            if Farbe[Index][SupIndex] == 'black':
                FarbeUmgekehrt = 'black'
            PositionX = Lang - Index - 1
            PositionY = Lang - SupIndex - 1
            Farbe[PositionX][PositionY] = FarbeUmgekehrt
            SupIndex = SupIndex + 1
        Index = Index + 1
    return(Farbe)

# Die Zellen am Anfang des Spiels werden hier generiert. (Schritt 1 -> Die obere Hälfte wird generiert)
def SpielBrettGenerierung(Farbe, Lang, Steine):
    Halblang = Lang // 2
    while Steine > 0:
        AuswahlX = randint(1, Halblang)
        AuswahlY = randint(1, Lang)
        AuswahlX = AuswahlX - 1
        AuswahlY = AuswahlY - 1
        if Farbe[AuswahlX][AuswahlY] == 'black':
            AuswahlF = randint(1, 2)
            if AuswahlF == 1:
                Farbe[AuswahlX][AuswahlY] = 'red'
            else:
                Farbe[AuswahlX][AuswahlY] = 'blue'
            Steine = Steine - 1
    Farbe=Punktspiegelung(Farbe, Lang, Halblang)
    return(Farbe)

# Der Benutzer hat den Button "Spiel starten" gedrückt.
def SpielStarten():
    global DebugModusStarter
    DebugModusStarter = False
    global MenuLoop
    MenuLoop = False
    Fenster.quit()

# Der Benutzer hat den Button "Spiel starten" gedrückt und das Spiel wird hier vorbereitet.
def HauptSpiel():
    global SpielImGang
    global Farbe
    global SpielBrettLaenge
    global SpielBrettSteine
    global DebugWiederholung
    global ZelleFarbwechselAktiviert
    global HauptSpielGenerierung
    DebugWiederholung = False
    SpielImGang = True
    if HauptSpielGenerierung == True:
        # Erzeugung der Zellen
        Farbe = ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'] 
        Farbe=SpielBrettGenerierung(Farbe, SpielBrettLaenge, SpielBrettSteine)
        # Zu Beginn startet Spieler 1
        global SpielerAmZug
        SpielerAmZug = 1
    # Erzeugung der Variablen
    global ImSpiel
    ImSpiel = True
    global ButtonAendern
    ButtonAendern = False
    global PositionsVermerk
    global NochmalSpielen
    NochmalSpielen = True
    global ComputerStaerke
    global ComputerStaerkeEins
    # Das Spiel ist im Gang
    while ImSpiel == True:   
        SpeicherKonverterHin()
        if SpielerAmZug == 1:
            if ComputerStaerkeEins == 0:
                ZugVomSpielerVorbereiten()
            else:
                ComputerZug()
                if ZelleFarbwechselAktiviert == True and ImSpiel == True:
                    Gewinncheck()
        else:
            if ComputerStaerke == 0:
                ZugVomSpielerVorbereiten()
            else:
                ComputerZug()
                if ZelleFarbwechselAktiviert == True and ImSpiel == True:
                    Gewinncheck()
    # Das Spiel wurde beendet
    if NochmalSpielen == True:
        NochmalAbfrage()
        
# Bevor der Spieler seinen Zug macht, werden alle vorherigen Aktionen des Spielers zurückgesetzt.
def ZugVomSpielerVorbereiten():
    global SpielerZugTyp
    global ZugBeendet
    ZugBeendet = False
    SpielerZugTyp = 0
    global PositionsVermerkEins
    global PositionsVermerkZweiEins
    global PositionsVermerkZweiZwei
    global PositionsVermerkZweiDrei
    PositionsVermerkEins = [-1, -2, 0]
    PositionsVermerkZweiEins = [-1, -1, 0]
    PositionsVermerkZweiZwei = [-1, -1, 0]
    PositionsVermerkZweiDrei = [-1, -1, 0]
    global ResetZelle
    ResetZelle = [-1, -1]
    global Farbaenderung
    Farbaenderung = [-1, -2, 0]
    global Farbentfernung
    Farbentfernung = [-1, -1]
    # Der Spieler verweilt im Menu.
    Spielerzug()
    # Der Spieler hat seinen Zug gemacht.
    PositionsVermerkEins = [-1, -2, 0]
    PositionsVermerkZweiEins = [-1, -1, 0]
    PositionsVermerkZweiZwei = [-1, -1, 0]
    PositionsVermerkZweiDrei = [-1, -1, 0]
    Reset()

# Der Benutzer hat den Button "Nochmal spielen" angeklickt.
def Neustart():
    global NeustartAbfrage
    NeustartAbfrage = True
    Fenster.quit()

# Das Menu nach einem Spiel wird angezeigt.
def NochmalAbfrage():
    Datei = open('Speicherung.txt', 'w', encoding='iso-8859-1') 
    Datei.write('')
    Datei.close()
    global ZelleFarbwechselAktiviert
    ZelleFarbwechselAktiviert = False
    global NeustartAbfrage
    NeustartAbfrage = False
    global Annulieren
    Annulieren = True
    ButtonsSpawner()
    # Die entsprechenen Buttons werden geladen.
    NochmalButton = Button(Fenster, text='Nochmal spielen', fg='black', bg='lightgrey', command=Neustart)
    NochmalButton.config(font=('Arial', 20))
    NochmalButton.place(x=780, y=280)
    ZurueckButton.place(x=760, y=360)
    # Der Benutzer verweilt in diesem Menu.
    Fenster.mainloop()
    # Die entsprechenen Buttons werden gelöscht bzw. zurückgesetzt.
    ZurueckButton.place(x=757, y=670)
    NochmalButton.destroy()
    GewinnerLabel.destroy()
    ZelleFarbwechselAktiviert = True
    Annulieren = False
    if NeustartAbfrage == True:
        Farbe = ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black']
        HauptSpiel()
    else:
        GewinnerLabel.destroy()
    
def SpeicherKonverterHin():
    # Das Spiel wird gespeichert
    global SpielerAmZug
    global SpielBrettLaenge
    global ComputerStaerke
    global ComputerStaerkeEins
    global SpielerFarbe
    # Generierung des Textes bezüglich KI, Schwierigkeitsgrad und der Spieler, der gerade am Zug ist
    SpeicherText = str(ComputerStaerkeEins) + str(ComputerStaerke) + str(SpielerAmZug)
    # Generierung des Textes bezüglich der Größe des Spielbretts
    if SpielBrettLaenge < 9:
        SpeicherText = SpeicherText + '1'
    elif SpielBrettLaenge < 11:
        SpeicherText = SpeicherText + '2'
    elif SpielBrettLaenge < 13:
        SpeicherText = SpeicherText + '3'
    elif SpielBrettLaenge < 15:
        SpeicherText = SpeicherText + '4'
    else:
        SpeicherText = SpeicherText + '5'
    # Generierung des Textes bezüglich der Größe der Spielbrettfarbe
    if SpielerFarbe[0] == 'red':
        SpeicherText = SpeicherText + '1'
    elif SpielerFarbe[0] == 'blue':
        SpeicherText = SpeicherText + '2'
    elif SpielerFarbe[0] == 'yellow':
        SpeicherText = SpeicherText + '3'
    else:
        SpeicherText = SpeicherText + '4'
    if SpielerFarbe[1] == 'red':
        SpeicherText = SpeicherText + '1'
    elif SpielerFarbe[1] == 'blue':
        SpeicherText = SpeicherText + '2'
    elif SpielerFarbe[1] == 'yellow':
        SpeicherText = SpeicherText + '3'
    else:
        SpeicherText = SpeicherText + '4'
    FarbSpeicherText=SpeicherKonverterHinFarbe()
    SpeicherText = SpeicherText + ' ' + FarbSpeicherText
    Datei = open('Speicherung.txt', 'w', encoding='iso-8859-1')
    Datei.write(SpeicherText)
    Datei.close()

# Generierung des Textes bezüglich der Farbe der Zellen
def SpeicherKonverterHinFarbe():
    global Farbe
    FarbSpeicherText = str()
    Index = 0
    Farbe=GenerationKorrektur(Farbe)
    while Index < len(Farbe):
        SupIndex = 0
        while SupIndex < len(Farbe[Index]):
            if Farbe[Index][SupIndex] == 'black':
                FarbSpeicherText = FarbSpeicherText + '0'
            elif Farbe[Index][SupIndex] == 'red':
                FarbSpeicherText = FarbSpeicherText + '1'
            else:
                FarbSpeicherText = FarbSpeicherText + '2'
            SupIndex = SupIndex + 1
        Index = Index + 1
    Farbe=GenerationAntiKorrektur(Farbe)
    return FarbSpeicherText

# Das Spiel, welches abgebrochen wurde, soll weitergespielt werden
def SpeicherungLaden():
    global SpielerAmZug
    global SpielBrettLaenge
    global ComputerStaerke
    global ComputerStaerkeEins
    global SpielerFarbe
    global Farbe
    Datei = open('Speicherung.txt', 'r', encoding='iso-8859-1')
    SpeicherText = Datei.read()
    Datei.close()
    # Wiederherstellen der Variablen
    ComputerStaerkeEins = int(SpeicherText[0])
    ComputerStaerke = int(SpeicherText[1])
    SpielerAmZug = int(SpeicherText[2])
    if SpeicherText[3] == '1':
        SpielBrettLaenge = 8
    elif SpeicherText[3] == '2':
        SpielBrettLaenge = 10
    elif SpeicherText[3] == '3':
        SpielBrettLaenge = 12
    elif SpeicherText[3] == '4':
        SpielBrettLaenge = 14
    else:
        SpielBrettLaenge = 16
    if SpeicherText[4] == '1':
        SpielerFarbe[0] = 'red'
    elif SpeicherText[4] == '2':
        SpielerFarbe[0] = 'blue'
    elif SpeicherText[4] == '3':
        SpielerFarbe[0] = 'yellow'
    else:
        SpielerFarbe[0] = 'green'
    if SpeicherText[5] == '1':
        SpielerFarbe[1] = 'red'
    elif SpeicherText[5] == '2':
        SpielerFarbe[1] = 'blue'
    elif SpeicherText[5] == '3':
        SpielerFarbe[1] = 'yellow'
    else:
        SpielerFarbe[1] = 'green'
    Farbe=SpeicherungsLadenFarbe(SpeicherText)

# Die Farben werden erzeugt, wenn das Spiel aus der Datei geladen wird
def SpeicherungsLadenFarbe(SpeicherText):
    SpeicherText = SpeicherText[7:]
    Farbe = ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black']
    Index = 0
    while Index < 16:
        SupIndex = 0
        while SupIndex < 17:
            if SpeicherText[0] == '0':  
                Farbe[Index][SupIndex] = 'black'
            elif SpeicherText[0] == '1':  
                Farbe[Index][SupIndex] = 'red'
            else:  
                Farbe[Index][SupIndex] = 'blue'
            SpeicherText = SpeicherText[1:]
            SupIndex = SupIndex + 1
        Index = Index + 1
    return(Farbe)

# Der Spieler hat den Button "gespeichertes Spiel laden" gedrückt
def SpeicherungLadenStart():
    global SpielLaden
    SpielLaden = True
    global MenuLoop
    MenuLoop = False
    Fenster.quit()
    
# Der Button "Spielregeln und Tipps" im Hauptmenu wurde angeklickt.
def TutorialStart():
    global TutorialStarter
    global MenuLoop
    TutorialStarter = True
    MenuLoop = False
    Fenster.quit()

# Der Spieler hat den Button "Weiter" im Tutorial angeklickt.
def TutorialWeiter():
    Fenster.quit()

# Der Spieler hat den Button "Tutorial beenden" angeklickt.
def TutorialBeenden():
    Fenster.quit()
    global TutorialSkip
    TutorialSkip = True

# Das Tutorial wird bendet
def TutorialBeendigung():
    global TutorialSkipButton
    TutorialSkipButton.destroy()
    TutorialBildAnzeige.destroy()

# Das Bild für die erste Seite des Tutorials wird eingeblendet.
def TutorialEins():
    global TutorialSkip
    global TutorialBildAnzeige
    global TutorialWeiterButton
    global TutorialSkipButton
    TutorialSkip = False
    TutorialWeiterButton = Button(Fenster, text='Weiter', bg='grey', command=TutorialWeiter)
    TutorialWeiterButton.config(font=('Arial', 20))
    TutorialWeiterButton.place(x=450, y=670)
    TutorialSkipButton = Button(Fenster, text='Tutorial beenden', bg='lightgrey', command=TutorialBeenden)
    TutorialSkipButton.config(font=('Arial', 18))
    TutorialSkipButton.place(x=803, y=675)
    TutorialBildAnzeige = Canvas(Fenster, width=1000, height=660)
    TutorialBildAnzeige.place(x=40, y=5)
    TutorialBild = PhotoImage(file='ErklaerungEins.png')
    TutorialBildAnzeige.create_image(0, 0, anchor=NW, image=TutorialBild)
    Fenster.mainloop()
    if TutorialSkip == False:
        TutorialZwei()
    else:
        TutorialWeiterButton.destroy()
        TutorialBeendigung()

# Das Bild für die zweite Seite des Tutorials wird eingeblendet.
def TutorialZwei():
    global TutorialWeiterButton
    global TutorialBildAnzeige
    TutorialBild = PhotoImage(file='ErklaerungZwei.png')
    TutorialBildAnzeige.create_image(0, 0, anchor=NW, image=TutorialBild)
    Fenster.mainloop()
    if TutorialSkip == False:
        TutorialDrei()
    else:
        TutorialWeiterButton.destroy()
        TutorialBeendigung()

# Das Bild für die dritte Seite des Tutorials wird eingeblendet.
def TutorialDrei():
    global TutorialWeiterButton
    global TutorialBildAnzeige
    TutorialBild = PhotoImage(file='ErklaerungDrei.png')
    TutorialBildAnzeige.create_image(0, 0, anchor=NW, image=TutorialBild)
    Fenster.mainloop()
    if TutorialSkip == False:
        TutorialVier()
    else:
        TutorialWeiterButton.destroy()
        TutorialBeendigung()

# Das Bild für die vierte Seite des Tutorials wird eingeblendet.
def TutorialVier():
    global TutorialWeiterButton
    global TutorialBildAnzeige
    TutorialBild = PhotoImage(file='ErklaerungVier.png')
    TutorialBildAnzeige.create_image(0, 0, anchor=NW, image=TutorialBild)
    TutorialWeiterButton.destroy()
    TutorialSkipButton.config(font=('Arial', 20), bg='grey')
    TutorialSkipButton.place(x=395, y=670)
    Fenster.mainloop()
    TutorialBeendigung()
    
# Hier wird registiert, dass die Buttons "Mensch", "dumme KI" und "kluge KI" gedrückt worden sind.
def WelcheKIEins():
    global ComputerStaerke
    ComputerStaerke = 0
    Fenster.quit()
    
def WelcheKIZwei():
    global ComputerStaerke
    ComputerStaerke = 1
    Fenster.quit()
    
def WelcheKIDrei():
    global ComputerStaerke
    ComputerStaerke = 2
    Fenster.quit()
    
def WelcheKIEinsEins():
    global ComputerStaerkeEins
    ComputerStaerkeEins = 0
    Fenster.quit()
    
def WelcheKIEinsZwei():
    global ComputerStaerkeEins
    ComputerStaerkeEins = 1
    Fenster.quit()
    
def WelcheKIEinsDrei():
    global ComputerStaerkeEins
    ComputerStaerkeEins = 2
    Fenster.quit()

# Hier wird registiert, dass die Buttons für die Spielbrettgröße gedrückt worden sind.
def SPGacht():
    global SpielBrettLaenge
    SpielBrettLaenge = 8
    Fenster.quit()
    
def SPGzehn():
    global SpielBrettLaenge
    SpielBrettLaenge = 10
    Fenster.quit()
    
def SPGzwoelf():
    global SpielBrettLaenge
    SpielBrettLaenge = 12
    Fenster.quit()
    
def SPGvierzehn():
    global SpielBrettLaenge
    SpielBrettLaenge = 14
    Fenster.quit()
    
def SPGsechzehn():
    global SpielBrettLaenge
    SpielBrettLaenge = 16
    Fenster.quit()
 
# Die Farbe von dem "Spieler 1" und dem "Spieler 2" Label entspricht der ausgewählten Farbe und die ausgewählte Farbe bekommt ein X.
def SpielerAFarbeRedAenderung():
    global SpielerFarbe
    SpielerFarbe[0] = 'red'
    Fenster.quit()
    
def SpielerAFarbeBlueAenderung():
    global SpielerFarbe
    SpielerFarbe[0] = 'blue'
    Fenster.quit()

def SpielerAFarbeYellowAenderung():
    global SpielerFarbe
    SpielerFarbe[0] = 'yellow'
    Fenster.quit()
    
def SpielerAFarbeGreenAenderung():
    global SpielerFarbe
    SpielerFarbe[0] = 'green'
    Fenster.quit()
    
def SpielerBFarbeRedAenderung():
    global SpielerFarbe
    SpielerFarbe[1] = 'red'
    Fenster.quit()
    
def SpielerBFarbeBlueAenderung():
    global SpielerFarbe
    SpielerFarbe[1] = 'blue'
    Fenster.quit()

def SpielerBFarbeYellowAenderung():
    global SpielerFarbe
    SpielerFarbe[1] = 'yellow'
    Fenster.quit()
    
def SpielerBFarbeGreenAenderung():
    global SpielerFarbe
    SpielerFarbe[1] = 'green'
    Fenster.quit()

# Diese Funktion sorgt dafür, dass die Buttons im Hauptmenu richtig anzeigt werden, wenn der Sieler an den Einstellungen etwas geändert hat.
def ButtonPlatzierung():
    global SpielBrettLaenge
    global SpielBrettSteine
    global ComputerStaerke
    global SpielerFarbe
    # Bei der Farbwahl erscheint ein X bei der ausgewählten Farbe
    if SpielerFarbe[0] == 'red':
        SpielerAFarbeRed.config(fg='black')
        SpielerAFarbeBlue.config(fg='blue')
        SpielerAFarbeYellow.config(fg='yellow')
        SpielerAFarbeGreen.config(fg='green')
    elif SpielerFarbe[0] == 'blue':
        SpielerAFarbeRed.config(fg='red')
        SpielerAFarbeBlue.config(fg='black')
        SpielerAFarbeYellow.config(fg='yellow')
        SpielerAFarbeGreen.config(fg='green')
    elif SpielerFarbe[0] == 'yellow':
        SpielerAFarbeRed.config(fg='red')
        SpielerAFarbeBlue.config(fg='blue')
        SpielerAFarbeYellow.config(fg='black')
        SpielerAFarbeGreen.config(fg='green')
    else:
        SpielerAFarbeRed.config(fg='red')
        SpielerAFarbeBlue.config(fg='blue')
        SpielerAFarbeYellow.config(fg='yellow')
        SpielerAFarbeGreen.config(fg='black')
    if SpielerFarbe[1] == 'red':
        SpielerBFarbeRed.config(fg='black')
        SpielerBFarbeBlue.config(fg='blue')
        SpielerBFarbeYellow.config(fg='yellow')
        SpielerBFarbeGreen.config(fg='green')
    elif SpielerFarbe[1] == 'blue':
        SpielerBFarbeRed.config(fg='red')
        SpielerBFarbeBlue.config(fg='black')
        SpielerBFarbeYellow.config(fg='yellow')
        SpielerBFarbeGreen.config(fg='green')
    elif SpielerFarbe[1] == 'yellow':
        SpielerBFarbeRed.config(fg='red')
        SpielerBFarbeBlue.config(fg='blue')
        SpielerBFarbeYellow.config(fg='black')
        SpielerBFarbeGreen.config(fg='green')
    else:
        SpielerBFarbeRed.config(fg='red')
        SpielerBFarbeBlue.config(fg='blue')
        SpielerBFarbeYellow.config(fg='yellow')
        SpielerBFarbeGreen.config(fg='black')
    # Die ausgewählte Option bei Spieler 1 und 2 mit "Mensch", "dumme KI" und "kluge KI" wird grau hinterlegt.
    if ComputerStaerke == 0:
        WelcheKIEinsFarbe = 'grey'
    else:
        WelcheKIEinsFarbe = 'lightgrey'
    if ComputerStaerke == 1:
        WelcheKIZweiFarbe = 'grey'
    else:
        WelcheKIZweiFarbe = 'lightgrey'
    if ComputerStaerke == 2:
        WelcheKIDreiFarbe = 'grey'
    else:
        WelcheKIDreiFarbe = 'lightgrey'
    global ComputerStaerkeEins
    if ComputerStaerkeEins == 0:
        WelcheKIEinsEinsFarbe = 'grey'
    else:
        WelcheKIEinsEinsFarbe = 'lightgrey'
    if ComputerStaerkeEins == 1:
        WelcheKIEinsZweiFarbe = 'grey'
    else:
        WelcheKIEinsZweiFarbe = 'lightgrey'
    if ComputerStaerkeEins == 2:
        WelcheKIEinsDreiFarbe = 'grey'
    else:
        WelcheKIEinsDreiFarbe = 'lightgrey'
    WelcheKIEins.config(font=('Arial', 20), bg=WelcheKIEinsFarbe)
    WelcheKIZwei.config(font=('Arial', 20), bg=WelcheKIZweiFarbe)
    WelcheKIDrei.config(font=('Arial', 20), bg=WelcheKIDreiFarbe)
    WelcheKIEinsEins.config(font=('Arial', 20), bg=WelcheKIEinsEinsFarbe)
    WelcheKIEinsZwei.config(font=('Arial', 20), bg=WelcheKIEinsZweiFarbe)
    WelcheKIEinsDrei.config(font=('Arial', 20), bg=WelcheKIEinsDreiFarbe)
    # Die ausgewählte Option bei "Spielbrettgröße" wird grau hinterlegt.
    if SpielBrettLaenge == 8:
        SPGachtFarbe = 'grey'
    else:
        SPGachtFarbe = 'lightgrey'
    if SpielBrettLaenge == 10:
        SPGzehnFarbe = 'grey'
    else:
        SPGzehnFarbe = 'lightgrey'
    if SpielBrettLaenge == 12:
        SPGzwoelfFarbe = 'grey'
    else:
        SPGzwoelfFarbe = 'lightgrey'
    if SpielBrettLaenge == 14:
        SPGvierzehnFarbe = 'grey'
    else:
        SPGvierzehnFarbe = 'lightgrey'
    if SpielBrettLaenge == 16:
        SPGsechzehnFarbe = 'grey'
    else:
        SPGsechzehnFarbe = 'lightgrey'
    SPGacht.config(font=('Arial', 20), bg=SPGachtFarbe)
    SPGzehn.config(font=('Arial', 20), bg=SPGzehnFarbe)
    SPGzwoelf.config(font=('Arial', 20), bg=SPGzwoelfFarbe)
    SPGvierzehn.config(font=('Arial', 20), bg=SPGvierzehnFarbe)
    SPGsechzehn.config(font=('Arial', 20), bg=SPGsechzehnFarbe)
    # Der passende Schieberegler für die Anzahl der Spielbrettsteine wird eingeblendet und deren Wert wird ermittelt.
    if SpielBrettLaenge == 8:
        SPSacht.place(x=275, y=450)
        SpielBrettSteine = SPSacht.get()
    else:
        SPSacht.place(x=99275, y=450)
    if SpielBrettLaenge == 10:
        SPSzehn.place(x=420, y=450)
        SpielBrettSteine = SPSzehn.get()
    else:
        SPSzehn.place(x=99275, y=450)
    if SpielBrettLaenge == 12:
        SPSzwoelf.place(x=577, y=450)
        SpielBrettSteine = SPSzwoelf.get()
    else:
        SPSzwoelf.place(x=99275, y=450)
    if SpielBrettLaenge == 14:
        SPSvierzehn.place(x=725, y=450)
        SpielBrettSteine = SPSvierzehn.get()
    else:
        SPSvierzehn.place(x=99275, y=450)
    if SpielBrettLaenge == 16:
        SPSsechzehn.place(x=860, y=450)
        SpielBrettSteine = SPSsechzehn.get()
    else:
        SPSsechzehn.place(x=99275, y=450)
    # Die Labels "1. Spieler:' und "2. Spieler:" erhalten ihre korrekte Farbe.
    WelcheKILabelFarbe = SpielerFarbe[1]
    if WelcheKILabelFarbe == 'yellow':
        WelcheKILabelFarbe = '#968A08'
    WelcheKIEinsLabelFarbe = SpielerFarbe[0]
    if WelcheKIEinsLabelFarbe == 'yellow':
        WelcheKIEinsLabelFarbe = '#968A08'
    WelcheKILabel.config(fg=WelcheKILabelFarbe)
    WelcheKIEinsLabel.config(fg=WelcheKIEinsLabelFarbe)
    
# Dieser Code wird beim Starten des Programms ausgeführt und erzeugt die graphische Benutzeroberfläche.
Fenster = Tk()
Fenster.title('Game of Life and Death')
Fenster.geometry('1060x730')
ErsteGenerierung = True
# Wenn der Benutzer nach einer Runde "Zurück zum Hauptmenu" anklickt oder wenn das Programm startet, dann wird er hierher geleitet.
while 1 < 2:
    # Erzeugung des Hauptmenus und von grundlegenden Variablen im Spiel.
    global PositionsVermerkZweiZwei
    global PositionsVermerkZweiDrei
    PositionsVermerkZweiZwei = [-1, -1, 0]
    PositionsVermerkZweiDrei = [-1, -1, 0]
    global PunktfarbenAussnahme
    PunktfarbenAussnahme = True
    global Annulieren
    Annulieren = False
    global xManipulation
    xManipulation = [-1, -1, -1]
    global ZelleFarbwechselAktiviert
    ZelleFarbwechselAktiviert = True
    global Position
    global DebugModusStarter
    global SpielBrettLaenge
    global SpielBrettSteine
    global Farbe
    global ComputerStaerke
    global ComputerStaerkeEins
    global SpielerFarbe
    DebugModusStarter = False
    global TutorialStarter
    TutorialStarter = False
    global SpielLaden
    SpielLaden = False
    global HauptSpielGenerierung
    HauptSpielGenerierung = True
    Farbe = ['black','black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black'],['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black'], ['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','black']
    # Erzeugung der graphischen Benutzeroberfläche des Menus.
    # Generierung des "1. Spieler" Labels
    WelcheKIEinsLabel = Label(Fenster, text='1. Spieler:') 
    WelcheKIEinsLabel.config(font=('Arial', 23))
    WelcheKIEinsLabel.place(x=118, y=200)
    # Generierung des "2. Spieler" Labels
    WelcheKILabel = Label(Fenster, text='2. Spieler:') 
    WelcheKILabel.config(font=('Arial', 23))
    WelcheKILabel.place(x=118, y=290)
    # Generierung des "Game of Life ausprobieren" Buttons
    MenuDebug = Button(Fenster, text='Game of Life ausprobieren', bg='lightgrey', command=DebugModusStarten)
    MenuDebug.config(font=('Arial', 18))
    MenuDebug.place(x=745, y=673)
    # Generierung des "Spiel starten" Buttons
    MenuStart = Button(Fenster, text='Spiel starten', bg='grey', command=SpielStarten)
    MenuStart.config(font=('Arial', 25))
    MenuStart.place(x=400, y=560)
    # Generierung des "gespeichertes Spiel fortsetzten" Buttons)
    FortsetzungsButton = Button(Fenster, text='gespeichertes Spiel fortsetzten', bg='lightgrey', command=SpeicherungLadenStart)
    FortsetzungsButton.config(font=('Arial', 18))
    FortsetzungsButton.place(x=330, y=645)
    # Generierung der Überschrift
    Headline = Label(Fenster, text='Game of Life and Death')
    Headline.config(font=('Arial', 35))
    Headline.place(x=280, y=30)
    SupHeadline = Label(Fenster, text='inspiriert von John Conways "Game of Life"')
    SupHeadline.config(font=('Arial', 27))
    SupHeadline.place(x=194, y=96)
    # Generierung des "Spielbrettgröße" Labels
    SPGLabel = Label(Fenster, text='Spielbrettgröße:')
    SPGLabel.config(font=('Arial', 23))
    SPGLabel.place(x=43, y=380)
    # Generierung des "Zellen pro Spieler" Labels
    SPSLabel = Label(Fenster, text='Zellen pro Spieler:')
    SPSLabel.config(font=('Arial', 23))
    SPSLabel.place(x=15, y=476)
    # Generierung des "Spielregeln und Tipps" Buttons
    TutorialButton = Button(Fenster, text='Spielregeln und Tipps', bg='lightgrey', command=TutorialStart)
    TutorialButton.config(font=('Arial', 18))
    if ErsteGenerierung == True:
        # Diese Buttons werden nur beim Starten des Programms geladen.
        ComputerStaerke = 0
        ComputerStaerkeEins = 0
        # Generierung der "Mensch", "dumme KI" und "kluge KI" Buttons.
        WelcheKIEins = Button(Fenster, text='Mensch', command=WelcheKIEins)
        WelcheKIZwei = Button(Fenster, text='dumme KI', command=WelcheKIZwei)
        WelcheKIDrei = Button(Fenster, text='kluge KI', command=WelcheKIDrei)
        WelcheKIEinsEins = Button(Fenster, text='Mensch', command=WelcheKIEinsEins)
        WelcheKIEinsZwei = Button(Fenster, text='dumme KI', command=WelcheKIEinsZwei)
        WelcheKIEinsDrei = Button(Fenster, text='kluge KI', command=WelcheKIEinsDrei)
        SpielBrettLaenge = 10
        # Generierung der Schieberegler für das Einstellen der Anzahl der Zellen pro Spieler.
        SPGacht = Button(Fenster, text='8x8', command=SPGacht)
        SPGzehn = Button(Fenster, text='10x10', command=SPGzehn)
        SPGzwoelf = Button(Fenster, text='12x12', command=SPGzwoelf)
        SPGvierzehn = Button(Fenster, text='14x14', command=SPGvierzehn)
        SPGsechzehn = Button(Fenster, text='16x16', command=SPGsechzehn)
        SPSacht = Scale(Fenster, from_=5, to=25, length=180, orient=HORIZONTAL, tickinterval=10)
        SPSacht.config(font=('Arial', 22))
        SPSacht.set(10)
        SPSzehn = Scale(Fenster, from_=5, to=45, length=180, orient=HORIZONTAL, tickinterval=20)
        SPSzehn.config(font=('Arial', 22))
        SPSzehn.set(17)
        SPSzwoelf = Scale(Fenster, from_=5, to=65, length=180, orient=HORIZONTAL, tickinterval=30)
        SPSzwoelf.config(font=('Arial', 22))
        SPSzwoelf.set(24)
        SPSvierzehn = Scale(Fenster, from_=5, to=85, length=180, orient=HORIZONTAL, tickinterval=40)
        SPSvierzehn.config(font=('Arial', 22))
        SPSvierzehn.set(31)
        SPSsechzehn = Scale(Fenster, from_=5, to=105, length=180, orient=HORIZONTAL, tickinterval=50)
        SPSsechzehn.config(font=('Arial', 22))
        SPSsechzehn.set(38)
        SpielerFarbe = ['red', 'blue']
        # Generierung der Buttons, mit denen der Benutzer die Farbbe der Knöpfe verändern kann.
        SpielerAFarbeRed = Button(Fenster, bg='red', text='X', command=SpielerAFarbeRedAenderung)
        SpielerAFarbeRed.config(font=('Arial', 22))
        SpielerAFarbeBlue = Button(Fenster, bg='blue', text='X', fg='blue', command=SpielerAFarbeBlueAenderung)
        SpielerAFarbeBlue.config(font=('Arial', 22))
        SpielerAFarbeYellow = Button(Fenster, bg='yellow', text='X', fg='yellow', command=SpielerAFarbeYellowAenderung)
        SpielerAFarbeYellow.config(font=('Arial', 22))
        SpielerAFarbeGreen = Button(Fenster, bg='green', text='X', fg='green', command=SpielerAFarbeGreenAenderung)
        SpielerAFarbeGreen.config(font=('Arial', 22))
        SpielerBFarbeRed = Button(Fenster, bg='red', text='X', fg='red', command=SpielerBFarbeRedAenderung)
        SpielerBFarbeRed.config(font=('Arial', 22))
        SpielerBFarbeBlue = Button(Fenster, bg='blue', text='X', command=SpielerBFarbeBlueAenderung)
        SpielerBFarbeBlue.config(font=('Arial', 22))
        SpielerBFarbeYellow = Button(Fenster, bg='yellow', text='X', fg='yellow', command=SpielerBFarbeYellowAenderung)
        SpielerBFarbeYellow.config(font=('Arial', 22))
        SpielerBFarbeGreen = Button(Fenster, bg='green', text='X', fg='green', command=SpielerBFarbeGreenAenderung)
        SpielerBFarbeGreen.config(font=('Arial', 22))
        GleicheFarbeLabel = Label(Fenster, text='Die Farben müssen unterschiedlich sein!')
        GleicheFarbeLabel.config(font=('Arial', 17))
        LadenNichtMoeglichLabel = Label(Fenster, text='Das Spiel konnte nicht geladen werden!')
        LadenNichtMoeglichLabel.config(font=('Arial', 17))
    else:
        ButtonDeSpawner()
    # Die Buttons und Schieberegler, die vorhin generiert worden sind, werden nun an der richtigen Stelle platziert.
    WelcheKIEins.place(x=330, y=282)
    WelcheKIZwei.place(x=470, y=282)
    WelcheKIDrei.place(x=640, y=282)
    WelcheKIEinsEins.place(x=330, y=192)
    WelcheKIEinsZwei.place(x=470, y=192)
    WelcheKIEinsDrei.place(x=640, y=192)
    SPGacht.place(x=330, y=373)
    SPGzehn.place(x=465, y=373)
    SPGzwoelf.place(x=620, y=373)
    SPGvierzehn.place(x=765, y=373)
    SPGsechzehn.place(x=900, y=373)
    SpielerAFarbeRed.place(x=805, y=192)
    SpielerAFarbeBlue.place(x=855, y=192)
    SpielerAFarbeYellow.place(x=905, y=192)
    SpielerAFarbeGreen.place(x=955, y=192)
    SpielerBFarbeRed.place(x=805, y=282)
    SpielerBFarbeBlue.place(x=855, y=282)
    SpielerBFarbeYellow.place(x=905, y=282)
    SpielerBFarbeGreen.place(x=955, y=282)
    TutorialButton.place(x=10, y=670)
    global MenuLoop
    MenuLoop = True
    # Hier landet der Benutzer im Hauptmenu und wählt sich den Spielmodus, etc. aus.
    while MenuLoop == True:
        ButtonPlatzierung()
        Fenster.mainloop()
    # Wenn der Benutzer das Spiel, Game of Life oder das Tutorial startet, dann landet er hier.
    # Hier werden einige Buttons elöscht oder außerhalb des Bildschirms gesetzt und verschwinden für den Benutzer somit.
    LadenNichtMoeglichLabel.place(x=99999, y=300)
    WelcheKIEins.place(x=99220, y=312)
    WelcheKIZwei.place(x=99420, y=312)
    WelcheKIDrei.place(x=99640, y=312)
    WelcheKIEinsEins.place(x=99220, y=312)
    WelcheKIEinsZwei.place(x=99420, y=312)
    WelcheKIEinsDrei.place(x=99640, y=312)
    SPGacht.place(x=99860, y=433)
    SPGzehn.place(x=99860, y=433)
    SPGzwoelf.place(x=99860, y=433)
    SPGvierzehn.place(x=99860, y=433)
    SPGsechzehn.place(x=99860, y=433)
    FortsetzungsButton.destroy()
    MenuDebug.destroy()
    MenuStart.destroy()
    SPGLabel.destroy()
    SPSLabel.destroy()
    Headline.destroy()
    SupHeadline.destroy()
    ButtonPlatzierung()
    WelcheKILabel.destroy()
    WelcheKIEinsLabel.destroy()
    TutorialButton.destroy()
    SPSacht.place(x=99275, y=410)
    SPSzehn.place(x=99275, y=410)
    SPSzwoelf.place(x=99275, y=410)
    SPSvierzehn.place(x=99275, y=410)
    SPSsechzehn.place(x=99875, y=410)
    SpielerAFarbeRed.place(x=9805, y=192)
    SpielerAFarbeBlue.place(x=9855, y=192)
    SpielerAFarbeYellow.place(x=9905, y=192)
    SpielerAFarbeGreen.place(x=9955, y=192)
    SpielerBFarbeRed.place(x=9805, y=282)
    SpielerBFarbeBlue.place(x=9855, y=282)
    SpielerBFarbeYellow.place(x=9905, y=282)
    SpielerBFarbeGreen.place(x=9955, y=282)
    ErsteGenerierung = False
    if SpielLaden == True:
        # Der Spieler möchte ein zuvor abgespeichertes Spiel laden
        GleicheFarbeLabel.place(x=99300, y=600)
        try:
            SpeicherungLaden()
            if SpielerFarbe[0] != SpielerFarbe[1]:
                # Das Spiel konnte erfolgreich geladen werden.
                ButtonsErstgenerierung()
                HauptSpielGenerierung = False
                HauptSpiel()
            else:
                # Das Spiel wird nicht geladen, wenn beide Spieler die gleiche Farbe haben würden.
                AbsichtlicherError = 1 / 0
        except:
            # Das Spiel konnte nicht geladen werden.
            LadenNichtMoeglichLabel.place(x=303,y=693)
            SpielLaden = False
            ErsteGenerierung = False
            ButtonsErstgenerierung()
    else:
        # Die Zellen werden generiert.
        ErsteGenerierung = False
        ButtonsErstgenerierung()
        if TutorialStarter == True:
            # Der Benutzer hat "Spielregeln und Tipps" angeklickt. Labels, Buttons und Zellen, die nicht benötigt werden, werden enfernt.
            GleicheFarbeLabel.place(x=99300, y=600)
            ButtonDeSpawner()
            TutorialEins()
        else:
            if SpielerFarbe[0] == SpielerFarbe[1]:
                # Die Farben der Spieler sind identisch und das Spiel startet somit nicht.
                GleicheFarbeLabel.place(x=300, y=693)
            else:
                GleicheFarbeLabel.place(x=99300, y=600)
                if DebugModusStarter == True:
                    # Der Benutzer hat "Game of Life ausprobieren" angeklickt.
                    Debug()
                else:
                    # Der Benutzer hat "Spiel starten" angeklickt.
                    HauptSpiel()