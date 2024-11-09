def JobScheduling(self,Jobs,n):
    Jobs.sort(key=lambda x:x.profit,reverse=True)
    profit=0
    count=0
    # for i in Jobs:
    #     print(i.profit,i.deadline,i.id)
    
    
    dead=-1
    count=0
    for i in Jobs:
        dead=max(dead,i.deadline)
    hashmap=[0]*(dead+1)
    
        
    for i in range(n):
        k=Jobs[i].deadline
        # print(k)
        for j in range(k,0,-1):
            if hashmap[j]==0:
                hashmap[j]=1
                profit=profit+Jobs[i].profit
                # print(profit)
                count+=1
                break
    return [count,profit]