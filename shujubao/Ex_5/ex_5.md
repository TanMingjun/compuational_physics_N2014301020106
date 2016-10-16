# The Fifth Time Homework-Realistic Projectile Motion

## 1.Abstract
In warfare you generally want to hit a particular target (as opposed to having the cannon shells land indicriminately). Of course, good prediction is quite helpful to realize it. Daily life tell us the trajectory of a cannon shell is related to a lot of factors, including the uniform air drag, the isothermal air drag, the adiabatic air drag and so on. Here, we will take some of them into consideration in the following parts. It will considerably important for us to learn and use the same method to solve similar problem in the furture.

![找一个大炮图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/figure/figure1.png)

In the last homework, we have already used the Euler method to solve questions, but, last time, we just applied it to differential equation of first order. Now, we will apply it to more complicated situations. To be specific, we consider a projectile such as a shell shot by a cannon. If we air resistance, the equations of motion, which are again obtained from Newton's second law, can be written as

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation1.png)

where x and y are the horizontal and vertical coordinates of the projectile, and g is the acceleration due to gravity. But these equation can't be used to python directly, so one can transform them into four first-order differential equations

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation2.png)

Under this condition, to use the Euler method, we write each derivative in finite difference form, which leads to

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation3.png)

Now, we can write codes to operate it. [Click the Code](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/code/%E5%8A%A0%E5%86%9C%E7%82%AE%E6%97%A0%E9%98%BB.py)

The result is below.

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/figure/figure_1.png)

Of course, just the gravity was considered, and here the gravity velocity are constant. In real war, the above situation is not work, in the following process, I will solve this problem step by step.

## 2.Background
### Question 2.9 and 2.8
Calculate the trajectory og our cannon shell including both air drag and the reduced air density at high altitudes so that you can reproduce the results in Figure 2.5. Preform your calculation for different firing angles and determine the value of the angle that gives the maximum range. In our model of cannon shell trajectory we have assumed that the acceleration due to gravity, g, is a constant. It will, of course, depend on altitude. Add this to the model and calculate how much it affects the range.

![找一个地球卫星模型](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/figure/figure2.png)

## 3.Body Content
### (1)The Uniform Air Drag
In our treatment of the bicycle problem we found that air resistance was very important, ao we now add that to the model. As the case with a bicycle, we will assume the magnitude of the drag force on our cannon shell is given by

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation4.png)

Adding this force to the equations of motion leads to

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation5.png)

But this is not enough, we must assure that y>=0, so, we have this procedure

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation6.png)

Always, we assume that cannon shells are same with ![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation7.png)

With the uniform air drag, we can obtain the code. [Click the Code](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/code/%E5%AF%86%E5%BA%A6%E4%B8%8D%E5%8F%9835%2045%2055.py). And the result is given below.

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/figure/figure_2.png)

In order to figure out the difference between the situation of no drag and that of uniform air drag, I chose some initial angles to show.

![图片]()

Obviously, they are almost totally different! With air drag, the maximum range is much small. And the situation of no drag can't be applied to warfare. Maybe our work is perfect now, but it is not true.

### (2)The Isothermal Ideal Gas Drag
Generally, the cannon shell, with initial speed 700m/s, can fly very high about several kilometers. Then, the question is "The air density vary as a function of the altitude, how can we solve it?". 

First, the most simplest approximation is to treat the atmosphere as an isothermal ideal gas. Through thermal physics, instantly, one have

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation8.png)

Then, we write their finite difference form as below

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation9.png)

Transform them into python code. [Click the Code](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/code/%E5%AF%86%E5%BA%A6%E6%94%B9%E5%8F%981.py). And the result is given below.

![图片]()

We can compare it with the situation of uniform air drag.

![图片]()

### (3)The Adiabatic Air Drag
Though we have take the air density into consideration, we find our prediction still can't match the measured data very well. In fact there exists a better approximation. That is 

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation10.png)

And  their finite difference form is

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation11.png)

Now, similarly, the code is [Click the Code](). The result is below.

Besides, the firing angles and the maximum range are also important for sodiers to hit targets, so it is quite necessary to show their relations. The code is [Click the Code](). The result is simple like this:

![图片]()

### (4)Variational Gravity
In fact, for a cannon shell, when it fly very high, the gravity also will change. We can explain it through Newton's law 

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation12.png).

Eventually, we can obtain the equation 

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation13.png)

Thus we put it into code, and I will show its influence of the cannon shell trajectory to you through comparing it with other situations.

![图片]()

## 4.Conclusion

## 5.Reference



