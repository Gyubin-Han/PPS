class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr=[]
        isUp=False

        digits[-1]+=1
        for i in range(1,len(digits)+1):
            if isUp:
                digits[-i]+=1
                isUp=False
            
            if digits[-i]>9:
                isUp=True
                digits[-i]=0
        
        if isUp:
            arr.append(1)
        for i in digits:
            arr.append(i)
        
        return arr
