from scipy.fft import fft
from scipy.signal import stft, istft
from scipy.signal.windows import boxcar
import sklearn
from sklearn.cluster import KMeans
import cmath
import math

def duet_source_separation(mic_data_folder, NUM_SOURCES):
    
    """DUET source separation algorithm. Write your code here.

    Args:
        mic_data_folder: name of folder (without a trailing slash) containing 
                         two mic datafiles `0.wav` and `1.wav`.

    Returns:
        NUM_SOURCES * recording_length numpy array, where NUM_SOURCES is the number of sources,
        and recording_length is the original length of the recording (in number of samples)

    """
    
    rate1 = scipy.io.wavfile.read(mic_data_folder + '/0.wav')[0]
    
    file1 = scipy.io.wavfile.read(mic_data_folder + '/0.wav')[1]
    samples1 = len(file1)
    # print(file1)
    rate2 = scipy.io.wavfile.read(mic_data_folder + '/1.wav')[0]
    file2 = scipy.io.wavfile.read(mic_data_folder + '/1.wav')[1]
    samples2 = len(file2)
    # print(file2)
    # plt.figure()
    # plt.plot(file1)
    
    # print(samples1)
    f1,t1,Zxx1 = stft(x = file1, fs=rate1, nperseg=2048)
    f2,t2,Zxx2 = stft(x = file2, fs=rate2, nperseg=2048)

    # print(Zxx1.shape)
    # print(Zxx2.shape)
    # print(f1)

    matrix = np.zeros((Zxx1.shape[0]-1,Zxx1.shape[1]))

    Zxx1 = Zxx1[1:,:]
    Zxx2 = Zxx2[1:,:]
    f1 = f1[1:]

    for i in range(Zxx1.shape[0]):
        for j in range(Zxx1.shape[1]):
            # print(i,j)
            stft1 = Zxx1[i][j]
            stft2 = Zxx2[i][j]
            ratio = stft2/(stft1+1e-20)
            theta = np.angle(ratio)
            matrix[i][j] = theta
    matrix = matrix.T / (2.*np.pi*f1)
    matrix = matrix.T
    matrix = matrix.flatten()
    matrix = matrix.reshape(-1, 1)
    

    kmeans = sklearn.cluster.KMeans(n_clusters=NUM_SOURCES)
    clusters = kmeans.fit_predict(matrix)
    labels = kmeans.labels_
    labels = labels.reshape(Zxx1.shape)
    
    output = []
    
    for i in range(NUM_SOURCES):
        inverse = Zxx1 * (labels == i)
        out = istft(inverse)[1]
        output.append(out.astype(np.int16)) 
        
    return output
