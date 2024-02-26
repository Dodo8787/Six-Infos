from tkinter import ttk
import tkinter
from controleur.generals_actions import General
from modele import m_access_to_settings


class VNetwork:
    def __init__(self):
        self.networkGraphFram = tkinter.Frame
        self.networkFrame = tkinter.Frame
        self.networkTitle = ttk.Label
        self.network_up_down_frame = tkinter.Frame
        self.networkDownDebit = ttk.Label
        self.networkUpDebit = ttk.Label
        self.label2Down = ttk.Label
        self.label2Up = ttk.Label
        self.frameRoot = tkinter.Frame
        self.networkDownFram = tkinter.Frame
        self.networkUpFram = tkinter.Frame

    def create_widget_network(self, frame_pour_network, row_network, col_net=1):
        gene = General()
        geter_vue_netw = m_access_to_settings.accessToSettings('font.ini')
        font_infos = str(geter_vue_netw.get('netw_font', 'netw_infos'))
        font_down = str(geter_vue_netw.get('netw_font', 'netw_down'))
        font_up = str(geter_vue_netw.get('netw_font', 'netw_up'))
        get_color_netw = m_access_to_settings.accessToSettings('colors.ini')
        color_princ = str(get_color_netw.get('Network', 'principale'))
        color_bg_down = str(get_color_netw.get('Network', 'coul_down'))
        color_bg_up = str(get_color_netw.get('Network', 'coul_up'))
        getter_color_font = m_access_to_settings.accessToSettings('color_font.ini')
        color_font_title = getter_color_font.get('Network_font', 'title')
        color_font_down = getter_color_font.get('Network_font', 'down')
        color_font_up = getter_color_font.get('Network_font', 'up')
        zoom_ratio = gene.get_zoom_ratio()
        try:
            self.networkFrame.destroy()
        except NameError:
            pass
        except TypeError:
            pass
        self.networkFrame = tkinter.Frame(frame_pour_network, relief='raised', borderwidth=4, background=color_princ)
        self.networkFrame.grid(column=col_net, row=row_network, sticky=tkinter.N)
        self.networkTitle = ttk.Label(self.networkFrame, text='Network Infos:', width=35, background=color_princ,
                                      font=(font_infos, int(10 * zoom_ratio)), foreground=color_font_title)
        self.networkTitle.grid(column=1, row=1, columnspan=2, sticky=tkinter.W)
        self.networkGraphFram = ttk.Frame(self.networkFrame, relief='ridge', borderwidth=1)
        self.networkGraphFram.grid(column=1, columnspan=2, row=2)
        # root.update()
        self.network_up_down_frame = tkinter.Frame(self.networkFrame, width=30)
        self.network_up_down_frame.grid(column=1, columnspan=2, row=3, pady=int(5 * zoom_ratio))

        self.networkDownFram = tkinter.Frame(self.network_up_down_frame, relief='ridge', borderwidth=2,
                                        background=color_bg_down)
        self.networkDownFram.grid(column=1, row=1)
        self.networkUpFram = tkinter.Frame(self.network_up_down_frame, relief='ridge', borderwidth=2, background=color_bg_up)
        self.networkUpFram.grid(column=2, row=1)

        self.label2Down = ttk.Label(self.networkDownFram, text="Down", background=color_bg_down,
                                    font=(font_down, int(8 * zoom_ratio)), foreground=color_font_down)
        self.label2Down.grid(column=1, row=1)
        self.label2Up = ttk.Label(self.networkUpFram, text='Up', background=color_bg_up,
                                  font=(font_up, int(8 * zoom_ratio)), foreground=color_font_up)
        self.label2Up.grid(column=1, row=1)

        widt = int(24 * zoom_ratio / 2)
        self.networkDownDebit = ttk.Label(self.networkDownFram, text='0', width=widt, background=color_bg_down,
                                          font=('arial', int(9 * zoom_ratio)), foreground=color_font_down)
        self.networkDownDebit.grid(column=2, row=1)
        self.networkUpDebit = ttk.Label(self.networkUpFram, text='0', width=widt, background=color_bg_up,
                                        font=('arial', int(9 * zoom_ratio)), foreground=color_font_up)
        self.networkUpDebit.grid(column=2, row=1)
        # root.update()
        # print_network_graph()
        return self.networkGraphFram, self.network_up_down_frame, self.networkUpDebit, self.networkDownDebit,\
            self.networkFrame

    def update_style_graph(self):
        gett = m_access_to_settings.accessToSettings('reliefs.ini')
        style_widg = gett.get('netw', 'widg')
        style_graph = gett.get('netw', 'graph')
        style_down = gett.get('netw', 'down')
        style_up = gett.get('netw', 'up')
        self.networkFrame.configure(relief=style_widg)
        self.networkGraphFram.configure(relief=style_graph)
        self.networkDownFram.configure(relief=style_down)
        self.networkUpFram.configure(relief=style_up)