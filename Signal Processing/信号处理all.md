信号处理原理

[TOC]

# 1. 信号的基本概念与数学基础

## 信号的概念

what is a signal? 

why does quality of sampling frequency affect audio quality?

what is signal processing? what is its purpose?

- purpose: remove redundant and minor components of signal, turn signal into a form that is easy to analyze and recognize, encoding (turn signal into form that is easy to transmit) and decoding (recover the original signal from encoded signal)
- question: how can the removal method ensure that signal is undistorted, will there be information loss in the signal during transformation of the domain, can decoded signal be exactly the same as signal before encoding

DPS is predictable and repeatable, small in size, low power consumption, high-flexibility, programmability, stable, noise accumulation can be controlled, easy to debug, simple hardware.

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230211657975.png" alt="image-20201230211657975" style="zoom:67%;" />

## 信号的描述

信号函数，序列 - function, sequence to describe signal, 

波形描述 - waveform showing relationship between function and independent variable

确定信号 - given value of independent variable, the value of the signal be uniquely determined, if not, then it is 随机信号

时域波形 (time vs voltage) vs 频谱图 (frequency vs magnitude)

周期信号 vs 非周期信号 $f(t)=f(t+T), \forall t \in R$

- 周期信号的周期 - smallest value of T
- 非周期信号 - can be seen as periodic signals with infinite periods

### 正余弦信号

![image-20201230213113881](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230213113881.png)

1. K 为振幅
2. $\omega$ 为角频率
3. $\theta$ 为初相位

### Sa函数信号

 $Sa(t) = \frac{sin(t)}{t}$ 

1. Sa 函数是偶函数
2. Sa 函数过零点位置 $K\pi$ , $K$ 为整数
3. 过零区间：width between zeroes is $\pi$, except for interval interval near the origin which is $2\pi$

![image-20201230213448394](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230213448394.png)

### 指数函数

## 欧拉公式

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230213555276.png" alt="image-20201230213555276" style="zoom:50%;" />

![image-20201230213741652](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230213741652.png)

实信号 - value of signal is real, 复信号 if its imaginary

## 函数分解

- 正交基（orthogonal basis）与标准正交基(orthonormal basis)
- V be  Euclid空间， 非零向量 $a_1,a_2,...,a_m \in V$, 
  - if they are orthogonal to each other, called 正交向量组
  - number of vectors contained in the 正交向量组 in n-dimensional Euclidean space is $\leq n$
  - in n-dimensional Euclidean space, the orthogonal vector group consisting of n vectors is called 正交基
  - the 正交基 composed of unit vectors is called 标准正交基
  - 完备的正交函数集

## 信号的基本运算

### 常规运算

the value of the signal after four arithmetic operations at **any point** is defined as the result of the same four arithmetic operations on the original signal at the **same point**

### 波形变换

时移运算： translate the waveform of the original signal f(t) by b units along the horizontal axis

反褶运算: reflect across f(t) axis (deconvolution)

压扩运算: stretch horizontally

### 数学运算

微分运算 describes the phenomenon of change

积分运算 describes cumulative phenomena

信号的能量定义: if the energy of the signal is limited, called 能量有限信号，称为能量信号

![image-20201228221726764](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201228221726764.png)

信号的功率定义: if the power of the signal is limited, it is called 能量有限信号，称为功率信号

![image-20201228221737356](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201228221737356.png)

### 相互运算

#### 卷积

f, g为两个连续时间信号函数

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230214847200.png" alt="image-20201230214847200" style="zoom:67%;" />

离散时间信号

![image-20201228222345432](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201228222345432.png)

f, g can be integrated, and convolution is bounded 

it is not the area of the intersecting part of the graph, but the area of the multiplication result function 

> A convolution is **an integral that expresses the amount of overlap of one function g as it is shifted over another function** f

during the t-axis sliding process of the unfolded signal of the signal, the area of the new signal obtained by multiplying the coincident (occupying the same area in at the same time) part of the signal with t is the waveform of the convolution of the two signal

性质：交换律，分配律，结合律

### 卷积的微分

applying similar deductions can derive operation law of convolutions high order derivative or multiple integrals

$(f_1 * f_2)^{(n)}(t) = f_1^{(m)}(t)*f_2^{(n-m)}(t)$

in the formula above, m, n, and n-m are the order of the derivative when they are integers, and the number of double integrations when they are negative integers.

### 相关运算 

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230215431938.png" alt="image-20201230215431938" style="zoom: 67%;" />

自相关运算： 函数自己与自己求相关: use autocorrelation function to detect the quasi-period(准周期信号) of the quasiperiodic signal

### 奇异信号

#### 单位斜边信号

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201229121209779.png" alt="image-20201229121209779" style="zoom:50%;" />

#### 单位阶跃信号

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201229121341127.png" alt="image-20201229121341127" style="zoom:67%;" />

- $R(t) = \int^{t}_{-\infty}{u(t)dt}$

