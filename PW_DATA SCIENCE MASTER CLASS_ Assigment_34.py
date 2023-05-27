#!/usr/bin/env python
# coding: utf-8

# # Assignment_10.03.2023(Advance Statistic-3)

# ## Q1. What is Estimation Statistics?Explain point estimate and interval estimate.
# 
# ## Ans:-
#         Estimation statistics is a branch of statistic that deals with estimate population parameters based on information
#         gathered from a sample. it is the first steps of infrential statistic. Estimation is specified observed numerical 
#         value use to estimate an unknown population parameter.
#                             There are two type of Estimation:
#                             1. Point Estimate
#                             2. Interval Estimate.
#                             
#         1. Point Estimate:- A point estimate is a single value that is used to estimate the value of a population parameter.
#                             For example, if we want to estimate the population mean, we might use the sample mean as the 
#                             point estimate. The sample mean is a point estimate of the population mean because it is a 
#                             single value that is used to estimate the population parameter.
#                             
#         2. Interval Estimate:- An interval estimate is a range of values that is used to estimate the value of a population
#                                parameter. For example, we might use a confidence interval to estimate the population mean.
#                                A confidence interval is an interval estimate that gives a range of values within which we 
#                                are confident that the true population parameter lies. The level of confidence is usually 
#                                expressed as a percentage, such as 95%. This means that if we were to take many samples and
#                                compute a confidence interval for each sample, approximately 95% of the intervals would 
#                                contain the true population parameter.
#         
#         Interval estimates are generally considered more informative than point estimates because they provide a range of
#         plausible values for the population parameter, rather than just a single point. However, interval estimates are 
#         also more complex to compute and interpret than point estimates.
#         

# ## Q2. Write a python function to estimate the population mean using a sample mean and standard deviation.
# 
# ## Ans:-

# In[1]:


def estimate_Population_mean(sample_mean,sample_std_dev,sample_size):
    import math 
    z_score = 1.96 # Assuming 95% confidence Interval 
    margin_of_error = z_score*(sample_std_dev/math.sqrt(sample_size))
    lower_bound = sample_mean-margin_of_error
    upper_bound = sample_mean+margin_of_error
    return(upper_bound,lower_bound)


# ## Q3. What is Hypothesis testing?why is it used? state the importance of hypothesis testing.
# 
# ## Ans:-
#         
#         Hypothesis testing is a statistical method used to determine if there is a significant difference between two groups
#         or if a certain assumption about a population is supported by the available data.It is used to determine if there is
#         sufficient evidence to support or reject a particular hypothesis or claim about a population parameter.
#         
#        In hypothesis testing, a researcher starts with a null hypothesis (H0) that states there is no significant difference
#        or relationship between the variables being studied. The researcher then collects data and uses statistical methods 
#        to determine if the null hypothesis should be rejected or not. If the results are statistically significant, the null
#        hypothesis is rejected in favor of an alternative hypothesis (H1) that states there is a significant difference or 
#        relationship between the variables being studied.
#         
#         Hypothesis testing is used in various fields, including science, engineering, business, and social sciences, to test
#         theories, evaluate experimental results, and make decisions based on data. It is an essential tool in scientific 
#         research and data analysis because it provides a systematic and objective way to determine if the observed data 
#         supports or contradicts a particular hypothesis or theory.
# 
#       The importance of hypothesis testing lies in its ability to provide a rigorous and objective framework for evaluating
#       the validity of scientific theories and experimental results. It allows researchers to determine whether the observed
#       results are due to chance or if they represent a genuine effect that can be generalized to the wider population. 
#       Hypothesis testing also helps to reduce the risk of making false conclusions based on incomplete or biased data, 
#       which is crucial in making informed decisions in various fields.
#         

# ## Q4. Create a hypothesis that states whether the average weight of meal college students is greater than the average weight of female college students.
# 
# ## Ans:-
# 
#      Null Hypothesis (H0): The average weight of male college students is equal to or less than the average weight of female
#                            college students.
# 
#     Alternative Hypothesis (H1): The average weight of male college students is greater than the average weight of female
#                                  college students.
#                                  
#           Assuming the parameter and calculate the math part latter.
#         
#           

# ## Q5. Write a python script to conduct a hypothesis test on the difference between two population means, given a sample from each population.
# 
# ## Ans:-

# In[2]:


