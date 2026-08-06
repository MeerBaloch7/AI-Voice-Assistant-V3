import asyncio
import sys

from PySide6.QtWidgets import QApplication
from qasync import QEventLoop

from app.ui.window import MainWindow


def main():

    app = QApplication(sys.argv)

    loop = QEventLoop(app)

    asyncio.set_event_loop(loop)

    window = MainWindow()

    window.show()

    with loop:

        loop.run_forever()


if __name__ == "__main__":
    main()