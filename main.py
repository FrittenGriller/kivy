from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
#from kivy.core.window import Window
#Window.size = (360, 640)

kvtext = """
<Mainscreen>:
    MDLabel:
        text: "Hallo"
"""

class Mainscreen(Screen):
    pass



class MainApp(MDApp):
    def build(self):
        #kv = Builder.load_file("SpielMD.kv")
        kv = Builder.load_string(kvtext)
        ms = ScreenManager()
        screen1 = Mainscreen()
        ms.add_widget(screen1)

        return ms


if __name__ == '__main__':
    MainApp().run()
