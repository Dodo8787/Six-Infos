#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import platform
import tkinter
from tkinter import ttk

import psutil
from ttkthemes import ThemedTk

os_actual = platform.system()
from psutil import cpu_percent, cpu_freq, virtual_memory, disk_partitions, cpu_count
if os_actual == 'Linux':
    from psutil import sensors_temperatures
else:
    os.system('diskperf -y')
from collections import deque
from pathlib import Path
from controleur.c_convert_bit import ConvertBit
from controleur.column_setter import ColumnSetter
import modele.m_access_to_settings as get_to_settings
import controleur.starting_verif as starting_verif
import controleur.generals_actions as generals_actions
import controleur.c_cpu as c_cpu
import controleur.c_disk as c_disk
import controleur.c_network as c_network

print("Six-Infos is running...")


cpufreq = cpu_freq()
ram1 = virtual_memory()
cpulist = cpu_percent(0, percpu=True)
nbrCpuCore = len(cpulist)
ramTotal = ram1.total
criticalcoretemp = 0
bitsunite = ('o', 'ko', 'mo', 'go', 'to')
bitsdivisor = 0
liste_disques = []
disk = psutil.disk_usage('/')
diskupdate = 0
caneva = None
plot1 = None
pass1 = True
refresh_after_id = None
diskBar = {}
readDiskPrecedent = 0
writeDiskPrecedent = 0
networkData = []
count = 0
queueNetworkSend = deque([])
queueNetworkRecv = deque([])
on_sec_send_converted = []
on_sec_recev_converted = []
on_sec_send = 0
on_sec_recv = 0
listesecReverse = []

fenetre_param_open = False
set_main_pos = False
start_x = 0
start_y = 0
liste_disques_affiches = []
part_to_forget = []
listepathtoforg = []
fen_param_isopen = False
posx = 0
posy = 0
previewposx = 0
previewposy = 0
actualiser_affichage_disques = False
preview_mp_to_forget = []
nbr_part_a_afficher = 4
limit_x = 60
lim_y = 'auto'
unit = 'auto'
unit_graph = ''
converter = ConvertBit
aff_graph = bool
aff_debit_netw = bool
affich_gen_disk = bool
ponder = 0
pond_up_divised = 0
pond_down_divised = 0
pond_up = deque
pond_down = deque
degres_cpu = 'celsius'
networkFrameUngrided = False
liste_dev = []




count = 0


def do_i_affiche_disk():
    geter_disk = get_to_settings.accessToSettings('settings.ini')
    return geter_disk.get('disk_reglages', 'afficher_general')

def do_i_affiche_network():
    geter_netw = get_to_settings.accessToSettings('settings.ini')
    return geter_netw.get('network_reglages', 'afficher_widget')

def delete_all_frames_disk(disk_widg):
    try:
        disk_widg.diskframegeneral.destroy()
        disk_widg.diskframegeneral2.destroy()
        disk_widg.diskframegeneral3.destroy()
        disk_widg.diskframegeneral4.destroy()
    except TypeError:
        pass
    except AttributeError:
        pass


def destroy_net_widg():
    netw_widg.network_frame.destroy()


def definir_col_netw_false_columnsetter(disk_frame_gen, disk_frame_gen2, disk_frame_gen3, disk_frame_gen4,
                                        cpu_last_col):
    if disk_frame_gen4 is not None:
        return 5
    if disk_frame_gen3 is not None:
        return 4
    if disk_frame_gen2 is not None:
        return 3
    if disk_frame_gen is not None:
        return 2
    else:
        return cpu_last_col + 1


def creer_fen_couleurs():
    ij = 0
    while ij <= 20:
        print(str(ij) + " sec")
        ij += 1
    print("loop completed")


def get_windows_pos(rot, base_x, base_y):
    root_x = rot.winfo_x()
    root_y = rot.winfo_y()
    return root_x, root_y


