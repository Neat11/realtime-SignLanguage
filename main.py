import kivy 
kivy.require('1.9.0')
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
import os
from kivymd.app import MDApp
from kivy.uix.stacklayout import StackLayout
import json
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.video import Video
from LanguageRecognition import LanguageRecognition as lr
import createAction

class ContentNavigationDrawer(BoxLayout):
    pass

class Help(Screen):
    pass

class Create(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def get_frames(self,textfield):
        word = textfield.text
        createAction.createAction(word)

class Launch(Screen):
    obj = lr()
    description = StringProperty("""In this world of 8 billion people about 470 million suffer from some kind of hearing or speech impairment. The main means of communication for the population is sign language, which many personnel in this world dont know. With Signo we aim to create something revolutionary; Something that diminishes the barrier and brings about a wave of change.""")
    def __init__(self, **kw):
        super().__init__(**kw)
        print("launch initiated")

    def launch_button(self):
        print("launch_button intiated")
        self.obj.startCapture()

    def oncall(self):
        print("button press")

class LearnPage(Screen):


    def __init__(self, **kw):
        super().__init__(**kw)
        b = StackLayout(orientation='lr-tb',size=(self.size),padding=(0,80))
        DATA_PATH = os.path.join("gestures")
        list = os.listdir(DATA_PATH)
        for i in list:
            bx = BoxLayout(orientation="vertical",padding=(30,30),size=(200,400))
            bx.add_widget(Video(source=os.path.join('gestures',i),size_hint=(1,1)))
            bx.add_widget(Label(text=i.replace(".avi","")))
            b.add_widget(bx)
        self.add_widget(b)
    


class Splash(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)     

    def launch(self):
        self.manager.current = 'Launch'
        print("kuch ho gaya")

class MyScreenManager(ScreenManager):
    def changescreen(self, value):
        self.manager.current = value

class SignApp(MDApp):
    def build(self):
        self.sm = MyScreenManager()
        return self.sm
    


SignApp().run()