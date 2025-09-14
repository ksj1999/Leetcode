# Error : case sensitive

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for i in s:
            if 48<= ord(i) <=57 or 65<= ord(i) <=90 or 97<= ord(i) <=122:
                temp.append(i)
            
        backward = temp[::-1]
        
        print(temp)
        print(backward)
        
        if temp == backward:
            return True
        else:
            return False

      ----------------------------------
# change all to lower case

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for i in s:
            if 48<= ord(i) <=57 or 65<= ord(i) <=90 or 97<= ord(i) <=122:
                temp.append(i.lower())
            
        backward = temp[::-1]

        print(temp)
        print(backward)
        
        if temp == backward:
            return True
        else:
            return False
