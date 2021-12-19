import matplotlib.pyplot as plt
 
#benchmark speclibm
#L1 Dcache
l1d = [32, 64, 128]
cpi = [2.650347, 2.640541, 2.636105]
 
plt.plot(l1d, cpi)
plt.xlabel('L1 Dcache')
plt.ylabel('CPI')
plt.title('Speclibm')
plt.show()

#L1 Icache
l1i = [32, 64, 128]
cpi = [2.640541, 2.640463, 2.640454]
 
plt.plot(l1i, cpi)
plt.xlabel('L1 Icache')
plt.ylabel('CPI')
plt.title('Speclibm')
plt.show()

#L2 cache
l2 = [512, 2048, 4096]
cpi = [2.640541, 2.638581, 2.636170]
 
plt.plot(l2, cpi)
plt.xlabel('L2 cache')
plt.ylabel('CPI')
plt.title('Speclibm')
plt.show()

#L1 assoc
l1_assoc = [1, 2, 4, 8]
cpi = [2.640541, 2.624978, 2.631263, 2.631263]
 
plt.plot(l1_assoc, cpi)
plt.xlabel('L1 Associativity')
plt.ylabel('CPI')
plt.title('Speclibm')
plt.show()
#L2 assoc
l2_assoc = [1, 2, 4, 8]
cpi = [2.640650, 2.640541, 2.640405, 2.639918]
 
plt.plot(l2_assoc, cpi)
plt.xlabel('L2 Associativity')
plt.ylabel('CPI')
plt.title('Speclibm')
plt.show()
#Cache Line Size
cl = [32, 64, 128] 
cpi = [3.925416, 2.640541, 2.008439]
 
plt.plot(cl, cpi)
plt.xlabel('Cache Line Size')
plt.ylabel('CPI')
plt.title('Speclibm')
plt.show()