"""
** orQanon **

Software synthesizer for the study of music theory and chords.

- main window -

Xaratustrah

November 2014
"""

from PyQt5.QtWidgets import QMainWindow, QGraphicsScene
from PyQt5.QtGui import QPixmap, QKeyEvent
from orQanon_ui import Ui_mainWindow

from synth import *


class mainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):

        super(mainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        self.statusbar.showMessage('Press Enter to synthesize sound.')

        self.comboBox.clear()
        # self.tonals = {'C' : 1,
        # 'C#' : 2,
        # 'D' : 3,
        #           'D#' : 4,
        #           'E' : 5,
        #           'F' : 6,
        #           'F#' : 7,
        #           'G' : 8,
        #           'G#' : 9,
        #           'A' : 10,
        #           'A#' : 11,
        #           'B' : 12}
        # for key in self.tonals.keys():
        #     self.comboBox.addItem(key)
        tonals = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.comboBox.addItems(tonals)

        self.synth = Synth(1024, 44100)

        #pushButtons = ["self.pushButton_" + str(x) for x in range(1,14)] # seriously?!!
        self.pushButtons = [self.pushButton_1,
                            self.pushButton_2,
                            self.pushButton_3,
                            self.pushButton_4,
                            self.pushButton_5,
                            self.pushButton_6,
                            self.pushButton_7,
                            self.pushButton_8,
                            self.pushButton_9,
                            self.pushButton_10,
                            self.pushButton_11,
                            self.pushButton_12,
                            self.pushButton_13]

        self.verticalSliders = [self.verticalSlider_1,
                                self.verticalSlider_2,
                                self.verticalSlider_3,
                                self.verticalSlider_4,
                                self.verticalSlider_5,
                                self.verticalSlider_6,
                                self.verticalSlider_7,
                                self.verticalSlider_8,
                                self.verticalSlider_9]

        self.tonic_combo = 0  # C key

        # signals and slots

        self.pushButton_reset.pressed.connect(self.do_reset)
        self.pushButton_synth.pressed.connect(self.start_beep)
        self.comboBox.activated.connect(self.onActivated)
        #self.comboBox.activated[str].connect(self.onActivatedstr)
        self.pushButton_str12.pressed.connect(self.on_str12)
        self.pushButton_str22.pressed.connect(self.on_str22)
        self.pushButton_str32.pressed.connect(self.on_str32)
        self.pushButton_str42.pressed.connect(self.on_str42)

        self.pushButton_str11.pressed.connect(self.on_str11)
        self.pushButton_str21.pressed.connect(self.on_str21)
        self.pushButton_str31.pressed.connect(self.on_str31)
        self.pushButton_str41.pressed.connect(self.on_str41)

        self.pushButton_str13.pressed.connect(self.on_str13)
        self.pushButton_str23.pressed.connect(self.on_str23)
        self.pushButton_str33.pressed.connect(self.on_str33)
        self.pushButton_str43.pressed.connect(self.on_str43)

    def on_str11(self):
        self.tonic_combo = self.get_forth(self.tonic_combo)
        self.set_octave()

    def on_str21(self):
        self.tonic_combo = self.get_forth(self.tonic_combo)
        self.set_major()

    def on_str31(self):
        self.tonic_combo = self.get_forth(self.tonic_combo)
        self.set_minor()

    def on_str41(self):
        self.tonic_combo = self.get_forth(self.tonic_combo)
        self.set_seventh()

    def on_str12(self):
        self.set_octave()

    def on_str22(self):
        self.set_major()

    def on_str32(self):
        self.set_minor()

    def on_str42(self):
        self.set_seventh()

    def on_str13(self):
        self.tonic_combo = self.get_fifth(self.tonic_combo)
        self.set_octave()

    def on_str23(self):
        self.tonic_combo = self.get_fifth(self.tonic_combo)
        self.set_major()

    def on_str33(self):
        self.tonic_combo = self.get_fifth(self.tonic_combo)
        self.set_minor()

    def on_str43(self):
        self.tonic_combo = self.get_fifth(self.tonic_combo)
        self.set_seventh()

    def get_forth(self, n):
        a = n - 7
        if a < 0:
            return a + 12
        else:
            return a

    def get_fifth(self, n):
        a = n + 7
        if a > 12:
            return a - 12
        else:
            return a

    def set_octave(self):
        for i in range(len(self.pushButtons)):
            self.pushButtons[i].setChecked(False)
        self.pushButtons[0].setChecked(True)
        self.pushButtons[12].setChecked(True)
        self.start_beep()

    def set_minor(self):
        for i in range(len(self.pushButtons)):
            self.pushButtons[i].setChecked(False)
        self.pushButtons[0].setChecked(True)
        self.pushButtons[3].setChecked(True)
        self.pushButtons[7].setChecked(True)
        self.start_beep()

    def set_major(self):
        for i in range(len(self.pushButtons)):
            self.pushButtons[i].setChecked(False)
        self.pushButtons[0].setChecked(True)
        self.pushButtons[4].setChecked(True)
        self.pushButtons[7].setChecked(True)
        self.start_beep()

    def set_seventh(self):
        for i in range(len(self.pushButtons)):
            self.pushButtons[i].setChecked(False)
        self.pushButtons[0].setChecked(True)
        self.pushButtons[4].setChecked(True)
        self.pushButtons[7].setChecked(True)
        self.pushButtons[11].setChecked(True)
        self.start_beep()


    def onActivated(self, number):
        self.tonic_combo = number

    # def onActivatedstr(self,text):
    # print(text)

    def do_reset(self):
        for i in range(len(self.pushButtons)):
            self.pushButtons[i].setChecked(False)
        self.pushButtons[0].setChecked(True)

        for i in range(len(self.verticalSliders)):
            self.verticalSliders[i].setValue(0)
        self.verticalSlider_3.setValue(8)

        self.doubleSpinBox_1.setValue(0.5)
        self.doubleSpinBox_2.setValue(440.0)
        self.spinBox.setValue(4)
        self.comboBox.setCurrentText('C')
        self.tonic_combo = 0  # C key
        self.radioButton_1.setChecked(True)
        self.radioButton_2.setChecked(False)
        self.checkBox.setChecked(True)

    def keyPressEvent(self, event):

        if type(event) == QKeyEvent:
            # here accept the event and do something
            if event.key() == 16777220:  # code enter key
                self.start_beep()
            event.accept()
        else:
            event.ignore()


    def start_beep(self):

        drawbars = str(self.verticalSlider_1.value()) + \
                   str(self.verticalSlider_2.value()) + \
                   str(self.verticalSlider_3.value()) + \
                   str(self.verticalSlider_4.value()) + \
                   str(self.verticalSlider_5.value()) + \
                   str(self.verticalSlider_6.value()) + \
                   str(self.verticalSlider_7.value()) + \
                   str(self.verticalSlider_8.value()) + \
                   str(self.verticalSlider_9.value())

        duration = self.doubleSpinBox_1.value()

        tonic_number = (12 * self.spinBox.value() + self.tonic_combo)
        tonic_frequency = 2 ** (( tonic_number - 57) / 12) * self.doubleSpinBox_2.value()
        self.statusbar.showMessage(
            'Fundamental frequency: {0:.2f} Hz. Press Enter to synthesize next sound.'.format(tonic_frequency))

        if self.radioButton_2.isChecked():
            frequencies = [tonic_frequency * 2 ** (x / 12) for x in range(len(self.pushButtons))]
        else:
            frequencies = [tonic_frequency * x for x in
                           [1, 256 / 243, 9 / 8, 32 / 27, 81 / 64, 4 / 3, 1024 / 729, 729 / 512, 3 / 2, 128 / 81,
                            27 / 16, 16 / 9, 243 / 128]]

        for i in range(len(self.pushButtons)):
            if not self.pushButtons[i].isChecked():
                frequencies[i] = 0

        t, x = self.synth.make_chord(frequencies, drawbars, duration, self.checkBox.isChecked())

        self.synth.play(x)
        xbar, inst_ph = self.synth.make_analytical(x)
        filename = 'synth.png'
        self.synth.plot_hilbert(xbar, filename)

        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(filename))
        self.graphicsView.setScene(scene)
