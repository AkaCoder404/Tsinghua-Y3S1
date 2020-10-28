# 实验一， 傅里叶级数的可视化

Visualization of Fourier Series

For a function $f(t)$ period  $T_1$, it's Fourier Series is 

$g(t) = a_0 + \sum^{\infty}_{n=1}(a_n cos{n\omega_1t} + b_n sin{n\omega_1t})$

## 任务一，可视化方波信号

Visualization of Square Signal Wave

原理

For a square signal wave $f(t)=0.5sgn{(sin{(t)})} + 0.5$  with period $2\pi$ that can be visualized as a fourier transformation, the square signal wave can be seen as (since period is $2\pi$,  $\omega_1 = 1$)

The Fourier series expansion $g(t)$ of a square wave is constructed as a superposition of multiple points $m_i$ moving on a circle as shown in the figure below. Each point $m_i$ has a fixed rotation frequency $n_i$ (Note: In the figure below, since $f(t)$ is approximately equal to $g(t)$, the red line is always approximately parallel to the x-axis

We will visualize this process in the experiment: We will draw the trajectory of each point on the circle, and verify that the value of the superimposed ordinate of these points is approximately equal to the value of the square wave function $f(t)$

结果

I first implemented the the signal function for $f(t)=0.5sgn{(sin{(t)})} + 0.5$ . Thanks to python's np library, this was quite easy. I used ```np.sin``` function and ```np.sign``` function to simulate taking the sin of t, and then the sigmoid (square wave) of the result. I then multiplied by 0.5 and added 0.5. The result I got was a curve slightly different than the one in the lab book.



![image-20201021181105229](C:\Users\ligeo\Desktop\Lab1\LabReport.assets\image-20201021181105229.png)



Then I implemented the ```fourier_coefficient``` function. The math required to find the fourier coefficients for a sgn function is quite simple. First, we need to find $a_0$​

Since, from $\pi$ to $ 2\pi $ is simply zero, we only really need to calculate the integral from $0$ to $\pi$ , and because $f(t)$ = 1 during that interval, we get the following value for $a_o$

$a_0 = \int_{0}^{\pi} 1dt = 0.5$ 

So when $n=0$ , then the fourier coefficient should return $0.5$

The same concept is applied in order to find $b_n$, but instead of just having $f(t)$ within the integral, we need $cos(nt)$ as well.

$b_n = \int^{\pi}_0 cos(nt) \rightarrow 1/(n\pi) (cos(nt) - 1)  $   

Thus, depending on what n is, we return $b_n$

Since $f(t)$ is an odd function, $a_n$ is equal to 0. 

After defining our functions, I slightly changed the main function so I wouldn't have to manually run it for each n. And the results of our square function can be found in Nsquare.mp4, where N is the value of N_Fourier. 

## 任务二， 可视化半圆波信号

The process of this experiment is exactly like the first task, the only difference is defining the ```fourier_coefficient``` function. Since the integrating the half circle wave formula $f(t) = \sqrt{(\pi^2 - (t-\pi)^2}$ is quite complicated for  $a_n$ and $b_n$  I used a library that would help do the integrations for me. 

I added ```from scipy.integrate import quad``` which would allow me to integrate functions that I have defined. The two being, ```def integrandbn``` and ```def integrandan``` which would find the values of $b_n$ and $a_n$ respectively. Finding both $a_n$ and $b_n$ are similar, so I will explain how I set up $b_n$. 

$b_n = \int^{2\pi}_{0} = \sqrt{(\pi^2 - (t-\pi)^2} cos(nt)$ 

Using the imported library, this can be translated to 

```math.sqrt(2 * math.pi * x - math.pow(x, 2)) * math.sin(N * x)``` where N is the value of m, and x is t. 

In order to call it, we use 

```
N = m
ans, err = quad(integrandbn, 0, 2*math.pi) 
```

where m is the current fourier transformation value, ans is the result, and err is the error of the calculation. 

Then we return ```ans \ {math.pi}``` to get the final value of $b_n$

Finding $a_0$  by hand is also quite complicated, but doable, the answer being $\pi^2/(4)$

The graph for when N_Fourier=128 is shown below:

![image-20201021184440865](C:\Users\ligeo\Desktop\Lab1\LabReport.assets\image-20201021184440865.png)

In both examples, the red line is parallel to the x-axis, so I believe that I had done the lab correctly. Thanks.