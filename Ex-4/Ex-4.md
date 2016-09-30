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
### [Click Here]()
