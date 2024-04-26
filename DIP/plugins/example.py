from DIP import DIPApp


class Extension:
    """Example of what a plugin should look like"""

    author = "Moosems"
    version = "0.1.0"

    def __init__(self, parent: DIPApp) -> None:
        self.parent = parent

        print(self.parent)

    def kill(self) -> None:
        # No attributes to destroy
        pass