import numpy as np
from scipy.stats import t

# Define the sample data for two populations
sample1 = [23, 27, 29, 25, 24, 28, 26, 30, 27, 26,18,17]
sample2 = [19, 21, 22, 20, 18, 24, 23, 20, 22, 21,16,10]

# Calculate sample statistics
mean1 = np.mean(sample1)
mean2 = np.mean(sample2)
std1 = np.std(sample1)
std2 = np.std(sample2)
n1 = len(sample1) 
n2 = len(sample2)

# Set the significance level (alpha)
alpha = 0.05

# Calculate the degrees of freedom
df = n1 + n2 - 2

# Calculate the pooled standard deviation
sp = np.sqrt(((n1 - 1) * std1 ** 2 + (n2 - 1) * std2 ** 2) / df)

# Calculate the t-statistic
t_stat = (mean1 - mean2) / (sp * np.sqrt(1 / n1 + 1 / n2))

# Calculate the critical t-value for a two-tailed test
critical_t = t.ppf(1 - alpha / 2, df)

# Compare the t-statistic with the critical t-value
if np.abs(t_stat) > critical_t:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

# Print the t-statistic and the critical t-value
print("t-statistic: ", t_stat)
print("Critical t-value: ", critical_t)


# In[3]:


import numpy as np
import scipy.stats as stats

def conduct_hypothesis_test(alpha=0.05):
    # Generate random sample sizes for each population
    n1 = np.random.randint(10, 20)
    n2 = np.random.randint(10, 20)

    # Generate random samples from each population
    population1 = np.random.normal(0, 1, n1)
    population2 = np.random.normal(0.5, 1, n2)

    # Calculate sample means and variances
    sample1 = np.random.choice(population1, size=n1, replace=True)
    sample2 = np.random.choice(population2, size=n2, replace=True)
    mean1 = np.mean(sample1)
    mean2 = np.mean(sample2)
    var1 = np.var(sample1, ddof=1)
    var2 = np.var(sample2, ddof=1)

    # Calculate test statistic and p-value
    test_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=True)

    # Perform hypothesis test
    if p_value < alpha:
        conclusion = "reject the null hypothesis"
    else:
        conclusion = "fail to reject the null hypothesis"

    # Return results
    result = {
        "sample_size1": n1,
        "sample_size2": n2,
        "sample_mean1": mean1,
        "sample_mean2": mean2,
        "sample_variance1": var1,
        "sample_variance2": var2,
        "test_statistic": test_stat,
        "p_value": p_value,
        "alpha": alpha,
        "conclusion": conclusion
    }
    return result

# Example usage
result = conduct_hypothesis_test()
print(result)


# ## Q6. what is null and alternative hypothesis? Give some example.
# 
# ## Ans:-
#     The null hypothesis and alternative hypothesis are concepts used in statistical hypothesis testing to make inferences
#     about a population based on sample data.
#     
#     1.The null hypothesis (H0) states that there is no significant difference or relationship between variables.Researchers
#     typically aim to reject the null hypothesis in favor of the alternative hypothesis.
#     
#     2.The alternative hypothesis (Ha or H1) proposes a specific relationship, difference, or effect between variables.It is
#     the hypothesis that researchers hope to support if the data provide strong evidence against the null hypothesis. 
#     
#     Example 1:
#             Null hypothesis (H0): There is no significant difference in mean test scores between students who receive 
#             tutoring and those who do not.
#             Alternative hypothesis (Ha): Students who receive tutoring have significantly higher mean test scores compared
#             to those who do not.
# 
#     Example 2:
#            Null hypothesis (H0): The new drug has no effect on reducing blood pressure.
#  
#            Alternative hypothesis (Ha): The new drug significantly reduces blood pressure in patients compared to a placebo.
# 
#     In both examples, the null hypothesis assumes no effect or difference, while the alternative hypothesis suggests a 
#     specific effect or difference that the researcher wants to investigate or support with evidence from the data.
#     

