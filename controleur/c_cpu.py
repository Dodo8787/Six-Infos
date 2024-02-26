from vue import v_cpu
import platform
actual_os = platform.system()
from psutil import virtual_memory, cpu_freq, cpu_count, cpu_percent
if actual_os == 'Linux':
    from psutil import sensors_temperatures
import controleur.c_convert_bit as c_convert_bit
import controleur.generals_actions as general

class ControlerCpu:

    def __init__(self, zoom_ratio, frame_root, root):
        if actual_os == 'Linux':
            self.critical_cpu_temp = self.get_critical_core_temp()
        else:
            self.critical_cpu_temp = None
        self.ram_total = self.get_ram_total()
        self.vue_cpu = v_cpu.AfficheurCpu(self.critical_cpu_temp, root)
        self.cpu_freq_max = cpu_freq().max
        self.nbr_cpu_cores = cpu_count()
        self.frame_root = frame_root
        self.zoom_ratio = zoom_ratio
        self.root = root

    def get_critical_core_temp(self):
        temp_all_core = sensors_temperatures()
        for names, entries in temp_all_core.items():
            if names == 'coretemp':
                for entry in entries:

                    if entry.label == 'Core 0':
                        critical_core_temp = entry.critical
                        return critical_core_temp

    def get_ram_total(self):
        converter = c_convert_bit.ConvertBit()
        ram = virtual_memory()
        ram_total = converter.convert_bit_to_go(ram.total, power=1024)
        ram_str = "{:.2f}".format(ram_total[0]) + str(ram_total[1])
        return ram_str

    def refresh_cpu(self):
        converter = c_convert_bit.ConvertBit()
        cpu_load = cpu_percent(0, percpu=False)
        ram = virtual_memory()
        ram_percent = ram.percent
        ram_used = converter.convert_bit_to_go(ram.total - ram.available, power=1024)
        cpu_freq_current = cpu_freq().current
        cpu_percent_per_core = cpu_percent(0, percpu=True)
        if actual_os == 'Linux':
            temp_all_cores = sensors_temperatures()
        else:
            temp_all_cores = None

        gener = general.General()
        zoom_ratio = gener.get_zoom_ratio()

        self.vue_cpu.v_refresh_load_cpu(cpu_load)
        self.vue_cpu.v_refresh_ram(ram_used, self.ram_total)
        self.vue_cpu.v_refresh_freq_cpu(cpu_freq_current, self.cpu_freq_max)
        self.vue_cpu.v_refresh_cores(self.nbr_cpu_cores, ram_percent, cpu_percent_per_core, temp_all_cores, zoom_ratio)

    def afficher_cpu(self, destroy=False):
        gene = general.General()
        self.zoom_ratio = gene.get_zoom_ratio()
        col_gen_disk, row_gen_disk = self.vue_cpu.afficher_cpu(self.zoom_ratio, self.frame_root, cpu_freq(),
                                                               self.root, destroy=destroy)
        return col_gen_disk, row_gen_disk


    def update_font(self):
        self.vue_cpu.v_update_font()

    def update_font_color(self):
        self.vue_cpu.v_update_font_color()

    def update_style(self):
        self.vue_cpu.update_style()
