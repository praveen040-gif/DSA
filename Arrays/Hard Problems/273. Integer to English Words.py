class Solution:
    def numberToWords(self, n: int) -> str:
        ones=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        teens=["","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens=["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
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
                    res+=ones[n//100]+" Hundred"+" "
                    n=n%100
            return res
        if n==0:
            return "Zero"
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
                res+=ones[n//100]+" Hundred"+" "
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
        return res.strip()
        