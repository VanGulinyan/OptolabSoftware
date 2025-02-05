import spc
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter


def get_spectra(path_file):
    path_to_file = path_file
    spectra = spc.File(path_to_file) # Reading .spc file
    x, y = (spectra.x, spectra.sub[0].y) # x-value, y-value
    y = savgol_filter(y, 19, 2)
    return x, y


def pl(y, y_d):
    y_t = (y - y_d)
    return y_t


date = ["2024", "12", "26"]
a = 0
for i in range(1, 106):
    if i < 10:
        a = "0" + str(i)
    else:
        a = i
    file_name = f"Spectrum_(LS6)-{date[0]}_{date[1]}_{date[2]}-ID_{a}.spc"

    file = fr"PATH\{date[0]}_{date[1]}_{date[2]}\{file_name}"
    [x, y] = get_spectra(file)

    plt.plot(x, y, label='исходный спектр')
    plt.xlabel("$\lambda, nm$")
    plt.ylabel("Intensity, a.e.")
    plt.ylim(0)
    plt.xlim(400, 900)
    plt.title(file_name)
    plt.savefig(fr"PATH\{date[0]}_{date[1]}_{date[2]}\{date[2]}.{date[1]}.{date[0]}.ID_{a}.jpg")
    plt.cla()
    # plt.axes()
    # plt.show()
    # plt.savefig('smart.pdf')

    # if name == 'smart.pdf':
    #     print(f'Saved to folder {path}')
    # # plt.show()

    np.savetxt(fr"PATH\{date[2]}.{date[1]}.{date[0]}\{'x_' + file_name + '.txt'}", x)
    np.savetxt(fr"PATH\{date[2]}.{date[1]}.{date[0]}\{'y_' + file_name + '.txt'}", y)

