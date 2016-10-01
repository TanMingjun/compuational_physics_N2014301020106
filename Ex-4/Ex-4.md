# The fourth time homework-question 1.5 from chapter 1

## 1.Background
Nowadays, computer technologies are applied to all manner of people's life and study. So it is considerably necessary for us to have good command of a kind of computer language especially for us who major in physics. From Chapter 1-A First Numerical Problem, we have learned the way to solve a radioactive decay problem. 
For uranium nuclei decay, it must satisfy the following equation:

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/equation/DUBC0F7EY4FBZ1.png)

Though we have known this equation, it is not enough to work out the figure. Using the Taylor expansion, the question will be simplified easily. One can obtain these formula:

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/equation/D8EQWQ391K67AOHZV0.png)

Obviously, when the change of time is small, higher powers of the change of time can be ignored. Thus, one can rewrite above equation as below:

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/equation/81KRZB9Q4RR%5DD4G78E4.png)

Combining with the first equation, eventually, we can get a very helpful quation:

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/equation/F745IUPTXKNE2HJHSX.png)

It is the key to deal with this problem.

## 2.Abstract
Now, return to problem that is required to solve here.
Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A. Strictly speaking, this is not a 'decay' process, since it is possible for the type B nuclei to turn back into type A nuclei. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/equation/0A2E00MI5YJP1XUO99YP3.png)

where for simplicity we have assumed that the two types of decay are characterized by the same time constant, tau. Solve this system of equations for the numbers of nuclei, NA and NB, as functions of time. Consider different initial conditions, such as NA=100, NB=0, etc., and take tau=1s. Show that your numerical results are consistent with the idea that system reaches a steady state in which NA and NB are constant. In such a steady state, the time derivatives dNA/dt and dNB/dt should vanish.

## 3.Body content
Similarly, for above question, we can obtain that:

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/equation/7D7E0TLG8EUZ2QJY.png)

Now, what we should do is to think of a program to draw a figure to show decay processes of the particle A and the particle B.
We put each step into two lists, one list for x-label, the other list for y-label. Plot these two lists, we can get the figure. There are lots of programs to conduct this work. Here, I will give two of them.

One of them is similar to program that given by teacher.
### [Code:Click Here](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/code/%E7%B2%92%E5%AD%90%E8%A1%B0%E5%8F%98%E6%A8%A1%E6%8B%9F1.py)
The other one is a little different from the first one.
### [Code:Click Here](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/code/%E7%B2%92%E5%AD%90%E8%A1%B0%E5%8F%982.py)
Operating these two programs, we have the same results as below. Here, we choose NA=100, NB=0, tau=1s, time of step=0.05s.
![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/code/figure_1-1.png)

But we can say this picture deplict the excat process of decay, as we all known, the accuracy of results relys on time of step, the smaller the time of step is, the more accurate the result is.

So, I just changed the value of the time of step, assume that time of step=0.2s. At the same picture, we find there are a little differences.

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/code/figure_1_2.png)

Why there are some differences between them? It is not hard for us to find that ,in the process of using the Euler method, we applied a numerical approach. When the time of each step  is smaller, the result is more closer to real situation. In oder to figure out how big the difference between the real value and our results here, I will solve this problem through using mathematical method again. After some simple calculate, I obtain the following solution:

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/code/LWBX32BUFZ7B0ISQ3FJ2.png)

Then, plot these formula on the pylab, compare it with our previous results, we find when the time of each step is smaller, the result we get is realer
###[Code:Click Here](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/code/%E7%9C%9F%E5%AE%9E%E8%A1%B0%E5%8F%98.py)
The comparing picture given by:
![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/code/figure_1_3.png)

Besides, even when N_A and N_B are other values in the begining, eventually, they will be equal. Look like this:
![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/code/figure_1_4.png)

Only when tau_A and tau_B are different, eventual results will be not equal. Here I will several situations:
![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/code/figure_1_5.png)
![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/Ex-4/code/figure_1_6.png)

## 4.Conclusion
Above results told us that the system eventually reached a steady state in which NA and NB are constant, and in such a steady state, the time derivatives dNA/dt and dNB/dt vanished. Though our result is a little different from the real result, but it is considerably accurate.

## 5.Reference
(1) Nicholas J. Giordance, Hisao Nakanishi, 2007, Computational Physics, 2d ed.

(2) [Chapter 1 A First Numerical Problem](https://www.evernote.com/shard/s140/sh/d351f9a3-8076-4274-944b-7043e0ce8cf3/4f89e8630604ea23262f00b3ed11f8ad)

(3) [How to draw planes from a set of linear equations in Python?](https://www.baidu.com/link?url=hsjFGQ4KxCqCTD9pQF-5J7NLrMGslArblR-IUTni4nyYKWGQ0LtLYXBwcFR2tr3fgo2bSrE5bf2raYRG0bFelHzTZLhEyLaoT7faXyH9L1aUwcWld2grK-cSS5tl93HZ7y4DFJrsAs4rn09Y5IZMyZ6ysTFD5dYYx0FKfbErMKi&ie=utf-8&f=8&tn=site888_3_pg&wd=how%20to%20draw%20a%20picture%20in%20python%20when%20equation%20is%20told&oq=how%20to%20draw%20a%20picture%20in%20python%20when%20formula%20is%20told&rqlang=cn&inputT=6463)
