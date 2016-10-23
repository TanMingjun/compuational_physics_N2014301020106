# The sixth time homework-question 2.10
## 1.Abstract
In the last homework, we have already drawn some trajectories of cannon shells. That situation requires known initial(firing) velocity and firing angle, and we just hit a random target. Of corse, it is not impractical in the war. In fact, what we can know is the distance between enemies(targets) and us. So, how can we use the distance and our cannon shells' firing velocity to hit the target. Besides, if the position of the target is told, what should we do to get the target with the smallest velocity. 

### Question 2.10 
Generalize the program developed for the previous problem so that it can deal with situations in which the target is at a different altitude than the cannon. Consider cases in which the target is higher and lower than the cannon. Also investigate how the minimum firing velocity requried to hit the target varies as the altitude of the target is varied. Consider the wind drag and use the adiabatic approxiation.

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

## 3.Body content
### Homework L1
#### Hit the target
In order to hit target, one sets firing velocity vo=700m/s, now, what we should do is to find angles that can make cannon shell hit the target, so we just scan angles one by one. Through operating our program, I found that it will take a long time for my computer to accomplish our scan. How to solve this problem? First, we can chose a large interval of angle, then chose the scale of angles that we need, and repeat above procedure. In this way, we can save a lot of time. Here, I just pick up two heights to discuss our problem.

(1) Height=5000m and x-distance=20000m
### [Click the Code]()
First, we scan angles by 1 degree, we can get two rough scale about the angle that we really want to get, for example, the scale can be find in [Notebook](),and we get the figure:

![tupian]()

Then in these small scale, we can continue scanning, then the a more accurate figure is

![tupian]()

Eventually, we can get two more accurate results. And from my notebook(file), these two angles are 41.122 degree and 58.655 degree.

Use these two angles that we get, we can draw trajectory of cannon shell right away:

![tupian]()

And the position, which cannon shell hit, also can be obtain:

![tupian]()

Ignore errors that come from dt=0.001s, we can calculate deflected distance about our cannon shell.
直接画图

(2) Height=-2000m and x-distance=25000m
The code is like below, just change Height of target.
Use the same method as above, we get two figures:

![picture]()

![picture]()

Instantly, we can obtain two firing angle, they are 30.895 degree and 52.592 degree. So, the trajectory of cannon shell is given by:

![picture]()

And the position, which is hited by our cannon shell is given below:

![picture]()

Similarily, we can analy the error:
直接画图

#### Find the minimum velocity
There we use two simple methods:

(1) Change firing velocity and scan angles from 0 to 90, assume the target height=5000m, x-distance=20000m

### [Click the code]()

And the result are given by:

![picture]()

The minimum ia about 672m/s.

(2) Similarily, we scan all possible results, and finally, we have:

![picture]()

## Conclusion

## Reference

















