class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result=[]
        for i in range(1,n+1):
            s=""
            if i%3==0:
                s+="Fizz"
            if i%5==0:
                s+="Buzz"
            if s=="":
                s=str(i)
            result.append(s)
        return result
