import psutil
import configparser
from pathlib import Path
from psutil import cpu_count
from modele import m_access_to_settings
import platform


def Verif_file_ini_to_start(nbr_cores, liste_part):
    os_actual = platform.system()
    verifier_theme_file()
    parser_theme = m_access_to_settings.accessToSettings('theme.ini')
    theme = parser_theme.get('theme', 'theme_actuel')

    verifier_settings_file(theme, os_actual)
    verifier_font_file_cpu(nbr_cores, theme)
    verif_font_file_disks(liste_part, theme)
    verif_font_file_network(theme)
    verif_colors_file(theme)
    verif_colors_font(theme)
    verif_reliefs_file(theme)
    verif_liaisons_file(theme)

def verifier_theme_file():
    directory = Path(__file__).parent.parent
    parser = configparser.ConfigParser()
    parser.read(str(directory) + '/theme.ini')
    black_list, can_i_write = parser_get_or_set(parser, 'theme', 'theme_actuel', 'Defaut', directory)
    if can_i_write:
        with open(str(directory) + '/theme.ini', 'w') as f:
            parser.write(f)


def verifier_settings_file(theme, os_actual):
    disk_partitions = psutil.disk_partitions()
    can_i_write = False
    if theme:
        directory = Path(__file__).parent.parent
        if os_actual == 'Windows':
            directory = str(directory) + '\\Themes\\' + theme + '\\'
        else:
            directory = str(directory) + '/Themes/' + theme + '/'
    parser = configparser.ConfigParser()
    parser.read(str(directory) + 'settings.ini')
    position_root_start, can_i_write = parser_get_or_set(parser, 'start', 'root_position', '+200+200')
    forget, can_i_write = parser_get_or_set(parser, 'disk', 'to_forget', 'void')
    black_list, can_i_write = parser_get_or_set(parser, 'disk', 'blacklist', ' ')
    for dis in disk_partitions:
        if os_actual == 'Windows':
            mtp = dis.mountpoint.lower()
        else:
            mtp = dis.mountpoint
        afficher_device_settings, can_i_write = parser_get_or_set(parser, 'disk_reglages', mtp,
                                                                  'devicemountp=>1ligne=>afficherused=>'
                                                                  'afficherLigneFree=>auto=>0=>1')
    tout, can_i_write = parser_get_or_set(parser, 'disk_reglages', 'settings_all', 'devicemountp=>1ligne=>afficherused=>'
                                                                                   'afficherLigneFree=>auto=>0=>1')
    update, can_i_write = parser_get_or_set(parser, 'disk_reglages', 'update', 'False')
    afficher_gen, can_i_write = parser_get_or_set(parser, 'disk_reglages', 'afficher_general', 'True')
    adjust_used, can_i_write = parser_get_or_set(parser, 'disk_reglages', 'adjust_used', '0')
    zone_1_max, can_i_write = parser_get_or_set(parser, 'disk_reglages', 'zone_1_max', '60')
    zone_2_max, can_i_write = parser_get_or_set(parser, 'disk_reglages', 'zone_2_max', '80')
    color1, can_i_write = parser_get_or_set(parser, 'disk_reglages', 'color1', 'green')
    color2, can_i_write = parser_get_or_set(parser, 'disk_reglages', 'color2', 'orange')
    color3, can_i_write = parser_get_or_set(parser, 'disk_reglages', 'color3', 'red')
    nbr_disk, can_i_write = parser_get_or_set(parser, 'disk_reglages', 'nbr_disk_a_afficher', '4')
    conv, can_i_write = parser_get_or_set(parser, 'disk_reglages', 'converter', '1024')
    conv, can_i_write = parser_get_or_set(parser, 'disk_reglages', 'font_update', 'False')

    aff_widg, can_i_write = parser_get_or_set(parser, 'network_reglages', 'afficher_widget', 'True')
    forget, can_i_write = parser_get_or_set(parser, 'network_reglages', 'unite_up_down', 'auto')
    forget, can_i_write = parser_get_or_set(parser, 'network_reglages', 'axe_y', 'auto')
    forget, can_i_write = parser_get_or_set(parser, 'network_reglages', 'axe_x', '60')
    val, can_i_write = parser_get_or_set(parser, 'network_reglages', 'update', 'False')
    val, can_i_write = parser_get_or_set(parser, 'network_reglages', 'afficher_debit', 'True')
    val, can_i_write = parser_get_or_set(parser, 'network_reglages', 'afficher_graph', 'True')
    val, can_i_write = parser_get_or_set(parser, 'network_reglages', 'afficher_net_inf', 'True')
    val, can_i_write = parser_get_or_set(parser, 'network_reglages', 'ponderation', '0')
    val, can_i_write = parser_get_or_set(parser, 'network_reglages', 'update_graph', 'False')
    val, can_i_write = parser_get_or_set(parser, 'network_reglages', 'font_update', 'False')

    load_cpu, can_i_write = parser_get_or_set(parser, 'cpu_reglages', 'afficher_load', 'True')
    load, can_i_write = parser_get_or_set(parser, 'cpu_reglages', 'afficher_freq', 'True')
    load, can_i_write = parser_get_or_set(parser, 'cpu_reglages', 'afficher_ram_go', 'True')
    load, can_i_write = parser_get_or_set(parser, 'cpu_reglages', 'aff_bar_ram', 'True')
    load, can_i_write = parser_get_or_set(parser, 'cpu_reglages', 'aff_pourc_ram', 'True')
    load, can_i_write = parser_get_or_set(parser, 'cpu_reglages', 'aff_bar_cores', 'True')
    load, can_i_write = parser_get_or_set(parser, 'cpu_reglages', 'aff_pourc_cores', 'True')
    load, can_i_write = parser_get_or_set(parser, 'cpu_reglages', 'degres_cpu', 'celsius')
    load, can_i_write = parser_get_or_set(parser, 'cpu_reglages', 'tj_max', 'auto')
    load, can_i_write = parser_get_or_set(parser, 'cpu_reglages', 'update', 'False')
    load, can_i_write = parser_get_or_set(parser, 'cpu_reglages', 'font_update', 'False')

    z, can_i_write = parser_get_or_set(parser, 'app_settings', 'update', 'False')
    z, can_i_write = parser_get_or_set(parser, 'app_settings', 'start', 'nothing')
    z, can_i_write = parser_get_or_set(parser, 'app_settings', 'monitor', 'not_set')
    z, can_i_write = parser_get_or_set(parser, 'app_settings', 'zoom', '100')
    z, can_i_write = parser_get_or_set(parser, 'app_settings', 'font_update', 'False')
    z, can_i_write = parser_get_or_set(parser, 'app_settings', 'zoom_need_update', 'False')
    if can_i_write:
        with open(str(directory) + 'settings.ini', 'w') as f:
            parser.write(f)