# ## Q7. Write down the steps involve in hState your research question: Clearly define what you want to investigate and identify the variables involved.ypothesis testing.
# 
# ## Ans:-
# Formulate your hypotheses: Create the null hypothesis (H0), which suggests no effect or difference, and the alternative hypothesis (Ha or H1), which proposes a specific effect or difference.
#          The steps involved in Hypothesis Testing.
#          
#          1.State your research question: Clearly define what you want to investigate and identify the variables involved.
#          
#          2.Formulate your hypotheses: Create the null hypothesis (H0), which suggests no effect or difference, and the 
#                                       alternative hypothesis (Ha or H1), which proposes a specific effect or difference.
#                                                                   
#          3.Choose your significance level: Decide on the level of significance (alpha) that determines how strong the 
#                                            evidence needs to be to reject the null hypothesis. Common choices are 0.05 (5%)
#                                            or 0.01 (1%).
#                                            
#          4.Collect and analyze data: Gather a representative sample and analyze the data using appropriate statistical 
#                                      methods for your research question.
#                                      
#          5.Calculate the test statistic: Compute a test statistic that measures the difference between your observed data 
#                                          and what would be expected under the null hypothesis.
#                                          
#          6.Determine the critical region: Establish a critical reagion or rejection region based on your chosen significance
#                                           level. This region consists of extreme values that would lead to rejecting the 
#                                           null hypothesis.
#                                           
#          7.Compare the test statistic with the critical value: Compare your calculated test statistic with the critical 
#                                                                value(s) from a statistical distribution. If the test 
#                                                                statistic falls within the critical region, reject the null
#                                                                hypothesis. If it falls outside the critical region, do not
#                                                                reject the null hypothesis.
#                                                                
#          8.Draw conclusions: Based on the analysis, make a decision about the null hypothesis. If it's rejected, provide
#                              evidence supporting the alternative hypothesis. If it's not rejected, conclude that there is 
#                              insufficient evidence to support the alternative hypothesis.
#                              
#          9. Interpret the results: Explain the findings in the context of your research question. Discuss the implications 
#                                    of the results and any limitations or assumptions made during the analysis.
#                                    
#                                     Hypothesis testing is a systematic process, but the steps may vary depending on the
#            specific test used and the complexity of the research question.

# ## Q8. Define p-value and explain its significance in hypothesis testing.
# 
# ## Ans:-
#            The p-value is a statistical measure that quantifies the strength of evidence against the null hypothesis in
#            hypothesis testing. It represents the probability of observing a test statistic as extreme as, or more extreme
#            than, the one calculated from the data, assuming the null hypothesis is true.
#            
#            The significance of the p-value in hypothesis testing is as follows:
# 
#            1.Assessing evidence against the null hypothesis: A small p-value (typically less than the chosen significance 
#            level) suggests strong evidence against the null hypothesis. It indicates that the observed data are unlikely 
#            to occur if the null hypothesis is true. Conversely, a large p-value suggests weak evidence against the null
#            hypothesis, indicating that the observed data are reasonably likely to occur even if the null hypothesis is true.
#            
#            2.Decision-making: The p-value helps in making decisions about whether to reject or fail to reject the null 
#            hypothesis. If the p-value is smaller than the chosen significance level (e.g., 0.05), it provides evidence to 
#            reject the null hypothesis in favor of the alternative hypothesis. If the p-value is greater than or equal to the
#            significance level, there is insufficient evidence to reject the null hypothesis.
#            
#            3.Strength of evidence: The p-value provides a measure of the strength of evidence against the null hypothesis. 
#            A smaller p-value indicates stronger evidence against the null hypothesis, while a larger p-value suggests weaker 
#            evidence.
#            
#            4.Interpretation: The p-value should be interpreted in the context of the research question and the chosen 
#            significance level. It does not provide information about the effect size or the practical significance of the
#            results. A significant p-value does not necessarily mean a large or important effect, and a non-significant 
#            p-value does not necessarily imply the absence of an effect.
#            
#            

# ## Q9.Generate a student's t-distribution plot using python's Matplotlib library, with the degrees of freedom parameter set to 10.
# 
# ## Ans:-

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Set degree of freedom df.
df = 10

# Generate x-value for the plot
x = np.linspace(-6,6,1000) ##Generates an arry of 100 equally spread value ranging from -5 to 5.
                             ## The value will be used as x-coordinates for the plot.
# compute the cooresponing y-value from the t-distribution
y = t.pdf(x,df)

plt.plot(x,y,label='t-distribution (df=10)')

# set the lable and tritle
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Student\'s t-distribution (df=10)')
#show legend and display the plot
plt.legend()
plt.plot()


