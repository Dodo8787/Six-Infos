class Disque:
    def __int__(self, mountpoint, conv, diskcanevas, disk_laber_read, disk_label_write, disbar, diskframe,
                disklabe, disklabelfree, devisse, pond='0', lignes='1Lignes', afficher_used='afficherused',
                ligne_free='afficherLigneFree', unit_w_r='auto', adjuste=0):
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
        self.devisse = devisse
        pass