def verifier_font_file_cpu(nbr_cores, theme):
    directory = Path(__file__).parent.parent
    directory = str(directory) + '/Themes/' + theme + '/'
    can_i_write = False
    parser_font_cpu = configparser.ConfigParser()
    parser_font_cpu.read(str(directory) + 'font.ini')
    cpu_inf, can_i_write = parser_get_or_set(parser_font_cpu, 'Cpu', 'cpu_infos', 'Arial')
    cpu_load, can_i_write = parser_get_or_set(parser_font_cpu, 'Cpu', 'cpu_load', 'Arial')
    cpu_freq, can_i_write = parser_get_or_set(parser_font_cpu, 'Cpu', 'cpu_freq', 'Arial')
    ram_go, can_i_write = parser_get_or_set(parser_font_cpu, 'Cpu', 'ram_go', 'Arial')
    i = 0
    while i < nbr_cores + 1:
        core_name = 'oups!!'
        if i == 0:
            core_name = 'ram'
        else:
            core_name = 'core' + str(i)
        core, can_i_write = parser_get_or_set(parser_font_cpu, 'Cpu', core_name, 'Arial')
        i += 1
    temp, can_i_write = parser_get_or_set(parser_font_cpu, 'Cpu', 'temp', 'Arial')
    if can_i_write:
        with open(str(directory) + 'font.ini', 'w') as f:
            parser_font_cpu.write(f)


