from scipy.fft import fft, ifft
from numpy import convolve
from numpy.polynomial import Polynomial as P
from numpy import polymul, pad
import numpy as np
from numpy.fft import rfft, irfft
from numpy import multiply

length = 100


def fft_test(arr_a, arr_b):  # fft based polynomial multiplication

    arr_a1 = pad(arr_a, (0, length), "constant")
    arr_b1 = pad(arr_b, (0, length), "constant")
    a_f = fft(arr_a1)
    b_f = fft(arr_b1)

    c_f = [0] * (2 * length)

    for i in range(len(a_f)):
        c_f[i] = a_f[i] * b_f[i]

    return ifft(c_f)


def fftrealpolymul(arr_a, arr_b):  # fft based real-valued polynomial multiplication

    L = len(arr_a) + len(arr_b) - 1
    a_f = rfft(arr_a, L)
    b_f = rfft(arr_b, L)

    return irfft(multiply(a_f, b_f))


if __name__ == "__main__":
    # max degree is 1, so FFT for one would be omega^2
    # max degree for three is 3*2
    a = [1, 1, 0, 0, 0, 0, 0, 0]
    b = [1, 1, 0, 0, 0, 0, 0, 0]
    c = [1, 1, 0, 0, 0, 0, 0, 0]
    ffta = fft(a)
    fftb = fft(b)
    fftc = fft(c)
    # these two below should be the same
    print(np.round(ifft(ffta * fftb * fftc), 1))  # O(nlogn())
    print(convolve(convolve(a, b), c))  # O(n^2)
