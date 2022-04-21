from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.storage.jsonstore import JsonStore
from kivy.uix.popup import Popup
from random import randint, random, choice

kv = Builder.load_file("Spiel.kv")


#Screens
class MainWindow(Screen):
    Label_main_spieler = ObjectProperty(None)
    Spieler_Liste = ['hergen', 'Nils']#zur Probe
    #checkbox_Liste = []
    Button_Liste =[]
    Boxlayout_Liste = []
    Label_Liste = []
    def Spieler_hinzu(self,Name):
        print("richtig")
        self.Spielername = Name
        #inputaufnahmen
        #self.Spielername = self.ids.input_box_main.text
        #self.ids.input_box_main.text = ''
        #inputweitergabe um Label zu bauen
        self.Spieler_Liste.append(self.Spielername)
        self.Spieler_Label_hinzu()#in Label

    def Spielernamen_laden(self):
        pass


    def Spiel_start(self):
        self.manager.current = "Zwischen_Karte" #zwischenkarte
        self.Spiel_klasse = Spiel()
        print("erstmal Klasse erstelt")
        print(self.Spiel_klasse)
        self.Spieler_klasse = Spieler(self.Spieler_Liste)
        #spielscreen.Spiel()
        #spielscreen.Spieler(self.Spieler_Liste)
        #spielscreen.Spieler_Scores_erstellen()


    def Spieler_Label_hinzu(self):
        self.spielerannehmen = BoxLayout(orientation='horizontal')
        spielername = Label(text=self.Spielername)
        self.ids.Box_main_spieler_name.add_widget(self.spielerannehmen)
        self.spielerannehmen.add_widget(spielername)
        self.Boxlayout_Liste.append(self.spielerannehmen)
        self.Label_Liste.append(spielername)
        print("hallo")
        print(self.Boxlayout_Liste[0])
        #print(self.ids.Box_main_spieler_name.spielerannehmen)

        self.Knopf = Button(text='X')# on_release=self.Spieler_loschen())
        #self.Knopf.on_release = self.Spieler_loschen
        self.Knopf.bind(on_release = self.Spieler_loschen)
        self.Button_Liste.append(self.Knopf)
        self.spielerannehmen.add_widget(self.Knopf)
        #check = CheckBox()
        #self.checkbox_Liste.append(check)
        #self.spielerannehmen.add_widget(check)
        #print(self.checkbox_Liste)
        print(self.Button_Liste)
        print(self.Spieler_Liste)

    def Spieler_loschen(self,event):
        print("gelöscht")
        print(event)
        print(self.Button_Liste)
        platz = 0
        for i in self.Button_Liste:
            if i == event:
                break
            else:
                platz += 1
        print(platz)

        self.Boxlayout_Liste[platz].remove_widget(event)
        self.Boxlayout_Liste[platz].remove_widget(self.Label_Liste[platz])
        self.ids.Box_main_spieler_name.remove_widget(self.Boxlayout_Liste[platz])
        #self.ids.Box_main_spieler_name.self.Boxlayout_Liste[0].remove_widget(event)
        #self.spielerannehmen.remove_widget(event)
        #self.Spieler_Liste.pop(platz)
        print(self.Button_Liste)
        #################################
        #spielernoch aus liste Löschen


    def open_Spieler_hinzu(self): #Popup für einstellungen
        pops = Spielerhizu()
        pops.open()

    def open_popup_spiel(self): #Popup für einstellungen
        pops = popupspiel()
        pops.open()

class popupspiel(Popup):
    pass
    #def Spielen(self):
    #    ms.current = "main"
class Spielerhizu(Popup):
    def hinzufugen(self):
        self.Spielername = self.ids.input_box_main.text
        if self.ids.input_box_main.text != '':
            self.ids.input_box_main.text = ''
            print("hinzu")
            mainscreen.Spieler_hinzu(self.Spielername)



class Zwischen_Karte(Screen):
    def weiter(self):
        self.manager.current = "Spiel_typ01"  # zwischenkarte

    def Spielaufbau(self):
        print("prüfung 1")
        print(mainscreen.Spiel_klasse)
        Name, Text, Ende = mainscreen.Spiel_klasse.Kartenauswahl()# diese soll wir dann die Karte zurückgeben
        if Ende == 0:
            print(Name, Text)
            spielscreen.ids.Aufgabe_name.text = Name
            spielscreen.ids.Aufgabe_text.text = Text

            #Spieler fehlt
            mainscreen.Spieler_klasse.naechster_Spieler() #Auswahl welcher Spieler dran ist
            print(mainscreen.Spieler_klasse.Spieler_liste)
            Spieler = mainscreen.Spieler_klasse.Spieler_dran_name()
            print(Spieler)
            spielscreen.ids.Spieler_name.text = Spieler

#Kartentyp 1
class Spiel_typ01(Screen):
    def test(self):
        print("hallo")

        Name, Text, Ende = mainscreen.Spiel_klasse.Kartenauswahl()
        if Ende == 0:   #für Abbruch der Mainschleife
            spielscreen.ids.Aufgabe_name.text = Name
            spielscreen.ids.Aufgabe_text.text = Text

            mainscreen.Spieler_klasse.naechster_Spieler()  # Auswahl welcher Spieler dran ist
            Spieler = mainscreen.Spieler_klasse.Spieler_dran_name()
            print(Spieler)
            spielscreen.ids.Spieler_name.text = Spieler

    def text_bearbeiten(self):
        mainscreen.Spiel_klasse.Kartenauswahl()
        #self.ids.Aufgabe_name.text = ""
        #self.ids.Aufgabe_text.text = ""





class Spiel_beenden(Screen):      # letzter Screen für neustart
    def neustart(self):
        self.manager.current = "main"


        #Screenmanager