def verif_font_file_disks(liste_part, theme):
    directory = Path(__file__).parent.parent
    directory = str(directory) + '/Themes/' + theme + '/'
    can_i_write = False
    parser_font_disk = configparser.ConfigParser()
    parser_font_disk.read(str(directory) + 'font.ini')
    dernier_choix, can_i_write = parser_get_or_set(parser_font_disk, 'disk_font', 'dernier_choix', 'nothing')
    disk_infos, can_i_write = parser_get_or_set(parser_font_disk, 'disk_font', 'disk_infos', 'Arial')
    for mp in liste_part:
        mount_p, can_i_write = parser_get_or_set(parser_font_disk, str(mp.mountpoint), 'nom_device', 'Arial')
        mount_p, can_i_write = parser_get_or_set(parser_font_disk, str(mp.mountpoint), 'mount_point', 'Arial')
        mount_p, can_i_write = parser_get_or_set(parser_font_disk, str(mp.mountpoint), 'used_et_total', 'Arial')
        mount_p, can_i_write = parser_get_or_set(parser_font_disk, str(mp.mountpoint), 'free', 'Arial')
        mount_p, can_i_write = parser_get_or_set(parser_font_disk, str(mp.mountpoint), 'font_read', 'Arial')
        mount_p, can_i_write = parser_get_or_set(parser_font_disk, str(mp.mountpoint), 'font_write', 'Arial')
    font_touts, can_i_write = parser_get_or_set(parser_font_disk, 'disk_font', 'toutes', 'Arial=>Arial=>Arial=>Arial=>'
                                                                                         'Arial=>Arial')
    if can_i_write:
        with open(str(directory) + 'font.ini', 'w') as f:
            parser_font_disk.write(f)


def verif_font_file_network(theme):
    directory = Path(__file__).parent.parent
    directory = str(directory) + '/Themes/' + theme + '/'
    parser_font_netw = configparser.ConfigParser()
    parser_font_netw.read(str(directory) + 'font.ini')
    netw_inf, can_i_write = parser_get_or_set(parser_font_netw, 'netw_font', 'netw_infos', 'Arial')
    netw_down, can_i_write = parser_get_or_set(parser_font_netw, 'netw_font', 'netw_down', 'Arial')
    netw_up, can_i_write = parser_get_or_set(parser_font_netw, 'netw_font', 'netw_up', 'Arial')
    if can_i_write:
        with open(str(directory) + 'font.ini', 'w') as f:
            parser_font_netw.write(f)


