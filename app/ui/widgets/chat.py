from PySide6.QtWidgets import QTextEdit


class ChatWidget(QTextEdit):

    def __init__(self):

        super().__init__()

        self.setReadOnly(True)

    def add_user_message(
        self,
        message: str,
    ):

        self.append(
            f"<b>You:</b> {message}"
        )

    def add_assistant_message(
        self,
        message: str,
    ):

        self.append(
            f"<b>Assistant:</b> {message}"
        )