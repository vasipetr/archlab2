import matplotlib.pyplot as plt
 
#benchmark specbzip
#L1 Dcache
l1d = [32, 64, 128]
cpi = [1.724417, 1.690421, 1.653960]
 
plt.plot(l1d, cpi)
plt.xlabel('L1 Dcache')
plt.ylabel('CPI')
plt.title('Specbzip')
plt.show()

#L1 Icache
l1i = [32, 64, 128]
cpi = [1.690421, 1.690265, 1.690291]
 
plt.plot(l1i, cpi)
plt.xlabel('L1 Icache')
plt.ylabel('CPI')
plt.title('Specbzip')
plt.show()

#L2 cache
l2 = [512, 2048, 4096]
cpi = [1.690421, 1.647989, 1.630425]
 
plt.plot(l2, cpi)
plt.xlabel('L2 cache')
plt.ylabel('CPI')
plt.title('Specbzip')
plt.show()

#L1 assoc
l1_assoc = [1, 2, 4, 8]
cpi = [1.690421, 1.657387, 1.641618, 1.635409]
 
plt.plot(l1_assoc, cpi)
plt.xlabel('L1 Associativity')
plt.ylabel('CPI')
plt.title('Specbzip')
plt.show()
#L2 assoc
l2_assoc = [1, 2, 4, 8]
cpi = [1.705559, 1.690421, 1.688809, 1.687959]
 
plt.plot(l2_assoc, cpi)
plt.xlabel('L2 Associativity')
plt.ylabel('CPI')
plt.title('Specbzip')
plt.show()
#Cache Line Size
cl = [32, 64, 128] 
cpi = [1.801988, 1.690421, 1.690916]
 
plt.plot(cl, cpi)
plt.xlabel('Cache Line Size')
plt.ylabel('CPI')
plt.title('Specbzip')
plt.show()