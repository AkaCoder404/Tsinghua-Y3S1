# 第一课
### Books
Introduction to Signal Processing 信号处理导论
1. S.J Orfanidis, Prentice-Hall, Inc

## 课程内容
1. 信号与信号处理的基本概念


## 考核方式
- 15% 平时作业
- 15% 课程实验
    1. 4% 实验1 傅里叶级数的可视化 (4-5 week)
    2. 5% 实验2 信号的评分复用 (10-13 week)
    3. 6% 实验3 Mel频谱与griffin_lim声码器 (15-17)
    4. 70% 期末考试 

computers process discrete signals, but most signals are continious 
study 物理现象 and 规律，course discusses mathematic properties to observe, so that we can use computers to process the signals

## 信号? 
观察， 传感器，测量
signal is a physical quantity that reflects information, it is thing being processed to achieve communications

铝带话筒 ribbon microphone https://proaudioland.com/news/ribbon-mics-microphones-benefits/

in actual engineering applications, we need to slect conversion parameters (抽样频率) according to the requirements of digital audio quality

## 信号处理的目的?
remove reduntant and minor components from the signal
turn signal into form that is easy to analyze and recognize
turn the signal into a form that is easy to transmit, exchange and store (encoding), or restore the original signal from the encoded signal (decoding)

## DSP系统的优点?
- work of digitable system is predictable and repeatable, 
- analog system is a circuit built by components, with a large manufacturing error range, and its characteristics change with temperature (temperature drift) and time (aging)
- Small size, low power consumption (development of mobile terminals)

## High flexibility？
- Analog vs. digital
- Analog audio uses the amplitude of the analog voltage to indicate - the strength of the sound
- Digital audio is a discrete sequence of numbers represented by finite values
- Modify some statements in the program to modify the system

## 数学描述？
- use mathematical expressions to describe the signal as a function - to describe as 函数 or 序列
- lianxu -> 函数
- lisan -> 序列

## 波形描述
- 时域波形 VS 频谱图
- 确定信号 VS 随机信号
- 周期信号 VS 非周期信号

need to know 欧拉公式 

## 是指信号 vs 符之信号?
If the value of the signal is a real number, it is called a real-valued signal, or real signal for short
If the value of the signal is a complex number, it is called a complex signal, or complex signal for short

Difficulty: How to uniformly describe the electric and magnetic field signals

Tip: Electric field is perpendicular to magnetic field
Solution: use real component to represent electric field and use imaginary component to represent magnetic field.

 
