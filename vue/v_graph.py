'''
class AfficheurGraph:
    def __init__(self):
        pass

    def print_network_graph(self, passtest=True, erase=False):
        global caneva
        global plot1
        global networkData
        global queueNetworkSend
        global queueNetworkRecv
        global on_sec_send_converted
        global on_sec_recev_converted
        global on_sec_send
        global on_sec_recv
        global limit_x
        global lim_y
        global listesecReverse
        global unit
        global unit_graph
        global aff_graph
        global aff_debit_netw
        global pond_up_divised
        global pond_down_divised
        global ponder
        global ponder_up
        global ponder_down
        global networkFrameUngrided
        global networkGraphFram
        global networkFrame
        global row_network
        global column_network





    def network_up_down_debit():
        global on_sec_send
        global on_sec_recv
        global networkUpDebit
        global networkDownDebit

        if aff_debit_netw:
            if ponder > 0:
                on_sec_send = pond_up_divised
                on_sec_recv = pond_down_divised
            if unit == 'auto':
                on_sec_send_conv = converter.convert_bit_to_go(on_sec_send, 1024, 'auto', bps=True)
                on_sec_recv_conv = converter.convert_bit_to_go(on_sec_recv, 1024, 'auto', bps=True)
            else:
                on_sec_send_conv = converter.convert_bit_to_go(on_sec_send, 1024, unit, bps=True)
                on_sec_recv_conv = converter.convert_bit_to_go(on_sec_recv, 1024, unit, bps=True)

            if len(on_sec_send_conv) == 2:
                networkUpDebit.configure(text=' {:.2f}'.format(on_sec_send_conv[0]) + ' '
                                              + str(on_sec_send_conv[1]))
            if len(on_sec_recv_conv) == 2:
                networkDownDebit.configure(text=' {:.2f}'.format(on_sec_recv_conv[0]) + ' '
                                                + str(on_sec_recv_conv[1]))
    def update_graphe(self):
        ponder = int(parser_update.get('network_reglages', 'ponderation'))
        ponder_up = deque([])
        ponder_down = deque([])
        i = 0
        while i < ponder:
            ponder_up.append(0)
            ponder_down.append(0)
            i += 1
        af_gra = parser_update.get('network_reglages', 'afficher_graph')
        af_deb_net = parser_update.get('network_reglages', 'afficher_debit')
        if af_deb_net == 'cach_debit':
            aff_debit_netw = False
            network_up_down_frame.grid_forget()
        else:
            aff_debit_netw = True
            network_up_down_frame.grid(column=1, row=3)
        if af_gra == 'pas_aff_graph':
            aff_graph = False
            networkGraphFram.grid_forget()
        elif af_gra == 'aff_graph' and networkFrameUngrided == True:
            aff_graph = True
            networkGraphFram.grid(column=1, row=2)
            reafficher_graph = True
        lim_y = parser_update.get('network_reglages', 'axe_y')

        limit_x = parser_update.get('network_reglages', 'axe_x')
        listesecReverse = []
        queueNetworkSend = deque([])
        queueNetworkRecv = deque([])
        if limit_x == 'auto':
            limit_x = 60
        else:
            limit_x = int(limit_x)
        i = limit_x - 1
        while i >= 0:
            listesecReverse.append(i)
            queueNetworkRecv.append(0)
            queueNetworkSend.append(0)
            i -= 1
        unit = parser_update.get('network_reglages', 'unite_up_down')
        if unit == 'auto':
            unit_graph = 'kbps'
        else:
            unit_graph = unit
        parser_update.set('network_reglages', 'update_graph', 'False')
        with open(str(directory) + '/settings.ini', 'w') as j:
            parser_update.write(j)
        if reafficher_graph:
            print_network_graph(True)

    def place_graph_widget(rown, col):
        global networkGraphFram
        global networkUpDebit
        global networkDownDebit
        global networkFrame
        global column_network
        global row_network
        global root
        global cpuFrame
        global frameRoot

        networkFrame.grid_forget()
        col = 1
        networkFrame.grid(column=col, columnspan=2, row=rown + 2, rowspan=10, sticky=N)
        root.update()
        if col_setter.valide_height(frameRoot.winfo_height()) == False:
            networkFrame.destroy()
            create_widget_network(frameRoot, 1, 2)
            root.update()
'''
