#!/usr/bin/env python
# coding: utf-8
#Q1: What are the Probability Mass Function (PMF) and Probability Density Function (PDF)? Explain with
an example.
Ans -Probability Mass Function
Probability mass function gives the probability that a discrete random variable will be exactly equal to a specific value. The probability mass function is only used for discrete random variables. For continuous random variables, the probability density function is used which is analogous to the probability mass function. 

Let X
 be a discrete random variable with range RX={x1,x2,x3,...}
 (finite or countably infinite). The function
PX(xk)=P(X=xk), for k=1,2,3,...,
is called the probability mass function (PMF) of X
 Probability density function-
    In probability theory, a probability density function (PDF) is used to define the random variable’s probability coming within a distinct range of values, as opposed to taking on any one value. The function explains the probability density function of normal distribution and how mean and deviation exists. 
   Ex Say we have a continuous random variable whose probability density function is given by f(x) = x + 2, when 0 < x ≤ 2. We want to find P(0.5 < X < 1). Then we integrate x + 2 within the limits 0.5 and 1. This gives us 1.375. Thus, the probability that the continuous random variable lies between 0.5 and 1 is 1.375.#Q2: What is Cumulative Density Function (CDF)? Explain with an example. Why CDF is used?
Ans-The Cumulative Distribution Function (CDF), of a real-valued random variable X, evaluated at x, is the probability function that X will take a value less than or equal to x.
The CDF defined for a discrete random variable and is given as

Fx(x) = P(X ≤ x)
The CDF defined for a continuous random variable is given as;

Cumulative Distribution Function
The most important application of cumulative distribution function is used in statistical analysis. In statistical analysis, the concept of CDF is used in two ways.

Finding the frequency of occurrence of values for the given phenomena using cumulative frequency analysis.
To derive some simple statistics properties, by using an empirical distribution function, that uses a formal direct estimate of CDFs.Q3: What are some examples of situations where the normal distribution might be used as a model?
Explain how the parameters of the normal distribution relate to the shape of the distribution.
Ans-In probability theory and statistics, the Normal Distribution, also called the Gaussian Distribution, is the most significant continuous probability distribution. Sometimes it is also called a bell curve. A large number of random variables are either nearly or exactly represented by the normal distribution, in every physical science and economics. Furthermore, it can be used to approximate other probability distributions.
Normal Distribution Formula
The probability density function of normal or gaussian distribution is given by;
 standard deviation, the Empirical Rule states that,

Approximately 68% of the data falls within one standard deviation of the mean. (i.e., Between Mean- one Standard Deviation and Mean + one standard deviation)
Approximately 95% of the data falls within two standard deviations of the mean. (i.e., Between Mean- two Standard Deviation and Mean + two standard deviations)
Approximately 99.7% of the data fall within three standard deviations of the mean. (i.e., Between Mean- three Standard Deviation and Mean + three standard deviations)
EX Calculate the probability density function of normal distribution using the following data. x = 3, μ = 4 and σ = 2.

Solution: Given, variable, x = 3

Mean = 4 and

Standard deviation = 2

By the formula of the probability density of normal distribution, we can write;

normal distribution example

Hence, f(3,4,2) = 1.106.




#Q4: Explain the importance of Normal Distribution. Give a few real-life examples of Normal Distribution.
Ans- One reason the normal distribution is important is that many psychological and educational variables are distributed approximately normally. Measures of reading ability, introversion, job satisfaction, and memory are among the many psychological variables approximately normally distributed.
It has the following properties:

Bell shaped
Symmetrical
Unimodal – it has one “peak”
Mean and median are equal; both are located at the center of the distribution
About 68% of data falls within one standard deviation of the mean
About 95% of data falls within two standard deviations of the mean
About 99.7% of data falls within three standard deviations of the mean

# In[2]:


#EX question  4
import numpy as np
 
def normal_dist(x, mean, sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density
 
mean = 2
sd = 4
x = 4
result = normal_dist(x, mean, sd)
print(result)

#Q5: What is Bernaulli Distribution? Give an Example. What is the difference between Bernoulli
Distribution and Binomial Distribution?
Ans- The Bernoulli distribution therefore describes events having exactly two outcomes, which are ubiquitous in real life. Some examples of such events are as follows: a team will win a championship or not, a student will pass or fail an exam, and a rolled dice will either show a 6 or any other number.
Binomial VS Bernoulli Keypoints!
Bernoulli deals with the outcome of the single trial of the event, whereas Binomial deals with the outcome of the multiple trials of the single event.
Bernoulli is used when the outcome of an event is required for only one time, whereas the Binomial is used when the outcome of an event is required multiple times.
#Q6. Consider a dataset with a mean of 50 and a standard deviation of 10. If we assume that the dataset
is normally distributed, what is the probability that a randomly selected observation will be greater
than 60? Use the appropriate formula and show your calculations.
Ans 0.343#Q7: Explain uniform Distribution with an example.
Ans-In statistics, uniform distribution refers to a type of probability distribution in which all outcomes are equally likely. A deck of cards has within it uniform distributions because the likelihood of drawing a heart, a club, a diamond, or a spade is equally likely.
A "uniform distribution" means all possible outcomes in the range have equal probability of occurring.#Q8: What is the z score? State the importance of the z score.
Ans-What Is Z-Score? Z-score is a statistical measurement that describes a value's relationship to the mean of a group of values. Z-score is measured in terms of standard deviations from the mean. If a Z-score is 0, it indicates that the data point's score is identical to the mean score.#Q9: What is Central Limit Theorem? State the significance of the Central Limit Theorem.
Ans-e central limit theorem states that whenever a random sample of size n is taken from any distribution with mean and variance, then the sample mean will be approximately a normal distribution with mean and variance. The larger the value of the sample size, the better the approximation of the normal
n other words, the central limit theorem states that for any population with mean and standard deviation, the distribution of the sample mean for sample size N has mean μ and standard deviation σ/√n.
1] The sample distribution is assumed to be normal when the distribution is unknown or not normally distributed according to the central limit theorem. This method assumes that the given population is distributed normally. It helps in data analysis.

2] The sample mean deviation decreases as we increase the samples taken from the population, which helps in estimating the mean of the population more accurately.

3] The sample mean is used to create a range of values which likely includes the population mean.

4] The concept of the central limit theorem is used in election polls to estimate the percentage of people supporting a particular candidate as confidence intervals.

5] CLT is used in calculating the mean family income in a particular country.

6] It is used in rolling many identical, unbiased dice.

7] The probability distribution for the total distance covered in a random walk will approach a normal distribution.

8] Flipping many coins will result in a normal distribution for the total number of heads (or, equivalently total number of tails).
#Q10: State the assumptions of the Central Limit Theorem.
Ans- Assumptions of the Central Limit Theorem
The sample should be drawn randomly following the condition of randomisation.
The samples drawn should be independent of each other. They should not influence the other samples.
When the sampling is done without replacement, the sample size shouldn’t exceed 10% of the total population.
The sample size should be sufficiently large.
# In[ ]:




