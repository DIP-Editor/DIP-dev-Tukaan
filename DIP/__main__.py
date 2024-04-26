from tukaan import App, MainWindow, KolorScheme, Button
from tukaan._tcl import Tcl
from platform import system


def main(no_loop: bool = False) -> None:
    """Main function for the DIP Code Editor"""
    root = App(name="DIP")
    window = MainWindow(title="DIP")  # noqa: F841

    # Get clam theme
    if system() not in {"Darwin", "Windows"}:
        root.theme = KolorScheme  # type: ignore

    # TODO: remove placeholder widget
    button = Button(window, text="Click Me!", tooltip="Placeholder Widget ;)")
    button.grid()

    # Resize Window
    width = Tcl.call(int, "winfo", "reqwidth", button)
    height = Tcl.call(int, "winfo", "reqheight", button)
    window.width = width
    window.height = height

    if not no_loop:
        root.run()
