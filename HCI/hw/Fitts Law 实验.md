# Fitts Law 实验

<center> 李天勤 2018080106 </center>

1. 通过anova分析A和W对于点击时间得影响是否在统计上显著 (analyze whether the impact of A and W on the click time is statiscally significant through anova)
2. 模拟Fitts Law,汇报你和得符合度（R^2值)，比较两种device的a和b，尝试给予物理解释 (best fit fitts law, report the fit degree (R^2) , compare the a and b of the two devices, and try to give a physical explanation)
3. 鼠标、触摸板和手机三个平台，三选二，至少需要8个被试 (three platforms, mouse, touchpad, and mobile phone, choose 2 out of 3, at least 8 subjects)
4. 每种A和W上的数据点求平均后再拟合 (the data points on each A and W are averaged and then fitted)
5. 制作点击任务，不做拖拽任务 (do only click tasks, not drag tasks)

## Fits Law

> A predictive model of human movement primarily used in human computer interaction and ergonomics. This scientific law predicts taht the time required to rapidly move to a target area is a function of the ratio between the distance to the target and the width of the target. Fitts law is used to model the actof pointing,either by phsycailly touching an object with a hand or finger, or virtually, by pointing to an object on a computer monitor using a pointing device.

There are many version's of the Fitt's Law, but the most commonly used equation to represent it is Sharon's Theorem, which is as follows: 
$$
T = B\log_2{(A/W + 1)}​ + A
$$
where the variables represent 

<center> 
    A = intercept <br>
    B = slope <br>
    A = Amplitude <br>
    W = Width <br>
</center>

## Experimental Design 

The goal of this experiment is to determine the residual values $$ R^2 $$ of the best fit line for Fitt's Law Test results among different devices.

The experimental settings and devices that are used are as follows:

Computer: Lenovo Thinkbook 14s

- Screen Diagonal: 14" -> 35.56 cm
- Screen Width:  12.21" -> 31.0134 cm
- Screen Height: 6.85" -> 17.399 cm 

Mobile: IPhone  11 Pro

- Screen Diagonal 5.8" -> 14.732 cm
- Screen Height: 5.67" -> 14.4018 cm
- Screen Width 2.81" -> 7.1374 cm

Repitition: 19

Target Width: 0.25, 0.50, 0.75 cm

Target Distance: 2, 3, 4 cm

## Participants 

There will be 8 subjects

| Participants | Gender | Age  |
| ------------ | ------ | ---- |
| 周凯兴       | 男     | 21   |
| 刘志恒       | 男     | 20   |
| 李天勤       | 男     | 20   |
| Kieren       | 男     | 21   |
| 周思祎       | 女     | 21   |
| Adele        | 女     | 21   |
| 郑相姬       | 女     | 21   |
| 李蓉         | 女     | 21   |

# Results

### Mouse and Laptop

1、Error Rate: 

There are a total of 19 repetitions * 3 (A values) * 3 (W values) * 8 (participants) = 1368 data points.

| Participants | Error Count |
| ------------ | ----------- |
| 周凯兴       | 7/171       |
| 刘志恒       | 14/171      |
| 李天勤       | 6/171       |
| Kieren       | 10/171      |
| 周思祎       | 2/171       |
| Adele        | 8/171       |
| 郑相姬       | 40/171      |
| 李蓉         | 10/171      |

Of those data points, there is a total of 97 failed cases, thus, the error on the mouse test is 97/1368 or 7.0906%

2、Regression Analysis

Per Subject:.

| $ log_2{(A/W+1)}$ | 李天勤   | 李志恒   | 周凯兴   | 郑相姬   | 周思祎   | Adele    | Kieren   | 李蓉     |
| ----------------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 1.87444289        | 481.5789 | 477.5789 | 517.8947 | 568.474  | 585.8421 | 637.6842 | 556.2105 | 610.375  |
| 2.32192802        | 508.9474 | 628.4211 | 556.1843 | 600.5263 | 644.2532 | 672.263  | 530.1053 | 639.1579 |
| 2.66295742        | 566.8421 | 661.079  | 600.123  | 644.253  | 652.9474 | 696.9211 | 579.7895 | 657.6316 |
| 2.80735492        | 637.1053 | 706.4211 | 663.5789 | 700.4211 | 752.5789 | 736.8947 | 628.0526 | 693.4474 |
| 3.169925          | 697.6316 | 839.3422 | 738.5789 | 779.3948 | 855.7632 | 816.6842 | 657.8421 | 816.8158 |
| 3.70043972        | 771.3684 | 802.9474 | 762.2895 | 833.7895 | 965.3684 | 883.4747 | 819.1053 | 948.5789 |
| 4.08746284        | 813.9474 | 900.842  | 827      | 890.7895 | 1038.105 | 1001.789 | 845.1579 | 1028     |

Results Per Person, the Y axis representing the average time in ms, while the X axis represents the difficulty

![image-20201117114949737](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\HCI\hw\Fitts Law 实验.assets\image-20201117114949737.png)

For each A/W values, calculate $ log_2{(A/W+1)} $ and the average time it takes to hit the target. 

