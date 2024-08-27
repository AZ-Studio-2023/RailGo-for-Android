import threading

from kivy.app import App
from kivy.clock import mainthread
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from Helper.apiHelper import getData


class EMU_RoutingInterface(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size, source="Resource/image/bg.png")
            self.bind(pos=self.update_rect, size=self.update_rect)

        self.title = Label(text="动车组交路查询", color="#abc0e4", font_size=40,
                           size_hint=[0.2, 0.15], pos_hint={"center_x": 0.5, "top": 0.95},
                           font_name="Resource/font/DingTalk_JinBuTi.ttf")

        self.back = Button(text="返回", on_press=self.toIndex, color="#abc0e4",
                           font_name="Resource/font/DingTalk_JinBuTi.ttf",
                           size_hint=[0.08, 0.05], pos_hint={"center_x": 0.05, "top": 0.98})

        self.train = TextInput(text="请输入车组号", font_name="Resource/font/DingTalk_JinBuTi.ttf",
                               size_hint=[0.5, 0.05], pos_hint={"center_x": 0.5, "top": 0.8},
                               background_color="#6b95ea")

        self.find = Button(text="查询", on_press=self.query, color="#abc0e4",
                           font_name="Resource/font/DingTalk_JinBuTi.ttf",
                           size_hint=[0.12, 0.05], pos_hint={"center_x": 0.5, "top": 0.72})

        self.scroll_view = ScrollView(size_hint=(0.9, 0.5), pos_hint={"center_x": 0.5, "top": 0.6})
        self.result_grid = GridLayout(cols=3, spacing=10, size_hint_y=None)
        self.result_grid.bind(minimum_height=self.result_grid.setter('height'))

        self.scroll_view.add_widget(self.result_grid)

        self.add_widget(self.title)
        self.add_widget(self.back)
        self.add_widget(self.train)
        self.add_widget(self.find)
        self.add_widget(self.scroll_view)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def toIndex(self, arg):
        App.get_running_app().screenManager.current = "Index"

    def query(self, arg):
        def fetch_data():
            response = getData(f"https://api.rail.re/emu/{self.train.text}")
            data_list = response.json()
            self.update_results(data_list)

        thread = threading.Thread(target=fetch_data)
        thread.start()

    @mainthread
    def update_results(self, data_list):
        self.result_grid.clear_widgets()

        self.result_grid.add_widget(Label(text="时间", color="#000000", size_hint_y=None, height=40,
                                          font_name="Resource/font/DingTalk_JinBuTi.ttf", font_size=16))
        self.result_grid.add_widget(Label(text="车组号", color="#000000", size_hint_y=None, height=40,
                                          font_name="Resource/font/DingTalk_JinBuTi.ttf", font_size=16))
        self.result_grid.add_widget(Label(text="车次", color="#000000", size_hint_y=None, height=40,
                                          font_name="Resource/font/DingTalk_JinBuTi.ttf", font_size=16))

        for data in data_list:
            self.result_grid.add_widget(Label(text=data['date'], color="#000000", size_hint_y=None, height=40,
                                              font_name="Resource/font/DingTalk_JinBuTi.ttf", font_size=13))
            self.result_grid.add_widget(Label(text=data['emu_no'], color="#000000", size_hint_y=None, height=40,
                                              font_name="Resource/font/DingTalk_JinBuTi.ttf", font_size=13))
            self.result_grid.add_widget(Label(text=data['train_no'], color="#000000", size_hint_y=None, height=40,
                                              font_name="Resource/font/DingTalk_JinBuTi.ttf", font_size=13))