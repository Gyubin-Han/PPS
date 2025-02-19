class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        last=strs[0]
        for i in range(1,len(strs)):
            if len(last)<1:
                break

            for j in range(min(len(last),len(strs[i]))):
                if not last[j]==strs[i][j]:
                    last=last[0:j]
                    break
            if len(last)>len(strs[i]):
                last=last[0:len(strs[i])]
        return last
