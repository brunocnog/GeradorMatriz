import random
for i in range(50):
    f1=open('arquivo'+str(i+1)+'.txt', 'w')
    for i in range(20):
        for j in range(10):
            n=str(round(random.uniform(0.1,0.99),2))
            x='{:.2f}'.format(float(n))
            if j<9:
                f1.write((x)+' ')
            else:
                f1.write((x))
        f1.write('\n')        
    f1.close()