from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QWidget,
)


class InputWidget(QWidget):

    message_sent = Signal(str)

    def __init__(self):

        super().__init__()

        layout = QHBoxLayout(self)

        self.input = QLineEdit()

        self.button = QPushButton("Send")

        layout.addWidget(self.input)

        layout.addWidget(self.button)

        self.button.clicked.connect(
            self._send
        )

        self.input.returnPressed.connect(
            self._send
        )

    def _send(self):

        text = self.input.text().strip()

        if not text:
            return

        self.message_sent.emit(text)

        self.input.clear()