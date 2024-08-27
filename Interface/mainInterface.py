from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.app import App


class mainInterface(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size, source="Resource/image/bg.png")
            self.bind(pos=self.update_rect, size=self.update_rect)
        self.title = Label(text="RailGo")
        self.title.color = "#abc0e4"
        self.title.font_size = 50
        self.title.size_hint = [0.2, 0.15]
        self.title.pos_hint = {"center_x": 0.5, "top": 0.95}
        self.title.font_name = "Resource/font/DingTalk_JinBuTi.ttf"
        self.EMU_Routing = Button(text="动车组交路查询", on_press=self.toEMU_Routing)
        self.EMU_Routing.color = "#abc0e4"
        self.EMU_Routing.font_name = "Resource/font/DingTalk_JinBuTi.ttf"
        self.EMU_Routing.size_hint = [0.8, 0.1]
        self.EMU_Routing.pos_hint = {"center_x": 0.5, "top": 0.8}
        self.add_widget(self.title)
        self.add_widget(self.EMU_Routing)

    def toEMU_Routing(self, arg):
        App.get_running_app().screenManager.current = "EMU_Routing"

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
