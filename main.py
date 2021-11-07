from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.popup import Popup

from random import randint, random, choice

#Builder.load_file("apptrinken.kv")


#Karten
class dict():

    #Runden einführen?????
    #wenn alle Karten gespielt gibt es ein Fehler

    Karte = {}

    #Spieler vars
    Spieler_dran = ""
    Spieler = []
    dict_Spieler = {}

    StaticSpeicher ={
        "karte1": {
        "headline": "Pech",
        "task" : "du hast heute pech, trinke 2 Schlücke",
        "Spielerauswahl": "zufall",
        },
        "karte2": {
        "headline": "Alter",
        "task": "der älteste Spieler trinkt 1 Schluck",
        "Spielerauswahl": "alle",
        },
        "Karte3": {
        "headline": "Blinde Schlücke",
        "task": "alle Spieler schließen die Augen und gucken in die Richtung eines Spielers. \nDie Spieler die sich bei Augen auf machen in die Augen gucken trinken 3 Schlücke",
        "Spielerauswahl": "alle",
        },
        "Karte4": {
        "headline": "Fresssack",
        "task": "Jeder Spieler der heute schon Fastfood gegessen hat trinkt trinkt 2 Schlücke",
        "Spielerauswahl": "alle",
        },

        "Karte5": {
        "headline": "Frauen sind dir heilig",
        "task": "trink für jede Frau im Raum 1 Schluck",
        "Spielerauswahl": "zufall",
        },

        "Karte6": {
        "headline": "Trinkbuddy",
        "task": "bestimme einen Spieler, der immer wenn du trinken musst, einen Schluck mittrinkt",
        "Spielerauswahl": "zufall",
        },

        "Karte7": {
        "headline": "Spongebob-Charaktere",
        "task": "nennt noch der Reihe Charaktere aus Spongebob, wer keinen mehr weiß oder \neinen doppelt nennt, trinkt 4 Schlücke",
        "Spielerauswahl": "zufall",
        },

        "Karte8": {
        "headline": "Investor",
        "task": "Trinke so viele Schlücke wie du willst, du darfst danach die doppelte Anzahl verteilen",
        "Spielerauswahl": "zufall",
        },

        "Karte9": {
        "headline": "Pokemon",
        "task": "nach der Reihe wird ein Pokemon der 1. Generation genannt, wer keine Antwort gibt \noder ein Pokemon doppelt nennt, trink 4 Schlücke",
        "Spielerauswahl": "zufall",
        },

        "Karte10": {
        "headline": "Liegestütze",
        "task": "mache 10 Liegestütze, für jede nicht geschaffte trinkst du 1 Schluck",
        "Spielerauswahl": "zufall",
        },

        "Karte11": {
        "headline": "Schere-Stein-Papier",
        "task": "Du spielst gegen jeden Mitspieler, der Verlierer trinkt 1 Schluck",
        "Spielerauswahl": "zufall",
        },

        "Karte12": {
        "headline": "Glück",
        "task": "Das Glück ist mit der Dummen, verteile 4 Schlücke",
        "Spielerauswahl": "zufall",
        },

        "Karte13": {
        "headline": "Koordination",
        "task": "versuche mit geschlossenen Augen deine Zeigefinger aus 20cm Distanz zusammenzuführen, \nwenn du es nicht schaffst, trinke 2 Schlücke, sonst verteile sie",
        "Spielerauswahl": "zufall",
        },

        "Karte15": {
        "headline": "21",
        "task": "suche dir jemanden aus, gegen den du das Spiel 21 spielst, verliere trinkt 1 Schluck",
        "Spielerauswahl": "zufall",
        },

        "Karte16": {
        "headline": "kleiner Finger",
        "task": "vergleiche die länge deines kleinen Finger mit der Höhe deines Getränks im Glas, \nist der Finger kürzer trinke 2 Schlücke",
        "Spielerauswahl": "zufall",
        },

        "Karte17": {
        "headline": "Bundeskanzler",
        "task": "Spiele mit einer belieben Person, sagt wie viele Bundeskanzler ihr wisst, \nwer die höhere Zahl sagt, muss sie aufzählen. Wenn alle richtig sind muss der andere die Anzahl trinken, \nwenn falsch muss er selber trinken",
        "Spielerauswahl": "zufall",
        },

        "Karte18": {
        "headline": "Wort",
        "task": "legt ein Wort fest, wer es als erster Sagt muss 1 Schluck trinken",
        "Spielerauswahl": "alle",
        },

        "Karte19": {
        "headline": "Krankenhaus",
        "task": "pro Krankenhausaufenthalt den du hattest, \ndarf du 1 Schluck verteilen (die Geburt zählt nicht, ihr Pappnasen)",
        "Spielerauswahl": "zufall",
        },

        "Karte20": {
        "headline": "Zeit zählen",
        "task": "Du muss 30s im Kopf zählen und dann Stopp sagen, wenn du näher als 2 Sekunden an der gestoppten Zeit bist, \nverteil 5 Schluck, wenn nicht trinke 1 Schluck",
        "Spielerauswahl": "zufall",
        },

        "Karte21": {
        "headline": "Aufholjagd",
        "task": "bestimmt den Spieler, der am wenigsten getrunken hat, er trinkt genüsslich 7 Schlücke",
        "Spielerauswahl": "alle",
        },

        "Karte22": {
        "headline": "Sprichwörter",
        "task": "sagt nacheinander Sprichwörter auf, der Verlierer trinkt 2 Schlücke, ",
        "Spielerauswahl": "zufall",
        },

         #################Schätzspiel gehen im Moment nicht
        #"Karte23": {
        #"headline": "Musikraten",
        #"task": "Aufgabe",
        #"Spielerauswahl": "zufall",
        #},

        "Karte24": {
        "headline": "Pi",
        "task": "nenne die erst drei Stellen der Zahl pi, wenn du es nicht schaffst, trinke 3 Schlücke",
        "Spielerauswahl": "zufall",
        },

        "Karte25": {
        "headline": "Spinger",
        "task": "Wenn du nicht weißt, aus was ein Charlie besteht, trinke 6 Schlücke",
        "Spielerauswahl": "zufall",
        },

        "Karte26": {
        "headline": "Kartensammler",
        "task": "hiermit erhälst du die Möglichkeit, deine Schlücke die du trinken müsstest \nan jemand andern weiterzuleiten",
        "Spielerauswahl": "zufall",
        },

        "Karte27": {
        "headline": "Spielleiter",
        "task": "Der Spielleiter muss die nächsten 3 Schlücke die er bekommt nicht trinken",
        "Spielerauswahl": "alle"
        },

        "Karte28": {
        "headline": "Streber",
        "task": "Jeder nennt sein Schulabschlussnotendurschnitt, 1 komma = 6, 2 komma =5, 3 komma = 4 usw.",
        "Spielerauswahl": "alle",
        },

        "Karte30": {
        "headline": "Shoppen wir teuer",
        "task": "für jedes Kleidungsstück, was neuer als 3 Monate ist, musst du ein Schluck trinken",
        "Spielerauswahl": "zufall",
        }

    }

    Speicher = StaticSpeicher.copy()

    def Kartendign_auswahl(self):      #Karten_Auswahl
        #Zahl = randint(1,len(self.Speicher))
        #print("neue Zahl:" + str(Zahl))
        Name_key = choice(list(self.Speicher))
        #print("wichtig")
        #print(Name_key)
        dict.Karte = self.Speicher.get(Name_key)
        #self.Karte = Karte

        ###### Remove die verwendete Karten
        dict.Speicher.pop(Name_key)
        #print(dict.Speicher)


    def Spieler_erstellen(self):     #Auswahl des Spielers für eine Karte

        for anzahl in range(0,len(self.Spieler)):
            dict.dict_Spieler[self.Spieler[anzahl-1]] = 0

        print("dict")
        print(dict.dict_Spieler)

    def Spieler_auswahl(self):       #Einschränkung des Randomfaktor der Auswahl des Spielers
        zahl = randint(1,len(self.Spieler))-1

        #Randomfaktor einschränken                              7777 abfrage dass Spieler vorhanden sind fehlt noch
        zahl_liste = []

        for anzahl in range(0,len(self.Spieler)):
            zahl_liste.append(self.dict_Spieler[self.Spieler[anzahl-1]])
        print(zahl_liste)
        if min(zahl_liste)+3 < max(zahl_liste):
            zahl_tief = self.dict_Spieler[self.Spieler[1]]
            for anz in range(0,len(self.Spieler)):
                if zahl_tief > self.dict_Spieler[self.Spieler[anz-1]]:
                    zahl_tief = self.dict_Spieler[self.Spieler[anz-1]]
            zahl = anz
            print(zahl)

        print(self.dict_Spieler[self.Spieler[zahl]])
        self.dict_Spieler[self.Spieler[zahl]] += 1
        print(self.dict_Spieler)
        dict.Spieler_dran = self.Spieler[zahl]





