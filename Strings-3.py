# Strings-3

## Problem 1 Integer to English Words (https://leetcode.com/problems/integer-to-english-words/)
 
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        self.thousands = ["","Thousand","Million","Billion"]
        self.below_20 = ["","One","Two","Three", "Four", "Five", "Six","Seven","Eight","Nine","Ten","Eleven", "Twelve","Thirteen","Fourteen","Fifteen","Sixteen", "Seventeen", "Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty", "Forty", "Fifty","Sixty","Seventy", "Eighty","Ninety"]
        i=0
        result = ""
        while num >0:
            if (num % 1000 != 0):
                result =  self.fun(num%1000)+self.thousands[i]+" "+result
            i = i+1
            num = num // 1000
        return result.strip()
    
    def fun(self,num):
        if num == 0:
            return ""
        elif num < 20:
            return self.below_20[num]+" "
        elif num <100:
            return self.tens[int(num/10)]+ " " +self.fun(num%10)
        else:
            return self.below_20[int(num/100)]+ " Hundred "+ self.fun(num%100)

# TC = O(1), SC = O(1)

## Problem 2 Basic Calculator || (https://leetcode.com/problems/basic-calculator-ii/)

class Solution:
    def calculate(self, s: str) -> int:
        if s== None or len(s) == 0:
            return 0
        num = 0
        calc = 0 
        tail = 0
        lastSign = '+'
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num*10 + (int)(c)
            if (not c.isdigit() and c!=' ') or (i== len(s)-1):
                if lastSign == '+':
                    calc = calc + num
                    tail = +num
                if lastSign == '-':
                    calc = calc - num
                    tail = -num
                if lastSign == '*':
                    calc = calc - tail + (tail*num)
                    tail = tail*num
                if lastSign == '/':
                    calc = calc - tail + int(tail/num)
                    tail = int(tail/num)
                lastSign = c
                num =0
        return calc
# TC = O(n); SC= O(1)

