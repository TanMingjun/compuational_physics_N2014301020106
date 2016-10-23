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














