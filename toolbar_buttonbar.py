from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import speech_recognition as sr
import playsound
from gtts import gTTS

Window.size = (350, 600)
screen_helper = """
Screen:
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "App"
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["clock", lambda x: app.navigation_draw()]]
            elevation: 13
        MDLabel:
            text: "You can start talking  by pressing the microphone button."
            halign: "center"
        
       
                
                                       
            

        MDBottomAppBar:
            MDToolbar:
                title: "Help"
                left_action_items: [["account", lambda x: app.navigation_draw()]]
                elevation: 13
                mode: "free-end" #free-end,end 
                type: "bottom"
                icon: "microphone-outline"
                on_action_button: app.voice_pyh()
        
            
"""


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.primary_hue = "A200"
        screen = Builder.load_string(screen_helper)
        return screen

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