- $\frac{dR(t)}{dt}=u(t)$

#### 单位矩形脉冲信号

![image-20201229121538578](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201229121538578.png)

通过单位阶跃信号的运算结果, it is no longer necessary to express the signal in the form of segments

when other signals are multiplied by a rectangular signal, the information of the other signals will retained only in the interval corresponding to the rectangular signal

#### 符号函数信号

![image-20201229122440713](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201229122440713.png)

$sgn(t)=2u(t)-1$

#### 单位冲激信号

use to describe phenomena in nature that have a short duration after occurrence

suppose 冲激信号 has total impulse pulse intensity, and its integral over the entire time domain is equal to the intensity value, and the value of the function at the points other than the impulse point is zero.

狄拉克定义是 Dirac

$\int^{\infty}_{-\infty}{\delta(t)dt=1}, \delta(t)=0,(t\neq 0)$

波形表示： draw a line with an arrow at the impulse point (t=to). the direction and length of the line are consistent with the sign and the magnitude of the impulse intensity

![image-20201229123403958](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201229123403958.png)

强度E在$t_0$等于$\delta_{E, t_o}(t)=E\delta(t-t_0)$

![image-20201229123605779](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201229123605779.png)

ordinary functions take limit approximation

$\delta(t)=lim_{\tau\rightarrow0}{\frac{G_\tau}{\tau}}$

$f(t)*\delta(t)=f(t)$

性质：

1. 扩充：move sampling characteristics: the convolution of a function and 单位冲激函数 is the equivalent to shifting the function the 冲激点位置 of the 单位冲激函数 $f(t)*\delta(t-t_o)=f(t-t_o)$

2. 函数$\rightarrow$值映射关系: the 冲激函数 can filter out the function value at the zero point from the 检验函数

   $\int^{\infty}_{-\infty}{\delta(t)\phi(t)}=\phi(0)$

   the above formula only borrows the form of integration, which means: the process of the impulse function assigning (赋予) a number to the test function , so it cannot be considered by ordinary integration problems: the reason for borrowing the form of integral is that it is in conformity with the corresponding properties of the integral operation, and ordinary integral operations actually produces a value

3. <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201229131033582.png" alt="image-20201229131033582" style="zoom:67%;" />

4. <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201229131152816.png" alt="image-20201229131152816" style="zoom:67%;" />

# 2. 信号的分解

## 信号的分解方法

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230221422821.png" alt="image-20201230221422821" style="zoom:50%;" />

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230221244458.png" alt="image-20201230221244458" style="zoom:67%;" />

## 函数的正交分解

1. 平方可积
2. 正交，内积于共轭：函数正交的充要条件时他们内积为0，当f1和f2互不含有对方分量
3. 正交函数集
4. 标准正交函数
5. 完备正交函数集

when the function f(t) has a continuous first derivative and a piecewise continuous second derivative in the interval [t1, t2], f(t) can be represented by a complete set of orthogonal functions ${\phi_i(t)}$, which is $f(t)=\Sigma^{\infty}_{i=1}{c_i\phi_i(t)}$, $c_i$

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230222035321.png" alt="image-20201230222035321" style="zoom:67%;" />

### 帕斯瓦尔定理

![image-20201230222244046](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230222244046.png)

it shows that when an orthogonal function set is used to accurately represent a signal, the energy of the signal is equal to the sum of the energy of the components of the corresponding orthogonal functions

## 信号的正交变换

### 信号的级数展开

![image-20201230222348063](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230222348063.png)

generally the coefficient $c_i$ is determined using some integral form of the signal $x(t)$,  this integral formula(formula for finding expansion coefficient), is called signal transformation

### 信号的正交变换

Karhunen-Loeve变换

![image-20201230222540886](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230222540886.png)

$\phi_i(t)$为标准晚辈正交基

### 【特例】周期信号的正交分解

满足狄义赫利条件(Dirichlet condition)的**周期函数**都可以在一组完备的正交基函数上展开成为无穷级数

1. number of discontinuities is limited
2. number of extreme points is limited
3. absolute integral has limited value

if the complete orthogonal function set is a trigonometric function set or an exponential function set, the series generated by the periodic function is the 傅里叶级数

- 三角形式傅里叶级数
- 复指数形式傅里叶级数

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230222816333.png" alt="image-20201230222816333" style="zoom:67%;" />

### 三角形式傅里叶级数

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230223017623.png" alt="image-20201230223017623" style="zoom:50%;" />

the relationship between time domain and frequency domain: Percival Function

the average power of a periodic signal is equal to the sum of the squares of the effective values of the harmonic components in the Fourier series expansion, and it also conserves energy in the real-time and frequency domains 

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230223825069.png" alt="image-20201230223825069" style="zoom:67%;" />

### 复指数形式傅里叶级数

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230223949797.png" alt="image-20201230223949797" style="zoom:67%;" />

偶周期信号的FS<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230224608916.png" alt="image-20201230224608916" style="zoom: 50%;" />

