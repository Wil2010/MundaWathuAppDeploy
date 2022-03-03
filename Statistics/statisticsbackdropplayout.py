from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
import kivy.utils
from kivy.uix.scrollview import ScrollView

# Your layouts.
KV = (
    '''
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:include Statistics/statisticsmapview.kv

<MyBackdropBackLayer@Screen>
    Image:
        source: "MundaView.jpg"
     
    
<MyBackdropFrontLayer@Screen>

<StatisticsDetailsBackdrop>
    MDBackdrop:
        id: backdrop
        left_action_items: [['transfer-down', lambda x: self.open()]]
        title: "MundaWathu Garden"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Malawi's Statistics:"
        
        
        
        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: container

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                id: frontlayer
        
'''
)


class StatisticsDetailsBackdrop(Screen):
    pass


class StatisticsDetailsBackdropLayout(FloatLayout):
    def run(self):
        Builder.load_string(KV)
        return StatisticsDetailsBackdrop()
