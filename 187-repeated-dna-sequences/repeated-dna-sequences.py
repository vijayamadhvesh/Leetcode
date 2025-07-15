class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen=set()
        result=set()
    
        for i in range(len(s)-10+1):
        
            sub_string=s[i:i+10]

            if sub_string not in seen:
                seen.add(sub_string)
            else:
               result.add(sub_string)
        

        return list(result)