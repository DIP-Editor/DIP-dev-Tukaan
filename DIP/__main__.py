from tukaan import App, MainWindow

def main() -> None:
    root = App(name="DIP")
    window = MainWindow(title="DIP") #noqa: F841
    root.run()
