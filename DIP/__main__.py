from tukaan import App, MainWindow, Button, Window
from tukaan._tcl import Tcl
from .plugins import get_extension_info
from gc import collect


class DIPApp(App):
    """The App class to be instantiated in main()"""

    def __init__(self) -> None:
        App.__init__(self, name="DIP")
        self.windows = []

        self.main_window = DIPMainWindow(self)


class DIPMainWindow(MainWindow):
    """The defacto MainWindow sublass for the DIP editor"""

    def __init__(self, parent: DIPApp) -> None:
        self.parent = parent
        MainWindow.__init__(self)

        # TODO: remove placeholder widget
        button = Button(self, text="Click Me!", tooltip="Placeholder Widget ;)")
        button.grid()

        # Resize Window
        width = Tcl.call(int, "winfo", "reqwidth", button)
        height = Tcl.call(int, "winfo", "reqheight", button)
        self.width = width
        self.height = height


class DIPWindow(Window):
    """The defacto Window sublass for the DIP editor"""

    def __init__(self, parent: DIPApp) -> None:
        self.parent = parent
        Window.__init__(self, self.parent)


def main(no_loop: bool = False) -> None:
    """Main function for the DIP Code Editor"""
    app = DIPApp()
    extension = get_extension_info(
        "DIP/plugins/example.py"
    )
    if extension is not None:
        print(extension)
        instance = extension[0].Extension(app)
        instance.kill()
        del instance, extension
        collect()


    if not no_loop:
        app.run()