def verif_colors_file(theme):
    nbr_cpu = cpu_count()
    directory = Path(__file__).parent.parent
    directory = str(directory) + '/Themes/' + theme + '/'
    parser_color_file = configparser.ConfigParser()
    parser_color_file.read(str(directory) + 'colors.ini')

    cpu_principale, can_i_write = parser_get_or_set(parser_color_file, 'Cpu', 'principale', '#dc7712')
    bout_param, can_i_write = parser_get_or_set(parser_color_file, 'Cpu', 'bout_param', '#a9723e')
    cpu_ram, can_i_write = parser_get_or_set(parser_color_file, 'Cpu', 'Ram', '#ad6b2c')
    fond_ram, can_i_write = parser_get_or_set(parser_color_file, 'Cpu', 'fond_ram', '#caa480')

    last_choice, can_i_write = parser_get_or_set(parser_color_file, 'Last_choice', 'colors_disks', 'no_setted')
    disk_principal, can_i_write = parser_get_or_set(parser_color_file, 'Disks', 'principale', '#dc7712')
    memo, can_i_write = parser_get_or_set(parser_color_file, 'Memo', 'mountpoint', 'color_princ=>'
                                                                                   'color_fond=>color_bar_zone1=>'
                                                                                   'color_bar_zone2=>'
                                                                                   'color_bar_zone3'
                                                                                   'color_write=>color_read')
    toutes, can_i_write = parser_get_or_set(parser_color_file, 'Disks', 'toutes',
                                            '#ad733b=>#caa480=>#c6ec98=>#eed399=>#ef95b4=>#caa480=>#ceac8c')
    change_toutes, can_i_write = parser_get_or_set(parser_color_file, 'Disks', 'change_dans_applique_a_toutes', '0=>1=>2=>'
                                                                                                                '3=>4=>5'
                                                                                                                '=>6')
    i = 0
    while i < nbr_cpu:
        core, can_i_write = parser_get_or_set(parser_color_file, 'Cpu', 'Core' + str(i + 1), '#b47435')
        fond_core, can_i_write = parser_get_or_set(parser_color_file, 'Cpu', 'fond_core' + str(i + 1), '#ddad7e')
        i += 1

    all_fond_cores, can_i_write = parser_get_or_set(parser_color_file, 'Cpu', 'fond_all_cores', 'True')
    all_bare_cores, can_i_write = parser_get_or_set(parser_color_file, 'Cpu', 'bare_all_cores', 'True')
    color_all_cores, can_i_write = parser_get_or_set(parser_color_file, 'Cpu', 'color_all_cores', '#b47435')
    color_all_fonds, can_i_write = parser_get_or_set(parser_color_file, 'Cpu', 'color_all_fonds', '#ddad7e')

    color_netw_princ, can_i_write = parser_get_or_set(parser_color_file, 'Network', 'principale', '#dc7712')
    color_down, can_i_write = parser_get_or_set(parser_color_file, 'Network', 'coul_down', '#caa480')
    color_up, can_i_write = parser_get_or_set(parser_color_file, 'Network', 'coul_up', '#caa480')
    down_curve_color, can_i_write = parser_get_or_set(parser_color_file, 'Network', 'down_curve', '#e04e58')
    up_curve_color, can_i_write = parser_get_or_set(parser_color_file, 'Network', 'up_curve', '#6d44d7')
    contour_graph, can_i_write = parser_get_or_set(parser_color_file, 'Network', 'contour_graph', '#ad9986')
    fond_graph, can_i_write = parser_get_or_set(parser_color_file, 'Network', 'fond_graph', '#ddad70')
    axes_x_et_y, can_i_write = parser_get_or_set(parser_color_file, 'Network', 'axes_x_et_y', '#201a15')

    if can_i_write:
        with open(str(directory) + 'colors.ini', 'w') as f:
            parser_color_file.write(f)

def verif_colors_font(theme):
    nbr_cpu = cpu_count()
    directory = Path(__file__).parent.parent
    directory = str(directory) + '/Themes/' + theme + '/'
    can_i_write = False
    parser_color_font = configparser.ConfigParser()
    parser_color_font.read(str(directory) + 'color_font.ini')
    color_title, can_i_write = parser_get_or_set(parser_color_font, 'cpu', 'title', '#211308', directory)
    color_cpu_load, can_i_write = parser_get_or_set(parser_color_font, 'cpu', 'cpu_load', '#211308', directory)
    color_cpu_freq, can_i_write = parser_get_or_set(parser_color_font, 'cpu', 'cpu_freq', '#211308', directory)
    color_ram, can_i_write = parser_get_or_set(parser_color_font, 'cpu', 'ram', '#211308', directory)
    color_all_cores, can_i_write = parser_get_or_set(parser_color_font, 'cpu', 'color_all_cores', 'True')
    color_all, can_i_write = parser_get_or_set(parser_color_font, 'cpu', 'color_all', '#211308')
    percent_ram, can_i_write = parser_get_or_set(parser_color_font, 'cpu', 'percent_ram', '#211308', directory)
    change_dans_appliquer_a_toutes, can_i_write = parser_get_or_set(parser_color_font,
                                                                    'Disks', 'change_dans_applique_a_toutes',
                                                                    '0=>1=>2=>3=>4=>5')
    toutes, can_i_write = parser_get_or_set(parser_color_font, 'disk', 'toutes',
                                            '#211308=>#211308=>#211308=>#211308=>#211308=>#211308=>#211308')
    i = 1
    color_core = []
    while i <= nbr_cpu:
        color_core.append('core_' + str(i))
        color_core[i - 1], can_i_write = parser_get_or_set(parser_color_font, 'cpu', 'core_' + str(i), '#211308',
                                                       directory)
        i += 1
    color_temp, can_i_write = parser_get_or_set(parser_color_font, 'cpu', 'temp', '#211308', directory)

    disk_title, can_i_write = parser_get_or_set(parser_color_font, 'disk', 'title', '#211308')

    netw_font_title, can_i_write = parser_get_or_set(parser_color_font, 'Network_font', 'title', '#211308')
    netw_font_down, can_i_write = parser_get_or_set(parser_color_font, 'Network_font', 'down', '#211308')
    netw_font_up, can_i_write = parser_get_or_set(parser_color_font, 'Network_font', 'up', '#211308')

    if can_i_write:
        with open(str(directory) + 'color_font.ini', 'w') as f:
            parser_color_font.write(f)


