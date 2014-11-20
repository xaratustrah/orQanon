# orQanon

### About
A software synthesizer for the study of music theory and chords written in Python and the QT GUI library. It is a versatile tool that can be used to create and visualize sounds with varying frequencies and timbres. It can also be used a tuning fork for tuning instruments.

![orQanon](https://raw.githubusercontent.com/xaratustrah/orQanon/master/rsrc/screenshot.png)

### Description

Sound generation is started by pressing the **Enter key** or the **synth** button. The individual configurations of the generated sound is explained below from top to buttom:

#### Drawbars

Drawbars are shown as in historical Hammond B3 analog synthesizer, which in turn is similar to church organs. Historically register drawbars are pulled towards the player for louder sounds. Thats why the drawbars are drawn from top to bottom in the GUI. The values are from zero (closed/off register) to eight (loudest). Also the colors and numbers beneath the registers resemble those on the Hammond B3 organ. The numbers are in foot length of organ pipe. Sub harmonics are red, fundamental (8') and higher harmonics are white, whereas other intervals are in black.

#### Hilbert Scope

This pane shows the hilber transform of the signal for the purpose of visualization.

#### Tonic

The program assumes a tone range of a hypothetical piano with 108 keys, from C0 to B8. This means e.g. that the key A4, usually taken as frequency standard (tuning fork) in the musicology, is the 57th key. In order to avoid confusion, it should be mentioned that the successtion of the piano keys are actually according to an **equal tempered** piano keyboard. This does not limit the versatility of the software since the user can achieve any frequency by changing the tuning fork.


#### Tone

Here you can set the duration of the tone and ADSR (Attack, Decay, Sustain, Release) curve. Currently each transient is set to 1/5th of the duration.

#### 12 Tone interval ratios

Here one can choose the ratios governing the 12 tone chord scale. Currently Pythagorean and 12 tone equal temperament can be chosen. Of course this does not affect the single tone generation (drawbars).

#### GUI reset

This button is for convenience, in order to quickly reset the GUI to the original settings, which may be faster for the user.

#### Chord intervals

Chords can contain as many intervals as desired using toggle buttons. The interval names are chosen as usual in musical theory, minor **m**, major **M**, augmented **A**, diminished **d** and perfect **P** followed by the interval length. The number of buttons resembles a 12 tone scale. By default the perfect unison is checked, which means only one sound is generated.

#### Statusbar

Shows the fundamental frequency of the generated tone.

### Installation

orQanon requires python 3.4 and pyqt for Qt5, as well as port audio. These can easily be installed on OSX, Linux and Win. In the future an app bundle and a binary file will be generated for OSX and Win respectively for convenience.

