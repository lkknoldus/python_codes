import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

x =np.array([8.0, 1, 2.5, 4, 28.0])
x_with_nan = np.array([8.0, 1, 2.5, math.nan, 4, 28.0])

# print(x)
# print(x_with_nan)
# =====================================================================

# mean_ = sum(x) / len(x)
# print(mean_)

# =====================================================================

# #mean
# mean_ = np.mean(x)
# print(mean_)

# =====================================================================

# #harmonic mean
# print(scipy.stats.hmean(x))
# =====================================================================

#geometry mean
# gmean = scipy.stats.gmean(x)
# print(gmean)

# =====================================================================

# #median
# median_ = np.median(x)
# print(median_)
# =====================================================================

# # mode 
# mode_ = scipy.stats.mode(x)
# print(mode_)
# =====================================================================

# # variance
# n = len(x)
# mean_ = sum(x) / n
# var_ = sum((item - mean_)**2 for item in x) / (n - 1)
# print(var_)

# # standard deviation
# std_ = var_ ** 0.5
# print(std_)

# # standard deviation using numpy
# print(np.std(x,ddof=1))

# #skewness formation
# skew_ = (sum((item - mean_)**3 for item in x)
#          * n / ((n - 1) * (n - 2) * std_**3))
# print("skewness: ",skew_)

# #skewness using scipy
# print( scipy.stats.skew(x,bias=False))

# =====================================================================

# Working With 2D Data

a = np.array([[1, 1, 1],
              [2, 3, 1],
              [4, 9, 2],
              [8, 27, 4],
              [16, 1, 1]])
print(a)

mean=np.mean(a)
print(mean)
print (a.mean())

print(np.median(a))

print(a.var(ddof=1))