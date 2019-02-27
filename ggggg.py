t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().strip().split(" ")))
    root=[-1]
    while 1:
        if arr.count(-2)==len(arr)-1 or len(root)==0:
            break
        else:
            temp=[]
            for j in range(0,n):
                if arr[j] in root:
                    print(j,end=" ")
                    arr[j]=-2
                    temp.append(j)
            print("\n")
            
                    
            root=temp.copy()
            #print("check roor",root)
       
                          
