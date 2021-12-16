import matplotlib.pyplot as plt
 
#benchmark spechmmer
#L1 Dcache
l1d = [32, 64, 128]
cpi = [1.361358, 1.338057, 1.318595]
 
plt.plot(l1d, cpi)
plt.xlabel('L1 Dcache')
plt.ylabel('CPI')
plt.title('Spechmmer')
plt.show()

#L1 Icache
l1i = [32, 64, 128]
cpi = [1.338057, 1.209540, 1.209429]
 
plt.plot(l1i, cpi)
plt.xlabel('L1 Icache')
plt.ylabel('CPI')
plt.title('Spechmmer')
plt.show()

#L2 cache
l2 = [512, 2048, 4096]
cpi = [1.338057, 1.338018, 1.338018]
 
plt.plot(l2, cpi)
plt.xlabel('L2 cache')
plt.ylabel('CPI')
plt.title('Spechmmer')
plt.show()

#L1 assoc
l1_assoc = [1, 2, 4, 8]
cpi = [1.338057, 1.185309, 1.184930, 1.184805]
 
plt.plot(l1_assoc, cpi)
plt.xlabel('L1 Associativity')
plt.ylabel('CPI')
plt.title('Spechmmer')
plt.show()
#L2 assoc
l2_assoc = [1, 2, 4, 8]
cpi = [1.338597, 1.338057, 1.338018, 1.338018]
 
plt.plot(l2_assoc, cpi)
plt.xlabel('L2 Associativity')
plt.ylabel('CPI')
plt.title('Spechmmer')
plt.show()
#Cache Line Size
cl = [32, 64, 128] 
cpi = [1.330125, 1.338057, 1.304301]
 
plt.plot(cl, cpi)
plt.xlabel('Cache Line Size')
plt.ylabel('CPI')
plt.title('Spechmmer')
plt.show()