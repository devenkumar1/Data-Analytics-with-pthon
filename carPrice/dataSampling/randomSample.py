import numpy as np

#population data
population=np.arange(1,101)

#random sample of 10 elements
sample= np.random.choice(population,size=10,replace=False)
print("Simple random sample",sample)

#systematic sampling
population= np.arange(1,1001)
n=10
step= len(population) // n
sample= population[::step][:n]
print("systematic sampling",sample)
