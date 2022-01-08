import numpy as np
import matplotlib.pyplot as plt

# 时长为1秒
t = 1
# 采样率为60hz
fs = 60
t_split = np.arange(0, t * fs)


# 1hz与25hz叠加的正弦信号
x_1hz = t_split * 1 * np.pi * 2 / fs
x_25hz = t_split * 25 * np.pi * 2 / fs
signal_sin_1hz = np.sin(x_1hz)
signal_sin_25hz = np.sin(x_25hz)

signal_sin = signal_sin_1hz + 0.25 * signal_sin_25hz

def hn(wc, n):
    if n == 0:
        return wc / np.pi
    else:
        return np.sin(wc * n) / (n * np.pi)

def hanning(M, n):
    return 0.5 + 0.5 * np.cos((2 * n * np.pi) / (M - 1) )

# TODO: 补全这部分代码
# 通带边缘频率为10Hz，
# 阻带边缘频率为22Hz，
# 阻带衰减为44dB，窗内项数为17的汉宁窗函数
# 构建低通滤波器
# 函数需要返回滤波后的信号
def filter_fir(input):
    #print("input", input)
    M = 17                                  # 窗内项数
    fc = 10 + (22 - 10) / 2                 # 截止频率
    wc = 2 * np.pi * fc / fs                # 理想数字滤波器的截止频率
    # 汉宁窗窗函数为
    start = int((-M +  1) / 2)              # -8
    stop =  int((M - 1)/2)                  # 8
    ha = [hanning(M, n) for n in range(start, stop + 1)]

    # 理想数字滤波器函数为
    hin = [hn(wc, n) for n in range(start, stop + 1)]

    # 滤波器的冲激响应
    h = [hin[n] * ha[n] for n in range(M)] 

    y_n = np.zeros(fs)
    # convolution
    for n in range(len(input)):
        for k in range(M):
            if (n >= k):
                y_n[n] += h[k] * input[n-k]
            else:
                break

    return y_n
    pass

# TODO: 首先正向对信号滤波(此时输出信号有一定相移)
# 将输出信号反向，再次用该滤波器进行滤波
# 再将输出信号反向
# 函数需要返回零相位滤波后的信号
def filter_zero_phase(input):
    y1 = filter_fir(input)
    x1 = np.flip(y1)
    y2 = filter_fir(x1)
    return np.flip(y2)
    pass


if __name__ == "__main__":
    delay_filtered_signal = filter_fir(signal_sin)
    zerophase_filtered_signal = filter_zero_phase(signal_sin)

    plt.plot(t_split, signal_sin, label = 'origin')
    plt.plot(t_split, delay_filtered_signal, label = 'fir')
    plt.plot(t_split, zerophase_filtered_signal, label = 'zero phase')

    plt.show()
