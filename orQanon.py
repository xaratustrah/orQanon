#!/usr/bin/env python
"""
** orQanon **

Software synthesizer for the study of music theory and chords.

- main application -

Xaratustrah

November 2014
"""

import sys
# sys.setrecursionlimit(300000)
from PyQt5.QtWidgets import QApplication
from orQanon_mainWindow import mainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = mainWindow()
    form.show()
    sys.exit(app.exec_())