def refresh():
    global count
    global liste_disk_afficher
    global preview_part_add_new
    global disk_fram_gen
    global disk_fram_gen2
    global disk_fram_gen3
    global disk_fram_gen4
    global col_gen_disk
    global row_gen_disk
    global col_network
    global row_network
    global cpu_widg
    global disk_widg
    global netw_widg
    global is_aff_disk
    global frame_network
    global frame_root
    global root
    global general
    global is_aff_netw
    global zoom_ratio
    global app_first_pass
    global font_update
    global update_objet
    global app_updt

    col_setter = ColumnSetter(root)
    geter_updt = get_to_settings.accessToSettings('settings.ini')
    update = general.verif_update('update')
    zoom_need_update = geter_updt.get('app_settings', 'zoom_need_update')
    if app_first_pass or zoom_need_update == 'True' or 'app' in update:
        geter_updt.set('app_settings', 'zoom_need_update', 'False')
        geter_updt.set('app_settings', 'font_update', 'False')

        gener = generals_actions.General()
        update_objet.append('cpu')
        geter_updt2 = get_to_settings.accessToSettings('settings.ini')
        geter_updt2.set('app_settings', 'update', 'False')
        zoom_ratio = gener.get_zoom_ratio()

        frame_root.destroy()
        frame_root = ttk.Frame(root)
        frame_root.grid()
        cpu_widg = c_cpu.ControlerCpu(zoom_ratio, frame_root, root)
        col_gen_disk, row_gen_disk = cpu_widg.afficher_cpu()
        cpu_widg.update_font()
        cpu_widg.update_font_color()
        cpu_widg.update_style()
        get_updt_cpu = get_to_settings.accessToSettings('settings.ini')
        get_updt_cpu.set('cpu_reglages', 'update', 'False')

        if do_i_affiche_disk() == 'True':
            try:
                netw_widg.network_frame.destroy()
            except NameError:
                pass
            try:
                delete_all_frames_disk(disk_widg)
            except:
                pass
            disk_widg = c_disk.CDisk(frame_root, root)
            liste_disk_afficher, col_network, row_network, frame_network, disk_fram_gen, disk_fram_gen2, \
                disk_fram_gen3, disk_fram_gen4, liste_disques = disk_widg.afficher_disks(frame_root,
                                                                                         col_gen_disk,
                                                                                         row_gen_disk,
                                                                                         zoom_ratio)
            liste_disk_afficher = liste_disk_afficher
            disk_widg.update_style()
            is_aff_disk = True
        else:
            try:
                delete_all_frames_disk(disk_widg)
            except NameError:
                pass
            is_aff_disk = False
            liste_disk_afficher = []
        geter_updt_disk = get_to_settings.accessToSettings('settings.ini')
        geter_updt_disk.set('disk_reglages', 'update', 'False')

        get_netw_upd = get_to_settings.accessToSettings('settings.ini')
        aff_graph = str(get_netw_upd.get('network_reglages', 'afficher_graph'))
        if aff_graph == 'True':
            aff_graph = True
        else:
            aff_graph = False
        if do_i_affiche_network() == 'True':
            try:
                netw_widg.network_frame.destroy()
            except NameError:
                pass

            if is_aff_disk:
                netw_widg = c_network.CNetwork(frame_network, root)
                netw_widg.creer_ou_refresh_ou_update_widg_network(1, row_network, pass1=True,
                                                                  aff_graph=aff_graph)
                root.update()
                if not col_setter.valide_height(frame_root.winfo_height()):
                    destroy_net_widg()
                    netw_widg = c_network.CNetwork(frame_root, root)
                    col_network = definir_col_netw_false_columnsetter(disk_fram_gen, disk_fram_gen2,
                                                                      disk_fram_gen3, disk_fram_gen4, 4)
                    row_network = 1
                    netw_widg.creer_ou_refresh_ou_update_widg_network(col_network, row_network, pass1=True,
                                                                      aff_graph=aff_graph)
                is_aff_netw = True
            else:
                netw_widg = c_network.CNetwork(frame_root, root)
                netw_widg.creer_ou_refresh_ou_update_widg_network(col_gen_disk, row_gen_disk, pass1=True,
                                                                  aff_graph=aff_graph)
                if not col_setter.valide_height(frame_root.winfo_height()):
                    destroy_net_widg()
                    netw_widg = c_network.CNetwork(frame_root, root)
                    new_col_netw = col_gen_disk + 1
                    netw_widg.creer_ou_refresh_ou_update_widg_network(new_col_netw, 1, pass1=True, aff_graph=aff_graph)

                is_aff_netw = True
            netw_widg.update_style_graph()
        else:
            try:
                netw_widg.network_frame.destroy()
            except NameError:
                pass
            is_aff_netw = False
        get_tt = get_to_settings.accessToSettings('settings.ini')
        get_tt.set('network_reglages', 'update', 'False')
    update_objet = []

    cpu_widg.refresh_cpu()
    if is_aff_disk:
        for disk in liste_disk_afficher:
            try:
                disk.read_write_disk()
            except AttributeError:
                pass

    get_netw_refresh = get_to_settings.accessToSettings('settings.ini')
    aff_graph2 = str(get_netw_refresh.get('network_reglages', 'afficher_graph'))
    if aff_graph2 == 'True':
        aff_graph2 = True
    else:
        aff_graph2 = False
    if is_aff_disk and is_aff_netw:
        netw_widg.creer_ou_refresh_ou_update_widg_network(col_network, row_network, False, aff_graph2,
                                                          just_refresh=True)
        if not col_setter.valide_height(frame_root.winfo_height()):
            destroy_net_widg()
            netw_widg = c_network.CNetwork(frame_root, root)
            new_col_netw = col_network + 1
            netw_widg.creer_ou_refresh_ou_update_widg_network(new_col_netw, 1, pass1=True,
                                                              aff_graph=aff_graph2, just_refresh=True)
    elif is_aff_netw:
        netw_widg.creer_ou_refresh_ou_update_widg_network(col_gen_disk, row_gen_disk, False, aff_graph2,
                                                          just_refresh=True)
        if not col_setter.valide_height(frame_root.winfo_height()):
            destroy_net_widg()
            netw_widg = c_network.CNetwork(frame_root, root)
            new_col_gen_disk = col_gen_disk + 1
            netw_widg.creer_ou_refresh_ou_update_widg_network(new_col_gen_disk, row_gen_disk, pass1=True,
                                                              aff_graph=aff_graph2, just_refresh=True)
    count += 1
    if count >= 3:
        general.verif_root_position(root)
        if is_aff_disk:
            add_new = disk_widg.verif_if_add_new_disk(preview_part_add_new, disk_partitions(), col_network, row_network)
            if add_new:
                liste_disk_afficher = disk_partitions()
                preview_part_add_new = liste_disk_afficher
                set_add_new = get_to_settings.accessToSettings('settings.ini')
                set_add_new.set('app_settings', 'update', 'True')
            for diskk in liste_disk_afficher:
                try:
                    if diskk.mountpoint.__contains__('\\'):
                        diskk.mountpoint = diskk.mountpoint[:1]
                    disk_widg.refresh_disk(zoom_ratio, diskk)
                except AttributeError:  # partiton n est plus existante
                    pass
        count = 0
    refresh_after_id = frame_root.after(1000, refresh)
    app_first_pass = False

