# Fixed Screen size as android screen
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')
# remove both line when build App

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

import speech_recognition as sr
import playsound
from gtts import gTTS



class DemoApp(MDApp):
    def change_screen(self,name):
        screen_manager.current = name

    def build(self):
        
        # self.theme_cls.primary_palette = "LightBlue"
        # self.theme_cls.primary_hue = "A200"
        # screen = Builder.load_string(screen_helper)
        # return screen
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("ui//login.kv"))
        screen_manager.add_widget(Builder.load_file("ui//signup.kv"))
        screen_manager.add_widget(Builder.load_file("ui//forgot.kv"))
        screen_manager.add_widget(Builder.load_file("ui//verification.kv"))
        screen_manager.add_widget(Builder.load_file("ui//home.kv"))
        self.theme_cls.theme_style="Light"
        
        return screen_manager

    def navigation_draw(self):
        print("deneme")

    def vioce_pyh(self):
        def speak(text):
            tts = gTTS(text=text, lang="en")
            filename = "voice.mp3"
            tts.save(filename)
            playsound.playsound(filename)

        def get_audio():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
                said = ""

                try:
                    said = r.recognize_google(audio)
                    print(said)
                except Exception as e:
                    print("Exception:" + str(e))

            return said

        print("Hey there! Please let me help you,say something.")

        while True:
            text = get_audio()

            if "hello" in text:
                speak("hey there ")
                text = get_audio()
                if "okay" in text:
                    speak("thanks for waiting")

            if "what is your name" in text:
                speak("my name is computer")


DemoApp().run()