寄周期信号的FS<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230224641639.png" alt="image-20201230224641639" style="zoom:50%;" />

### 傅里叶变换 - 频谱 

![image-20201230224656253](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230224656253.png)

周期信号的傅里叶频谱特点

1. 仅在一些离散频率点$nw_1$上有值（谱波）
2. 离散间隔为$w_1=2\pi f_1 = 2\pi /T_1$
3. Fn是双边谱,正负频率的频谱幅度相加才是实际幅度 (Fn is the bilateral spectrum, and the addition of the spectrum amplitude of the positive and negative frequencies is the actual amplitude)
4. 信号的功率为$\sum_{-\infty}^{\infty}{|F_n|^2}$

### 周期信号的FS 

周期矩形脉冲信号的FS

suppose the pulse width of periodic rectangular pulse signal f(t) is $\tau$, the pulse amplitude is E, and the repetition period is FS of the T1-shaped pulse signal

![image-20201229165121608](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201229165121608.png)

the spectral line is the Sa function, interval of line is ... 

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230225632832.png" alt="image-20201230225632832" style="zoom:50%;" />

谱线包络线$\frac{E\tau}{T_1}{sa(\frac{w\tau}{2})}$

- in the frequency domain, the energy is mainly concentrated within the first zero point
- 常把$\frac{-2\pi}{\tau}\leq|w|\leq\frac{2\pi}{\tau}$这段频率范围称为举行信号的**频带宽度**（bandwidth），简称带宽
- 带宽只与脉冲的脉宽有关，而与脉高和周期均无关。

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230230242383.png" alt="image-20201230230242383" style="zoom:50%;" />

### 周期vs非周期信号的FS

aperiodic signals can be regarded as periodic signals whose period T tends to infinity

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230230656562.png" alt="image-20201230230656562" style="zoom:67%;" />

从频谱分量到频谱密度 spectral components to spectral density

- physical meaning: both signals must of energy, energy is conserved
- mathematical meaning: sum of infinitely many and infinitely small quantities, limit since it may be equal to a finite value, previous question only said that each component became an infinitesimal quantity, but did not say that the sum is zero

## 非周期信号的FT

is there a better way of defining 非周期傅里叶频谱?

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230231924486.png" alt="image-20201230231924486" style="zoom:67%;" />

信号的傅里叶变换一般为复值函数

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230232005862.png" alt="image-20201230232005862" style="zoom:67%;" />

### 物理信号的例子

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230232208314.png" alt="image-20201230232208314" style="zoom:67%;" />

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230232224398.png" alt="image-20201230232224398" style="zoom:67%;" />

### FT于IFT的唯一性于可逆性

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230232317001.png" alt="image-20201230232317001" style="zoom:67%;" />

## 梳理：FT与FS的关系

**Fourier series is an expansion of periodic signal as a linear combination of sines and cosines** while Fourier transform is the process or function used to convert signals from time domain in to frequency domain.

|                | FS                              | FT                   |
| -------------- | ------------------------------- | -------------------- |
| 被分析对象     | 周期信号                        | 非周期信号           |
| 频率定义域     | 离散频率，谐波频率处 (harmonic) | 连续频率，整个频率轴 |
| 哈桑农户值意义 | 频率分量的数值                  | 频率分量的密度值     |

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230232809745.png" alt="image-20201230232809745" style="zoom:50%;" />

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230233129117.png" alt="image-20201230233129117" style="zoom: 50%;" />

The coefficient $F_n$ of the nth harmonic component of the periodic signal, the corresponding frequency is nw1, and the coefficient value is equal to the value of the spectral density function F(w) of the non-periodic signal f(t) at the frequency $nw_1$ divided by T1

推论： If the signal f(t) is periodically repeated with different cycles, for these different periodic signals, their FS coefficients are all related to the FT of the signal f(t)

### FS与非周期信号

if f(t) is a 非周期信号, the 分解区间 is limited (to, to + T1), that is, FS is only valid in the interval (t0, t0+1)

FS is a kind of 正交分解, so it can be also used to expand (分解) a segment of 非周期信号 in a specific interval

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230234109015.png" alt="image-20201230234109015" style="zoom:67%;" />

### FT与周期信号

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230234008159.png" alt="image-20201230234008159" style="zoom:67%;" />

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230234433089.png" alt="image-20201230234433089" style="zoom:50%;" />

### 实例：典型非周期信号的FT

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230235020198.png" alt="image-20201230235020198" style="zoom:50%;" />

### FT的性质

1. 线性运算 

   <img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230235214052.png" alt="image-20201230235214052" style="zoom:67%;" />

2. FT的反褶和共轭性

   <img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201230235246918.png" alt="image-20201230235246918" style="zoom:50%;" />

3. IFT和FT的对偶性 

   1. FT与IFT的变换核函数是共轭对称的
   2. $F(t) \Leftrightarrow 2\pi f(-\omega)$