# ## Q10. Write a python program to calculate the two -sample t-test for independent samples, give two random samples of equal size  and null hypothesis that a population means are equal.
# 
# ## Ans:-

# In[5]:


import scipy.stats as stats

# Random sample data for two groups
group1 = [2, 3, 4, 5, 6,7,8,9]
group2 = [1, 2, 3, 4, 5,6,7,8]

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(group1, group2)

# Print the results
print("Two-sample t-test results:")
print("t-statistic:", t_statistic)
print("p-value:", p_value)


# ## Q11. What is student's distribution ? when to use the t-distribution?
# 
# ## Ans:-
#            The Student's distribution, also known as the t-distribution, is a probability distribution that is used in
#            statistical inference when the sample size is small and the population standard deviation is unknown. It is 
#            similar to the standard normal distribution but has thicker tails, which accounts for the increased uncertainty 
#            that arises from working with smaller samples.
#            
#  ## The t-distribution is used in the following scenarios:
# 
#             1.When the population standard deviation is unknown: When the population standard deviation is unknown, the
#             t-distribution is used to estimate the population mean based on a sample mean. It provides a more accurate
#             estimation when working with small sample sizes.
# 
#             2.Small sample sizes: The t-distribution is particularly useful when working with small sample sizes 
#             (typically less than 30) where the sample size is not large enough to rely on the assumptions of the normal 
#             distribution.
# 
#             3.When performing hypothesis testing: In hypothesis testing, if the sample size is small and the population
#             standard deviation is unknown, the t-distribution is used to determine critical values and calculate p-values.
# 
#             4.Confidence intervals: The t-distribution is used to construct confidence intervals for the population mean 
#             when the sample size is small and the population standard deviation is unknown.
# 
#                         It's worth noting that as the sample size increases, the t-distribution approaches the standard 
#             normal distribution. Therefore, for larger sample sizes (typically above 30) or when the population standard
#             deviation is known, the standard normal distribution can be used instead of the t-distribution.
# 

# ## Q12. What is t-statistic ? State the formula for t-statistic.
# 
# ## Ans:-
#         The t-statistic is a measure used in hypothesis testing to determine the significance of the difference between 
#         sample means or regression coefficients. It indicates how many standard deviations the sample mean or coefficient
#         is away from the null hypothesis.
#         
#         The Formula of t- Satistic is in given below
#         
#          t = x̅ - µ /(s/√n)
#          
#                 where :  
#                     x̅ = Sample mean
#                     µ = Population Mean
#                     s = sample standard deviation
#                     n = Sample size.
#                     
#                     Note that this formula assumes that the samples are independent and come from populations that follow
#                     a normal distribution.
#                     
# 

# ## Q13. A coffee shop owner want to estimate the average daily revenue for their shop. They take a random sample of 50 days and find the sample mean revenue to be 500 with a standard deviation of 50. Estimate the population mean revenue with a 95% confidence interval.
# 
# ## Ans:-
#             To estimate the population mean revenue with 95% confidence interval, we can use the formula for confidence 
#             interval :-
#              
#              confidance Interval = Sample mean ± (Critical value) * (Sample Standard deviation/sqrt(Sample size))
#              
#              In this poblem statement :-
#                                 Sample mean (x̅)        = 500
#                                 Sample Std Deviation(s) =  50
#                                 Sample size (n)         =  50
#                                 Confidance interval (CI)=  95%
#              first find  the critical value for a 95% of CI. Since the sanple size large (n=50), then we can use the Z-table
#              for Normal Distribution.
#              For a 95% confidence Interval,the critical value (Z) is approximately 1.96.
#               
#               Now we can calculate the CI:
#               
#               CI = 500 ± (1.96)*(50/Sqrt(50))
#                    500 ± 1.96* (50/7.071) [Squreroot of 50, which is 7.071]
#                    500 ± 1.96*7.071
#                    500 ± 13.85916
#              Then the CI of NormalDistribution
#                    Lower bound = 500-13.85916 = 486.14
#                    Upper bound = 500+13.85916 = 513.86
#                    
#                    Therefore the estimate the population mean revenue with a 95% CI is between 486.14 and 513.86 rupees.
#   
#         

