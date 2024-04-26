from tukaan import App, MainWindow


def main(no_loop: bool = False) -> None:
    root = App(name="DIP")
    window = MainWindow(title="DIP")  # noqa: F841
    if not no_loop:
        root.run()
