import numpy as np
import time
import os
def quad_bubble_sort(arr:list):
    n=len(arr)
    l_mid=r_mid=n//2
    start=0
    end=n-1
    while True:
        swap=False
        for i in range(start,end):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swap=True
                print(arr)
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(0.1)
        end-=1;swap=False
        for j in range(end,start,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                swap=True
                print(arr)
                time.sleep(0.1)
            os.system('cls' if os.name == 'nt' else 'clear')
        start+=1;swap=False
        
        for k in range(l_mid,start-1,-1):
            if arr[k]<arr[k-1]:
                arr[k],arr[k-1]=arr[k-1],arr[k]
                swap=True
                print(arr)
                time.sleep(0.1)
            os.system('cls' if os.name == 'nt' else 'clear')
        l_mid-=1;swap=False
        
        for l in range(r_mid,end):
            if arr[l]>arr[l+1]:
                arr[l],arr[l+1]=arr[l+1],arr[l]
                swap=True
                print(arr)
                time.sleep(0.1)
            os.system('cls' if os.name == 'nt' else 'clear')
        r_mid+=1
        
        if not swap:
            break
    return arr
a=[float(i)for i in np.linspace(0,1,10)]
np.random.shuffle(a)
print(quad_bubble_sort(a))