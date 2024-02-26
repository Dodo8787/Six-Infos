from modele import m_access_to_settings as getter
from controleur import c_fenetre_param
from controleur import column_setter
from tkinter import ttk
import tkinter
from pathlib import Path
from psutil import cpu_freq, cpu_count
import platform


class AfficheurCpu:

    def __init__(self, critical_cpu_temp, root):
        self.zoom_ratio = 0
        self.cpu_frame = ttk.Frame
        self.img_param = tkinter.BitmapImage
        self.directory = Path(__file__).parent.parent
        self.bout_Param = ttk.Button
        self.nbr_cpu_cores = cpu_count()
        self.label_title_cpu = ttk.Label
        self.label_cpu_load = ttk.Label
        self.label_freq_cpu = ttk.Label
        self.label_ram = ttk.Label
        self.list_bar_size = []
        self.list_lab_name = []
        self.list_canvas_name = []
        self.list_core_bar_name = []
        self.actual_os = platform.system()
        j = 0
        while j < self.nbr_cpu_cores + 1:
            self.list_bar_size.append(tkinter.IntVar)
            self.list_lab_name.append(ttk.Label)
            self.list_canvas_name.append(tkinter.Canvas)
            j += 1
        self.core_temp_lab = ttk.Label
        self.critical_cpu_temp = critical_cpu_temp
        self.list_disk_afficher = []
        self.root = root
        self.possibles_part = []
        self.col_disk = 1
        self.row_disk = 1
        geter_updt = getter.accessToSettings('settings.ini')
        self.aff_load_cpu = geter_updt.get('cpu_reglages', 'afficher_load')
        self.aff_freq = geter_updt.get('cpu_reglages', 'afficher_freq')
        self.aff_ram_go = geter_updt.get('cpu_reglages', 'afficher_ram_go')
        self.aff_bar_ram = geter_updt.get('cpu_reglages', 'aff_bar_ram')
        self.aff_pourc_ram = geter_updt.get('cpu_reglages', 'aff_pourc_ram')
        self.aff_bar_cores = geter_updt.get('cpu_reglages', 'aff_bar_cores')
        self.aff_pourc_cores = geter_updt.get('cpu_reglages', 'aff_pourc_cores')
        self.geter_color = getter.accessToSettings('colors.ini')
        self.bg_principale = str(self.geter_color.get('Cpu', 'principale'))
        self.bg_bout_param = str(self.geter_color.get('Cpu', 'bout_param'))
        self.bg_barre_ram = str(self.geter_color.get('Cpu', 'ram'))
        self.bg_fond_ram = str(self.geter_color.get('Cpu', 'fond_ram'))
        self.bg_barre_core = []
        self.bg_fond_core = []
        self.fen_param = None
        all_core_colors = self.geter_color.get('Cpu', 'bare_all_cores')
        all_fond_colors = self.geter_color.get('Cpu', 'fond_all_cores')
        for cpu in range(cpu_count()):
            if all_core_colors == 'True':
                self.bg_barre_core.append(str(self.geter_color.get('Cpu', 'color_all_cores')))
            else:
                self.bg_barre_core.append(str(self.geter_color.get('Cpu', 'core' + str(cpu + 1))))
            if all_fond_colors == 'True':
                self.bg_fond_core.append(str(self.geter_color.get('Cpu', 'color_all_fonds')))
            else:
                self.bg_fond_core.append(str(self.geter_color.get('Cpu', 'fond_core' + str(cpu + 1))))

    def afficher_cpu(self, zoom_ratio, frame_root, freq_cpu, win_root, destroy):
        self.zoom_ratio = zoom_ratio
        col_setter = column_setter.ColumnSetter(win_root)
        get_aff = getter.accessToSettings('settings.ini')
        self.aff_load_cpu = get_aff.get('cpu_reglages', 'afficher_load')
        self.aff_freq = get_aff.get('cpu_reglages', 'afficher_freq')
        self.aff_ram_go = get_aff.get('cpu_reglages', 'afficher_ram_go')
        self.aff_bar_ram = get_aff.get('cpu_reglages', 'aff_bar_ram')
        self.aff_pourc_ram = get_aff.get('cpu_reglages', 'aff_pourc_ram')
        self.aff_bar_cores = get_aff.get('cpu_reglages', 'aff_bar_cores')
        self.aff_pourc_cores = get_aff.get('cpu_reglages', 'aff_pourc_cores')
        rowspan_cpu = 0
        if self.aff_load_cpu == 'True':
            rowspan_cpu += 1
        if self.aff_freq == 'True':
            rowspan_cpu += 1
        if self.aff_ram_go == 'True':
            rowspan_cpu += 1
        if self.aff_bar_ram == 'True' or self.aff_pourc_ram == 'True':
            rowspan_cpu += 1
        if self.aff_bar_cores == 'True' or self.aff_pourc_cores == 'True':
            rowspan_cpu += int(self.nbr_cpu_cores)

        if destroy:
            self.cpu_frame.destroy()
        self.cpu_frame = tkinter.Frame(frame_root, relief='raised', borderwidth=4, height=340,
                                       background=self.bg_principale)
        self.cpu_frame.grid(column=1, row=1, sticky=tkinter.N)

        self.color_bout_param = str(self.geter_color.get('Cpu', 'bout_param'))
        self.img_param = tkinter.BitmapImage(master=self.cpu_frame, file=str(self.directory) + '/Images/parametres.xbm')
        self.bout_Param = tkinter.Button(self.cpu_frame, command=self.instancier_obj_param_fen, image=self.img_param,
                                         width=20, background=self.bg_bout_param, highlightthickness=0)
        self.bout_Param.grid(column=2, row=2, rowspan=2, sticky=tkinter.E)
        self.label_title_cpu = tkinter.Label(self.cpu_frame, text=" CPU Infos:",
                                             font=('Arial', int(10 * zoom_ratio)), width=35, background=self.bg_principale)
        self.label_title_cpu.grid(column=1, columnspan=2, row=1)

        self.label_cpu_load = tkinter.Label(self.cpu_frame, text="Cpu load",
                                            font=('Arial', int(10 * zoom_ratio)), background=self.bg_principale)
        if self.aff_load_cpu == 'True':
            self.label_cpu_load.grid(column=1, row=2, sticky=tkinter.W)

        self.label_freq_cpu = tkinter.Label(self.cpu_frame, text="{:.2f}".format(freq_cpu.current / 1000) + " ghz / "
                                                             + "{:.2f}".format(freq_cpu.max / 1000) + " ghz (max)",
                                            font=('Arial', int(10 * zoom_ratio)), background=self.bg_principale,
                                            width=28, anchor=tkinter.W)
        if self.aff_freq == 'True':
            self.label_freq_cpu.grid(column=1, columnspan=2, row=3, sticky=tkinter.W)

        self.label_ram = tkinter.Label(self.cpu_frame, text='ram: xx go / xx go',
                                       font=('Arial', int(10 * zoom_ratio)), background=self.bg_principale)
        if self.aff_ram_go == 'True':
            self.label_ram.grid(column=1, columnspan=2, row=4, sticky=tkinter.W)

        i = 0
        col_x = 0
        adj_row = 5
        passe = 1
        self.core_color = []
        while i < self.nbr_cpu_cores + 1:
            all_color_bare = self.geter_color.get('Cpu', 'bare_all_cores')
            if i == 0:
                self.core_color.append(self.geter_color.get('Cpu', 'ram'))
            elif all_color_bare == 'True':
                self.core_color.append(self.geter_color.get('Cpu', 'color_all_cores'))
            else:
                self.core_color.append(self.geter_color.get('Cpu', 'Core' + str(i)))
            self.list_bar_size[i] = tkinter.IntVar()
            if i == 0:
                core_name = "ram"
                bg_barre_color = self.bg_barre_ram
                bg_fond_color = self.bg_fond_ram
            else:
                core_name = "core " + str(i)
                bg_barre_color = self.bg_barre_core[i - 1]
                bg_fond_color = self.bg_fond_core[i - 1]

            self.list_lab_name[i] = tkinter.Label(self.cpu_frame, text=core_name + ' = 00.00%',
                                                  font=('Arial', int(10 * zoom_ratio)), width=15,
                                                  background=self.bg_principale)
            if (i == 0 and self.aff_pourc_ram == 'True') or (i > 0 and self.aff_pourc_cores == 'True'):
                self.list_lab_name[i].grid(column=2 + col_x, row=adj_row, sticky=tkinter.W)

            self.list_canvas_name[i] = tkinter.Canvas(self.cpu_frame, height=int(10 * zoom_ratio),
                                                      width=int(100 * zoom_ratio), relief='raised', borderwidth=2,
                                                      background=bg_fond_color, highlightthickness=0)
            if (i == 0 and self.aff_bar_ram == 'True') or (i > 0 and self.aff_bar_cores == 'True'):
                self.list_canvas_name[i].grid(column=1 + col_x, row=adj_row, sticky=tkinter.W)
                self.cpu_frame.update()
            self.list_core_bar_name.append(self.list_canvas_name[i].create_rectangle(0.0, 0.0, 0.0, 0.0,
                                                                                     fill=bg_barre_color))
            i += 1
            adj_row += 1
            self.cpu_frame.update()
            lastwidget = i - 1
            if not col_setter.valide_height(self.cpu_frame.winfo_height()):
                passe += 1
                col_x = 2 * passe
                adj_row = 1
                self.list_lab_name[lastwidget].grid(column=2 + col_x, row=adj_row, sticky=tkinter.W)
                self.list_canvas_name[lastwidget].grid(column=1 + col_x, row=adj_row, sticky=tkinter.W)
                adj_row += 1
        if self.critical_cpu_temp is None:
            self.critical_cpu_temp = 'None'
        self.core_temp_lab = ttk.Label(self.cpu_frame, text='Temp Cpu: ... / ' + str(self.critical_cpu_temp)
                                                            + '°c Max (Tj)',
                                       font=('Arial', int(8 * zoom_ratio)), width=int(10 * zoom_ratio),
                                       background=self.bg_principale)
        self.core_temp_lab.grid(column=1 + col_x, columnspan=2, row=adj_row, sticky=tkinter.EW)
        frame_root.update()
        windo_height = frame_root.winfo_height()
        if not col_setter.valide_height(frame_root.winfo_height()):
            col_x = 2 * passe
            adj_row = 1
            passe += 1
            self.core_temp_lab.destroy()
            if self.critical_cpu_temp is not None:
                self.core_temp_lab = ttk.Label(self.cpu_frame, text='Temp Cpu: ... / ' + str(self.critical_cpu_temp)
                                                                    + '°c Max (Tj)',
                                               font=('Arial', int(10 * zoom_ratio)), width=int(8 * zoom_ratio))
                self.core_temp_lab.grid(column=1 + col_x, columnspan=2, row=adj_row, sticky=tkinter.EW)
            frame_root.update()
            adj_row += 1

        col_for_frame_gen_disk = col_x + 1
        row_for_frame_gen_disk = adj_row + 1
        self.cpu_frame.update()
        self.col_disk = col_for_frame_gen_disk
        self.row_disk = 2
        return self.col_disk, self.row_disk

    def instancier_obj_param_fen(self):
        if self.fen_param is not None:
            self.fen_param.on_closing_fen_param()
        self.fen_param = c_fenetre_param.FenParam(self.list_disk_afficher, self.root, self.possibles_part)
        self.fen_param.open_window()

    def v_update_cpu_zoom(self, zoom_ratio):
        self.label_title_cpu.configure(font=('Arial', int(10 * zoom_ratio)))
        if self.aff_load_cpu == 'True':
            self.label_cpu_load.configure(font=('Arial', int(10 * zoom_ratio)))
        if self.aff_freq == 'True':
            self.label_freq_cpu.configure(font=('Arial', int(10 * zoom_ratio)))
        if self.aff_ram_go == 'True':
            self.label_ram.configure(font=('Arial', int(10 * zoom_ratio)))

    def v_refresh_load_cpu(self, cpu_load):
        if self.aff_load_cpu == 'True':
            self.label_cpu_load.configure(text="Cpu load: " + str(cpu_load) + "%")

    def v_refresh_ram(self, ram_load, ram_total):
        if self.aff_ram_go == 'True':
            self.label_ram.configure(text="Ram: " + "{:.2f}".format(ram_load[0]) + " " + ram_load[1] +
                                          " / " + "{}".format(ram_total) + " " + ram_total[1])

    def v_refresh_freq_cpu(self, freq_current, freq_max):
        if self.aff_freq == 'True':
            self.label_freq_cpu.configure(text="Cpu freq: " + "{:.2f}".format(freq_current / 1000) + " ghz / "
                                               + "{:.2f}".format(freq_max / 1000) + " ghz (max)")

    def v_refresh_cores(self, nbr_cpu_cores, ram_percent, cpup2, temp_all_cores, zoom_ratio):
        geter = getter.accessToSettings('settings.ini')
        j = 0
        while j < (nbr_cpu_cores + 1):
            if j == 0:
                text = "ram = " + str(ram_percent) + " %"
                color = self.core_color[0]
                percent = ram_percent
            else:
                text = "core" + str(j) + " = " + str(cpup2[j - 1]) + "%"

                color = self.core_color[j]
                percent = cpup2[j - 1]
            if (j == 0 and self.aff_pourc_ram == 'True') or (j > 0 and self.aff_pourc_cores == 'True'):
                self.list_lab_name[j].configure(text=text)
            if (j == 0 and self.aff_bar_ram == 'True') or (j > 0 and self.aff_bar_cores == 'True'):
                self.list_canvas_name[j].delete(self.list_core_bar_name[j])
                self.list_core_bar_name[j] = self.list_canvas_name[j].create_rectangle(0.0, 3.0, (percent * zoom_ratio
                                                                                                  + 2), (12 *
                                                                                                         zoom_ratio)
                                                                                       + 1, fill=color)
            j += 1
        if temp_all_cores is not None:
            cputemp, critical_temp = self.get_max_temp_core(temp_all_cores)
            tj_max_perso = geter.get('cpu_reglages', 'tj_max')
            if tj_max_perso == 'auto':
                critical_core_temp = critical_temp
            else:
                critical_core_temp = int(tj_max_perso)
            degres_cpu = geter.get('cpu_reglages', 'degres_cpu')
            if critical_core_temp == None:
                critical_core_temp = 0.00
            if degres_cpu != 'celsius':
                cputemp = cputemp * 1.8 + 32
                critical_core_temp = critical_core_temp * 1.8 + 32
                self.core_temp_lab.configure(text='Temp Cpu: {:.2f}'.format(cputemp) +
                                                  ' °f / {:.2f}'.format(critical_core_temp) +
                                                  ' °f Max (Tj)')
            else:
                self.core_temp_lab.configure(text='Temp Cpu: {:.2f}'.format(cputemp) +
                                                  ' °c / {:.2f}'.format(critical_core_temp) + ' °c Max (Tj)')

    def get_max_temp_core(self, temp_all_cores):
        for names, entries in temp_all_cores.items():
            if names == 'coretemp':
                core_temp_max = 0
                for entry in entries:
                    if int(entry.current) > core_temp_max:
                        core_temp_max = int(entry.current)
                        critic = entry.critical
                return core_temp_max, critic
            elif names == 'cpu_thermal':
                for entry in entries:
                    return entry.current, entry.critical

    def v_update_cpu(self):
        geter_updt = getter.accessToSettings('settings.ini')

        self.aff_load_cpu = geter_updt.get('cpu_reglages', 'afficher_load')
        if self.aff_load_cpu == 'True':
            self.label_cpu_load.grid(column=1, columnspan=2, row=2, sticky=tkinter.W)
        else:
            try:
                self.label_cpu_load.grid_forget()
            except TypeError:
                pass
        self.aff_freq = geter_updt.get('cpu_reglages', 'afficher_freq')
        if self.aff_freq == 'True':
            self.label_freq_cpu.grid(column=1, columnspan=2, row=3, sticky=tkinter.W)
            self.label_freq_cpu.configure(fg='#ffffff')
        else:
            try:
                self.label_freq_cpu.grid_forget()
            except TypeError:
                pass
        self.aff_ram_go = geter_updt.get('cpu_reglages', 'afficher_ram_go')
        if self.aff_ram_go == 'True':
            self.label_ram.grid(column=1, columnspan=2, row=4, sticky=tkinter.W)
        else:
            try:
                self.label_ram.grid_forget()
            except TypeError:
                pass
        self.aff_bar_ram = geter_updt.get('cpu_reglages', 'aff_bar_ram')
        if self.aff_bar_ram == 'True':
            self.list_canvas_name[0].grid(column=1, row=5, sticky=tkinter.W)
        else:
            try:
                self.list_canvas_name[0].grid_forget()
            except TypeError:
                pass
        self.aff_pourc_ram = geter_updt.get('cpu_reglages', 'aff_pourc_ram')
        if self.aff_pourc_ram == 'True':
            if self.aff_bar_ram == 'True':
                self.list_lab_name[0].grid(column=2, row=5, sticky=tkinter.W)
            else:
                self.list_lab_name[0].grid(column=1, columnspan=1, row=5, sticky=tkinter.W)
        else:
            try:
                self.list_lab_name[0].grid_forget()
            except TypeError:
                pass
        self.aff_bar_cores = geter_updt.get('cpu_reglages', 'aff_bar_cores')
        self.aff_pourc_cores = geter_updt.get('cpu_reglages', 'aff_pourc_cores')

        i = 1
        while i <= self.nbr_cpu_cores:
            if self.aff_bar_cores == 'True':
                self.list_canvas_name[i].grid(column=1, row=i + 5, sticky=tkinter.W)
            else:
                try:
                    self.list_canvas_name[i].grid_forget()
                except TypeError:
                    pass
            if self.aff_pourc_cores == 'True' and self.aff_bar_cores == 'False':
                self.list_lab_name[i].grid(column=1, row=i + 5, sticky=tkinter.W)
            elif self.aff_pourc_cores == 'True':
                self.list_lab_name[i].grid(column=2, row=i + 5, sticky=tkinter.W)
            else:
                try:
                    self.list_lab_name[i].grid_forget()
                except TypeError:
                    pass
            i += 1
        return self.col_disk, self.row_disk

    def v_update_font(self):
        get_cpu_font = getter.accessToSettings('font.ini')
        self.label_title_cpu.configure(font=(get_cpu_font.get('Cpu', 'cpu_infos'), int(10 * self.zoom_ratio)))
        self.label_cpu_load.configure(font=(get_cpu_font.get('Cpu', 'cpu_load'), int(10 * self.zoom_ratio)))
        self.label_freq_cpu.configure(font=(get_cpu_font.get('Cpu', 'cpu_freq'), int(10 * self.zoom_ratio)))
        self.label_ram.configure(font=(get_cpu_font.get('Cpu', 'ram_go'), int(10 * self.zoom_ratio)))
        i = 0
        while i < len(self.list_lab_name):
            if i == 0:
                self.list_lab_name[i].configure(font=(get_cpu_font.get('Cpu', 'ram'), int(10 * self.zoom_ratio)))
            else:
                core_name = 'core' + str(i)
                self.list_lab_name[i].configure(font=(get_cpu_font.get('Cpu', core_name), int(10 * self.zoom_ratio)))
            i += 1
        if self.critical_cpu_temp is not None:
            self.core_temp_lab.configure(font=(get_cpu_font.get('Cpu', 'temp'), int(10 * self.zoom_ratio)))

    def v_update_font_color(self):
        geter_color_font = getter.accessToSettings('color_font.ini')
        color_title = geter_color_font.get('cpu', 'title')
        color_cpu_load = geter_color_font.get('cpu', 'cpu_load')
        color_freq_cpu = geter_color_font.get('cpu', 'cpu_freq')
        color_ram = geter_color_font.get('cpu', 'ram')
        color_percent_ram = geter_color_font.get('cpu', 'percent_ram')
        i = 1
        list_core_color = []
        while i < len(self.list_lab_name):
            list_core_color.append(geter_color_font.get('cpu', 'core_' + str(i)))
            i += 1
        color_temp = geter_color_font.get('cpu', 'temp')

        self.label_title_cpu.configure(foreground=color_title)
        self.label_cpu_load.configure(foreground=color_cpu_load)
        self.label_freq_cpu.configure(foreground=color_freq_cpu)
        self.label_ram.configure(foreground=color_ram)
        i = 0
        for lab in self.list_lab_name:
            if i == 0:
                lab.config(foreground=color_percent_ram)
            else:
                lab.configure(foreground=list_core_color[i - 1])
            i += 1
        if self.critical_cpu_temp is not None:
            self.core_temp_lab.configure(foreground=color_temp)

    def update_style(self):
        getter_style = getter.accessToSettings('reliefs.ini')
        relief_widg = getter_style.get('cpu', 'widg')
        relief_ram = getter_style.get('cpu', 'ram')
        relief_cores = getter_style.get('cpu', 'cores')
        self.cpu_frame.configure(relief=relief_widg)

        j = 0
        while j < len(self.list_canvas_name):
            if j == 0:
                self.list_canvas_name[j].configure(relief=relief_ram)
            else:
                self.list_canvas_name[j].configure(relief=relief_cores)
            j += 1
