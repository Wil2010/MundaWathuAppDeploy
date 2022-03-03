from kivymd.app import MDApp
from specialbuttons import LabelButton, ImageButton
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from homemapview import HomeMapView
from searchpopupmenu import SearchPopupMenu
from homegpshelper import HomeGpsHelper
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd.uix.picker import MDThemePicker
from about import AboutBannerHeader, AboutBanner
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from climate_folder.climatemapview import ClimateMapView
from Statistics.statisticsbackdropplayout import StatisticsDetailsBackdropLayout
from Statistics.statisticsmapview import StatisticsMapView

from kivy.core.window import Window
import sqlite3
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()


class HomeScreen(Screen):
    pass

class ClimateScreen(Screen):
    pass

class StatisticsScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class PopulationMapScreen(Screen):
    pass
class RainfallMapScreen(Screen):
    pass
class TemperatureMapScreen(Screen):
    pass
class OccupationMapScreen(Screen):
    pass

class mainApp( MDApp):
    search_menu = None
    climatemapview = ObjectProperty(None)
    statisticsmapview = ObjectProperty(None)
    # For refreshing about service
    #refresh_about_service = None
    current_screen_is_about_screen = False


    current_lat = -13.9626
    current_lon = 33.7741

    if os.path.isfile("profile_source.txt"):
        with open("profile_source.txt", "r") as f:
            some_path = f.read()
            if len(some_path) > 0:
                img_source_path = some_path
            else:
                img_source_path = "MundaDemo.jpg"
    else:
        img_source_path = "MundaDemo.jpg"

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def print_theme(self):
        self.cursor.execute("""SELECT * FROM theme ;""")
        current_theme = self.cursor.fetchall()
        self.connection.commit()

        if len(current_theme) == 0:
            self.cursor.execute("""INSERT INTO theme (primary_palette, accent_palette, theme_style) VALUES (?, ?, ?);""",
            (self.theme_cls.primary_palette, self.theme_cls.accent_palette, self.theme_cls.theme_style))
            self.connection.commit()
        else:
            self.cursor.execute("""UPDATE theme SET primary_palette = ? , accent_palette = ? , theme_style = ? ;""", (
            self.theme_cls.primary_palette, self.theme_cls.accent_palette, self.theme_cls.theme_style))
            self.connection.commit()



    def on_start(self):
        # https://kivymd.readthedocs.io/en/latest/themes/theming/
        #self.theme_cls.primary_palette = 'BlueGray'
        #self.theme_cls.primary_hue = "500"
        #self.theme_cls.theme_style = "Light"

        # Initialize GPS
        HomeGpsHelper().run()
        # Connect to database
        self.connection = sqlite3.connect("myapp.db")
        self.cursor = self.connection.cursor()

        # https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.cursor.execute("""SELECT * FROM theme ;""")
        current_theme = self.cursor.fetchall()
        self.connection.commit()

        # print(current_theme)
        # [('Purple', 'BlueGray', 'Light')]

        if len(current_theme) == 0:
            self.theme_cls.primary_palette = 'BlueGray'
            self.theme_cls.accent_palette = "BlueGray"
            self.theme_cls.primary_hue = "500"
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.primary_palette = current_theme[0][0]
            self.theme_cls.accent_palette = current_theme[0][1]
            self.theme_cls.primary_hue = "500"
            self.theme_cls.theme_style = current_theme[0][2]
        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()

        # Instantiate the statistics back drop
        self.statistics_backdroplayout = StatisticsDetailsBackdropLayout().run()
        # Add statistics back drop to the statistical screen
        self.root.ids.statistics_screen.ids.statisticsbackdrop.add_widget(self.statistics_backdroplayout)

        # For About header
        aboutheader = self.root.ids.about_screen.ids.aboutheader
        self.aboutbannerheader = AboutBannerHeader()
        aboutheader.add_widget(self.aboutbannerheader)

    def go_to_about(self, *args):
        aboutbody = self.root.ids.about_screen.ids.aboutbody
        try:
            for w in aboutbody.walk():
                if w.__class__ == AboutBanner:
                    aboutbody.remove_widget(w)
                else:
                    continue
        except:
            print("Something is wrong")
            pass
        if self.current_screen_is_about_screen == False:
            # print("First load")
            self.root.ids.titlename.title = "About MundaWathu"
            self.current_screen_is_about_screen = True
            self.change_screen("about_screen", direction='down', mode='push')

        else:
            # print(args[0])
            print("Refreshing")

    def touch_event(self, touch):
        # Override Scatter's `on_touch_down` behavior for mouse scroll
        scatter_ = self.root.ids.populationmap_screen.ids.scatter
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                if scatter_.scale < 20:
                    scatter_.scale = scatter_.scale * 1.1
            elif touch.button == 'scrollup':
                if scatter_.scale > 1:
                    scatter_.scale = scatter_.scale * 0.8
        # If some other kind of "touch": Fall back on Scatter's behavior
        else:
            print("nothing happen")

    def touch_events(self, touch):
        # Override Scatter's `on_touch_down` behavior for mouse scroll
        scatter_ = self.root.ids.rainfallmap_screen.ids.scatter
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                if scatter_.scale < 20:
                    scatter_.scale = scatter_.scale * 1.1
            elif touch.button == 'scrollup':
                if scatter_.scale > 1:
                    scatter_.scale = scatter_.scale * 0.8
        # If some other kind of "touch": Fall back on Scatter's behavior
        else:
            print("nothing happen")

    def change_profile_source(self, path):
        self.root.ids.profile.source = path  # For mobile phone
        self.root.ids.nav_drawer.toggle_nav_drawer()
        with open("profile_source.txt", "w") as f:
            f.write(path)  # For mobile phone

    def change_screen(self, screen_name, direction='forward', mode=""):
        # Get the screen manager from the kv file.
        screen_manager = self.root.ids.screen_manager

        if direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name

        if screen_name == "home_screen":
            self.root.ids.titlename.title = "MundaWathu"

        if screen_name == "climate_screen":
            self.root.ids.titlename.title = "Climatic Conditions Of Malawi"
            climatescreen_mapview = self.root.ids.climate_screen.ids.climatemapview

            try:
                # Remove climatemapview widget
                for w in climatescreen_mapview.walk():
                    if w.__class__ == ClimateMapView:

                        climatescreen_mapview.remove_widget(w)
                    else:
                        continue
                        # print("No widget to remove")
            except:
                print("Something is wrong")
                pass

            self.climatemapview = ClimateMapView()
            climatescreen_mapview.add_widget(self.climatemapview)

            from climate_folder.climategpshelper import ClimateGpsHelper
            ClimateGpsHelper().run()
            self.climatemapview.center_on(self.current_lat, self.current_lon)

        if screen_name == "statistics_screen":
            self.root.ids.titlename.title = "Statistics Of Malawi"
            self.root.ids.statistics_screen.ids.statisticstoolbar.ids.label_title.font_size = '13sp'
            statistics_backdropfrontlayer = self.statistics_backdroplayout.ids.frontlayer

            try:
                # Remove statisticsmapview widget
                for w in statistics_backdropfrontlayer.walk():
                    if w.__class__ == StatisticsMapView:
                        print("remove occupationmapview widget")
                        statistics_backdropfrontlayer.remove_widget(w)
                    else:
                        continue
            except:
                print("Something is wrong")
                pass


            self.statisticsmapview = StatisticsMapView()
            statistics_backdropfrontlayer.add_widget(self.statisticsmapview)

            from Statistics.statisticsgpshelper import StatisticsGpsHelper
            StatisticsGpsHelper().run()
            self.statisticsmapview.center_on(self.current_lat, self.current_lon)


        if screen_name != "about_screen":
            self.current_screen_is_about_screen = False

        if screen_name == "populationmap_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Population Map"
        if screen_name == "rainfallmap_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Rainfall Map"
        if screen_name == "temperaturemap_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Temperature Map"
        if screen_name == "occupationmap_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Occupation"

mainApp().run()