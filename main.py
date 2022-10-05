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
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, NoTransition
#from kivy.storage.jsonstore import JsonStore
from kivy.uix.popup import Popup
from random import randint, random, choice
from kivy.core.window import Window
#Window.size = (360, 640) #nur für die auflösung jetzt ##rausnehmen beim hochladen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, theme_font_styles
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem, ILeftBodyTouch, CheckboxRightWidget
from kivymd.uix.button import MDFlatButton,MDTextButton,MDIconButton,MDRaisedButton,MDFillRoundFlatButton
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.chip import MDChip
from kivy.core.window import Window

#### Beachten beim übertragen aufs Handy
#- Window.size aus
#- Spielernamen löschen
#- Anzahl der Spiele richig einstellen



#kv = Builder.load_file("Spiel.kv")
kvtext='''

'''

class ItemConfirm(OneLineAvatarIconListItem):
    divider = None
    def set_icon(self, instance_check):
        print("seticon ausgelöst")
        instance_check.active = True
        #check_list = instance_check.get_widgets(instance_check.group)
        #for check in check_list:
        #    if check != instance_check:
        #        check.active = False


#class CheckboxLeftWidget(ILeftBodyTouch, MDCheckbox):
 #   '''Custom right container.'''


class Content(BoxLayout):
    pass

class Info(BoxLayout):
    pass

class Fehler(BoxLayout):
    pass

