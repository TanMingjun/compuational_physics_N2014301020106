# A Brief Introduction to Random and Its Applications In Some physical models 
#####姓名：谭善
#####学号：2014301020106
#####班级：14级弘毅班
***
## Abstract
A stochastic process (or random process) is a probability model used to describe phenomena that evolve over time or space. It plays quite important role in Statistical and Thermal Physics, especially Thermal Physics. It is so fundamental that it was put in the first chapter in most Thermal textbooks. In this paper, I mainly talked random walks in one, two and three dimension situa-tions. Besides, I disscussed another example about random. Here, I used different functions of python to realize our goals.
***
## 1. Backgroud
Stochastic processes were first studied rigorously in the late 19th century to aid in understanding financial markets and Brownian motion. The first person to describe the mathematics behind Brownian motion was Thorvald N. Thiele in a paper on the method of least squares published in 1880. This was followed independently by Louis Bachelier in 1900 in his PhD thesis "The theory of speculation", in which he presented a stochastic analysis of the stock and option markets. Albert Einstein (in one of his 1905 papers) and Marian Smoluchowski (1906) brought the solution of the problem to the attention of physicists, and presented it as a way to indirectly confirm the existence of atoms and molecules. Their equations describing Brownian motion were subsequently verified by the experimental work of Jean Baptiste Perrin in 1908. It boosted the development of physics, so, we are really interested in it.
***
## 2. Generation of random number
Random numbers are required in different techniques of statistics, such as when a representative sample is taken from the population as a whole, or when animals are assigned to a different test group or during a Monte Carlo simulation and so on. True random numbers are generated using physical phenomena. But, we can obtain Pseudo random number by using computer.

* Just like following two groups date. We can get random number using "prob=random.random()" or "x=random.randrange(N)":

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_18.png)
![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_17.png)
##### This is what we obtained, if you run the program again and again, you will find that there is no regularity about the number we get. 

***
## 3. Random walk in one dimension
Assuming that a walker that is able to take steps of length unity along a line. And the walker can go left and right, we just want to study its position(or deviation from the origin). 
In theory, setting each step as s_i, then, we have 

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Equation/equation_3.png)
![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Equation/equation_4.png)
Simplifying it, we have
![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Equation/equation_5.png)

Now, one can assume that the walker move one step during \Delta t=1, and the walker can go right and left with the same probability. Besides, in order to study the walker's mean position and mean value of x^2. We just looped over 10000 times.

* Following pictures can represent two walkers and three walkers in one dimension, their tracks are random.

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_1.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_2.png)

##### From here, we just know that we can predict the walker's track.
* The following is the figure about the walker's mean displacement.

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_3.png)

##### Obviously, the mean displacement of the walker will fluctuate near 0. In theory, the walker have same probability to go to right and left, so it is not surprising to get this result.
* Instantly, we can plot the mean value of the square of the displacement.

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_4.png)

##### From the figure, we know the mean value of the square of the displacement is in direct proportion to the time t. In theory, we have
![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Equation/equation_1.png)
So, here, D=1/2

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_12.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_13.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_16.png)



![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Equation/equation_2.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Equation/equation_6.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Equation/equation_7.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Equation/equation_8.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Equation/equation_9.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Equation/equation_10.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Equation/equation_11.png)




![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/GIF/GIF.gif)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/GIF/GIF2.gif)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_11.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_6.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_5.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_10.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_8.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_19.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_20.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/GIF/GIF4.gif)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/GIF/GIF5.gif)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_7.png)

![](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Final%20project/Figure/figure_9.png)