4. FT的尺度变换性

   <img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231000535437.png" alt="image-20201231000535437" style="zoom:50%;" />

5. <img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231000609418.png" alt="image-20201231000609418" style="zoom: 50%;" />

6. FT的频移特性

   Theoretically, multiply the time domain signal by a complex exponential signal, and the frequency spectrum of the original signal will be moved to the frequency of the complex exponential signal.

   In practical applications, the Euler formula is used to multiply the sine or cosine number to achieve the purpose of spectrum shifting.

   ![image-20201231001234479](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231001234479.png)

7. FT积分运算

   <img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231001813606.png" alt="image-20201231001813606" style="zoom:50%;" />

8. FT卷积定理

   <img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231001842103.png" alt="image-20201231001842103" style="zoom:50%;" />

9. FT时域相关性定理

   <img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231001920795.png" alt="image-20201231001920795" style="zoom:50%;" />

## 采样与量化的概念

采样 - turn analog signal to digital signal, sampled at intervals, amplitude value is sampled on the analog signal waveform

采样周期$T_s$ 

- 其倒数称为采样频率$f_s=1/T_s$，​
- 采样角频率$\omega_s=2\pi/T_s$

## 采样与采样定理

study relationship between continuous-time signals and discrete-time signals

questions: 

1. during what conditions can continuous time signals be replaced with its discrete time samples without losing original information? 
2. how to restore original continuous-time signal from discrete-time samples of the continuous time signal without distortion?

### 采样的数学模型

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231002549881.png" alt="image-20201231002549881" style="zoom:50%;" />

冲激串采样(理想采样)

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231002634957.png" alt="image-20201231002634957" style="zoom:50%;" />

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231002701941.png" alt="image-20201231002701941" style="zoom:50%;" />

$x_p(t)$的傅里叶频谱

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231002924125.png" alt="image-20201231002924125" style="zoom:67%;" />

It can be seen that ideally sampling a continuous-time signal in the time domain is equivalent to extending the spectrum of the continuous-time signal with a period of $w_s$ in the frequency domain.

any physical signal can be decomposed into a number of discrete frequencies, or a spectrum of frequencies over a continuous range

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201230095620372.png" alt="image-20201230095620372" style="zoom: 67%;" />

例子

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231003513051.png" alt="image-20201231003513051" style="zoom: 67%;" />

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231003754672.png" alt="image-20201231003754672" style="zoom: 50%;" />

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231003953518.png" alt="image-20201231003953518" style="zoom:50%;" />

The sampling period becomes larger, the period of the spectrum becomes smaller, and the spectrum of the discrete signal overlaps each other: 混叠

> aliasing is the result of a lower resolution sampling, which translates to **poor sound quality and static**. This occurs when audio is sampled at a lower resolution than the original recording. We can simply avoid aliasing by **sampling the signal at a higher rate than the Nyquist rate (Fs>Fm). Or, we can use anti-aliasing filters**.

To make the sampled signal samples completely represent the original signal, it means to be able to separate $X (jw)$ from $X_p(jw)$ without distortion. This requires that $X(jw)$ does not cause spectrum aliasing during periodic extension. For this it must be required:

1.  $x(t)$ must be time-limited, the highest frequency component is $\omega_m$

2. The sampling interval (period) cannot be arbitrary, and the sampling frequency $\omega_s$>= 2$\omega_m$ must be guaranteed, where $\omega_s = 2\pi/T$ is the sampling frequency

### Nyquist 采样定理

For the continuous time signal x(t) with the highest frequency $\omega_m$, if $w_s \geq 2w_m$ spectrum is ideally sampled, then $x(t)$ can be uniquely determined by its sample $x(nT)$

### 内插

the process of reconstructing a function from sample values

理想内插：take the unit impulse response (Sa function form) of an ideal low-pass filter (频率矩形脉冲) as the 内插函数

![image-20201230122137491](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201230122137491.png)

![image-20201230122322796](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201230122322796.png)

这种内插称为时域中**带限内插**， 

如何恢复原始的时间连续信号？

use 滤波器函数 to 内插 the 信号抽样值 to reconstruct the 模拟信号, it is equivalent to the convolution between the 滤波器的冲激响应 and 信号值为权重的脉冲串.  

### 零阶保持

(zero order hold)内插的内插函数$h_0(t)$

![image-20201230123814186](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201230123814186.png)

> The zero-order hold (ZOH) is a mathematical model of the practical signal reconstruction done by a conventional digital-to-analog converter (DAC). That is, it describes the effect of converting a discrete-time signal to a continuous-time signal by holding each sample value for one sample interval. It has several applications in electrical communication.

### 一阶保持

（first order hold)内插（线性内插）:In linear interpolation, the interpolation function is triangular pulse

![image-20201230123957862](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201230123957862.png)

### 次采样：频谱混叠

If sampling does not meet the requirements of the 采样定理, 频谱混叠 will definitely occur, when the x(t) 频谱周期延拓. 

