import tkinter
from tkinter import ttk
from psutil import disk_io_counters
from configparser import ConfigParser
from pathlib import Path

class MappingDisk:

    def __init__(self, disk_part):
        self.fen_map_is_open = True
        self.fen_map = tkinter.Toplevel()
        self.fen_map.title('Parametres')
        self.fen_map.protocol("WM_DELETE_WINDOW", self.on_closing_fen_map)
        self.mp = []
        for disk in disk_part:
            self.mp.append(disk.mountpoint)
        self.dis = {}
        self.dis = disk_io_counters(perdisk=True)
        self.disk = []
        for di, rr in self.dis.items():
            self.disk.append(di)

        self.stop()
    def on_closing_fen_map(self):
        pass

    def stop(self):
        print(self.mp)
        print("__")
        print(self.disk)


