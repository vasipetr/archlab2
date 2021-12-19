import numpy as np
import matplotlib.pyplot as plt
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')

benchmarks = ('specbzip\nCPI=1.615699', 'specmcf\nCPI=1.154912', 'spechmmer\nCPI=1.179978', 'specsjeng\nCPI=6.795293', 'speclibm\nCPI=2.576597')
costs = [441.6, 441.6, 392.4, 699.6, 725.2]

plt.rcParams["figure.figsize"] = (12, 8)

plt.bar(benchmarks, costs)
addlabels(benchmarks,costs)
plt.xlabel("Benchmarks", fontsize=15)
plt.ylabel("Cost", fontsize=15)
plt.title("Cost Evaluation", fontsize=15)
plt.show()
