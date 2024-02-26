from psutil import disk_usage, disk_io_counters
from controleur.c_convert_bit import ConvertBit
from collections import deque
from tkinter import ttk


class Disque:
    mountpoint = ""
    diskBar = {}
    diskLabel = ttk.Label
    diskFam = {}
    diskLabelFree = {}
    diskabel = ttk.Label
    diskCaneva = {}
    endColorGreen = 0
    endColorOrange = 0
    readDiskPrecedent = 0
    writeDiskPrecedent = 0
    diskLabRead = ttk.Label
    diskLabWrite = ttk.Label
    bitsUnite = ["o", "ko", "mo", "go", "to"]
    diskTotal = 0
    diskfree = 0
    diskInfo = {}
    readdisk = []
    writedisk = []
    device = ""
    diskUsedPrint = ""
    diskFreePrint = ""
    ligne = ""
    unite_w_r = ""
    unit_convert = 0
    adjust = ""
    ponder = ""
    list_last_values_read = deque
    list_last_values_write = deque

    def __init__(self, mount_po, unite_convert, pond, lignes='1ligne', afficherUsed='afficherused',
                 ligneFree='afficherLigneFree', disbar='',
                 diskframe='', disklabe=None, disklabelfree='',
                 diskcanevas='', disk_label_read=None, disk_label_write='', devisse='', endcolorgree=65,
                 endcolororan=85, unit_w_r='auto', adjuste=0):
        self.mountpoint = mount_po
        self.diskBar = disbar
        self.diskFram = diskframe
        self.diskLabelFree = disklabelfree
        self.diskabel = disklabe
        self.diskCaneva = diskcanevas
        self.endColorGreen = endcolorgree
        self.endColorOrange = endcolororan
        self.diskLabRead = disk_label_read
        self.diskLabWrite = disk_label_write
        self.diskinfo = ConvertBit()
        self.diskfree = 0
        self.readDiskPrecedent = 0
        self.writeDiskPrecedent = 0
        self.device = devisse
        self.diskUsedPrint = afficherUsed
        self.diskFreePrint = ligneFree
        self.ligne = lignes
        self.unite_w_r = unit_w_r
        self.unit_convert = unite_convert
        self.adjust = adjuste
        self.ponder = pond
        self.list_last_values_read = deque([])
        self.list_last_values_write = deque([])

                                                     "(erreur peu importante)")

