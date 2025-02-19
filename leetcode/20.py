class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]

        for c in s:
            if c in ['(','{','[']:
                arr.append(c)
                continue

            if c in [')','}',']']:
                if len(arr)<0+1:
                    return False
                p=arr.pop()

                if not((c==')' and p=='(') or (c=='}' and p=='{') or (c==']' and p=='[')):
                    return False

        if len(arr)>0:
            return False
        else:
            return True