1. In the case of spectrum aliasing, the time-domain signal changes, but the value at the sampling point remains unchanged
2. In this case, the original signal cannot be obtained even through ideal interpolation. But no matter what, the recovered signal $x_r(t)$ and the original signal x(t) will have the same value at the sampling point, that is, $x_r(nT)=x(nT)$

### 小结

In the time domain, the discrete-time signal is sampled at intervals of Ts; in the frequency domain, the signal's spectrum is a period of the discrete-time signal's spectrum that periodically extends at intervals of $2\pi / T_s$

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231013701031.png" alt="image-20201231013701031" style="zoom:67%;" />

This shows that: ideally sampling the spectrum of the signal in the frequency domain is equivalent to infinitely extending the signal in the time domain with a period of $2\pi/w_o$

![image-20201230132518437](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201230132518437.png)

At this time, the original signal can be taken out from the periodically extended signal through the rectangular window

In the frequency domain, the frequency domain time limit interpolation process when reconstructing the continuous spectrum from the samples of the frequency spectrum is realized by using the spectrum of the rectangular window as the interpolation function

It should be noted:
There is no necessary logical connection between band limit and time limit. Please pay attention to the band limit requirements in the application conditions of the time domain sampling theorem. The same applies to frequency domain sampling. Therefore, when the band-limited signal is sampled in the frequency domain, if the time domain does not specify the time limit, there is no guarantee that the samples of the spectrum can be restored to the original signal

# 3. 离散时间信号的傅里叶分析

## 实际信号的特点

时域：连续时间信号，待续时间较长

邻域：频谱是连续的

数字处理设备（计算机）的特点

- Limited storage space --- Only a limited amount of data can be stored, Discrete points in time, Limited time frame
- Represents limited space --- Can only represent a limited number of values, The value is within a certain accuracy, value is within a certain range

## 要解决的问题

###  1. 在时域如何对信号进行离散化? 

must ensure that information of signal is not damaged

- 信息不受损<>可以恢复原信号
- 乘以冲激串信号，在时域进行理想抽样
- 要求抽样过程满足抽样两个定义
  - 信号频带宽度有限
  - 抽样频率时信号最高频率的两倍

### 2. 如何从抽样信号的频谱恢复原信号

- 抽样信号与原信号频谱有什么关系？

### 3. 抽样信号的频谱如何计算

- 得到抽样信号以后，如何计算频谱？
  - 输入：抽样信号
  - 输出：出样信号的频谱

### 4. 截取一段信号进行频谱分析时，信号的频谱与原频谱相比会发生什么变换？

### 5.如何存储离散时间信号的频谱？

- 只能存储有限长度的频谱（一个周期的信息）
- 只能存储有限数目的频谱（离散频率点处的频谱值）

如何从有限的离散频谱恢复出抽样信号？

### 6. 如何编程实现：

1. 如何由离散信号计算离散频谱
2. 如何由离散频谱恢复离散信号

## 解决问题

### 先来解决问题3

时域信号无数学表达式

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231014640551.png" alt="image-20201231014640551" style="zoom:67%;" />

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231014746923.png" alt="image-20201231014746923" style="zoom:67%;" />

#### DTFT 离散傅里叶变换的定义

based on FT 

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231015105033.png" alt="image-20201231015105033" style="zoom:67%;" />

Using only the sampling value sequence f(nT), the 频谱密度函数 of the ideal sampling signal can be calculated

The spectral density function obtained from the sequence value is still a periodic function

#### 逆变换 IFS

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231015538841.png" alt="image-20201231015538841" style="zoom:67%;" />

#### DTFT进行频率归一化

"Normalize" the sampling frequency, that is, abstract the specific physical time as a unit time, use 1 to represent： 数字时间

数字信号：normalized 时间间隔 of 离散信号（序列）

数字频谱：normalized  频谱 of 数字信号 DTFT

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231020136817.png" alt="image-20201231020136817" style="zoom:50%;" />

数字信号 x(n), 数字频谱 X(w)

### 模拟频率与数字频率

In the second chapter, CTFT gets the analog frequency Ω, after DTFT introduces the normalization time, the conversion result is the digital frequency ω

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231020651822.png" alt="image-20201231020651822" style="zoom: 50%;" />

### DTFT的性质

- 周期函数
- 线性变换
- 频移特性
- 反褶，共轭
- 时域扩展
- 相应
- 微分
- 卷积

## 连续时间信号的频谱分析

> DFT is a sampled function of DTFT and the rate is the length of DFT
>
> output of DTFT is continuous, cannot be processed with computers 
>
> It is a tool used to convert the finite sequence of equally-spaced samples of any function into an equivalent-length sequence.

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201230190846315.png" alt="image-20201230190846315" style="zoom:67%;" />

### 用DFT计算非周期信号的FT

The value of the spectrum at the corresponding frequency is equal to the DFT result multiplied by Ts

