
import statistics
import matplotlib.pyplot as plt


estimate=[10,20,30,45,54,56,52,53,12,13,16,61,62,68,78,98,85,74,877,56,987,548,54,56,93,21,41,23,100,120,200,200,300,524,257,801,520,457,8,5,6,2,5,4,1,5,48,54,89,6,9,1,6,25,13,65,41,25,48,75,89,56,54,2,15]
y=[]

    
estimate.sort()
tv=int(0.1*(len(estimate)))
estimate=estimate[tv:]
estimate=estimate[:len(estimate)-tv]
for i in range(len(estimate)):
      y.append(5)
plt.plot(estimate,y,'bs')
plt.plot([statistics.mean(estimate)],[5],'ro')
plt.plot([statistics.median(estimate)],[5],'g^')

plt.plot([987],[5],'r^')