class MainWindow(Screen, dict): #Main Screen für Einstellungen und start
    box1 = ObjectProperty(None)
    MainW = ObjectProperty(None)
    anderung = StringProperty("")
    Spieler_eingabe = []

    def Button_start(self):
        #Labeländerungen
        button1 = self.button1.text
        box1 = self.box1.text
        label1 = self.ids.label1.text

        self.Spieler_eingabe.append(box1)

        Personen = "\n".join(self.Spieler_eingabe)
        self.ids.label1.text = Personen
        self.ids.box1.text = ''

        #SpielerListe übernehmen
        print(self.Spieler_eingabe)
        dict.Spieler = self.Spieler_eingabe

    def open_popup_main(self):
        pops = popupmain()
        pops.open()

    def Spielernamen_speichern(self):
        if dict.Spieler == []:
            print("Bitte Spielernamen eingeben")
        else:
            self.manager.current = "Karte"
            #MainWidget.Karte_Aufgabe_wechseln(self)

            ###Spielstart
            #zuweisen der Karten
            #anzahl spieler und wer dran ist
            # Spielerauswahl
            dict.Spieler_erstellen(self)
            dict.Spieler_auswahl(self)
            Spieler = dict.Spieler_dran
            Spieler_j_N = dict.Karte.get("Spielerauswahl")
            if Spieler_j_N == "alle":
                Spieler = ""
            dict.Kartendign_auswahl(self)

            print(dict.Karte)
            print(dict.Speicher)

            headline = dict.Karte.get("headline")
            #task = dict.Karte.get("task")

            #erste karte richtig darstellen
            self.manager.get_screen('Karte').labelText = headline            #######################################
            #self.manager.get_screen('zweite').label_kartenaufgabe = task      ################


            #MainWidget.ids.label_headline.text = headline





