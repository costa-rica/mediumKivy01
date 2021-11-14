from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        return Builder.load_file('design.kv')

MainApp().run()