def verif_reliefs_file(theme):
    directory = Path(__file__).parent.parent
    directory = str(directory) + '/Themes/' + theme + '/'
    can_i_write = False
    parser_reliefs = configparser.ConfigParser()
    parser_reliefs.read(str(directory) + 'reliefs.ini')
    relief_widg_cpu, can_i_write = parser_get_or_set(parser_reliefs, 'cpu', 'widg', 'raised')
    relief_ram, can_i_write = parser_get_or_set(parser_reliefs, 'cpu', 'ram', 'sunken')
    relief_cores, can_i_write = parser_get_or_set(parser_reliefs, 'cpu', 'cores', 'raised')

    relief_widg_disk, can_i_write = parser_get_or_set(parser_reliefs, 'disks', 'widg', 'raised')
    relief_partitions, can_i_write = parser_get_or_set(parser_reliefs, 'disks', 'partition', 'raised')
    relief_barre, can_i_write = parser_get_or_set(parser_reliefs, 'disks', 'barre', 'sunken')
    relief_write, can_i_write = parser_get_or_set(parser_reliefs, 'disks', 'write', 'groove')
    relief_read, can_i_write = parser_get_or_set(parser_reliefs, 'disks', 'read', 'groove')

    relief_widg_netw, can_i_write = parser_get_or_set(parser_reliefs, 'netw', 'widg', 'raised')
    relief_netw_graph, can_i_write = parser_get_or_set(parser_reliefs, 'netw', 'graph', 'ridge')
    relief_netw_down, can_i_write = parser_get_or_set(parser_reliefs, 'netw', 'down', 'groove')
    relief_netw_up, can_i_write = parser_get_or_set(parser_reliefs, 'netw', 'up', 'groove')

    if can_i_write:
        with open(str(directory) + 'reliefs.ini', 'w') as f:
            parser_reliefs.write(f)

def verif_liaisons_file(theme):
    directory = Path(__file__).parent.parent
    directory = str(directory) + '/Themes/' + theme + '/'
    can_i_write = False
    parser_liaisons = configparser.ConfigParser()
    parser_liaisons.read(str(directory) + 'liaisons.ini')
    liaisons_liste, can_i_write = parser_get_or_set(parser_liaisons, 'liaisons', 'liste', '')
    if can_i_write:
        with open(str(directory) + 'liaisons.ini', 'w') as f:
            parser_liaisons.write(f)


def parser_get_or_set(parser, section, option=None, defaut_value=None, directory=None):
    try:
        if option.__contains__('\\'):
            option = option[:1]
        value = parser.get(str(section), str(option))
        return value, True
    except configparser.NoOptionError:
        if defaut_value:
            if option.__contains__('\\'):
                option = option[:1]
            parser.set(str(section), str(option), str(defaut_value))
            return defaut_value, True
        else:
            if option.__contains__('\\'):
                option = option[:1]
            parser.set(str(section), str(option))
            return True, True
    except configparser.NoSectionError:
        parser.add_section(str(section))
        if option.__contains__('\\'):
            option = option[:1]
        parser.set(str(section), str(option), str(defaut_value))
        return True, True