class MainWidget(Screen, dict):  #Aufgaben "Karte"
    labelText = StringProperty("")                  #########################
    var_Start = False

    def Button_wechsel_main(self):
        #Seite Wechseln
        print("Button_wechsel_main")
        self.manager.current = "zweite"

        #Kartenänderungen
        self.Karte_Aufgabe_wechseln()# Problem mit dem Thread, Gui wird erst geupdatet wenn die Methode fertig ist

    def Karte_Aufgabe_wechseln(self):  ####### Auswahl der Karte und des Spielers

        # wechsel der Taskkarte
        task = dict.Karte.get("task")
        Spieler = dict.Spieler_dran
        Spieler_j_N = dict.Karte.get("Spielerauswahl")
        if Spieler_j_N == "alle":
            Spieler = ""

        task = (Spieler + " " + task)
        self.manager.get_screen('zweite').labelKartenaufgabe = task
        print(task)
        print(self.var_Start)

        #if self.var_Start == True:
        print("im if state")
        #Spielerauswahl
        #dict.Spieler_erstellen(self)
        dict.Spieler_auswahl(self)
        Spieler = dict.Spieler_dran
        Spieler_j_N = dict.Karte.get("Spielerauswahl")
        if Spieler_j_N == "alle":
            Spieler = ""

        #neue Karte durch zahl auswählen
        dict.Kartendign_auswahl(self)
        print(dict.Karte)
                                                #es fehlt ein beenden des Spiels, wenn alle Karten durch sind

        #Label neue Texte geben
        headline = dict.Karte.get("headline")
        # Aufbau des tasktextes: "Spielername", mache dies und das
        #task = dict.Karte.get("task")
        #print(dict.Karte)

        self.ids.label_headline.text = headline
        #self.ids.label_Aufgabe.text = (Spieler +" " +task)



        ####erstes Wechseln der Karte
        #self.var_Start = True


    def open_popup_main(self):
        pops = popupmain()
        pops.open()




