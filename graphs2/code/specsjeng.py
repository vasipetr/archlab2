import matplotlib.pyplot as plt
 
#benchmark specsjeng
#L1 Dcache
l1d = [32, 64, 128]
cpi = [7.061319, 7.060753, 7.062413]
 
plt.plot(l1d, cpi)
plt.xlabel('L1 Dcache')
plt.ylabel('CPI')
plt.title('Specsjeng')
plt.show()

#L1 Icache
l1i = [32, 64, 128]
cpi = [7.060753, 7.060751, 7.060732]
 
plt.plot(l1i, cpi)
plt.xlabel('L1 Icache')
plt.ylabel('CPI')
plt.title('Specsjeng')
plt.show()

#L2 cache
l2 = [512, 2048, 4096]
cpi = [7.060753, 7.059627, 7.057942]
 
plt.plot(l2, cpi)
plt.xlabel('L2 cache')
plt.ylabel('CPI')
plt.title('Specsjeng')
plt.show()

#L1 assoc
l1_assoc = [1, 2, 4, 8]
cpi = [7.060753, 7.041210, 7.041189, 7.041202]
 
plt.plot(l1_assoc, cpi)
plt.xlabel('L1 Associativity')
plt.ylabel('CPI')
plt.title('Specsjeng')
plt.show()
#L2 assoc
l2_assoc = [1, 2, 4, 8]
cpi = [7.060691, 7.060753, 7.060774, 7.060066]
 
plt.plot(l2_assoc, cpi)
plt.xlabel('L2 Associativity')
plt.ylabel('CPI')
plt.title('Specsjeng')
plt.show()
#Cache Line Size
cl = [32, 64, 128] 
cpi = [11.669499, 7.060753, 5.015396]
 
plt.plot(cl, cpi)
plt.xlabel('Cache Line Size')
plt.ylabel('CPI')
plt.title('Specsjeng')
plt.show()