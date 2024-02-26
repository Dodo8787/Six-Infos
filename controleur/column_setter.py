from screeninfo import get_monitors
from modele import m_column_setter


class ColumnSetter:
    app_height = 0

    def __init__(self, root_win):
        self.pos_y = root_win.winfo_y()
        m_col_setter = m_column_setter.MColumnSetter()
        for m in get_monitors():
            self.screen_height = m.height
            if m.name == m_col_setter.monitor:
                break

    def add_height(self, widget_height):
        self.app_height += widget_height
        if self.app_height > self.screen_height:
            return False
        else:
            return True

    def valide_height(self, widg_height):
        if (widg_height + self.pos_y) < (self.screen_height - 15):
            return True
        else:
            return False
