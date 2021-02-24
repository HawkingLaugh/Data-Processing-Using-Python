#%%
import urllib.request
import scipy.io.wavfile as wav
import os.path
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import wave
import numpy

if not os.path.isfile('english.wav'):
    urllib.request.urlretrieve(r'http://www.nch.com.au/acm/11k16bitpcm.wav', 'english.wav')
    # another way to get the file
    # response = urllib.request.urlopen(r'http://www.nch.com.au/acm/11k16bitpcm.wav')
    # wave = 'english.wav'
    # file = open(wave, 'wb+')
    # file.write(response.read())
    # file.close()
wave_file = wav.read('english.wav')
# print(wave_file[1])

# draw waveform graph of the audio

wavefile = wave.open('english.wav', 'r')
params = wavefile.getparams()
nchannels, sample_width, framerate, numfreams = params[:4]
sample_rate, data = wave_file
plt.subplot(2,1,1)
plt.title('Original')
plt.plot(data)

# set an new data as quiet with only 0.2x of original
newdata = data * 0.2
newdata = newdata.astype(numpy.int16)
wav.write('silent.wav', sample_rate, newdata)
plt.subplot(2,1,2)
plt.title('Quiet')
plt.plot(newdata)

plt.show()

result = pylab.specgram(data, NFFT=1024, Fs = sample_rate, noverlap=900)

pylab.show()
# %%
