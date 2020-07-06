from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)
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
            text: "Hello There"
            halign: "center"
        
        MDBottomAppBar:
            MDToolbar:
                title: "Help"
                left_action_items: [["account", lambda x: app.navigation_draw()]]
                elevation: 13
                mode: "free-end" #free-end,end 
                type: "bottom"
                icon: "microphone-outline"
                on_action_button: app.navigation_draw()
"""


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.primary_hue = "A200"
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("navigation")


DemoApp().run()
