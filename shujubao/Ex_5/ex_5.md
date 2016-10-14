# The Fifth Time Homework-Realistic Projectile Motion

## 1.Background
In warfare you generally want to hit a particular target (as opposed to having the cannon shells land indicriminately). Of course, good prediction is quite helpful to realize it. Daily life tell us the trajectory of a cannon shell is related to a lot of factors, including the uniform air drag, the isothermal air drag, the adiabatic air drag and so on. Here, we will take some of them into consideration in the following parts. It will considerably important for us to learn and use the same method to solve similar problem in the furture.

![图片]()

In the last homework, we have already used the Euler method to solve questions, but, last time, we just applied it to differential equation of first order. Now, we will apply it to more complicated situations. To be specific, we consider a projectile such as a shell shot by a cannon. If we air resistance, the equations of motion, which are again obtained from Newton's second law, can be written as

![图片]()

where x and y are the horizontal and vertical coordinates of the projectile, and g is the acceleration due to gravity. But these equation can't be used to python directly, so one can transform them into four first-order differential equations

![图片]()

Under this condition, to use the Euler method, we write each derivative in finite difference form, which leads to

![图片]()

Of course, just the gravity was considered, and here the gravity velocity are constant. In real war, the above situation is not work, in the following process, I will solve this problem step by step.





