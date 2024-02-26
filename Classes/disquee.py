import tkinter
from psutil import disk_io_counters
from collections import deque
import controleur.c_convert_bit as convert
import modele.m_access_to_settings as getter

class UnDisque:

    def __int__(self):
        self.mountpoint = str
        self.conv = str
        self.pond = str
        self.lignes = str
        self.afficher_used = str
        self.ligne_free = str
        self.disbar = None
        self.diskframe = tkinter.Frame
        self.disklabe = tkinter.Label
        self.disklabelfree = tkinter.Label
        self.unit_w_r = str
        self.adjuste = str
        self.diskcanevas = tkinter.Canvas
        self.disk_label_read = tkinter.Label
        self.disk_label_write = tkinter.Label
        self.devisse = str

    def creer_disque(self, mountpoint, conv, diskcanevas=None, disk_laber_read=None, disk_label_write=None,
                     disbar=None, diskframe=None, disklabe=None, disklabelfree=None, devisse=None, pond='0',
                     lignes='1Lignes', afficher_used='afficherused', ligne_free='afficherLigneFree',
                     unit_w_r='auto', adjuste=0):
        self.mountpoint = mountpoint
        self.conv = conv
        self.pond = pond
        self.lignes = lignes
        self.afficher_used = afficher_used
        self.ligne_free = ligne_free
        self.disbar = disbar
        self.diskframe = diskframe
        self.disklabe = disklabe
        self.disklabelfree = disklabelfree
        self.unit_w_r = unit_w_r
        self.adjuste = adjuste
        self.diskcanevas = diskcanevas
        self.disk_label_read = disk_laber_read
        self.disk_label_write = disk_label_write
        self.device = devisse
        self.readDiskPrecedent = 0
        self.writeDiskPrecedent = 0
        self.ponder = pond
        self.diskLabRead = disk_laber_read
        self.diskLabWrite = disk_label_write
        self.diskinfo = convert.ConvertBit()
        self.list_last_values_read = deque([])
        self.list_last_values_write = deque([])
        conv = getter.accessToSettings('settings.ini').get('disk_reglages', 'converter')
        self.unit_convert = int(conv)
        self.liaison = ''

    def read_write_disk(self, unite='auto'):
        readdisko = 0.0
        writedisko = 0.0
        octet = ''
        unite = self.unit_w_r
        if unite == 'auto':
            octet = 'o'
        else:
            octet = unite
        diskcount = disk_io_counters(perdisk=True)
        try:
            if self.liaison == '':
                gette = getter.accessToSettings('liaisons.ini')
                liste_liaison = gette.get('liaisons', 'liste').split('==>')
                for items in liste_liaison:
                    if items == '':
                        continue
                    couple = items.split('=>')
                    if couple[1] == self.device:
                        self.liaison = couple[0]
                        break
            if self.liaison != '':
                readdisktotal = diskcount[self.liaison].read_bytes
            else:
                readdisktotal = diskcount[self.device[5:]].read_bytes
        except KeyError:
            return 'Key_Error'
        if self.readDiskPrecedent > 0:
            readdisko = readdisktotal - self.readDiskPrecedent
        else:
            readdisko = 0
        self.list_last_values_read.append(readdisko)
        result = 0
        if len(self.list_last_values_read) > int(self.ponder):
            self.list_last_values_read.popleft()

            i = 1
            somme = 0
            divisor = 0
            while i <= int(self.ponder):
                somme += self.list_last_values_read[i - 1] * i
                divisor += i
                i += 1
            result = somme / divisor
        self.readdisk = self.diskinfo.convert_bit_to_go(result, self.unit_convert, unite)
        self.readDiskPrecedent = readdisktotal
        if self.diskLabRead is not None:
            self.diskLabRead.configure(text='R: {:.2f}'.format(self.readdisk[0]) + ' ' +
                                            str(self.readdisk[1]) + '/s')

        if self.liaison == '':
            writedisktotal = diskcount[self.device[5:]].write_bytes
        else:
            writedisktotal = diskcount[self.liaison].write_bytes
        if self.writeDiskPrecedent > 0:
            writedisko = writedisktotal - self.writeDiskPrecedent
        else:
            writedisko = 0
        self.list_last_values_write.append(writedisko)
        result = 0
        if len(self.list_last_values_write) > int(self.ponder):
            self.list_last_values_write.popleft()

            i = 1
            somme = 0
            divisor = 0
            while i <= int(self.ponder):
                somme += self.list_last_values_write[i - 1] * i
                divisor += i
                i += 1
            result = somme / divisor
        self.writedisk = self.diskinfo.convert_bit_to_go(result, self.unit_convert, unite)
        self.writeDiskPrecedent = writedisktotal
        if self.diskLabWrite is not None:
            self.diskLabWrite.configure(text='W: {:.2f}'.format(self.writedisk[0]) + ' ' +
                                             str(self.writedisk[1]) + '/s')