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

import asyncio

from app.ui.controller import UIController


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
            self.on_message,
        )
        self.controller = UIController(self)
    
    def on_message(
        self,
        message: str,
    ):

        self.chat.add_user_message(
            message,
        )

        asyncio.create_task(
            self.controller.send_message(
                message,
            )
        )