![image-20201230191954375](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201230191954375.png)

### 用IDFT计算非周期信号的IFT

The value of the signal at the corresponding time point is equal to the IDFT result divided by Ts

![image-20201230192057059](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\信号处理原理notes.assets\image-20201230192057059.png)

### 用DFT计算周期信号的FS

FS频谱分量 is equal to DFT结果divided by N

![image-20201231024006763](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20201231024006763.png)

## FFT应用 

序列卷积的快速算法

计算DFT的快速算法  Fast Fourier Transformations

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231025256202.png" alt="image-20201231025256202" style="zoom:50%;" />

directly calculating DFT has 0(N^2), too time exhausting

其算法基础是：W 的两个性质

1. 具有周期性![image-20201231025833666](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231025833666.png)
2. W具有对称性 ![image-20201231025842858](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231025842858.png)

After periodic and pairwise simplifications, it is easy to find unnecessary repetitive calculations in DFT calculations. Avoiding such repetitions is the key to simplifying calculations.

N-point DFT operation can be decomposed into two sets of N/2-point DFT operations, and then take the sum

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231030807471.png" alt="image-20201231030807471" style="zoom: 67%;" />

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231031417787.png" alt="image-20201231031417787" style="zoom:67%;" />

## 离散傅里叶变换

计算机只能存储有限长的频谱信息

### 序列DFT的定义

![image-20201231122910112](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231122910112.png)

![image-20201231122925550](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231122925550.png)



### N 与 L 社么关系？

Theoretically, N and L in DFT transformation can be determined independently of each other. L is the number of time domain samples in the data record, it may be unlimited; and N is the number of frequency points at which DTFT is sampled. Usually, when discussing and using DTFT (especially programming implementation), we often see L=N. Since L and N are not necessarily related, why should they be equal? For what reason?

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231123535945.png" alt="image-20201231123535945" style="zoom: 50%;" />

#### N > L  序列补零

#### N < L 回绕序列

### DFT频谱的特点

离散的，周期的： 因为他是对DTFT频谱抽样的

### DFT变换的性质

1. 线性变换

2. 奇对称和偶对称序列

3. 

4. 实序列

5. 虚序列

6. 反褶与共轭

   <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231131357986.png" alt="image-20201231131357986" style="zoom: 50%;" />

7. 频移 ![image-20201231131448094](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231131448094.png)

8. 对称性

 <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231131501088.png" alt="image-20201231131501088" style="zoom:50%;" />

8. 时移特性

   ![image-20201231131852214](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231131852214.png)

9. 时域卷积

   ![image-20201231132019664](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231132019664.png)

   <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231132043840.png" alt="image-20201231132043840" style="zoom:50%;" />

   

   <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231132510250.png" alt="image-20201231132510250" style="zoom: 33%;" />

![image-20201231132734545](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231132734545.png)

10. 频率卷积

    <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231132818914.png" alt="image-20201231132818914" style="zoom:50%;" />

![image-20201231132835967](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231132835967.png)

### 模拟信号到数字信号的转换

![image-20201231133843817](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231133843817.png)

### 坑混叠滤波器

### 过采样和抽取

over sampling

down sampling

### 数字信号到模拟信号的转换

![image-20201231135621589](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231135621589.png)

### 采样提升与插零

un sampling

# 4. 滤波器

高通波吕齐（HP)，低通滤波器（LP），带通滤波器（BP），带阻滤波器（BS）

全通滤波器（AP）

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231140345721.png" alt="image-20201231140345721" style="zoom:50%;" />



Change the frequency characteristics of the signal in a specific way, thereby transforming the signal processing system

The digital filter is implemented in software and has rarely been recommended. A series of program instructions for filtering software knowledge. Although it is run on the recommended frequency platform from time to time, the recommended platform itself does not determine the performance of the filter. The performance of a digital filter is determined by a set of coefficients

数字率滤波器实现方式

用流图计算滤波器的输出
用差分方程计算滤波器的输出
用卷积过程计算滤波器的输出
用DTFT直接改变信号的频谱

## 什么时系统？

In layman's terms, the various environments in which signals are processed can be called systems. In the field of signal processing, a system is a certain combination of signals to transmit or process signals.

### 系统类型

1. 连续时间的系统： input output both 连续信号
2. 离散时间系统：input output both 离散信号

this class will cover 离散时间系统

系统

线性系统 Linear system
A system that satisfies both superposition and homogeneity at the same time.
• Satisfying superposition means: when several input signals are simultaneously input to the system, the total output of the system is equal to the sum of the output signals when each input signal is individually input to the system.
•Satisfying homogeneity means that when the input signal is multiplied by a certain constant, the output of the system is also multiplied by the same constant

时不变系统Time-invariant system
If the output of the system is the same whenever it receives input, the system is called a time-invariant system. Otherwise, it is called a time-varying system.

线性时不变系统 Linear time invariant system LTI

