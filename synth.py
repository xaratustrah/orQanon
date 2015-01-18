"""
** orQanon **

Software synthesizer for the study of music theory and chords.

- synth engine -

Xaratustrah

November 2014
"""

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert


class Synth:
    def __init__(self, chunk, rate):
        """Make the instance"""

        self.chunk = chunk
        self.rate = rate
        self.port = pyaudio.PyAudio()
        self.stream = self.port.open(format=pyaudio.paFloat32, channels=2, rate=rate, output=True,
                                     frames_per_buffer=chunk)
        self.adsr = 0.2


    def play(self, x):
        """ play the sound """
        self.stream.write(x.astype(np.float32).tostring())


    def stop(self):
        """ Stop the stream"""
        self.stream.stop_stream()

    @staticmethod
    def exponential(t, sl):

        y = np.e ** (-t * 7 / sl)
        return y[1:sl]

    def make_chord(self, frequencies, draw_bars, duration, make_adsr=True):

        fs = self.rate
        t = np.arange(0, duration, 1 / fs)
        x = np.zeros(len(t))

        for i in range(len(frequencies)):
            x += int(draw_bars[0]) / 8 * np.sin(2 * np.pi * frequencies[i] / 16 * 8 * t)  # 16 '
            x += int(draw_bars[1]) / 8 * np.sin(2 * np.pi * frequencies[i] / 16 / 3 * 8 * t)  # 16/3 '
            x += int(draw_bars[2]) / 8 * np.sin(2 * np.pi * frequencies[i] / 8 * 8 * t)  # 8 '
            x += int(draw_bars[3]) / 8 * np.sin(2 * np.pi * frequencies[i] / 4 * 8 * t)  # 4 '
            x += int(draw_bars[4]) / 8 * np.sin(2 * np.pi * frequencies[i] / 8 / 3 * 8 * t)  # 8/3 '
            x += int(draw_bars[5]) / 8 * np.sin(2 * np.pi * frequencies[i] / 2 * 8 * t)  # 2 '
            x += int(draw_bars[6]) / 8 * np.sin(2 * np.pi * frequencies[i] / 8 / 5 * 8 * t)  # 8/5 '
            x += int(draw_bars[7]) / 8 * np.sin(2 * np.pi * frequencies[i] / 4 / 3 * 8 * t)  # 4/3 '
            x += int(draw_bars[8]) / 8 * np.sin(2 * np.pi * frequencies[i] / 1 * 8 * t)  # 1 '
        if make_adsr:
            # new version
            # seg = int(len(t) / 4)  # define a segment of the time signal
            # difference = len(t) - 4 * seg
            # z = np.concatenate(
            #     (1 - self.exponential(t, seg), .25 * self.exponential(t, seg) + .75, .75 * np.ones((1, seg - 1))[0, :],
            #      0.75 * self.exponential(t, seg)
            #     )
            # )
            # x *= np.append(z, np.zeros((len(t) - len(z))))  # Append zeros to compensate for the int operation

            # old version
            x *= 1 - np.e ** (-t * 5 / self.adsr / duration)

        return t, x

    def make_analytical(self, x):
        """Make an analytical signal from the real signal"""

        y = hilbert(x)
        ii = np.real(y)
        qq = np.imag(y)
        x_bar = np.vectorize(complex)(ii, qq)
        ins_ph = np.angle(x_bar) * 180 / np.pi
        return x_bar, ins_ph


    def plot_hilbert(self, x_bar, filename):
        """Show Hilbert plot."""

        fig = plt.figure()
        axes = plt.gca()
        axes.set_xlim([-4, 4])
        axes.set_ylim([-4, 4])
        plt.plot(np.real(x_bar)[0:600], np.imag(x_bar)[0:600], color="#000080")
        plt.grid(False)
        plt.axis('off')
        fig.set_size_inches(4.5, 4.5)
        fig.savefig(filename, dpi=600)
        fig.savefig(filename)


    def __del__(self):
        """ Destructor """

        # self.stream.stop_stream()
        # self.stream.close()
        # self.port.terminate()

