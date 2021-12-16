import matplotlib.pyplot as plt
 
#benchmark specmcf
#L1 Dcache
l1d = [32, 64, 128]
cpi = [1.341420, 1.329469, 1.327828]
 
plt.plot(l1d, cpi)
plt.xlabel('L1 Dcache')
plt.ylabel('CPI')
plt.title('Specmcf')
plt.show()

#L1 Icache
l1i = [32, 64, 128]
cpi = [1.329469, 1.146805, 1.146778]
 
plt.plot(l1i, cpi)
plt.xlabel('L1 Icache')
plt.ylabel('CPI')
plt.title('Specmcf')
plt.show()

#L2 cache
l2 = [512, 2048, 4096]
cpi = [1.329469, 1.322913, 1.322560]
 
plt.plot(l2, cpi)
plt.xlabel('L2 cache')
plt.ylabel('CPI')
plt.title('Specmcf')
plt.show()

#L1 assoc
l1_assoc = [1, 2, 4, 8]
cpi = [1.329469, 1.285876, 1.13141, 1.142834]
 
plt.plot(l1_assoc, cpi)
plt.xlabel('L1 Associativity')
plt.ylabel('CPI')
plt.title('Specmcf')
plt.show()
#L2 assoc
l2_assoc = [1, 2, 4, 8]
cpi = [1.331251, 1.329469, 1.328785, 1.328623]
 
plt.plot(l2_assoc, cpi)
plt.xlabel('L2 Associativity')
plt.ylabel('CPI')
plt.title('Specmcf')
plt.show()
#Cache Line Size
cl = [32, 64, 128] 
cpi = [1.433500, 1.329469, 1.335210]
 
plt.plot(cl, cpi)
plt.xlabel('Cache Line Size')
plt.ylabel('CPI')
plt.title('Specmcf')
plt.show()