| A/W    | $ log_2{(A/W+1)}$ | Time (ms） |
| ------ | ----------------- | ---------- |
| 2.666  | 1.87444289        | 554.4548   |
| 4      | 2.32192802        | 597.4823   |
| 5.3333 | 2.66295742        | 632.4483   |
| 6      | 2.80735492        | 689.8125   |
| 8      | 3.169925          | 775.2566   |
| 12     | 3.70043972        | 848.3653   |
| 16     | 4.08746284        | 918.2039   |

The scatter plot with the best fit line can be shown below: 

![image-20201117115117164](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\HCI\hw\Fitts Law 实验.assets\image-20201117115117164.png)

From the graph, we find that:

A = 204.76

B = 173.71

$$ R^2 $$ = 0.9785

The results from the linear regression show that the value of $$ R^2 $$ is around 93 percent. The points generally follow the Fitts Law equation but the only 2 are really touching/on the line. This result is generally bad for statisical test, but I will later explain possible errors for our data.

### Mobile Touch

Since the process is the same as above, I will only show the important information

1、Error Rate: 

Out of all the data points, 265 of those points were failed cases. Thus, the error rate on the mobile test is 19.37%。

2、Regression Analysis

For each A/W values, calculate $ log_2{(A/W+1)} $ and the average time it takes to hit the target. 

| A/W    | $ log_2{(A/W+1)} $ | Time (ms) |
| ------ | ------------------ | --------- |
| 2.666  | 1.87444289         | 311.322   |
| 4      | 2.32192802         | 360.96    |
| 5.3333 | 2.66295742         | 376.986   |
| 6      | 2.80735492         | 408       |
| 8      | 3.169925           | 453.978   |
| 12     | 3.70043972         | 513.898   |
| 16     | 4.08746284         | 541.99    |

The data is shown below

![image-20201117111055599](C:\Users\ligeo\Desktop\Y3S1\Tsinghua-Y3S1\HCI\hw\Fitts Law 实验.assets\image-20201117111055599.png)

From the graph we get, 

A = 105.32

B = 108.12

$$ R^2 $$ = 0.9897

The results from the linear regression treadline show that the Fitt's Law is relatively predictive when applied to mobile screens. This result is higher than the mouse and laptop test.

## ANOVA Analysis

Analyze whether the impact of A and W on the click time is statiscally significant through ANOVA

### The Effects of Distance (A) on target selection time

Summary

| Groups | Average  | Varience |
| ------ | -------- | -------- |
| A = 2  | 656.8082 | 59868.74 |
| A = 3  | 725.863  | 56693.98 |
| A = 4  | 758.4178 | 64073.27 |

ANOVA

| Source of Varience | SS        | df   | MS       | f        | P-value | Fcrit    |
| ------------------ | --------- | ---- | -------- | -------- | ------- | -------- |
| Between Groups     | 7861071.2 | 2    | 393053.6 | 6.527829 | 0.00161 | 3.016458 |
| Within Groups      | 26192217  | 435  | 60211.99 |          |         |          |
|                    |           |      |          |          |         |          |
| Total              | 26978325  | 437  |          |          |         |          |



### The Effects of Width (W) on target selection time

Summary

| Groups   | Average  | Variance |
| -------- | -------- | -------- |
| W = .25  | 904.8923 | 93327.29 |
| W = 0.5  | 759.938  | 68156.92 |
| W = 0.75 | 702.4215 | 63885.09 |

ANOVA

| Source of Varience | SS       | df   | MS      | f      | P-value  | Fcrit    |
| ------------------ | -------- | ---- | ------- | ------ | -------- | -------- |
| Between Groups     | 2982688  | 2    | 1491344 | 19.852 | 5.92E-09 | 3.017836 |
| Within Groups      | 30650224 | 408  | 75123.1 |        |          |          |
|                    |          |      |         |        |          |          |
| Total              | 33632912 | 410  |         |        |          |          |

As seen from the above table, the p-value is $$ 5.92*10^{-9} $$ , which is less than the significance threshold 0.05. This means that the target selection time is significantly affected by the size, or width W, of the target from the starting position to the target position. Also, we can can tell from the mean value that the target slection time is negatively correlated with W.

### The Effect of Method (mouse or mobile) on target selection time

Summary

| Groups | Average    | Variance   |
| ------ | ---------- | ---------- |
| mouse  | 762.85906  | 58964.23   |
| mobile | 450.328947 | 17436.5136 |
|        |            |            |

ANOVA

| Source of Varience | SS         | df   | MS         | f          | P-value    | Fcrit      |
| ------------------ | ---------- | ---- | ---------- | ---------- | ---------- | ---------- |
| Between Groups     | 7349319.01 | 1    | 7349319.01 | 193.443659 | 2.9511E-34 | 3.87274718 |
| Within Groups      | 11359619.6 | 299  | 37992.0388 |            |            |            |
|                    |            |      |            |            |            |            |
| Total              | 18708938.6 | 300  |            |            |            |            |

As seen from the above table, the p-value is $$ 2.9511*10^{-34} $$, which is less than the significance threshold 0.05. Theis means that the target slection time is influenced by the target selection method. It takes more time to select targets on a computer by mouse than on a mobile phone through touchscreen.

## 总结

Comparing the $ R^2 $ regression of the two pointer types, mouse and computer versus mobile, the participants performed slightly better on the mobile test. This is probably because of familiarity, users were more comfortable using an iphone rather than the mouse I had supplied them to use (MX Master 3). A few of the participants normally did not use mouses and thus could wasn't always consistent, since it was also their first time performing the test. The mobile test was taking after the computer test, thus it was more familiar since they had better sense of what was happening. As the participants in the test did not take it in a controlled environment, there may be errors due to distractions such as noise. 

We can also see the mobile test had significantly more errors than the mouse and laptop test. This is generally because of differing finger sizes. The lines on the mobile test were smaller than the width of the finger for all the participants, thus there would be more error even if the user pressed in the intended location. The tests were quicker because it is easier to move a finger than a mouse across a table.

