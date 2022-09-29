import sys
import matplotlib
import pandas as pd
# from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("mnist_train.csv")
d = []
d_2 = []
d_3 = []
for i in data.dropna():
  d.append(i[0])
  d_2.append(i[1])
  d_3.append(i[2])
print(d)  
print(d_2)
print(d_3)
fig, axs = plt.subplots(3, sharex=True)
fig.suptitle('Sharing both axes')
cm = 1/2.54 
axs[0].plot(d,'tab:green')
axs[1].plot(d_2)
axs[2].plot(d_3)
# plt.subplots(figsize=(15*cm, 5*cm))
plt.show()
print("\n")
fig, (ax1,ax2) = plt.subplots(1, 2,subplot_kw=dict(projection='polar'))
ax1.plot(d)
ax2.plot(d_2)
# plt.plot(d)
plt.show()

print("\n")
fig, (ax1,ax2) = plt.subplots(1, 2,subplot_kw=dict(projection='polar'))
ax1.plot(d)
ax2.plot(d_3)
# plt.plot(d)
plt.show()
