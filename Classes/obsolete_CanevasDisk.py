import configparser
from tkinter import ttk
import tkinter
from tkinter import *
from psutil import disk_usage
from Classes.obsolete_Disk import Disque
from configparser import ConfigParser
from pathlib import Path
from controleur.column_setter import ColumnSetter

class Canevasdisques:
    listeDiskAfficher = []
    canevas = Canvas
    liste_complete_partiti = []
    liste_disk_to_forget = []
    diskFrameGen = ttk.Frame
    diskFrameGen2 = ttk.Frame
    device = ''
    zone_1_max = 0
    zone_2_max = 0
    green = '#4ef14e'
    orange = '#ff8800'
    redd = '#f00000'
    directory2 = Path(__file__).parent.parent
    convert_unite = 0
    zoom_rat = 0
    colu_pour_network = 0
    row_pour_network = 0
    col_setter = ColumnSetter
    listDiskFrameGen = []
    diskframegeneral = ttk.Frame
    diskframegeneral2 = ttk.Frame
    diskframegeneral3 = ttk.Frame
    diskframegeneral4 = ttk.Frame
    frame_pour_network = ttk.Frame
    listpathtoforget2 = [""]

    def __init__(self, screenHeight, liste_complete_part, convert_uni, zone_1_max, zone_2_max, zoom_ratio, disFramGen,
                 listetoforget = []):
        self.listeDiskAfficher = []
        self.liste_complete_partiti = liste_complete_part
        self.liste_disk_to_forget = listetoforget
        self.device = ''
        self.zone_1_max = zone_1_max
        self.zone_2_max = zone_2_max
        self.convert_unite = convert_uni
        self.zoom_rat = zoom_ratio
        self.diskFrameGen = disFramGen
        self.col_setter = ColumnSetter(screenHeight)
        self.colu_pour_network = 0
        self.row_pour_network = 0
        self.diskframegeneral = ttk.Frame
        self.diskframegeneral2 = ttk.Frame
        self.diskframegeneral3 = ttk.Frame
        self.diskframegeneral4 = ttk.Frame
        self.frame_pour_network = ttk.Frame
        self.listpathtoforget2 = [""]



    def update_liste_complete_part(self, liste_complete_part):  # peut-etre inutile...
        self.liste_complete_partiti = liste_complete_part
        return liste_complete_part
