class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[[1]]

        for r in range(2,numRows+1):
            nr=[1]
            for i in range(1,r-1):
                nr.append(arr[r-2][i-1]+arr[r-2][i])
            nr.append(1)
            arr.append(nr)
        return arr