class SecondWindow(Screen,dict): #Lösungen der Aufgaben/ Schlücke          "zweite"
    #Buttonpopup = ObjectProperty(None)
    labelKartenaufgabe = StringProperty("sdsdsd")

    def Button_Ende(self):
        # Seite Wechseln
        print("SecondWindow")
        self.manager.current = "Karte"

        # Kartenänderungen
        self.Karte_Auflösung_Wechseln() # Problem mit dem Thread, Gui wird erst geupdatet wenn die Methode fertig ist

    def Karte_Auflösung_Wechseln(self):
        print(dict.Karte)

        #Spielerauswahl
        Spieler = dict.Spieler_dran
        Spieler_j_N = dict.Karte.get("Spielerauswahl")
        if Spieler_j_N == "alle":
            Spieler = "der Verlierer"





        #sips = dict.Karte.get("sips")
        #endtext = dict.Karte.get("endtext")

        #Labeländerungen
        #self.ids.Label_endtext.text = (" "+Spieler+" trinkt "+ str(sips) +" Schlücke")

    def open_popup_main(self):
        pops = popupmain()
        pops.open()

class End_Screen(Screen):
    pass

class popupmain(Popup, dict):
    def neustart(self):
        print("schließen")
        #Main Bild aufrufen
        #ManagerWindow.current = "erste"
        #MainWindow.Neustart_wechsel(self)
        #funktioniet nicht

        #alle Karten Laden
        dict.Speicher = dict.StaticSpeicher.copy()

        #Spieler löschen
        dict.Spieler = []


class ManagerWindow(ScreenManager):
    pass

kvtext= """ 
#:import NoTransition kivy.uix.screenmanager.NoTransition
#Screenmanger mit allen möglichen Screens
ManagerWindow:
    transition: NoTransition()

    MainWindow:
    SecondWindow:
    MainWidget:


    End_Screen:



#Main Screen für Einstellungen etc.
<MainWindow>:
    name: "erste"

    #Variablen
    button1: button1
    box1: box1



    BoxLayout:
        size: root.width, root.height
        orientation: 'vertical'

        #size_hint_y:0.1
        AnchorLayout:
            size_hint_y:0.1
            anchor_x:'right'
            Button:
                on_release: root.open_popup_main()
                text:"11"
                size_hint_x:0.2
            Label:
                text:"Menü"



        BoxLayout:
            orientation: 'vertical'
            Label:
                text:"Spielernamen eintragen"
                size_hint_y: 0.2
                #background_color: 0.94,0.2,0.9,1
            TextInput:
                id: box1
                multiline:False

            Button:
                id: button1
                text:"Bestätigen"
                on_release: root.Button_start()

            Label:
                id:label1
                text: "Mitspielende Personen"



        #Start Button
        Button:
            text:"Start"
            size_hint_y:0.1
            on_release:
                root.Spielernamen_speichern() ##################################





#Screen für die Karten/ Aufgaben
<MainWidget>:
    name: "Karte"

    #ids #nur kleine ids



    buttonmain: buttonmain

    BoxLayout:
        size: root.width, root.height
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y:0.1
            Label:
                #text: root.labelText
            Button:
                on_release: root.open_popup_main()
                text:"11"
                size_hint_x:0.1


        BoxLayout:
            orientation: 'horizontal'
            size_hint_y:0.2

            Label:
                #id: label_headline
                text: "Kartenname"



        Label:
            id: label_headline
            #id: label_Aufgabe
            size_hint_y:0.9
            text: root.labelText  ####################################################


        Button:
            id: buttonmain
            text: "zur Aufgabe"
            size_hint_y:0.2
            on_release:
                root.Button_wechsel_main()





#Screen mit der auswertung
<SecondWindow>: #Lösung/Auswertung
    name: "zweite"

    BoxLayout:
        size: root.width, root.height
        orientation: 'vertical'

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y:0.1
            Label:
                text: "    Aufgabe"
            Button:
                on_release: root.open_popup_main()
                text:"11"
                size_hint_x:0.1

        Label:
            id: label_Aufgabe
            #id: Label_endtext
            text: root.labelKartenaufgabe

        Button:
            text:"nächste Karte"
            size_hint_y:0.2
            on_release:
                root.Button_Ende()




<popupmain>
    auto_dismiss: False
    title: "Einstellungen"
    size_hint: 0.6, 0.2
    pos_hint: {"x": 0.2, "top":0.9}
    BoxLayout:
        Button:
            text: "close"
            on_release:
                root.dismiss()

        Button:
            text: "Neustart"
            on_release:
                root.neustart()


<End_Screen>:
    BoxLayout:
        size: root.width, root.height
        orientation: 'vertical'
        Label:
            text: "Ende"
        


"""

#kv = Builder.load_file("apptrinken.kv")
kv = Builder.load_string(kvtext)


class MainApp(App):
    def build(self):

        return kv

if __name__ == '__main__':
    MainApp().run()
