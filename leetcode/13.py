class Solution:
    def romanToInt(self, s: str) -> int:
        sv={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        msv={'C':set(['D','M']),'X':set(['L','C']),'I':set(['V','X'])}
        r=0
        mc=''

        for c in s:
            r+=sv[c]
            if mc in msv and c in msv[mc]:
                r-=(sv[mc]*2)
            if c in msv:
                mc=c
            else:
                mc=''
        return r