#Screens
class MainWindow(Screen):
    dialog = None
    dialog1 = None
    dialog2 = None
    dialog3 = None
    selected_project = StringProperty()
    def __init__(self,**kwargs):
        super(MainWindow,self).__init__(**kwargs)
        #self.dialog = None
        ## um Vars zu erstellen


        self.erstesItem = ItemConfirm(text="Basic")
        self.erstesItem.ids.check.active = True
        self.erstesItem.ids.check.disabled = True
        self.zweitesItem = ItemConfirm(text="Kategorien")
        self.zweitesItem.ids.check.active = True
        self.drittesItem = ItemConfirm(text="Abstimmungen")
        self.drittesItem.ids.check.active = True
        self.viertesItem = ItemConfirm(text="Daumenspiel")
        self.viertesItem.ids.check.active = True
        self.funftesItem = ItemConfirm(text="Wenn ich du wäre")
        self.funftesItem.ids.check.active = True
        self.sechstesItem = ItemConfirm(text="Aktivitäten")
        self.sechstesItem.ids.check.active = True


    Label_main_spieler = ObjectProperty(None)
    Spieler_Liste = []#zur Probe'hergen', 'Nils'
    Button_Liste =[]
    Boxlayout_Liste = []
    Label_Liste = []
    def Spieler_hinzu(self,Name):

        print("richtig")
        self.Spielername = Name
        self.Spieler_Liste.append(self.Spielername)
        self.Spieler_Label_hinzu()#in Label

    def Spiel_start(self):
        if self.Spieler_Liste != []:

            self.manager.current = "Zwischen_Karte" #zwischenkarte
            self.Spiel_klasse = Spiel()
            print("erstmal Klasse erstelt")
            print(self.Spiel_klasse)
            self.Spieler_klasse = Spieler(self.Spieler_Liste)
        else:
            self.fehlertest()


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

        self.Knopf = MDFillRoundFlatButton(text='X')#pos_hint={"x": 0.2,"y": 0})# on_release=self.Spieler_loschen())
        self.Knopf.size_hint_x= 2
        self.Knopf.md_bg_color =(116/255,216/255,140/255,1)

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
                    #ItemConfirm(text="Erweiterung"),

                ],
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release=self.close_Dialog_items,
                    )
                ],
            )
        self.dialog.size_hint_x = 1
        self.dialog.size_hint_y = 0.65
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
        self.dialog1.size_hint_x = 1
        self.dialog1.size_hint_y = 0.3
        self.dialog1.open()



    def close_Dialog_items(self, obj):
        self.dialog.dismiss()

    def close_Dialog(self, obj):
        self.dialog1.dismiss()


    def pruf(self, obj):
        print("prüf")
        if self.dialog1.content_cls.ids.content_text.text != '':
            self.Name = self.dialog1.content_cls.ids.content_text.text
            self.dialog1.content_cls.ids.content_text.text = ''
            print(len(self.Name))
            self.Name = self.Name[:10]
            print(self.dialog1.content_cls.ids.content_text.text)
            self.Spieler_hinzu(self.Name)
        self.dialog1.dismiss()
        #print(text)



    def infotext(self):
        print("hallo")
        if not self.dialog2:
            self.dialog2 = MDDialog(
                #title="Address:",
                title="Infos",
                type="custom",
                content_cls=Info(),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release=self.close_Dialog_info,
                        #text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog2.size_hint_x = 1
        self.dialog2.size_hint_y = 0.3
        self.dialog2.open()

    def close_Dialog_info(self, obj):
        self.dialog2.dismiss()



    def fehlertest(self):
        if not self.dialog3:
            self.dialog3 = MDDialog(
                #title="Address:",
                title="Fehler",
                type="custom",
                content_cls=Fehler(),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        on_release=self.close_Dialog_fehler,
                        #text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog3.size_hint_x = 1
        self.dialog3.size_hint_y = 0.3
        self.dialog3.open()

    def close_Dialog_fehler(self, obj):
        self.dialog3.dismiss()


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

class Info3(BoxLayout):
    pass
#Kartentyp 1
class Spiel_typ01(Screen):
    dialog3 = None
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

    def infotext3(self):
        print("hallo")
        if not self.dialog3:
            self.dialog3 = MDDialog(
                #title="Address:",
                title="Spiel beenden?",
                type="custom",
                content_cls=Info3(),
                buttons=[
                    MDFlatButton(
                        text="Nein",
                        theme_text_color="Custom",
                        on_release=self.close_Dialog3,

                    ),
                    MDFlatButton(
                        text="Ja",
                        theme_text_color="Custom",
                        on_release=self.close_Dialog_info3,
                        #text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog3.size_hint_x = 1
        self.dialog3.size_hint_y = 0.3
        self.dialog3.open()

    def close_Dialog3(self, obj):
        self.dialog3.dismiss()

    def close_Dialog_info3(self, obj):
        print("neustart")
        self.dialog3.dismiss()
        print("neustart")
        self.neustart()

    def neustart(self):
        self.manager.current = "Spiel_beenden"
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
    Anzahl_Karten_spielen = 30 #davon 1 anders
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

        print(self.Karten_Sammlung)

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

            if welcher_kartentyp <=2 and len(self.Karten_sammlung_typ_alle) >= 1: #aus welchem Kartentyp gewählt    chance der KArten 10%
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
            "task": "du hast heute pech, trinke [b]2 Schlücke[/b]",
            "frequency": 1      #von 1-10
        },
        "karte2": {
            "headline": "Fastfood",
            "task": "trinke so [b]viele Schlücke[/b], wie oft du diese Woche schon Fastfood gegessen hat",
            "frequency": 1
        },
        "karte3": {
            "headline": "Investor",
            "task": "trinke so [b]viele Schlücke[/b] wie du möchtest, du darfst danach die doppelte Anzahl verteilen",
            "frequency": 2
        },
        "karte4": {
            "headline": "Schere-Stein-Papier",
            "task": "du spielst gegen jeden Mitspieler Schere-Stein-Papier, der Verlierer trinkt [b]1 Schluck[/b]",
            "frequency": 1
        },
        "karte5": {
            "headline": "kleiner Finger",
            "task": "vergleiche die Länge deines kleinen Fingers mit der Höhe deines Getränks im Glas, ist der Finger kürzer, trinke [b]2 Schlücke[/b]",
            "frequency": 1
        },
        "karte6": {
            "headline": "Krankenhaus",
            "task": "pro Krankenhaus- aufenthalt den du hattest, darfst du [b]1 Schluck[/b] verteilen (die Geburt zählt nicht, du Pappnase)",
            "frequency": 1
        },
        "karte7": {
            "headline": "Zeit zählen",
            "task": "ein anderer Spieler stoppt die Zeit. Du musst 30s im Kopf zählen und dann Stopp sagen, wenn du näher als 5 Sekunden an der gestoppten Zeit bist, verteile [b]5 Schlücke[/b], wenn nicht trinke [b]2 Schlücke[/b]",
            "frequency": 1
        },
        "karte9": {
            "headline": "Glückspilz",
            "task": "das Glück ist mit den Dummen, verteile [b]4 Schlücke[/b]",
            "frequency": 1
        },
        "karte10": {
            "headline": "Shoppen ist teuer",
            "task": "für jedes Kleidungsstück das du trägst, was neuer als 3 Monate ist, musst du [b]ein Schluck[/b] trinken",
            "frequency": 1
        },
        "karte11": {
            "headline": "Hübsch",
            "task": "verteile [b]3 Schlücke[/b] an die Person, die du am hübschsten findest",
            "frequency": 1
        },
        "karte12": {
            "headline": "Intelligenzbolzen",
            "task": "verteile [b]2 Schlücke[/b] an eine Person die intelligenter ist als du",
            "frequency": 1
        },
        "karte13": {
            "headline": "Wahltag",
            "task": "beginnt, jeder wählt im Uhrzeigersinn eine Person aus, die [b]2 Schlücke[/b] trinkt",
            "frequency": 1
        },
        "karte14": {
            "headline": "coole Leute",
            "task": "für jeden Spieler, den du kürzer als einen Monat kennst trinkst du [b]1 Schluck[/b]",
            "frequency": 1
        },
        "karte15": {
            "headline": "Tattoos",
            "task": "trinke für jedes Tattoo, das du hast, [b]1 Schluck[/b]",
            "frequency": 1
        },
        "karte16": {
            "headline": "Gläser",
            "task": "trinke für jedes Glas, das auf dem Tisch steht [b]1 Schluck[/b]",
            "frequency": 1
        },
                    #         1         2         3         4
        "karte17": {
            "headline": "Dichter",
            "task": "finde bis zu 5 Reime auf -Drucker-. Für jeden Reim verteile [b]1 Schluck[/b]",
            "frequency": 1
        },
        "karte18": {
            "headline": "Rauchen ist für Loser",
            "task": "trinke für jede Zigarette in deiner Schachtel [b]1 Schluck[/b] maximal [b]8 Schluck[/b]",
            "frequency": 1
        },
                    #         1         2         3         4#         1         2         3         4#         1         2         3         4
        "karte19": {
            "headline": "Happy Birthday",
            "task": "sage die Geburtstage von den Mitspielernauf, verteile für jeden richtigen [b]1 Schluck[/b]",
            "frequency": 1
        },
        "karte20": {
            "headline": "Astrologie",
            "task": ""
                    "Dein Chinesisches Sternzeichen nach Geburtsjahr"
                    "\nSchwein: 1995 [b]S. = 1[/b]"
                    "\nRatte: 1996 [b]S. = 2[/b]"
                    "\nBüffel: 1997 [b]S. = 1[/b]"
                    "\nTiger: 1998 [b]S. = 3[/b]"
                    "\nHase: 1999 [b]S. = 2[/b]"
                    "\nDrache: 2000 [b]S. = 4[/b]"
                    "\nSchlange: 2001 [b]S.  = 1[/b]",
            "frequency": 1
        },
        "karte21": {
            "headline": "stay hydrated",
            "task": "trinke [b]ein Glas Wasser[/b] auf ex",
            "frequency": 1
        },
        "karte22": {
            "headline": "Selfietime",
            "task": "mach ein schlechtes Gruppenselfie",
            "frequency": 1
        },
        "karte23": {
            "headline": "Streber",
            "task": "wenn dein Schulabschluss besser als 2,5 war, trinke [b]5 Schlücke[/b]",
            "frequency": 1
        },
        "karte24": {
            "headline": "Hausverbot",
            "task": "trinke [b]1 Schluck[/b] pro Hausverbot, dass du schon bekommen hast",
            "frequency": 1
        },
                    #         1         2         3         4
        "karte25": {
            "headline": "Charmeur",
            "task": "mache einem Mitspieler ein Kompliment, der Spieler trinkt [b]3 Schlucke[/b]",
            "frequency": 1
        },
        "karte26": {
            "headline": "Adonis",
            "task": "bewerte, wer die beste Figur hat. Die Person trinkt [b]3 Schlucke[/b]",
            "frequency": 1
        },
        "karte27": {
            "headline": "Joker",
            "task": "Das nächste mal, wenn du trinken musst, kannst du stattdessen [b]2 Schlucke[/b] verteilen",
            "frequency": 1
        },
        "karte28": {
            "headline": "Kontinente",
            "task": "trinke [b]1 Schluck[/b] für jeden Kontinent, auf dem du warst",
            "frequency": 1
        },
        "karte29": {
            "headline": "Land",
            "task": "zähle ein Land auf, wenn nur du in diesem Land warst, verteile [b]4 Schlücke[/b]",
            "frequency": 1
        },
        "karte30": {
            "headline": "Mails checken",
            "task": "verteile für jeden E-mail account, den du hast [b]1 Schluck[/b]",
            "frequency": 1
        },
        "karte31": {
            "headline": "Kopf oder Zahl",
            "task": "Wirf eine Münze ist es Kopf trinke [b]1 Schluck[/b], bei Zahl trinke [b]3 Schluck[/b]",
            "frequency": 1
        },
        "karte32": {
            "headline": "Stolz wie Bolle",
            "task": "erzähle, wann du das letzte mal Stolz warst, verteile dafür [b]2 Schlücke[/b]",
            "frequency": 1
        },
        "karte33": {
            "headline": "Party",
            "task": "nenne den besten Partysong und trinke darauf [b]1 Schlucke[/b]",
            "frequency": 1
        },
        "karte34": {
            "headline": "Peinlich",
            "task": "erzähle deine peinlichste Partystory, trinke vor [b]3 Schlücke[/b]",
            "frequency": 1
        },
        "karte35": {
            "headline": "Kopf oder Zahl",
            "task": "Wirf eine Münze ist es Kopf trinke [b]2 Schluck[/b], bei Zahl verteile [b]4 Schlucke[/b]",
            "frequency": 1
        },
        "karte36": {
            "headline": "Bonze",
            "task": "Wenn dein Smartphone teuer als 300€, trinke [b]2 Schlücke[/b]",
            "frequency": 1
        },
        "karte37": {
            "headline": "Exen",
            "task": "Trinke für jede/n Exfreund/in [b]1 Schlücke[/b]",
            "frequency": 1
        },
        "karte38": {
            "headline": "Bilder",
            "task": "Zeige das letzte Bild, was du in Whatsapp bekommen hast, verteile dafür [b]4 Schlücke[/b]",
            "frequency": 1
        },
        "karte39": {
            "headline": "Mimen",
            "task": "Mime einen Mitspieler, die erratene Person verteilt [b]2 Schlücke[/b]",
            "frequency": 1
        },
        "karte40": {
            "headline": "Respekt",
            "task": "Trinke aus respekt vor den anderen Mitspielern [b]3 Schlücke[/b] mit beiden Händen am Glas",
            "frequency": 1
        },
        "karte41": {
            "headline": "Trinkgeselle",
            "task": "Erzähle warum man mit dir gut trinken gehen kann, alle trinken darauf [b]1 Schluck[/b]",
            "frequency": 1
        },
        "karte42": {
            "headline": "Lieblingssong",
            "task": "Sag deinen momentanen Lieblingssong oder mach ihn an, trinke für jeden Mitspieler der ihn nicht mag [b]1 Schluck[/b]",
            "frequency": 1
        },
        "karte43": {
            "headline": "Profikoch",
            "task": "Erzähle ein Missgeschick, dass dir beim Kochen passiert ist, trinke drauf [b]1 Schluck[/b]",
            "frequency": 1
        },
    }

    ####Basic
    # Alle Spieler
    Speicherfuralle = {
                    #         1         2         3         4#         1         2         3         4#         1         2         3         4
        "karte1": {
            "headline": "Zahlen",
            "task": "Alle sagen einen zahl zwischen 1 und 100 die, die am Durchschnitt der Zahlen am nahsten und am weitesten entfernt ist, trinken [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte2": {
            "headline": "Festival",
            "task": "Wer als letzes auf einem Festival war, verteilt [b]3 Schlucke[/b]",
            "frequency": 1
        },
        "karte3": {
            "headline": "Gesundes Essen",
            "task": "Wer schon mal in einem Fastfood Restaurant, etwas gesundes bestellt hat trinkt [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte4": {
            "headline": "Promi",
            "task": "Wer schon mal ein Foto mit einem Promi gemacht hat, trinkt [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte5": {
            "headline": "Sahneschnitten",
            "task": "Jede/r trinkt die Anzahl an [b]Schlucke[/b] pro heißen Typen/Mädel, die mitspielen",
            "frequency": 1
        },
        "karte6": {
            "headline": "zwei in Folge",
            "task": "Wer gestern schon getrunken hat, trinkt [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte7": {
            "headline": "Meckerliese",
            "task": "Wer gemeckert hat, dieses Spiel zu spielen trinkt [b]4 Schlucke[/b]",
            "frequency": 1
        },
        "karte8": {
            "headline": "Haustier",
            "task": "Wer ein Haustier besitzt, trinkt [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte9": {
            "headline": "Fußball",
            "task": "Jeder der noch nie in einem Fußballstadion war, trinkt [b]2 Schlucke[/b]",
            "frequency": 1
        },
    }


    #Alle Spieler
    Dict_Abstimmung = {
        "karte1": {
            "headline": "Clown",
            "task": "Stimmt auf 3 ab, wer am lustigsten ist, der Klassenclown trinkt [b]3 Schlücke[/b]",
            "frequency": 1
        },
        "karte2": {
            "headline": "Opfer",
            "task": "Entscheidet, wer das Opfer der Runde ist, es trinkt [b]3 Schlücke[/b]. Wenn niemand gewählt wird,trinken alle [b]5 Schlücke[/b]",
            "frequency": 1
        },
        "karte3": {
            "headline": "Abstimmung",
            "task": "Wer ist der netteste Spieler der Runde, zeigt auf 3 auf den Spieler, jeder Spieler trinkt so [b]viele Schlücke[/b], wie Finger auf ihn zeigen",
            "frequency": 1
        },
    }
    #Alle Spieler
    Dict_Daumenspiel = {
        "karte1": {
            "headline": "Daumenspiel",
            "task": "Lieber Bier oder Wein, jeder Spieler zeigt auf 3 mit seinem Daumen nach unten oder hoben, die Verlierer trinken [b]1 Schluck[/b], bei Gleichstand [b]trinken alle einen[/b]",
            "frequency": 1
        },
        "karte2": {
            "headline": "Daumenspiel",
            "task": "Lieber Ananas oder Mais auf Pizza, jeder Spieler zeigt auf 3 mit seinem Daumen nach unten oder hoben, die Verlierer trinken [b]1 Schluck[/b], bei Gleichstand [b]trinken alle einen[/b]",
            "frequency": 1
        },
    }
    # ein Spieler
    Dict_Kategorien = {
        "karte1": {
            "headline": "Automarken",
            "task": "beginnt. zählt nacheinander Automarken auf. Bei Wiederholung oder falschen trinkt der Verlierer [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte2": {
            "headline": "Cocktails",
            "task": "beginnt. zählt nacheinander Cocktailnamen auf. Bei Wiederholung oder falschen trinkt der Verlierer [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte3": {
            "headline": "Bäume",
            "task": "beginnt, zählt nacheinander Baumarten auf. Bei Wiederholung oder falschen trinkt der Verlierer [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte4": {  # kategorie
            "headline": "Sprichwörter",
            "task": "beginnt, zählt nacheinander Sprichwörter auf, der Verlierer trinkt [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte5": {
            "headline": "Metalle",
            "task": "beginnt, zählt nacheinander Metalle auf, der Verlierer trinkt [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte6": {
            "headline": "Vornamen",
            "task": "beginnt, zählt nacheinander Vornamen beginnend mit 'A' auf, der Verlierer trinkt [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte7": {
            "headline": "Kater",
            "task": "beginnt, zählt nacheinander Tipps gegen Kater auf, der Verlierer trinkt [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte8": {
            "headline": "Unglück",
            "task": "beginnt, zählt nacheinander Dinge die Pech bringen auf, der Verlierer trinkt [b]2 Schlucke[/b]",
            "frequency": 1
        },


        "karte20": {
            "headline": "Maler",
            "task": "zähle berühmte Maler auf. Für jeden richtigen drafst du [b]1 Schluck[/b] verteilen, bei einem falschen, trinke [b]5 Schlucke[/b] selber",
            "frequency": 1
        },
    }


    # ein Spieler
    Dict_wennich = {
        "karte26": {
            "headline": "Wenn ich du wäre",
            "task": "stelle eine 'wenn ich du wäre Aufgabe' an einen Mitspieler deiner Wahl, du trinkst dafür [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte27": {
            "headline": "ich habe noch nie",
            "task": "stelle eine 'ich habe noch nie Aufgabe', alle die es schon mal gemacht haben trinken [b]1 Schluck[/b]",
            "frequency": 4
        },
    }
    # ein Spieler
    Dict_Aktivitat_korper = {
        "karte1": {
            "headline": "Liegestütze",
            "task": "mache 10 Liegestütze oder trinke [b]3 Schlucke[/b]",
            "frequency": 1
        },
        "karte2": {
            "headline": "Pantomime",
            "task": "stelle ein ausgedachtes Wort pantomimisches da, trinke [b]5 Schlucke[/b] wenn es keiner errät, der Errater verteilt 2 Schlucke",
            "frequency": 3
        },
        "karte3": {
            "headline": "Plätzetausch",
            "task": "tausche mit deinem Spieler deiner Wahl die Plätze trinke auf den besseren Platz [b]ein Schluck[/b]",
            "frequency": 1
        },
        "karte4": {
            "headline": "Dancemove",
            "task": "zeige einen deiner Dancemoves oder trinke [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte5": {
            "headline": "Armdrücken",
            "task": "Mache gegen ein Mitspieler Armdrücken, der Verlieren trinkt [b]2 Schlucke[/b]",
            "frequency": 1
        },
        "karte6": {
            "headline": "Kniebeugen",
            "task": "Mache 10 Kniebeugen oder trinke [b]3 Schlucke[/b]",
            "frequency": 1
        },
        "karte7": {
            "headline": "Daumenwrestling",
            "task": "Spiel gegen eine Mitspieler eine Runde Daumenwrestling, der Verlierer [b]3 Schlucke[/b]",
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
        kv = Builder.load_file("Spiel.kv")
        #kv = Builder.load_string(kvtext)
        #self.theme_cls.theme_style = "Dark"

        ms = ScreenManager(transition=NoTransition())
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
    Mainclass = MainApp()
    Mainclass.run()


