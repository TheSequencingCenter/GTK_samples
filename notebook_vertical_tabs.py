import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title="Notebook Demo")
        self.set_border_width(10)
        self.Notebook = Gtk.Notebook()
        self.Notebook.set_tab_pos(Gtk.PositionType.LEFT)
        self.add(self.Notebook)

        # First page
        self.page1 = Gtk.Box()
        self.set_border_width(10)
        self.page1.add(Gtk.Label(label="Page 1 label"))
        self.Notebook.append_page(self.page1, Gtk.Label(label="First tab"))

        # Second page
        self.page2 = Gtk.Box()
        self.set_border_width(10)
        self.page2.add(Gtk.Label(label="Page 2 label"))
        icon = Gtk.Image.new_from_icon_name("gnome-dev-cdrom-audio", Gtk.IconSize.MENU)
        self.Notebook.append_page(self.page2, Gtk.Label(label="Second tab"))

window = MainWindow()
window.connect("delete_event", Gtk.main_quit)
window.show_all()
Gtk.main()