ms = ScreenManager()
mainscreen = MainWindow(name="main")
zwischenscreen = Zwischen_Karte()
spielscreen = Spiel_typ01()
spielende = Spiel_beenden()
ms.add_widget(mainscreen)
ms.add_widget(zwischenscreen)
ms.add_widget(spielscreen)
ms.add_widget(spielende)

#Classen
class Spiel():
    Wiederholung = 0 #0: nein, 1: ja
    Anzahl_Karten_spielen = 2
    Karten_gespielt = 0


    def __init__(self):
        self.Kartensammlungs_auswahl()
        print("neuerstelung der Sammlung")
        #Spieler

    def Kartensammlungs_auswahl(self):
        self.Sammlung = dict()
        self.Karten_Sammlung = self.Sammlung.Speicher
        print("Überprüfung")
        print(self.Sammlung.StaticSpeicher)
        print(self.Sammlung)
        print(self.Karten_Sammlung)

    def Kartenauswahl(self):
        print(self.Karten_gespielt)
        if self.Karten_gespielt >= self.Anzahl_Karten_spielen:
            print("Spiel wird beenden")#Screen machen
            #mainscreen.Spiel_klasse.Spielabbruch()
            self.Spielabbruch()
            Ende = 1        # für Abbruch der mainschleife
            name = "ende"
            text = "ende"
            return name, text, Ende
        else:
            self.Karten_gespielt += 1
            Ende = 0

            print("los gehts")
            #keys = mainscreen.Spiel_klasse.Sammlung.Speicher.keys()
            keys = self.Karten_Sammlung.keys()
            print(keys)
            key = choice(list(keys))
            #item = mainscreen.Spiel_klasse.Sammlung.Speicher.get(key)
            item = self.Karten_Sammlung.get(key)
            name = item.get('headline')
            text = item.get('task')
            self.Karten_Sammlung.pop(key)
            return name, text, Ende

    def Spielabbruch(self):
        spielende.manager.current= "Spiel_beenden"
        #gilt vielleicht nur für den bestimmten Screen



class Spieler():
    def __init__(self,Spieler_liste):
        self.Spieler_liste = Spieler_liste
        self.Spieler_anzahl = len(self.Spieler_liste)
        self.Spieler_dran = 0    #random auswhälen


    def naechster_Spieler(self):
        print(self.Spieler_dran)
        if self.Spieler_dran +1 < self.Spieler_anzahl:
            self.Spieler_dran +=1
            print(self.Spieler_dran)
        else:
            self.Spieler_dran = 0
        print(self.Spieler_anzahl)
        print(self.Spieler_dran)
    def Spieler_dran_name(self):
        print(self.Spieler_liste[self.Spieler_dran])
        return self.Spieler_liste[self.Spieler_dran]

    #def Karten_spieler(self):
    #    self.Spieler(self.Spieler_dran)


#KartenSpiecher für verschiedene Kartentypen
class dict(): #mehr karten haben als Spielrunden möglich !!!!!
    StaticSpeicher = {

        "karte1": {
            "headline": "Pech",
            "task": "du hast heute pech, trinke 2 Schlücke",
        },
        "karte2": {
            "headline": "Fastfood",
            "task": "trinke so viele Schlücke, wie oft du diese Woche schon Fastfood gegessen hat",
        },
        "karte3": {
            "headline": "Investor",
            "task": "Trinke so viele Schlücke wie du willst, du darfst danach die doppelte Anzahl verteilen",
        },
        "karte4": {
            "headline": "Schere-Stein-Papier",
            "task": "Du spielst gegen jeden Mitspieler Schere-Stein-Papier, der Verlierer trinkt 1 Schluck",
        },
        "karte5": {
            "headline": "kleiner Finger",
            "task": "Vergleiche die Länge deines kleinen Finger mit der Höhe deines Getränks im Glas, \nist der Finger kürzer trinke 2 Schlücke",
        },
        "karte6": {
            "headline": "Krankenhaus",
            "task": "Pro Krankenhausaufenthalt den du hattest, darfst du 1 Schluck verteilen \n(die Geburt zählt nicht, du Pappnase)",
        },
        "karte7": {
            "headline": "Zeit zählen",
            "task": "Du muss 30s im Kopf zählen und dann Stopp sagen, wenn du näher als 2 Sekunden an der gestoppten Zeit bist, \nverteile 5 Schlücke, wenn nicht trinke 1 Schluck",
        },
        "karte8": {
            "headline": "Sprichwörter",
            "task": "fängt an. Sagt nacheinander Sprichwörter auf, der Verlierer trinkt 2 Schlücke,",
        },
        "karte9": {
            "headline": "Glückspilz",
            "task": "Das Glück ist mit den Dummen, verteile 4 Schlücke",
        },
        "karte10": {
            "headline": "Shoppen ist teuer",
            "task": "für jedes Kleidungsstück, was neuer als 3 Monate ist, musst du ein Schluck trinken",
        },
        "karte11": {
            "headline": "Hübsch",
            "task": "verteile 3 Schlucke an die Person, die du am hübschsten findest",
        },
        "karte12": {
            "headline": "",
            "task": "verteile 2 Schlücke an eine Person die intelligenter ist als du",
        },
        "karte13": {
            "headline": "",
            "task": "beginnt, jeder wählt im Uhrzeigersinn eine Person aus, die 2 Schlücke trinkt",
        },
        "karte14": {
            "headline": "",
            "task": ", für jeden Spieler, den du kürzer als einen Monat kennst trinkst du 1 Schluck",
        },
    }
    def __init__(self):
        self.Speicher = self.StaticSpeicher.copy()

#Ausführen
class MainApp(App):
    def build(self):
        return ms

if __name__ == '__main__':
    MainApp().run()