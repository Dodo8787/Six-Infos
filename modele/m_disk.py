import configparser

from modele import m_access_to_settings as acces

class MDisk:

    def __init__(self):
        self.accesseur = acces.accessToSettings('settings.ini')
        self.conv = self.get_conv()
        self.liste_path_to_forget = self.get_list_path_to_forget()
        self.afficher_disk_widget = self.get_afficher_widg_disk()

    def get_list_path_to_forget(self):
        self.liste_path_to_forget = self.accesseur.get('disk', 'to_forget').split('=>')
        return self.liste_path_to_forget

    def get_conv(self):
        try:
            self.conv = int(self.accesseur.get('disk_reglages', 'converter'))
        except configparser.NoOptionError:
            self.conv = 1024
        return self.conv

    def get_afficher_widg_disk(self):
        return self.accesseur.get('disk_reglages', 'afficher_general')

    def lire_et_actualiser_part_to_forget(self):
        lis = []
        liste_dev = []

        conv = self.get_conv()
        strinn = str(self.accesseur.get('disk', 'to_forget'))
        if len(strinn) > 0:
            lis = strinn.split('=>')
        for li in lis:
            dev = Disque(mount_po=li, unite_convert=conv, pond=1, lignes="", afficherUsed='', ligneFree="")
            liste_dev.append(dev)
        return liste_dev