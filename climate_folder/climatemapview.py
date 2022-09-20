from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.uix.button import Button
from kivymd.uix.dialog import MDDialog
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.app import App
from climate_folder.climatemarker import ClimateMarker


class ClimateMapView(MapView):
    #Karonga Dialog
    def show_karonga(self, instance):
        self.dialog = MDDialog(
            title= "Karonga Climatic Conditions",
            text= "Annual Rainfall (Average) 2008-2017: 947"
                  "\nAverage Monthly Rainfall 2008-2017 (Total): 934"
                  "\nAverage Monthly Maximum Temperature 2008-2017: 25.4"
                  "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 30.3\nMin: 20.3",
            size_hint = [.9, .5],
            auto_dismiss= False
        )
        self.dialog.open()
    #Chitipa Dialog
    def show_chitipa(self, instance):
        self.dialog = MDDialog(
            title= "Chitipa Climatic Conditions",
            text= "Annual Rainfall (Average) 2008-2017: 911\nAverage Monthly Rainfall 2008-2017 (Total): 904"
                  "\nAverage Monthly Maximum Temperature 2008-2017: 22.0"
                  "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:"
                  "\nMax: 27.1\nMin: 16.8",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Rumphi Dialog
    def show_rumphi(self, instance):
        self.dialog = MDDialog(
            title="Rumphi Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 681"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 24.1"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 28.8\nMin: 16.1",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Nkhata Bay Dialog
    def show_nkhatabay(self, instance):
        self.dialog = MDDialog(
            title="Nkhata Bay Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 1,571"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 1544"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 22.5"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 30.3\nMin: 18.0",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Likoma Dialog
    def show_likoma (self, instance):
        self.dialog = MDDialog(
            title="Likoma Climatic Conditions",
            text="Not Available",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Mzimba Dialog
    def show_mzimba(self, instance):
        self.dialog = MDDialog(
            title="Mzimba Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 755"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 757"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 21.3"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 26.9\nMin: 15.6",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Mzuzu Dialog
    def show_mzuzu (self, instance):
        self.dialog = MDDialog(
            title="Mzuzu Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 1,176"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 1160"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 19.4"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 24.9\nMin: 13.9",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Lilongwe Dialog
    def show_lilongwe(self, instance):
        self.dialog = MDDialog(
            title="Lilongwe Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 815"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 815"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 21.4"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 27.5\nMin: 15.3",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Dedza Dialog
    def show_dedza(self, instance):
        self.dialog = MDDialog(
            title="Dedza Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 957"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 939"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 18.6"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 23.4\nMin: 13.8",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Salima Dialog
    def show_salima(self, instance):
        self.dialog = MDDialog(
            title="Salima Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 1,132"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 1096"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 25.3"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 29.9\nMin: 20.6",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Dowa Dialog
    def show_dowa(self, instance):
        self.dialog = MDDialog(
            title="Dowa Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 755",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Kasungu Dialog
    def show_kasungu(self, instance):
        self.dialog = MDDialog(
            title="Kasungu Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 682"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 22.2"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 28.4\nMin: 15.9",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Mchinji Dialog
    def show_mchinji(self, instance):
        self.dialog = MDDialog(
            title="Mchinji Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 986",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Nkhotakota Dialog
    def show_nkhotakota(self, instance):
        self.dialog = MDDialog(
            title="Nkhotakota Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 1,465"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 1373"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 24.5"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 28.8\nMin: 20.3",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Ntchisi Dialog
    def show_ntchisi(self, instance):
        self.dialog = MDDialog(
            title="Ntchisi Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 871",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Ntcheu Dialog
    def show_ncheu(self, instance):
        self.dialog = MDDialog(
            title="Ntcheu Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 996",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Mangochi Dialog
    def show_mangochi(self, instance):
        self.dialog = MDDialog(
            title="Mangochi Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 868"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 862"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 25.4"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 30.9\nMin: 19.9",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Machinga Dialog
    def show_machinga(self, instance):
        self.dialog = MDDialog(
            title="Machinga Climatic Conditions",
            text="Not Available",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Balaka Dialog
    def show_balaka(self, instance):
        self.dialog = MDDialog(
            title="Balaka Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 527",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Neno Dialog
    def show_neno(self, instance):
        self.dialog = MDDialog(
            title="Neno Climatic Conditions",
            text="Not Available",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Mwanza Dialog
    def show_mwanza(self, instance):
        self.dialog = MDDialog(
            title="Mwanza Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 920",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Chiradzulu Dialog
    def show_chiradzulu(self, instance):
        self.dialog = MDDialog(
            title="Chiradzulu Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 937",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Blantyre Dialog
    def show_blantyre(self, instance):
        self.dialog = MDDialog(
            title="Blantyre Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 1,160"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 1108"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 21.4"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 26.3\nMin: 16.4",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Zomba Dialog
    def show_zomba(self, instance):
        self.dialog = MDDialog(
            title="Zomba Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 1,193"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 963"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 21.6"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 27.1\nMin: 16.0",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Chikwawa Dialog
    def show_chikwawa (self, instance):
        self.dialog = MDDialog(
            title="Chikwawa Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 819"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 796"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 26.9"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 33.2\nMin: 20.6",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    #Thyolo Dialog
    def show_thyolo(self, instance):
        self.dialog = MDDialog(
            title="Thyolo Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 1,182"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 1136"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 20.1"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 25.0\nMin: 15.0",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Mulanje Dialog
    def show_mulanje(self, instance):
        self.dialog = MDDialog(
            title="Mulanje Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 2,071"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 1531"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 22.9"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 29.2\nMin: 16.6",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Phalombe Dialog
    def show_phalombe(self, instance):
        self.dialog = MDDialog(
            title="Phalombe Climatic Conditions",
            text="Not Available",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()
    # Nsanje Dialog
    def show_nsanje(self, instance):
        self.dialog = MDDialog(
            title="Nsanje Climatic Conditions",
            text="Annual Rainfall (Average) 2008-2017: 819"
                 "\nAverage Monthly Rainfall 2008-2017 (Total): 796"
                 "\nAverage Monthly Maximum Temperature 2008-2017: 26.9"
                 "\nAverage Monthly Maximum and Minimum Temperatures 2008-2017:\nMax: 33.2\nMin: 20.6",
            size_hint=[.9, .5],
            auto_dismiss=False
        )
        self.dialog.open()

    def on_start(self):
        #Karonga Coordinates
        marker = MapMarkerPopup(lat=-9.9525, lon=33.9248, source="icons\marker.png", on_release = self.show_karonga)
        self.add_widget(marker)
        #Chitipa Coordinates
        marker = MapMarkerPopup(lat=-9.7038, lon=33.2700, source="icons\marker.png", on_release = self.show_chitipa)
        self.add_widget(marker)
        #Rumphi Coordinates
        marker = MapMarkerPopup(lat=-11.0172, lon=33.8551, source="icons\marker.png", on_release = self.show_rumphi)
        self.add_widget(marker)
        #Nkhata Bay Coordinates
        marker = MapMarkerPopup(lat=-11.6086, lon=34.2949, source="icons\marker.png", on_release = self.show_nkhatabay)
        self.add_widget(marker)
        #Likoma Coordinates
        marker = MapMarkerPopup(lat=-12.0625, lon=34.7409, source="icons\marker.png", on_release = self.show_likoma)
        self.add_widget(marker)
        #Mzimba Coordinates
        marker = MapMarkerPopup(lat=-11.8992, lon=33.5924, source="icons\marker.png", on_release = self.show_mzimba)
        self.add_widget(marker)
        # Mzuzu Coordinates
        marker = MapMarkerPopup(lat=-11.4390, lon=34.0084, source="icons\marker.png", on_release = self.show_mzuzu)
        self.add_widget(marker)
        #Lilongwe Coordinates
        marker = MapMarkerPopup (lat= -13.9626,  lon= 33.7741, source= "icons\marker.png", on_release = self.show_lilongwe)
        self.add_widget(marker)
        #Dedza Coordinates
        marker = MapMarkerPopup(lat=-14.3817, lon=34.3255, source="icons\marker.png", on_release = self.show_dedza)
        self.add_widget(marker)
        #Salima Coordinates
        marker = MapMarkerPopup(lat=-13.7796, lon=34.4586, source="icons\marker.png", on_release = self.show_salima)
        self.add_widget(marker)
        #Dowa Coordinates
        marker = MapMarkerPopup(lat=-13.6515, lon=33.9360, source="icons\marker.png", on_release = self.show_dowa)
        self.add_widget(marker)
        #Kasungu Coordinates
        marker = MapMarkerPopup(lat=-13.0357, lon=33.4720, source="icons\marker.png", on_release = self.show_kasungu)
        self.add_widget(marker)
        #Mchinji Coordinates
        marker = MapMarkerPopup(lat=-13.800, lon=32.8930, source="icons\marker.png", on_release = self.show_mchinji)
        self.add_widget(marker)
        #Nkhotakota Coordinates
        marker = MapMarkerPopup(lat=-12.9317, lon=34.2811, source="icons\marker.png", on_release = self.show_nkhotakota)
        self.add_widget(marker)
        #Ntchisi Coordinates
        marker = MapMarkerPopup(lat=-13.2842, lon=33.8858, source="icons\marker.png", on_release = self.show_ntchisi)
        self.add_widget(marker)
        #Ntcheu Coordinates
        marker = MapMarkerPopup(lat=-14.9038, lon=34.7741, source="icons\marker.png", on_release = self.show_ncheu)
        self.add_widget(marker)
        #Mangochi Coordinates
        marker = MapMarkerPopup(lat=-14.4862, lon=35.2533, source="icons\marker.png", on_release = self.show_mangochi)
        self.add_widget(marker)
        #Machinga Coordinates
        marker = MapMarkerPopup(lat=-15.1700, lon=35.3000, source="icons\marker.png", on_release = self.show_machinga)
        self.add_widget(marker)
        #Balaka Coordinates
        marker = MapMarkerPopup(lat=-14.9876, lon=34.9562, source="icons\marker.png", on_release = self.show_balaka)
        self.add_widget(marker)
        #Neno Coordinate
        marker = MapMarkerPopup(lat=-15.6851, lon=34.5750, source="icons\marker.png", on_release = self.show_neno)
        self.add_widget(marker)
        #Mwanza Coordinates
        marker = MapMarkerPopup(lat=-15.5998, lon=34.5141, source="icons\marker.png", on_release = self.show_mwanza)
        self.add_widget(marker)
        #Chiradzulu
        marker = MapMarkerPopup(lat=-15.6759, lon=35.1406, source="icons\marker.png", on_release = self.show_chiradzulu)
        self.add_widget(marker)
        #Blantyre Coordinates
        marker = MapMarkerPopup(lat=-15.7667, lon=35.0168, source="icons\marker.png", on_release = self.show_blantyre)
        self.add_widget(marker)
        #Zomba Coordinates
        marker = MapMarkerPopup(lat=-15.3766, lon=35.3357, source="icons\marker.png", on_release = self.show_zomba)
        self.add_widget(marker)
        #Chikwawa Coordinates
        marker = MapMarkerPopup(lat=-16.0438, lon=34.8017, source="icons\marker.png", on_release = self.show_chikwawa)
        self.add_widget(marker)
        #Thyolo Coordinates
        marker = MapMarkerPopup(lat=-16.0693, lon=35.1406, source="icons\marker.png", on_release = self.show_thyolo)
        self.add_widget(marker)
        #Mulanje Coordinates
        marker = MapMarkerPopup(lat=-16.0252, lon=35.5083, source="icons\marker.png", on_release = self.show_mulanje)
        self.add_widget(marker)
        #Phalombe Coordinates
        marker = MapMarkerPopup(lat=-15.7633, lon=35.6588, source="icons\marker.png", on_release = self.show_phalombe)
        self.add_widget(marker)
        #Nsanje Coordinates
        marker = MapMarkerPopup(lat=-16.9206, lon=35.2533, source="icons\marker.png", on_release = self.show_nsanje)
        self.add_widget(marker)

