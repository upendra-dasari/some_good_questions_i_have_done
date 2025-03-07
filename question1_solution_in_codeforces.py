
import numpy as np
def fn(a,i,n):
    if(n==4):
        return 1
    else:
        r,c=i
        a[r,c]=-1
        (c1,)=np.where(a[r,:]==0)
        (r1,)=np.where(a[:,c]==0)
        p = [(r, col) for col in c1] + [(row, c) for row in r1]
        if(len(p)==0):
            return 0
        else:
            s=0
            for j in p:
                s=s+fn(a.copy(),j,n+1)
            return s    
                
a=np.array([[0,-1,0,-1],[-1,0,0,0],[0,-1,-1,-1]])
r,c = np.where(a == 0)  

p = list(zip(r,c))
s=0 
for i in p:
    s=s+fn(a.copy(),i,1)
print(s)    

