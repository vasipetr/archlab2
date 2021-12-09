import numpy as np
import matplotlib.pyplot as plt

benchmarks = ('specbzip', 'specmcf', 'spechmmer', 'specsjeng', 'speclibm')


#Execution Time
exec_times = [0.083982, 0.064955, 0.059396, 0.513528, 0.174671]

plt.bar(benchmarks, exec_times, color = 'black')
plt.xlabel("Benchmarks", fontsize=15)
plt.ylabel("Execution Time (s)", fontsize=15)
plt.title("Execution Time of Benchmarks", fontsize=15)
plt.show()

#CPI
cpi = [1.679650, 1.299095, 1.187917, 10.270554, 3.493415]

plt.bar(benchmarks, cpi, color = 'darkred')
plt.xlabel("Benchmarks", fontsize=15)
plt.ylabel("CPI", fontsize=15)
plt.title("CPI (Cycles per Instruction)", fontsize=15)
plt.show()

#Miss Rate - L1 Dcache
l1d = [0.014798, 0.002108, 0.001637, 0.121831, 0.060972]

plt.bar(benchmarks, l1d, color = 'midnightblue')
plt.xlabel("Benchmarks", fontsize=15)
plt.ylabel("Miss Rate (%)", fontsize=15)
plt.title("L1 Dcache Miss Rate", fontsize=15)
plt.show()

#Miss Rate - L1 Icache
l1i = [0.000077, 0.023612, 0.000221, 0.000020, 0.000094]
plt.bar(benchmarks, l1i, color = 'indigo')
plt.xlabel("Benchmarks", fontsize=15)
plt.ylabel("Miss Rate (%)", fontsize=15)
plt.title("L1 Icache Miss Rate", fontsize=15)
plt.show()

#Miss Rate - L2 cache
l2 = [0.282163, 0.055046, 0.077760, 0.999972, 0.999944]

plt.bar(benchmarks, l2, color = 'orangered')
plt.xlabel("Benchmarks", fontsize=15)
plt.ylabel("Miss Rate (%)", fontsize=15)
plt.title("L2 cache Miss Rate", fontsize=15)
plt.show()