app_first_pass = True
update_objet = []
font_update = []
app_updt = False
preview_part_add_new = disk_partitions()

# verif file ini to start
nbr_core = cpu_count()
starting_verif.Verif_file_ini_to_start(nbr_core, preview_part_add_new)
# obtenir nom du theme
getter = get_to_settings.accessToSettings('theme.ini')
general = generals_actions.General()
theme = getter.get('theme', 'theme_actuel')
# creer fenetre
root = ThemedTk()
root.geometry(getter.get('start', 'root_position'))
root.title('Six-Infos')
# creer frame root
frame_root = ttk.Frame(root)
frame_root.grid()
pos_y = root.winfo_y()
col_setter = ColumnSetter(root)
# get zoom ratio
zoom_ratio = general.get_zoom_ratio()

labName = {}
labTemp = {}
canvasName = {}
coreBarName = {}
barSize = {}
diskBar = {}

i = 0
col_x = 0
adj_row = 5
already = False
passe = 1
lastwidget = 0

refresh()

directory = Path(__file__).parent
p1 = tkinter.PhotoImage(file=str(directory) + '/Images/icone.png')
root.iconphoto(False, p1)

def on_closing_main_window():
    general.on_closing_main_window(frame_root, refresh_after_id, root)

root.protocol("WM_DELETE_WINDOW", on_closing_main_window)

root.mainloop()
