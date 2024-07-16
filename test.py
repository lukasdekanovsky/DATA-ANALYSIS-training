import random
import numpy as np
import matplotlib.pyplot as plt

for age in range(18,80):
    ratio_adjustment = (age - 18) / (80 - 18) 
    plt.scatter(age, ratio_adjustment, color="red")
plt.show()