# ## Q14. A researcher hypothesizes that a new drug will decrease blood pressure by 10 mmHg. They conduct a clinical trial with 100 patients and find that the sample mean decrease in blood pressure is 8 mmHg with a standard deviation of 3 mmHg.Test the hypothesis with a significance level of 0.05.
# 
# ## Ans:-
#     Here are the perform the hypothesis tetin is given as 0.05
#     
#     1. H0 = The mean decrease in blood pressure not eqal to 10 mmHg. (i.e mmHg = millimeter of mercury, measure pressure)
#        H1 = The mean decrease in blood pressure eqal to 10 mmHg.
# 
#     2. The significance level(α) is given as 0.05
#     3. we don't Know the population std deviation (sigma) value then 
#        then the test statistic for one sample t-test.
#        Calculated using in below formula
#                 t = (Sample mean - hypothesized mean)/(sample std Deviation/sqrt(sample size))
#                 
#                 t = x̅ - µ /(s/√n)
#                             In this case:
#                             sample mean (x̅) = 8 mmHg
#                             Hypothesized mean(µ) = 10 mmHg
#                             Sample Standard deviation (s) = 3mmHg
#                             Sample Size(n) = 100
#                    
#                    so, t = (8-10)/(3/Sqrt(100))
#                             -2/(3/10)
#                             -20/3
#                             -6.67
#                             
#        4.Since the alternative hypothesis is two-tailed test, we need to find the critical t-value at the significance
#          level of 0.05/2=0.025.
#          with the sample size of 100, the degree of freedom (df) are (n-1) ~ 100-1=99.
#          The critical t-value in a t -distribution table or using a satistical calculator 
#          we find the approximately ±1.984.
#          
#        5. t-value ( in calculation) > t-critical value( calculated through the t- distribution table)
#           -6.67 > ±1.984
#            so, we reject the null hypothesis(H0).
#            
#        6. Conclusion - Base on data, at a significance level of 0.05,there is sufficient evidence to suggest that
#                        the new drug decreases blood pressure by 10 mmHg.
#          
#          

# ## Q15. An electronics company produces a certain type of product with a mean weight of 5 pounds and a standard deviation  of 0.5 pounds. A random sample of 25 products is taken and the sample mean wieght is found to be 4.8 pounds. Test the hypotesis that the true mean weight of the products is less than 5 pounds with a significance level of 0.01.
# 
# ## Ans:-
# 
#         The hypothesis that the true mean weight of the products is less than 5 pounds, we can use a one-sample t-test.
#         due to population sample size n<30.
#         
#            Null Hypothesis (H0) is μ=5 pound
#            Alternet Hypothesis (H1) is μ≠5 pound
#            
#            significance level (α) is given proble statement is 0.01.
#         
#            The popiulation sample size is less than equal to 30 so that we can proform t-statistic for calulation.
#            so that giveh
#             
#              Sample mean(x̄) = 4.8 pounds
#              Population mean (μ) = 5 pounds
#              Population standard deviation (σ) = 0.5 pounds
#              Sample size (n) = 25
#              
#              We can calculate the test statistic using the formula:
#             t = (Sample mean - Population mean)/(population std Deviation/sqrt(sample size))
#             t = (x̄ - μ) / (σ / √n)
#             
#             t= (4.8-5.0)/(0.5/sqrt(25))
#             t= -0.2/(0.5/5) i.e sqrt(25) = 5
#             t = -0.2/0.1
#             t= -2
#             
#             The tested Statistic is -2.
#             
#             To test the hypothesis, we compare the test statistic with the critical value from the t- distrubution 
#             at a significance level of 0.01 and the degree of freedom (n-1) = 25-1=24.
#             
#             Since as per problem statement test the hypotesis that the true mean weight of the products is less than
#             5 pounds, we are conducting a one-tail test,so we need to find the critical value for the lower tail.
#             
#             Using a t-distribution table, the critical value for a one- tail test with a significance level of 0.01 and 24
#             degree of freedom is approxmately -2.492.
#             
#             After calculation we find that the test statistic (-2) is garter than the critical value (-2.492),we fail to
#             reject the null hypothesis.
#             
#             

