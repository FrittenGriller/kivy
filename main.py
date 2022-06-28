from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.gridlayout import GridLayout
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
#from kivy.core.window import Window
#Window.size = (360, 640) #nur für die auflösung jetzt
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.button import MDFlatButton,MDTextButton,MDIconButton,MDRaisedButton,MDFillRoundFlatButton
from kivymd.uix.chip import MDChip
#from kivy.core.window import Window

#kv = Builder.load_file("Spiel.kv")
kvtext='''
<ItemConfirm>
    on_release: root.set_icon(check)

    CheckboxLeftWidget:
        id: check
        #group: "check"
        #active: True



<Content>
    orientation: "vertical"
    #spacing: 20
    size_hint_y: None
    height: 20  ####################### potentieller fehler

    MDTextField:
        id: content_text
        hint_text: "Name"



<MainWindow>:
    name: "main"
    canvas.before:
        Color:
            rgba: (0.4,0.1,0.7,1)
        Rectangle:
            pos: self.pos
            size: self.size
    #Image:
    #    source: 'Grille.png'
    #    size: self.texture_size

    FloatLayout:
        size: root.width, root.height
        orientation: 'vertical'

        MDFillRoundFlatButton:
            text: "Spielen"
            md_bg_color: (116/255,216/255,140/255,1)
            on_release: root.Spiel_start()
            #on_release: root.open_popup_spiel()
            pos_hint: {"x": 0.3,"y": 0.}
            size_hint: (0.4,0.2)
            font_size: self.width/5


        Label: #Spieler
            id: Label_main_spieler
            text:"Spieler"
            font_size: self.width/10
            pos_hint: {"x": 0.,"y": 0.3}
                        #size_hint: (0.2,0.1)
                        #color: 1, 1, 0, 1


        ##muss noch geändert weerden
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            pos_hint: {"x": 0.25,"y": 0.4}
            size_hint: (0.6,0.3)
            BoxLayout:
            #ScatterLayout:
            #GridLayout
                orientation: 'vertical'
                #pos_hint: {"x": 0.3,"y": 0.5}
                #size_hint: (1,0.2)
                size_hint_y: None
                #height: 20
                height: self.minimum_height
                id: Box_main_spieler_name
                spacing:40
                padding: 30

        MDRectangleFlatButton:
            text: "Karten"
            text_color: (116/255,216/255,140/255,1)
            line_color: (116/255,216/255,140/255,1)
            pos_hint: {"x": 0.35,"y": 0.3}
            size_hint: (0.3,0.05)
            on_release: root.show_alert_dialog()




        ##Spieler eintragen
        #Button:
        MDFillRoundFlatButton:
            text:"hinzufügen"
            md_bg_color: (116/255,216/255,140/255,1)
            pos_hint: {"x": 0.7,"y": 0.75}
            size_hint: (0.2,0.1)
            font_size: self.width/8
            on_release: root.show_Spielerhinzu_dialog()
            #on_release: root.open_Spieler_hinzu()


<Spielerhizu>
    auto_dismiss: False
    title: "Einstellungen"
    size_hint: 0.6, 0.4
    pos_hint: {"x": 0.2, "top":0.9}
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            #Label:
            MDLabel:
                text:"Spielername eingeben"
                font_size: self.width/12
                size_hint: (0.8,1)

            Button:
                text: "close"
                size_hint: (0.2,1)
                font_size: self.width/8
                on_release:
                    root.dismiss()

        TextInput:
            id: input_box_main
            multiline:False
            #font_size: self.width/8
            #pos_hint: {"x": 0.8,"y": 0.5}
            #size_hint: (0.2,0.2)

        Button:
            text: "hinzufügen"
            #size_hint: (0.2,0.2)
            font_size: self.width/10
            on_release:
                root.hinzufugen()
            on_release:
                root.dismiss()



<popupspiel>
    auto_dismiss: False
    title: "Einstellungen"
    size_hint: 0.6, 0.2
    pos_hint: {"x": 0.2, "top":0.9}
    BoxLayout:
        Button:
            text: "close"
            font_size: self.width/8
            on_release:
                root.dismiss()

        Button:
            text: "Neustart"
            font_size: self.width/8
            on_release:
                root.Spielen()



<Zwischen_Karte>:
    name: "Zwischen_Karte"
    FloatLayout:
        size: root.width, root.height
        orientation: 'vertical'

        MDFillRoundFlatButton:
            text: "Weiter"
            on_release: root.weiter()
            on_release: root.Spielaufbau()
            pos_hint: {"x": 0.3,"y": 0.}
            size_hint: (0.4,0.2)
            font_size: self.width/8

        MDLabel:
            id: Zwischen
            text:"Viel Spaß"
            size_hint: (0.3,0.2)
            pos_hint: {"x": 0.4,"y": 0.8}
            font_size: self.width/5
            #color: 1, 1, 0, 1

        MDLabel:
            text:"...."
            size_hint: (0.3,0.2)
            pos_hint: {"x": 0.4,"y": 0.6}
            font_size: self.width/7
            #color: 1, 1, 0, 1


<Spiel_typ01>:
    name: "Spiel_typ01"
    FloatLayout:
        size: root.width, root.height
        orientation: 'vertical'

        MDFillRoundFlatButton:
            text: "Weiter"
            on_release: root.test()
            pos_hint: {"x": 0.3,"y": 0.}
            size_hint: (0.4,0.2)
            font_size: self.width/8

        MDLabel:
            id: Aufgabe_name
            text:"Aufgabe"
            size_hint: (0.3,0.1)
            pos_hint: {"x": 0.4,"y": 0.85}
            #color: 1, 1, 0, 1
            font_size: self.width/5

        MDLabel:
            id: Aufgabe_text
            text:"Spieler ... mache das und das, sonst trinke zwei schlücke"
            size_hint: (0.4,0.4)
            pos_hint: {"x": 0.2,"y": 0.3}
            #color: 1, 1, 0, 1
            font_size: self.width/8
        MDLabel:
            id: Spieler_name
            text:""
            size_hint: (0.2,0.1)
            pos_hint: {"x": 0.4,"y": 0.7}
            #color: 1, 1, 0, 1
            font_size: self.width/4


<Spiel_beenden>:
    name: "Spiel_beenden"
    FloatLayout:
        size: root.width, root.height
        orientation: 'vertical'

        MDFillRoundFlatButton:
            text: "Neustart"
            on_release: root.neustart()
            pos_hint: {"x": 0.3,"y": 0.}
            size_hint: (0.4,0.2)
            font_size: self.width/8

        MDLabel:
            id: Spiel_ende
            text:"Spiel beendet"
            size_hint: (0.2,0.1)
            pos_hint: {"x": 0.4,"y": 0.65}
            #color: 1, 1, 0, 1
            font_size: self.width/3
'''

class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False





class Content(BoxLayout):
    pass


#Screens
class MainWindow(Screen):
    dialog = None
    dialog1 = None
    selected_project = StringProperty()
    def __init__(self,**kwargs):
        super(MainWindow,self).__init__(**kwargs)
        ## um Vars zu erstellen
        #self.show_alert_dialog()
        #self.dialog.dismiss()
        self.erstesItem = ItemConfirm(text="Basic")
        self.erstesItem.ids.check.active = True
        self.erstesItem.ids.check.disabled = True
        self.zweitesItem = ItemConfirm(text="Kategorien")
        self.drittesItem = ItemConfirm(text="Abstimmungen")
        self.viertesItem = ItemConfirm(text="Daumenspiel")
        self.funftesItem = ItemConfirm(text="widw und ihnn")
        self.sechstesItem = ItemConfirm(text="Aktivitäten")


    Label_main_spieler = ObjectProperty(None)
    Spieler_Liste = ['hergen', 'Nils']#zur Probe
    Button_Liste =[]
    Boxlayout_Liste = []
    Label_Liste = []
    def Spieler_hinzu(self,Name):

        print("richtig")
        self.Spielername = Name
        self.Spieler_Liste.append(self.Spielername)
        self.Spieler_Label_hinzu()#in Label

    def Spiel_start(self):
        self.manager.current = "Zwischen_Karte" #zwischenkarte
        self.Spiel_klasse = Spiel()
        print("erstmal Klasse erstelt")
        print(self.Spiel_klasse)
        self.Spieler_klasse = Spieler(self.Spieler_Liste)


    def Spieler_Label_hinzu(self):
        self.spielerannehmen = BoxLayout(orientation='horizontal')
        #self.spielerannehmen = AnchorLayout(size_hint=(1,1))
        #self.spielerannehmen = ScatterLayout(size_hint=(1, 1))
        spielername = MDLabel(text=self.Spielername)
        self.ids.Box_main_spieler_name.add_widget(self.spielerannehmen)
        self.spielerannehmen.add_widget(spielername)
        self.Boxlayout_Liste.append(self.spielerannehmen)
        self.Label_Liste.append(spielername)
        print("hallo")
        print(self.Boxlayout_Liste[0])
        #print(self.ids.Box_main_spieler_name.spielerannehmen)

        #zwischen Boxlayout
        self.zwischenbox = AnchorLayout(size_hint=(0.25,1))
        #self.zwischenbox = BoxLayout(orientation='horizontal')
        self.spielerannehmen.add_widget(self.zwischenbox)

        self.Knopf = MDFillRoundFlatButton(text='X',size_hint_x= 0.2)#pos_hint={"x": 0.2,"y": 0})# on_release=self.Spieler_loschen())
        #self.Knopf.on_release = self.Spieler_loschen
        self.Knopf.bind(on_release = self.Spieler_loschen)
        self.Button_Liste.append(self.Knopf)
        #self.spielerannehmen.add_widget(self.Knopf)#############

        self.zwischenbox.add_widget(self.Knopf)#################
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

    def show_alert_dialog(self):  ####man kann nur eins anklicken, muss angeklickt werdenoder ähnliches
        #self.erstesItem = ItemConfirm(text="Basic")
        #self.erstesItem.ids.check.active = True
        #self.zweitesItem = ItemConfirm(text="erweiterung")
        #self.erstesItem.active= True
        if not self.dialog:
            self.dialog = MDDialog(
                title="Kartensets",
                type="confirmation",
                items=[
                    self.erstesItem,
                    self.zweitesItem,
                    self.drittesItem,
                    self.viertesItem,
                    self.funftesItem,
                    self.sechstesItem,
                    #ItemConfirm(text="Basic"),
                    #ItemConfirm(text="erweiterung")

                ],
            )
        self.dialog.open()
        #print(erstesItem.divider)
        #print(self.erstesItem.ids.check.active)#######


    def show_Spielerhinzu_dialog(self):
        if not self.dialog1:
            self.dialog1 = MDDialog(
                #title="Address:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        on_release= self.close_Dialog,

                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release=self.pruf,
                        #text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog1.open()

    def close_Dialog(self, obj):
        print("eeee")
        self.dialog1.dismiss()


    def pruf(self, obj):
        print("prüf")
        self.Name = self.dialog1.content_cls.ids.content_text.text
        self.dialog1.content_cls.ids.content_text.text = ''
        print(len(self.Name))
        self.Name = self.Name[:10]
        print(self.dialog1.content_cls.ids.content_text.text)
        self.Spieler_hinzu(self.Name)
        self.dialog1.dismiss()
        #print(text)


#Popups können entfernt werden

class popupspiel(Popup):
    pass

class Spielerhizu(Popup):
    def __init__(self,**kwargs):
        super(Spielerhizu,self).__init__(**kwargs)

    def hinzufugen(self):
        self.Spielername = self.ids.input_box_main.text
        if self.ids.input_box_main.text != '':
            self.ids.input_box_main.text = ''
            print("hinzu")
            #mainscreen.Spieler_hinzu(self.Spielername)
            #self.parent.Spieler_hinzu(self.Spielername)
            Mainclass.mainscreen.Spieler_hinzu(self.Spielername)
            #MainWindow.Spieler_hinzu(self,self.Spielername)



class Zwischen_Karte(Screen):
    def weiter(self):
        self.manager.current = "Spiel_typ01"  # zwischenkarte

    def Spielaufbau(self):
        print("prüfung 1")
        print(Mainclass.mainscreen.Spiel_klasse)
        Name, Text, Ende, welcher_Spieler = Mainclass.mainscreen.Spiel_klasse.Kartenauswahl()# diese soll wir dann die Karte zurückgeben
        #welcher_Spieler = 0: spieler, welcher_Spieler= 1 alle
        if Ende == 0:
            print(Name, Text)
            Mainclass.spielscreen.ids.Aufgabe_name.text = Name
            Mainclass.spielscreen.ids.Aufgabe_text.text = Text


            if welcher_Spieler == 0:
                Mainclass.mainscreen.Spieler_klasse.naechster_Spieler() #Auswahl welcher Spieler dran ist
                print(Mainclass.mainscreen.Spieler_klasse.Spieler_liste)
                Spieler = Mainclass.mainscreen.Spieler_klasse.Spieler_dran_name()
                print(Spieler)
                Mainclass.spielscreen.ids.Spieler_name.text = Spieler
            else:
                Mainclass.spielscreen.ids.Spieler_name.text = ""

#Kartentyp 1
class Spiel_typ01(Screen):
    def test(self):
        print("hallo")


        Name, Text, Ende, welcher_Spieler = Mainclass.mainscreen.Spiel_klasse.Kartenauswahl()
        if Ende == 0:   #für Abbruch der Mainschleife
            Mainclass.spielscreen.ids.Aufgabe_name.text = Name
            Mainclass.spielscreen.ids.Aufgabe_text.text = Text

            if welcher_Spieler == 0:
                Mainclass.mainscreen.Spieler_klasse.naechster_Spieler()  # Auswahl welcher Spieler dran ist
                Spieler = Mainclass.mainscreen.Spieler_klasse.Spieler_dran_name()
                print(Spieler)
                Mainclass.spielscreen.ids.Spieler_name.text = Spieler
            else:
                Mainclass.spielscreen.ids.Spieler_name.text = ""

    #def text_bearbeiten(self):
    #    mainscreen.Spiel_klasse.Kartenauswahl()
        #self.ids.Aufgabe_name.text = ""
        #self.ids.Aufgabe_text.text = ""





class Spiel_beenden(Screen):      # letzter Screen für neustart
    def neustart(self):
        self.manager.current = "main"
        print("neustart")
        print(Mainclass.mainscreen.erstesItem.ids.check.active)


        #Screenmanager
"""
ms = ScreenManager()
mainscreen = MainWindow(name="main")
zwischenscreen = Zwischen_Karte()
spielscreen = Spiel_typ01()
spielende = Spiel_beenden()
ms.add_widget(mainscreen)
ms.add_widget(zwischenscreen)
ms.add_widget(spielscreen)
ms.add_widget(spielende)
"""

#Classen
class Spiel():
    Wiederholung = 0 #0: nein, 1: ja
    Anzahl_Karten_spielen = 3 #davon 1 anders
    Karten_gespielt = 0


    def __init__(self):
        self.Kartensammlungs_auswahl()
        #Mainclass.mainscreen.erstesItem.ids.check.active
        print("neuerstelung der Sammlung")
        #Spieler

    def Kartensammlungs_auswahl(self):
        self.Sammlung = dict()

        #self.Karten_Sammlung = self.Sammlung.Speicher
        #self.Karten_sammlung_typ_alle = self.Sammlung.Speicherfuralle

        #einzelnen Dict zusammen führen
        if Mainclass.mainscreen.zweitesItem.ids.check.active == True:   #Kategrien, ein Spieler
            self.Sammlung.Speicher.update(self.Sammlung.Dict_Kategorien)
        if Mainclass.mainscreen.drittesItem.ids.check.active == True:   #Abstimmungen, alle Spielr
            self.Sammlung.Speicher_alle.update(self.Sammlung.Dict_Abstimmung)
        if Mainclass.mainscreen.viertesItem.ids.check.active == True:   #Daumenspiel, alle Spieler
            self.Sammlung.Speicher_alle.update(self.Sammlung.Dict_Daumenspiel)
        if Mainclass.mainscreen.funftesItem.ids.check.active == True:   #wennich , ein Spieler
            self.Sammlung.Speicher.update(self.Sammlung.Dict_wennich)
        if Mainclass.mainscreen.sechstesItem.ids.check.active == True:   #aktivität_körper, ein Spieler
            self.Sammlung.Speicher.update(self.Sammlung.Dict_Aktivitat_korper)

        self.Karten_Sammlung = self.Sammlung.Speicher
        self.Karten_sammlung_typ_alle = self.Sammlung.Speicher_alle

        ## Problem Namen der Karten überschneidungen

    def Kartenauswahl(self):
        print(self.Karten_gespielt)
        if self.Karten_gespielt >= self.Anzahl_Karten_spielen:  # if für kartenanzahl
            print("Spiel wird beenden")#Screen machen
            #mainscreen.Spiel_klasse.Spielabbruch()
            self.Spielabbruch()
            Ende = 1        # für Abbruch der mainschleife
            name = "ende"
            text = "ende"
            welcher_Spieler = 0
            return name, text, Ende, welcher_Spieler
        else:
            self.Karten_gespielt += 1
            Ende = 0

            #auswahl welcher Kartentyp
            welcher_kartentyp = randint(1,10)

            if welcher_kartentyp <=1 and len(self.Karten_sammlung_typ_alle) >= 1: #aus welchem Kartentyp gewählt    chance der KArten 10%
                #alle typ
                keys = self.Karten_sammlung_typ_alle.keys()
                print(keys)
                probabillity = []
                for k in keys:
                    haufig = self.Karten_sammlung_typ_alle[k]['frequency']
                    for i in range(0, haufig):
                        probabillity.append(k)
                newkey = choice(probabillity)
                print("wahrscheinkeit:" + newkey)
                ###
                key = newkey  # choice(list(keys))
                #key = choice(list(keys))
                item = self.Karten_sammlung_typ_alle.get(key)
                name = item.get('headline')
                text = item.get('task')
                frequenz = item.get('frequency')
                #self.Karten_sammlung_typ_alle.pop(key)
                welcher_Spieler = 1#alle Spieler
                if frequenz == 1:
                    self.Karten_sammlung_typ_alle.pop(key)
                else:
                    self.Karten_sammlung_typ_alle[key]['frequency'] -= 1
            else: #nur ausgewählte spieler
                print("los gehts")
                #keys = mainscreen.Spiel_klasse.Sammlung.Speicher.keys()
                keys = self.Karten_Sammlung.keys()

                ##### richtige wahrscheinlichkeit
                print(keys)
                probabillity = []
                for k in keys:
                    haufig = self.Karten_Sammlung[k]['frequency']
                    for i in range(0,haufig):
                        probabillity.append(k)
                newkey = choice(probabillity)
                print("wahrscheinkeit:" +newkey)
                ###
                key = newkey#choice(list(keys))
                #item = mainscreen.Spiel_klasse.Sammlung.Speicher.get(key)
                item = self.Karten_Sammlung.get(key)
                name = item.get('headline')
                text = item.get('task')
                frequenz = item.get('frequency')
                print("freqenz ändern")
                print(self.Karten_Sammlung[key]['frequency'])
                if frequenz == 1:
                    self.Karten_Sammlung.pop(key)
                else:
                    self.Karten_Sammlung[key]['frequency'] -= 1
                #self.Karten_Sammlung.pop(key)
                print(len(name))
                print(len(text))
                welcher_Spieler = 0#ein Spieler
            return name, text, Ende, welcher_Spieler

    def Spielabbruch(self):
        Mainclass.spielende.manager.current= "Spiel_beenden"
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
                    #         1         2         3         4
        "karte1": {
            "headline": "Pech",
            "task": "du hast heute pech, trinke 2 Schlücke",
            "frequency": 1      #von 1-10
        },
        "karte2": {
            "headline": "Fastfood",
            "task": "trinke so viele Schlücke, wie oft du diese"
                    "\n   Woche schon Fastfood gegessen hat",
            "frequency": 1
        },
        "karte3": {
            "headline": "Investor",
            "task": "trinke so viele Schlücke wie du\nmöchtest, du darfst danach die doppelte\nAnzahl verteilen",
            "frequency": 2
        },
        "karte4": {
            "headline": "Schere-Stein-Papier",
            "task": "du spielst gegen jeden Mitspieler\nSchere-Stein-Papier, der Verlierer\n trinkt 1 Schluck",
            "frequency": 1
        },
        "karte5": {
            "headline": "kleiner Finger",
            "task": "vergleiche die Länge deines kleinen\nFingers mit der Höhe deines Getränks im \nGlas, ist der Finger kürzer, trinke 2 Schlücke",
            "frequency": 1
        },
        "karte6": {
            "headline": "Krankenhaus",
            "task": "pro Krankenhausaufenthalt den du\nhattest, darfst du 1 Schluck verteilen\n(die Geburt zählt nicht, du Pappnase)",
            "frequency": 1
        },
        "karte7": {
            "headline": "Zeit zählen",
            "task": "ein anderer Spieler benutzt eine\nStoppuhr. Du musst 30s im Kopf zählen und\ndann Stopp sagen, wenn du näher als\n2 Sekunden an der gestoppten Zeit bist,\nverteile 5 Schlücke, wenn nicht trinke 1 Schluck",
            "frequency": 1
        },
        "karte9": {
            "headline": "Glückspilz",
            "task": "das Glück ist mit den Dummen, verteile\n4 Schlücke",
            "frequency": 1
        },
        "karte10": {
            "headline": "Shoppen ist teuer",
            "task": "für jedes Kleidungsstück das du trägst,\nwas neuer als 3 Monate ist, musst du ein\nSchluck trinken",
            "frequency": 1
        },
        "karte11": {
            "headline": "Hübsch",
            "task": "verteile 3 Schlücke an die Person, die\ndu am hübschsten findest",
            "frequency": 1
        },
        "karte12": {
            "headline": "Intelligenzbolzen",
            "task": "verteile 2 Schlücke an eine Person die\nintelligenter ist als du",
            "frequency": 1
        },
        "karte13": {
            "headline": "Wahltag",
            "task": "beginnt, jeder wählt im Uhrzeigersinn \neine Person aus, die 2 Schlücke trinkt",
            "frequency": 1
        },
        "karte14": {
            "headline": "coole Leute",
            "task": "für jeden Spieler, den du kürzer als\neinen Monat kennst trinkst du 1 Schluck",
            "frequency": 1
        },
        "karte15": {
            "headline": "Tattoos",
            "task": "trinke für jedes Tattoo, das du hast,\neinen Schluck",
            "frequency": 1
        },
                    #         1         2         3         4
        "karte17": {
            "headline": "Dichter",
            "task": "finde bis zu 5 Reime auf -Drucker-. Für\njeden Reim verteile ein Schluck",
            "frequency": 1
        },
                    #         1         2         3         4#         1         2         3         4#         1         2         3         4
        "karte19": {
            "headline": "Happy Birthday",
            "task": "sage die Geburtstage von den\nMitspielernauf, verteile für jeden\nrichtigen ein Schluck",
            "frequency": 1
        },
        "karte20": {
            "headline": "Astrologie",
            "task": "\n"
                    "Dein Chinesisches Sternzeichen"
                    "\nSchwein: Geburtsjahr = 1995 Schlücke = 1"
                    "\nRatte: Geburtsjahr = 1996 Schlücke = 2"
                    "\nBüffel: Geburtsjahr = 1997 Schlücke = 1"
                    "\nTiger: Geburtsjahr = 1998 Schlücke = 3"
                    "\nHase: Geburtsjahr = 1999 Schlücke = 2"
                    "\nDrache: Geburtsjahr = 2000 Schlücke = 4"
                    "\nSchlange: Geburtsjahr = 2001 Schlücke = 1",
            "frequency": 1
        },
        "karte21": {
            "headline": "stay hydrated",
            "task": "trinke ein Glas Wasser auf ex",
            "frequency": 1
        },
        "karte22": {
            "headline": "Selfietime",
            "task": "mach ein schlechtes Gruppenselfie",
            "frequency": 1
        },
        "karte23": {
            "headline": "Streber",
            "task": "wenn dein Schulabschluss besser als\n2,5 war, trinke 5 Schlücke",
            "frequency": 1
        },
        "karte24": {
            "headline": "Hausverbot",
            "task": "trinke ein Schluck pro Hausverbot,\ndass du schon bekommen hast",
            "frequency": 1
        },
                    #         1         2         3         4
        "karte25": {
            "headline": "Charmeur",
            "task": "mache einem Mitspieler ein Kompliment,\nder Spieler trinkt 3 Schlucke",
            "frequency": 1
        },
        "karte28": {
            "headline": "Kontinente",
            "task": "trinke 1 Schluck für jeden Kontinent,\nauf dem du warst",
            "frequency": 1
        },
        "karte29": {
            "headline": "Land",
            "task": "zähle ein Land auf, wenn nur du in\ndiesem Land warst, verteile 4 Schlücke",
            "frequency": 1
        },
        "karte30": {
            "headline": "Mails checken",
            "task": "verteile für jeden E-mail account, den\ndu hast 1 Schluck",
            "frequency": 1
        },
        #"karte31": {
        #    "headline": "Beste Leben",
        #    "task": "erzähle eins deiner besten Ereignisse\nin deinem Leben. Trinke drauf 2 Schlücke",
        #    "frequency": 1
        #},
        "karte32": {
            "headline": "Stolz wie Bolle",
            "task": "erzähle wann du das letzte mal Stolz\nwarst, verteile dafür 2 Schlücke",
            "frequency": 1
        },
        "karte33": {
            "headline": "Party",
            "task": "nenne den besten Partysong und trinke\ndarauf einen Schluck",
            "frequency": 1
        },
        "karte34": {
            "headline": "Peinlich",
            "task": "erzähle deine peinlichste Partystory,\ntrinke vor 3 Schlücke",
            "frequency": 1
        },
        "karte36": {
            "headline": "Dancemove",
            "task": "zeige einen deiner Dancemoves oder\ntrinke 2 Schlücke",
            "frequency": 1
        },
    }

    ####Basic
    # Alle Spieler
    Speicherfuralle = {
                    #         1         2         3         4#         1         2         3         4#         1         2         3         4
        "karte1": {
            "headline": "Zahlen",
            "task": "Alle sagen einen zahl zwischen 1 und 100\ndie, die am Durchschnitt der Zahlen am\nnahsten und am weitesten entfernt ist\ntrinkt 2 Schlückte",
            "frequency": 1
        },
    }


    #Alle Spieler
    Dict_Abstimmung = {
        "karte1": {
            "headline": "",
            "task": "",
            "frequency": 1
        },
        "karte2": {
            "headline": "Opfer",
            "task": "Entscheidet, wer das Opfer\nder Runde ist, es trinkt 3 Schlücke.\nWenn niemand gewählt wird,trinken\nalle 5 Schlücke",
            "frequency": 1
        },
        "karte3": {
            "headline": "Abstimmung",
            "task": "Wer ist der netteste Spieler\nder Runde, zeigt auf 3 auf den Spieler,\njeder Spieler trinkt so viele Schlücke,\nwie Finger auf ihn zeigen",
            "frequency": 1
        },
    }
    #Alle Spieler
    Dict_Daumenspiel = {
        "karte1": {
            "headline": "",
            "task": "",
            "frequency": 1
        },
        "karte2": {
            "headline": "Daumenspiel",
            "task": "Lieber Ananas oder Mais auf Pizza,\njeder Spieler zeigt auf 3 mit seinem\nDaumen nach unten oder hoben, die\nVerlierer trinken 1 Schluck, bei\nGleichstand trinken alle einen",
            "frequency": 1
        },
    }
    # ein Spieler
    Dict_Kategorien = {
        "karte1": {
            "headline": "",
            "task": "",
            "frequency": 1
        },
        "karte38": {
            "headline": "Cocktails",
            "task": "beginnt. Sagt nacheinander Cocktailnamen\nauf. Bei Wiederholung oder falschen\ntrinkt der Verlierer  2 Schlücke,",
            "frequency": 1
        },
        "karte37": {
            "headline": "Bäume",
            "task": "beginnt. Sagt nacheinander Baumarten\nauf. Bei Wiederholung oder falschen trinkt\nder Verlierer  2 Schlücke,",
            "frequency": 1
        },
        "karte8": {  # kategorie
            "headline": "Sprichwörter",
            "task": "fängt an. Sagt nacheinander Sprichwörter\nauf, der Verlierer trinkt 2 Schlücke,",
            "frequency": 1
        },
    }
    # ein Spieler
    Dict_wennich = {
        "karte1": {
            "headline": "",
            "task": "",
            "frequency": 1
        },
        "karte26": {
            "headline": "Wenn ich du wäre",
            "task": "stelle eine -wenn ich du wäre Aufgabe-\nan einen Mitspieler deiner Wahl, du\ntrinkst dafür 2 Schlücke",
            "frequency": 1
        },
        "karte27": {
            "headline": "ich habe noch nie",
            "task": "stelle eine -ich habe noch nie Aufgabe-\nalle die es schon mal gemacht haben\ntrinken 1 Schluck",
            "frequency": 3
        },
    }
    # ein Spieler
    Dict_Aktivitat_korper = {
        "karte1": {
            "headline": "",
            "task": "",
            "frequency": 1
        },
        "karte35": {
            "headline": "Liegestütze",
            "task": "mache 10 Liegestütze oder trinke\n3 Schlücke",
            "frequency": 1
        },
        "karte18": {
            "headline": "Pantomime",
            "task": "stelle ein ausgedachtes Wort\npantomimisches da, trinke 5 Schlucke\nwenn es keiner errät, der Errater\nverteilt 2 Schlucke",
            "frequency": 3
        },
        "karte16": {
            "headline": "Plätzetausch",
            "task": "tausche mit deinem Spieler deiner Wahl\ndie Plätze trinke auf den besseren Platz\nein Schluck",
            "frequency": 1
        },
    }

    def __init__(self):
        self.Speicher = self.StaticSpeicher.copy()
        self.Speicher_alle = self.Speicherfuralle.copy()



#Ausführen
class MainApp(MDApp):
    def __init__(self, **kwargs):
        super(MainApp,self).__init__(**kwargs)

    def build(self):
        #kv = Builder.load_file("Spiel.kv")
        kv = Builder.load_string(kvtext)
        #self.theme_cls.theme_style = "Dark"

        ms = ScreenManager()
        self.mainscreen = MainWindow(name="main")
        self.zwischenscreen = Zwischen_Karte()
        self.spielscreen = Spiel_typ01()
        self.spielende = Spiel_beenden()
        ms.add_widget(self.mainscreen)
        ms.add_widget(self.zwischenscreen)
        ms.add_widget(self.spielscreen)
        ms.add_widget(self.spielende)
        return ms


if __name__ == '__main__':
    #MainApp().run()
    Mainclass = MainApp()
    Mainclass.run()