因果系统 Causal system
If the output of the system depends on the current and previous input data and has nothing to do with the future input data, then the system is called a causal system. All actual systems are causal systems

稳定系统 Stable system
If the input of the system is bounded, the output is also bounded, and the system is called a stable system. This property is often referred to as the BIBO principle

## 系统的描述方法

### 差分方程

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231142536688.png" alt="image-20201231142536688" style="zoom:33%;" />

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231142552286.png" alt="image-20201231142552286" style="zoom:50%;" />

## 系统响应分类

### 1 Zero input response
The system may produce signal output when no excitation signal is applied. In this case, the output of the system is obviously independent of the outside world (because the outside world does not input signals to the system), and the output is caused by the internal information of the system itself.

The internal information of the system itself may be the result of the previous excitation (or turbulence). However, there is no need to pursue the detailed process of their historical evolution, just know the instantaneous state of the system when the current excitation is connected to the system.

From this point of view, the zero-input response of the system is a response purely generated by the initial state of the system

### 2 Zero status response
The system corresponds to a state at each moment, and the state the system is in at the time the system is studied is called the initial state.

The so-called zero state response of the system means that the state value of the system is zero when the system is in the initial state (equivalent to the system does not store any energy and information).

In this situation, input an excitation signal to the system, and the output response produced by the system is called the zero-state response of the system.

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231145403658.png" alt="image-20201231145403658" style="zoom:50%;" />

IIR 不考！！！！！

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231145608907.png" alt="image-20201231145608907" style="zoom:50%;" />

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231155333327.png" alt="image-20201231155333327" style="zoom: 33%;" />

Both convolution and difference equations can be used to calculate filters. For FIR, both convolution operations and difference equations are used. For IIR, the difference equation is better.



From the above equation 《数字滤波器输出等于输入与脉冲响应的卷积》

1. The output signal can be obtained by convolution of the input signal and the impulse response (function)
2. The output signal is equal to the convolution of the input signal and the impulse response (signal)

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231174327729.png" alt="image-20201231174327729" style="zoom:50%;" />

系统的**频率响应**，简称频响，它反映了系统对激励中各频率分量的幅度和相位影响。reflects the amplitude and phase influence of each frequency component in the system excitation.

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231174437811.png" alt="image-20201231174437811" style="zoom:50%;" />

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231174538691.png" alt="image-20201231174538691" style="zoom:50%;" />

![image-20201231183652606](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231183652606.png)

## ZT的意义

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231190556833.png" alt="image-20201231190556833" style="zoom:50%;" />

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231190640846.png" alt="image-20201231190640846" style="zoom:50%;" />

### ZT的意义

An important mathematical tool in the theoretical research of discrete-time signals and systems in Z-transform

It converts the mathematical model of the discrete system-difference equations into simple algebraic equations, simplifying the solution process

1. Understand the Z transformation from the perspective of flow graphs, difference equations, and DTFT
2. How to use the Z transformation to establish the difference equation H(z)

This is a form of summing power series. Obviously, this power series sum does not always converge. It is neither valid for all sequences, nor for all z values of a certain sequence.

But if a specific sequence is given, then all z-value sets that make the above formula true can be found

We call X(z) to converge so that z has the range of convergence of X(z), abbreviated as R0C

### Z变换收敛域的一般特点
The general form of the domain of convergence is a ring centered on the origin in the z plane

The region of convergence does not contain extremes, and extremes are often used as the boundary of the region of convergence

In ROC, ZT and its reciprocal are continuous functions of z, that is, the ZT function is an analytic function that converges to every point in it

### Z变换手来你域的求解

Z transformation is a power series. The convergence range of the power series is called the convergence circle, and the radius of the convergence circle is called the convergence radius of the power series. The convergence radius calculation method includes the ratio method and the root value method.

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231193150619.png" alt="image-20201231193150619" style="zoom:50%;" />

### ZT 的性质

1. 线性 ![image-20201231193555866](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231193555866.png)

2. 时域频移性 <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231193608419.png" alt="image-20201231193608419" style="zoom:50%;" />

3. 时域扩展性 <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231193657331.png" alt="image-20201231193657331" style="zoom:50%;" />

   <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231193715557.png" alt="image-20201231193715557" style="zoom:50%;" />

4. 对成性<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231193732811.png" alt="image-20201231193732811" style="zoom:50%;" />

5. 时域共轭性 <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231193858868.png" alt="image-20201231193858868" style="zoom:50%;" />

6. 如果一个序列是时序列 <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231193951731.png" alt="image-20201231193951731" style="zoom:50%;" />

7. Z域尺度变换 <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231194152007.png" alt="image-20201231194152007" style="zoom:50%;" />

8. Z域微分<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231194210766.png" alt="image-20201231194210766" style="zoom:50%;" /><img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231194353294.png" alt="image-20201231194353294" style="zoom:50%;" />

9. 初值定理 

   <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231194428731.png" alt="image-20201231194428731" style="zoom:50%;" />

10. 终值定理 

    <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231194512084.png" alt="image-20201231194512084" style="zoom:50%;" />

11. 时域卷积定理 <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231194549416.png" alt="image-20201231194549416" style="zoom:50%;" />

12. Z域卷积定理

    <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231194756046.png" alt="image-20201231194756046" style="zoom:50%;" />

    <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231194807301.png" alt="image-20201231194807301" style="zoom:50%;" />

    $C_1$和$C_2$的收敛域重叠部分内逆时真旋转的危险

    ![image-20201231195023663](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231195023663.png)

11. Perceval's Theorem

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231195034603.png" alt="image-20201231195034603" style="zoom:50%;" />



### 逆Z变换的求解3

case 1: <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231201133343.png" alt="image-20201231201133343" style="zoom:33%;" />

case 2:<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231201151313.png" alt="image-20201231201151313" style="zoom: 50%;" />

case 3: <img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231202842969.png" alt="image-20201231202842969" style="zoom:50%;" />

### 传递函数

离散时间LTI系统输入输出满足下列关系

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20210101154118835.png" alt="image-20210101154118835" style="zoom:50%;" />

H(z)与系统特性有一一对应关系，也可以说是系统特性的一种反映，所以通常称H(z)为LTI系统的传递函数，也称**系统函数**

传递函数H(z) 实际上是系统单位冲激响应 h(n)的 Z 变换，可以 直接由单位冲激响应求出来

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20210101154403376.png" alt="image-20210101154403376" style="zoom: 50%;" />

系统的并联组合

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20210101154507825.png" alt="image-20210101154507825" style="zoom:33%;" />

系统的串联组合

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20210101154526107.png" alt="image-20210101154526107" style="zoom:33%;" />

Conclusion 1 The necessary and sufficient bar for a discrete linear time-invariant system to be a causal system is: the transfer function ROC is the area outside a certain circle, including the point at infinity.

Conclusion 2 The necessary and sufficient for a discrete linear time-invariant system to be a stable system is: the ROC of the transfer function includes the unit circle.

If the system is a stable causal system, its transfer function ROC is as follows

![image-20210101155046557](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20210101155046557.png)

# 5. 数字滤波器的设计

## FIR数字滤波器的设计

（有限脉冲响应滤波器）

滤波器对输入信号的频率分量进行处理

![image-20210101160255666](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20210101160255666.png)

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20210101160312318.png" alt="image-20210101160312318" style="zoom:50%;" />

1. 滤波器的单位冲激响应$h(n)$可以表征系统
2. 理想低通滤波器的$h(n)$无限长，且有负责值下标，是物理不可实现的
3. FIR滤波器的单位冲激响应$h'(n)$是有限长，（只有有限的非零值）的因果序列



### FIR数字滤波器的窗函数设计法

1. $h'(n)$将满足要求的理想低通滤波器的$h(n)$
2. 因为时域频移之影响相位，所以可以将截断后的$h(n)$平移称因果序列（而不影响系统的复频响应的特性 （because of time-domain frequency shift, it can be called a causal sequence
3. 用所得h(n)实现的滤波器即为所需FIR的h’(n)

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20210101160546349.png" alt="image-20210101160546349" style="zoom:50%;" />

在$\omega_c$截断

The cut-off frequency of an ideal low-pass filter, because the unit impulse response is truncated into a finite term, the frequency response characteristics of the filter will change. According to experience, when designing a filter, the cut-off frequency of an ideal low-pass filter does not use the edge frequency of the passband, but uses the frequency at the midpoint of the transition band. which is:

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20210101161227223.png" alt="image-20210101161227223" style="zoom:50%;" />

<img src="C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20210101161236064.png" alt="image-20210101161236064" style="zoom:50%;" />

### 理想低通滤波器的$h(n)$被不同的窗函数截断时性能

![image-20210101162438678](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20210101162438678.png)

### 低通FIR滤波器的设计部署

1. 在过度带宽中间，选择理想低通滤波器的截止频率$f_c(Hz)$

   $f_c(Hz)=设计指标要求的通带边绿频率+（过渡带宽度）/2$

2. 计算截止频率的**数字频率**

   $h(n)=\frac{sin(n\omega_c)}{n\pi},\omega_C = 2\pi f_c / f_s $

3. 从表中选择满足阻带衰减即其他要求的窗函数，计算窗内非零项的数目，选择奇数项（好处：脉冲响应完成对称，相位没有失真），计算出窗函数的表达式

4. 用窗函数与$h(n)$相乘，计算有限长脉冲响应

5. 将秒冲响应右移(N-1)/2,使第一个非零值在n=0处

## IIR 数字滤波器 (不考)





## 作业题

## Week 8

![image-20201231133119892](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231133119892.png)

## Week 9

![image-20201231135954925](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20201231135954925.png)

## Week 10

![image-20210101155424602](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\Signal Processing\all notes.assets\image-20210101155424602.png)