# ## Q16. Two group of students are given different study materials to prepare for a test. The first group (n1=30) has a mean score of 80 with standard deviation of 10, and the second group (n2=40) has a mean score of 75 with standard deviation of 8. Test the hypothesis that the population means for the two groups are equal with significance level of 0.01.
# 
# ## Ans:-
# 
#     Let's define our hypotheses:
# 
#     Null Hypothesis (H0): The population means for the two groups are equal.
#     Alternative Hypothesis (H1): The population means for the two groups are not equal.
#     We can use the following formula to calculate the test statistic for a two-sample t-test:
# 
#     t = (mean1 - mean2) / sqrt((s1^2 / n1) + (s2^2 / n2))
# 
#     where:
# 
#         mean1 and mean2 are the sample means of the two groups.
#         s1 and s2 are the sample standard deviations of the two groups.
#         n1 and n2 are the sample sizes of the two groups.
#     Given:
#         Group 1:
# 
#         Sample size (n1) = 30
#         Sample mean (x̄1) = 80
#         Sample standard deviation (s1) = 10
#     Group 2:
# 
#         Sample size (n2) = 40
#         Sample mean (x̄2) = 75
#         Sample standard deviation (s2) = 8
#         
#         Let's calculate the test statistic using these values:
# 
#         t = (80 - 75) / sqrt((10^2 / 30) + (8^2 / 40))
# 
#                 Now, we can compare the calculated test statistic to the critical value from the t-distribution table with 
#                 (n1 + n2 - 2) degrees of freedom and a significance level of 0.01 to determine whether to reject or fail to
#                 reject the null hypothesis.
# 
#     The critical value is found using a t-distribution table or statistical software. For a significance level of 0.01 and 
#     degrees of freedom (df) = (n1 + n2 - 2) = (30 + 40 - 2) = 68, the critical value is approximately ±2.627.
# 
#     If the calculated test statistic is greater than the critical value or less than its negative, we reject the null 
#     hypothesis; otherwise, we fail to reject the null hypothesis.
# 
#     Now, let's calculate the test statistic and compare it to the critical value:
# 
#         t = (80 - 75) / sqrt((10^2 / 30) + (8^2 / 40))
#         t = 5 / sqrt((100/30) + (64/40))
#         t = 5 / sqrt(3.333 + 1.6)
#           ≈ 5 / sqrt(4.933)
#           ≈ 5 / 2.22
#           ≈ 2.25
# 
#         Since the calculated test statistic (2.25) is less than the critical value (±2.627), we fail to reject the null 
#         hypothesis.
# 
#         Therefore, based on the given data and a significance level of 0.01, there is not enough evidence to conclude that
#         the population means for the two groups are different.
# 

# ## Q17. A marketing company wants to estimate the average number of  ads watched by viewers during a TV program. They take a random samples of 50 viewers and find the sample mean is 4 with a standard deviation of 1.5. Estimate the population mean with a 99% confidance interval.
# 
# 
# ## Ans:-
#         To estimate the population mean with a 99% confidence interval, we can use the formula 
#         confidance interval = sample mean ± (Critical Value * Standard Error)
#         in the proble statement :
#             1.Sample mean :- The mean of the sample given as 4.
#             2.Critical value :- The value obtained from the t-distribution table.
#             3.Standard Error :- The standard deviation of the sample divided by the Square root of the sample size
#             
#             Given value in proble statement
#               sample mean (x̄)          = 4
#               Sample Std Deviation (s) = 1.5
#               Sample size (n)          = 50
#               Confidance interval      = 99%(which corresponds to significance level of 0.01)
#               
#               Now first calculte the critical value for a 99% confidance level with (n-1)degree of freedom.
#               in this case, the degree of freedom would be :-
#               
#               df= (n-1)= 50-1 = 49
#               
#               Using t-distribution table, the critical value of two tailed test with a significance level of 0.01and
#               degree of freedom (df)equal to 49 is approximately 2.6842.
#               
#               Then we can calculated the standard error:
#               
#               Standard Error = Sample std deviation/sqrt(Sample size)
#                              = 1.5/sqrt(50)
#                              = 1.5/7.071
#                              = 0.212
#               Now calculate the confidance interval
#               
#               confidance interval = sample mean ± (Critical Value * Standard Error)
#                             CI = 4±(2.6842*0.212 )
#                             CI = 4±0.568
#                             then lower point = 4-0.568 = 3.423
#                                  Upper point = 4+0.568 = 4.568
#                      so that, The CI is approximately (3.423,4.568)
#                      
#             Therefore, with 99% confidence, we can estimate that the population mean number of ads watched by viewers
#             during a TV program falls between 3.432 and 4.568.
#               
