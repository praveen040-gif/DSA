n=int(input())
ones=["","one","two","three","four","five","six","seven","eight","nine"]
teens=["","eleven","twelve","thirteen","fourteen","fivteen","sixteen","seventeen","eightteen","nineteen"]
tens=["","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
res=""
def thousands(n):
    res=""
    while n!=0:
        if n<10:
            res=res+ones[n]+" "
            n=n//10
        elif n>10 and n<20:
            res=res+teens[n%10]+" "
            n=n//20
        elif n>=10 and n<100:
            res+=tens[n//10]+" "
            n=n%10
        elif n>=100 and n<1000:
            res+=ones[n//100]+" Hundered"+" "
            n=n%100
    return res
if n==0:
    print("Zero")
while n!=0:
    if n<10:
        res=res+ones[n]+" "
        n=n//10
    elif n>10 and n<20:
        res=res+teens[n%10]+" "
        n=n//20
    elif n>=10 and n<100:
        res+=tens[n//10]+" "
        n=n%10
    elif n>=100 and n<1000:
        res+=ones[n//100]+" Hundered"+" "
        n=n%100
    elif n>=1000 and n<1000000:
        ans=n//1000
        res1=thousands(ans)
        res+=res1+"Thousand "
        n=n%1000
    elif n>=1000000 and n<1000000000:
        ans=n//1000000
        res1=thousands(ans)
        res+=res1+"Million "
        n=n%1000000
    elif n>=1000000000:
        ans=n//1000000000
        res1=thousands(ans)
        res+=res1+"Billion "
        n=n%1000000000
    


print(res.strip())