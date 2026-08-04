from PySide6.QtWidgets import QLabel


class StatusWidget(QLabel):

    def __init__(self):

        super().__init__("Ready")

    def set_status(
        self,
        text: str,
    ):

        self.setText(text)