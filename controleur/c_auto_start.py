from os import path as osPath
from pathlib import Path


def ajouter_ou_enlever_demarrage_auto(action):
    directory = Path(__file__).parent
    user = osPath.expanduser('~')
    path = user + '/.config/autostart'
    file_start = Path(path + '/Six-Infos.desktop')
    if file_start.is_file() and action == 'ajouter':
        return True
    elif file_start.is_file() and action == 'retirer':
        try:
            os.remove(file_start)
            return True
        except OSError:
            print('erreur lors de la suppression du fichier .config/Six-Infos.desktop (autostart)')
            return False
    elif not file_start.is_file() and action == 'ajouter':
        ff = open(file_start, 'w')
        ff.write('[Desktop Entry]\nExec=' + str(directory) + '/main.py\nName=Six-Infos\n')
        ff.write('Terminal=False\n')
        ff.write('Type=Application')
        ff.close()
        return True
    elif not file_start.is_file() and action == 'retirer':
        return True
