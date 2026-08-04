from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from app.ui.widgets import (
    ChatWidget,
    InputWidget,
    StatusWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "AI Voice Assistant"
        )

        self.resize(
            900,
            700,
        )

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout(
            central,
        )

        self.chat = ChatWidget()

        self.input = InputWidget()

        self.status = StatusWidget()

        layout.addWidget(self.chat)

        layout.addWidget(self.input)

        layout.addWidget(self.status)
        self.input.message_sent.connect(
            self.chat.add_user_message,)