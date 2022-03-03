from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from specialbuttons import ImageButton, LabelButton
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.app import App
import kivy.utils
import requests, json
from functools import partial
from datetime import datetime
import math
from kivy.properties import StringProperty

class AboutBannerHeader(GridLayout):
    rows = 1

    def __init__(self, **kwargs):
        super().__init__()

        with self.canvas.before:
            self.canvas_color = Color(rgb=kivy.utils.get_color_from_hex("c8fcf7"))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

        # First Header: Fruit Seedling Available
        firstheader = FloatLayout()
        firstheaderimage = ImageButton(source="icons/seatsavailable.png", size_hint=(1, 0.5), pos_hint={"top": 1, "right": 1})
        firstheaderlabel = Label(text="[color=000000]Fruit\nSeedling[/color]", markup=True, size_hint=(1, .2),
                                 pos_hint={"top": .45, "right": 1})
        firstheader.add_widget(firstheaderimage)
        firstheader.add_widget(firstheaderlabel)

        # Second Header: Smallholder Farmers
        secondheader = FloatLayout()
        secondheaderimage = ImageButton(source="icons/standingavailable.png", size_hint=(1, 0.5),
                                  pos_hint={"top": 1, "right": 1})
        secondheaderlabel = Label(text="[color=000000]Smallholder\nFarmers[/color]", markup=True, size_hint=(1, .2),
                                  pos_hint={"top": .45, "right": 1})
        secondheader.add_widget(secondheaderimage)
        secondheader.add_widget(secondheaderlabel)

        # Third Header: Exotic Seedling
        thirdheader = FloatLayout()
        thirdheaderimage = Image(source="icons/limitedstanding.png", size_hint=(1, 0.5),
                                 pos_hint={"top": 1, "right": 1})
        thirdheaderlabel = Label(text="[color=000000]Exotic\nSeedling[/color]", markup=True, size_hint=(1, .2),
                                 pos_hint={"top": .45, "right": 1})
        thirdheader.add_widget(thirdheaderimage)
        thirdheader.add_widget(thirdheaderlabel)



        self.add_widget(firstheader)
        self.add_widget(secondheader)
        self.add_widget(thirdheader)


    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class AboutBanner(GridLayout):
    rows = 1