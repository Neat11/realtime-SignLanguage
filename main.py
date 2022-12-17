import kivy 
kivy.require('1.9.0')
from kivy.core.window import Window
Window.size = (600, 400)
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import os
from LanguageRecognition import LanguageRecognition


class Launch(Screen):
    obj = LanguageRecognition()
    def __init__(self, **kw):
        super().__init__(**kw)
        print("launch initiated")

    def launch_button(self):
        print("launch_button intiated")

class Splash(Screen):
    obj = LanguageRecognition()
    def launch(self):
        self.manager.current = 'Launch'
        print("kuch ho gaya")
        self.obj.startCapture()
class MyScreenManager(ScreenManager):
    def changescreen(self, value):
        self.manager.current = value

class SignApp(App):
    def build(self):
        self.sm = MyScreenManager()
        return self.sm


SignApp().run()