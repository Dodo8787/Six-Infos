from collections import deque
from vue import v_network
import modele.m_access_to_settings as getter
from controleur import generals_actions as general
from controleur import c_convert_bit as converter
from controleur import column_setter
from matplotlib import pyplot as plt
from vue import v_network
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
from psutil import net_io_counters


class CNetwork:

    def __init__(self, root_frame, root_window):
        self.v_net = v_network.VNetwork()
        self.queueNetworkRecv = deque([])
        self.queueNetworkSend = deque([])
        self.listesecReverse = []
        i = 60 - 1
        while i >= 0:
            self.listesecReverse.append(i)
            self.queueNetworkRecv.append(0)
            self.queueNetworkSend.append(0)
            i -= 1
        self.geter = getter.accessToSettings('settings.ini')
        self.root_frame = root_frame
        self.network_frame_ungrided = False
        self.col_network = 0
        self.row_network = 0
        self.plot1 = plt
        self.lim_y = 0
        self.limit_x = 0
        self.aff_debit_netw = True
        self.network_up_down_frame = tkinter.Frame
        self.networkGraphFram = tkinter.Frame
        self.network_graph_fram = tkinter.Frame
        self.plot1 = plt
        self.ponder = 0
        self.ponder_up = deque([])
        self.ponder_down = deque([])
        self.network_data = []
        self.conv = converter.ConvertBit()
        self.aff_graph = bool
        self.unit_graph = None
        self.reafficher_graph = False
        self.caneva = FigureCanvasTkAgg
        self.update_graph = ''
        self.pond_up_divised = 0
        self.pond_down_divised = 0
        self.unit = "auto"
        self.af_deb_net = True
        self.label_up_debit = tkinter.Label
        self.label_down_debit = tkinter.Label
        self.on_sec_send = 0
        self.on_sec_recv = 0
        self.network_frame = tkinter.Frame
        self.root_window = root_window
        self.zoom_ratio = 10

    def creer_ou_refresh_ou_update_widg_network(self, col_network, row_network, pass1=False, aff_graph=True,
                                                just_refresh=False):
        gene = general.General()
        self.zoom_ratio = gene.get_zoom_ratio()
        self.aff_graph = aff_graph
        self.col_network = col_network
        self.row_network = row_network
        self.reafficher_graph = False
        if aff_graph == False:
            try:
                self.network_graph_fram.grid_forget()
            except TypeError:
                pass
            self.aff_graph = False
        aff_net_inf = self.geter.get('network_reglages', 'afficher_widget')
        if aff_net_inf == False:
            self.network_frame.grid_forget()
            self.network_frame_ungrided = True
            self.geter.set('network_reglages', 'update_graph', 'False')
            return
        elif aff_net_inf == 'True' and self.network_frame_ungrided:
            self.network_frame.grid(column=self.col_network,
                                    row=self.row_network, rowspan=10)

            self.network_frame_ungrided = False

        self.update_graph = self.geter.get('network_reglages', 'update_graph')
        if pass1:
            self.network_graph_fram, self.network_up_down_frame, self.label_up_debit, self.label_down_debit,\
                self.network_frame = \
                self.v_net.create_widget_network(self.root_frame, self.row_network, self.col_network)
        if not pass1 and (aff_net_inf == 'True' or aff_graph == True):
            self.updater_graph()

        if pass1 and aff_graph == True:
            self.ponder = int(self.geter.get('network_reglages', 'ponderation'))
            self.ponder_up = deque([])
            self.ponder_down = deque([])
            geter_curve = getter.accessToSettings('colors.ini')
            self.down_curve_color = geter_curve.get('Network', 'down_curve')
            self.up_curve_color = geter_curve.get('Network', 'up_curve')
            self.color_contour_graph = geter_curve.get('Network', 'contour_graph')
            self.color_fond_graph = geter_curve.get('Network', 'fond_graph')
            self.color_axes_x_et_y = geter_curve.get('Network', 'axes_x_et_y')


            i = 0
            while i < self.ponder:
                self.ponder_up.append(0)
                self.ponder_down.append(0)
                i += 1
            self.lim_y = self.geter.get('network_reglages', 'axe_y')
            self.limit_x = self.geter.get('network_reglages', 'axe_x')
            self.unit = self.geter.get('network_reglages', 'unite_up_down')
            if self.unit == 'auto':
                self.unit_graph = 'ko'
            else:
                self.unit_graph = self.unit
            self.listesecReverse = []
            self.queueNetworkSend = deque([])
            self.queueNetworkRecv = deque([])
            if self.limit_x == 'auto':
                self.limit_x = 60
            else:
                self.limit_x = int(self.limit_x)
            i = self.limit_x - 1
            while i >= 0:
                self.listesecReverse.append(i)
                self.queueNetworkRecv.append(0)
                self.queueNetworkSend.append(0)
                i -= 1
            if aff_graph:
                fig = plt.figure(figsize=(3.8 * self.zoom_ratio, 1.9 * self.zoom_ratio), dpi=56)
                fig.set_facecolor(self.color_contour_graph)  # couleur du contour du graph
                self.plot1 = plt
                ax = self.plot1.axes()
                ax.set_facecolor(self.color_fond_graph)  # couleur fond centre graph
                self.plot1.tick_params(labelcolor=self.color_axes_x_et_y)  # axes x et y color

                self.caneva = FigureCanvasTkAgg(fig, master=self.network_graph_fram)
                self.caneva.get_tk_widget().grid(column=1, columnspan=2, row=1)
            # col_setter = column_setter.ColumnSetter(self.root_window)


    def updater_graph(self):
        ponder = int(self.geter.get('network_reglages', 'ponderation'))

        ponder_up = deque([])
        ponder_down = deque([])
        i = 0
        while i < ponder:
            ponder_up.append(0)
            ponder_down.append(0)
            i += 1
        af_gra = self.geter.get('network_reglages', 'afficher_graph')
        af_deb_net = self.geter.get('network_reglages', 'afficher_debit')
        if af_deb_net == 'False':
            self.aff_debit_netw = False
            self.network_up_down_frame.grid_forget()
        else:
            self.aff_debit_netw = True
            try:
                self.network_up_down_frame.grid(column=1, row=3)
            except TypeError:
                pass
        if af_gra == 'False':
            self.aff_graph = False
            try:
                self.networkGraphFram.grid_forget()
            except TypeError:
                pass
        elif af_gra == 'True' and self.network_frame_ungrided:
            self.aff_graph = True
            self.networkGraphFram.grid(column=1, row=2)
            self.reafficher_graph = True
        self.lim_y = self.geter.get('network_reglages', 'axe_y')

        limit_x = self.geter.get('network_reglages', 'axe_x')
        if self.reafficher_graph:
            self.listesecReverse = []
            self.queueNetworkSend = deque([])
            self.queueNetworkRecv = deque([])
            if self.limit_x == 'auto':
                self.limit_x = 60
            else:
                limit_x = int(limit_x)
            i = limit_x - 1
            while i >= 0:
                self.listesecReverse.append(i)
                self.queueNetworkRecv.append(0)
                self.queueNetworkSend.append(0)
                i -= 1
        unit = self.geter.get('network_reglages', 'unite_up_down')
        if unit == 'auto':
            self.unit_graph = 'ko'
        else:
            self.unit_graph = unit
        setter = getter.accessToSettings('settings.ini')
        get = getter.accessToSettings('settings.ini')
        do_updt_graph = get.get('network_reglages', 'update_graph')
        if do_updt_graph == 'True':
            setter.set('network_reglages', 'update_graph', 'False')

        if self.reafficher_graph:
            self.creer_ou_refresh_ou_update_widg_network(self.col_network, self.row_network, True)
        if self.plot1 is not None:
            self.plot1.cla()
            if self.lim_y == 'auto':
                self.plot1.ylim(auto=True)
            else:
                self.plot1.ylim(top=int(self.lim_y))
        net_info = net_io_counters()
        sent = net_info.bytes_sent
        received = net_info.bytes_recv
        self.on_sec_send = 0
        self.on_sec_recv = 0
        if len(self.network_data) >= 1:
            self.on_sec_send = sent - self.network_data[0]
            self.on_sec_recv = received - self.network_data[1]
        if self.ponder > 0:
            self.ponder_up.append(self.on_sec_send)
            self.ponder_down.append(self.on_sec_recv)
            if len(self.ponder_up) > self.ponder:
                self.ponder_up.popleft()
            if len(self.ponder_down) > self.ponder:
                self.ponder_down.popleft()
            i = 1
            pond_up = 0
            pond_down = 0
            divisor = 0
            while i <= self.ponder:
                pond_up += self.ponder_up[i - 1] * i
                pond_down += self.ponder_down[i - 1] * i
                divisor += i
                i += 1
            self.pond_up_divised = pond_up / divisor
            self.pond_down_divised = pond_down / divisor
        self.network_data = [sent, received]
        if self.on_sec_send >= self.on_sec_recv:
            on_sec_send_converted = self.conv.convert_bit_to_go(self.on_sec_send, unite=self.unit_graph, power=1024, bps=False)
            on_sec_recev_converted = self.conv.convert_bit_to_go(self.on_sec_recv, unite=on_sec_send_converted[1],
                                                                 power=1024, bps=False)
        else:
            on_sec_recev_converted = self.conv.convert_bit_to_go(self.on_sec_recv, unite=self.unit_graph, power=1024,
                                                                 bps=False)
            on_sec_send_converted = self.conv.convert_bit_to_go(self.on_sec_send, unite=on_sec_recev_converted[1],
                                                                power=1024, bps=False)

        self.queueNetworkSend.append(on_sec_send_converted[0])
        self.queueNetworkRecv.append(on_sec_recev_converted[0])
        if len(self.queueNetworkSend) >= self.limit_x:
            self.queueNetworkSend.popleft()
        if len(self.queueNetworkRecv) >= self.limit_x:
            self.queueNetworkRecv.popleft()
        y1 = []
        k = 0
        while k < len(self.queueNetworkSend):
            y1.append(self.queueNetworkSend[k])
            k += 1
        y2 = []
        kk = 0
        while kk < len(self.queueNetworkRecv):
            y2.append(self.queueNetworkRecv[kk])
            kk += 1
        x = self.listesecReverse
        if self.aff_graph:
            self.plot1.plot(x, y1, color=self.up_curve_color)  # Up curve (courbe Up)
            self.plot1.plot(x, y2, color=self.down_curve_color)  # Down curve (courbe Down)
            self.caneva.draw()
        self.network_up_down_debit()

    def network_up_down_debit(self):
        if self.aff_debit_netw:
            if self.ponder > 0:
                self.on_sec_send = self.pond_up_divised
                self.on_sec_recv = self.pond_down_divised

            if self.unit == 'auto':
                on_sec_send_conv = self.conv.convert_bit_to_go(self.on_sec_send, 1024, 'auto', bps=False)
                on_sec_recv_conv = self.conv.convert_bit_to_go(self.on_sec_recv, 1024, 'auto', bps=False)
            else:
                on_sec_send_conv = self.conv.convert_bit_to_go(self.on_sec_send, 1024, self.unit, bps=False)
                on_sec_recv_conv = self.conv.convert_bit_to_go(self.on_sec_recv, 1024, self.unit, bps=False)
            geter_c_netw = getter.accessToSettings('font.ini')
            font_down = str(geter_c_netw.get('netw_font', 'netw_down'))
            font_up = str(geter_c_netw.get('netw_font', 'netw_up'))
            if len(on_sec_send_conv) == 2:
                self.label_up_debit.configure(text=' {:.2f}'.format(on_sec_send_conv[0]) + ' '
                                              + str(on_sec_send_conv[1]) + '/s',
                                              font=(font_up, int(8 * self.zoom_ratio)))
            if len(on_sec_recv_conv) == 2:
                self.label_down_debit.configure(text=' {:.2f}'.format(on_sec_recv_conv[0]) + ' '
                                                + str(on_sec_recv_conv[1]) + '/s',
                                                font=(font_down, int(8 * self.zoom_ratio)))

    def update_style_graph(self):
        self.v_net.update_style_graph()
