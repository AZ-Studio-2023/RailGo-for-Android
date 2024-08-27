from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from Helper.getValue import pages

class RailGo_for_Android(App):
    def build(self):
        self.screenManager = ScreenManager()
        for item, page in pages.items():
            self.default_page = page
            screen = Screen(name=item)
            screen.add_widget(self.default_page)
            self.screenManager.add_widget(screen)
        return self.screenManager
