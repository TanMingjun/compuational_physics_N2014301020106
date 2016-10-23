# The sixth time homework-question 2.10
## 1.Abstract
In the last homework, we have already drawn some trajectories of cannon shells. That situation requires known initial(firing) velocity and firing angle, and we just hit a random target. Of corse, it is not impractical in the war. In fact, what we can know is the distance between enemies(targets) and us. So, how can we use the distance and our cannon shells' firing velocity to hit the target. Besides, if the position of the target is told, what should we do to get the target with the smallest velocity. 

### Question 2.10 
Generalize the program developed for the previous problem so that it can deal with situations in which the target is at a different altitude than the cannon. Consider cases in which the target is higher and lower than the cannon. Also investigate how the minimum firing velocity requried to hit the target varies as the altitude of the target is varied. Consider the wind drag and use the adiabatic approxiation.

***

## 2.Background and introduction
In the last section, we have already gotten the differential equations of motorial cannon shells. It were given below:

![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/euqation/equation_1.png) (1)

Now, let next add the effect of the wind. We will assume that it is blowing in horizontal (x) direction and has a constant magnitude and direction during flight of cannon shell. In this case the compnonents of the drag force become:

![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/euqation/equation_2.png) (2)

Or we can rewrite the compnonents of the drag force in another form:

![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/euqation/equation_3.png) (3)

So, combine (1)(3), the equations of motion become as:

![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/euqation/equation_4.png) (4)

Though it seems that everything was been done, one forget to conduct a transform:

![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/euqation/equation_5.png) (5)

Thus, equation (4) can be expressed like this:

![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/euqation/equation_6.png) (6)

When it comes to here, it's time for us to write our programs. By the way, don't forget to put this constants into our program:

![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/euqation/equation_7.png), ![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/euqation/equation_8.png), ![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/euqation/equation_9.png), ![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/euqation/equation_10.png)

***

## 3.Body content
### Homework L1
#### Hit the target
In order to hit target, one sets firing velocity vo=700m/s, now, what we should do is to find angles that can make cannon shell hit the target, so we just scan angles one by one. Through operating our program, I found that it will take a long time for my computer to accomplish our scan. How to solve this problem? First, we can chose a large interval of angle, then chose the scale of angles that we need, and repeat above procedure. In this way, we can save a lot of time. Here, I just pick up two heights to discuss our problem.

(1) Height=5000m and x-distance=20000m
### [Click the Code](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/code/untitled6.py)
First, we scan angles by 1 degree, we can get two rough scale about the angle that we really want to get, for example, the scale can be find in [Notebook](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/code/angle%20and%20maximum%20distance),and we get the figure:

![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/figure/figure_1.png)

Then in these small scale, we can continue scanning, then the a more accurate figure is

![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/figure/figure_2.png)

Eventually, we can get two more accurate results. And from my notebook(file), these two angles are 41.122 degree and 58.655 degree.

### [Click the code](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/code/shiyong.py)

Use these two angles that we get, we can draw trajectory of cannon shell right away:

![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/figure/figure_3.png)

And the position, which cannon shell hit, also can be obtain:

![tupian](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/figure/figure_4.png)

Ignore errors that come from dt=0.001s, we can calculate deflected distance about our cannon shell.

| Angle[degree] | Distance[m] | error |
|-----|-----|-----|
| 41.122 | 20000.01491930314 | 0.000075% |
| 58.655 | 20000.085483244966 | 0.00043% |

(2) Height=-2000m and x-distance=25000m
The code is like below, just change Height of target.
Use the same method as above, we get the figure:

![picture](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/figure/figure_5.png)

Instantly, we can obtain two firing angle, they are 30.895 degree and 52.592 degree. So, the trajectory of cannon shell is given by:

![picture](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/figure/figure_6.png)

And the position, which is hited by our cannon shell is given below:

![picture](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/figure/figure_7.png)

Similarily, we can analy the error:

| Angle[degree] | Distance[m] | error |
|-----|-----|-----|
| 30.895 | 25000.189592005132 | 0.00076% |
| 52.592 | 24999.911797205175 | 0.00035% |

#### Find the minimum velocity
There we use two simple methods:

(1) Change firing velocity and scan angles from 0 to 90, assume the target height=5000m, x-distance=20000m

### [Click the code](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/code/%E9%80%BC%E8%BF%91%E6%B3%95.py)

And the result are given by:

![picture](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/figure/figure_8.png)

The minimum ia about 672m/s.

(2) Similarily, we scan all possible results, and finally, we have:

![picture](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/figure/figure_10.png)

### [Click the Code](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_6/code/bijin2.py)

So, the minimum firing velocity is about 672m/s

***

## 4.Conclusion
##### 1.Wherever the target is, can we always hit it exactly through scan angles with a small angle interval, like 0.001 degree even smaller.
##### 2.Generally, there are two firing angles that are corrresponding to one target that we want to hit.
##### 3.We can use many methods to find the minimum firing velocity, here, I just used two simple and rough ways to realize get it. Hope that I have ability to improve it later.
##### 4.These methods are very helpful for wars, but we don't want to see wars.

***

## 5.Reference
(1) Nicholas J. Giordano Hisao Nakanishi, Computational Physics(Second Edition)

(2) [The ppt of professor cai](https://www.evernote.com/shard/s140/sh/26f85380-ee6c-4b4b-b33f-6871804d91ff/fb8cc702cb0e8ed7fafb50b2de4596ca)
