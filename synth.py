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
        self.stream = self.port.open(format=pyaudio.paFloat32, channels=2, rate=rate, output=True, frames_per_buffer=chunk)
        self.adsr = 0.2


    def play(self, x):
        """ play the sound """
        self.stream.write(x.astype(np.float32).tostring())

        
    def stop(self):
        """ Stop the stream"""
        self.stream.stop_stream()

        
    def make_chord(self, frequencies, drawbars, duration, make_adsr = True):

        fs = self.rate
        t = np.arange(0, duration, 1/fs)
        x = np.zeros(len(t))

        for i in range (len(frequencies)):
            x +=  int(drawbars[0])/8 * np.sin(2 * np.pi * frequencies[i]/ 16 * 8 * t) # 16 '
            x +=  int(drawbars[1])/8 * np.sin(2 * np.pi * frequencies[i]/ 16 / 3 * 8 * t) # 16/3 '
            x +=  int(drawbars[2])/8 * np.sin(2 * np.pi * frequencies[i]/ 8 * 8 * t) # 8 '
            x +=  int(drawbars[3])/8 * np.sin(2 * np.pi * frequencies[i]/ 4 * 8 * t) # 4 '
            x +=  int(drawbars[4])/8 * np.sin(2 * np.pi * frequencies[i]/ 8 / 3 * 8 * t) # 8/3 '
            x +=  int(drawbars[5])/8 * np.sin(2 * np.pi * frequencies[i]/ 2 * 8 * t) # 2 '
            x +=  int(drawbars[6])/8 * np.sin(2 * np.pi * frequencies[i]/ 8 / 5 * 8 * t) # 8/5 '
            x +=  int(drawbars[7])/8 * np.sin(2 * np.pi * frequencies[i]/ 4 / 3 * 8 * t) # 4/3 '
            x +=  int(drawbars[8])/8 * np.sin(2 * np.pi * frequencies[i]/ 1 * 8 * t) # 1 '
        if make_adsr:
            x *= 1-np.e**(-(t)*5/self.adsr/duration)

        return t, x
            
    def make_adsr(fs, l = 1, rt = 0.2):
        """Make an ADSR curve."""
        
        t = np.arange(0, l, 1/fs)
        return t, x

    def make_analytical(self, x):
        """Make an analitical signal from the real signal"""

        y= hilbert(x)
        I = np.real(y)
        Q = np.imag(y)
        xbar = np.vectorize(complex)(I,Q)
        ins_ph = np.angle(xbar)*180/np.pi
        return xbar, ins_ph

    
    def plot_hilbert(self, xbar, filename):
        """Show Hilbert plot."""

        fig = plt.figure()
        axes = plt.gca()
        axes.set_xlim([-4,4])
        axes.set_ylim([-4,4])
        plt.plot(np.real(xbar)[0:600], np.imag(xbar)[0:600], color="#000080")
        plt.grid(False)
        plt.axis('off')
        fig.set_size_inches(4.5,4.5)
        fig.savefig(filename,dpi=600)
        fig.savefig(filename)

    
    def __del__(self):
        """ Destructor """
        
        self.stream.stop_stream()
        self.stream.close()
        self.port.terminate()

