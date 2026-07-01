class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str=""
        for s in strs:
            enc_str += str(len(s))+"#"+s
        return enc_str

    def decode(self, s: str) -> List[str]:
        strs=[]
        i=0 #to keep  tab on our current position in string
        while i<len(s):
            #finding the #
            j=i
            while s[j] !="#":
                j+=1
            #getting the length of the next word which is between i and j could be 1 or 11
            length=int(s[i:j])
            #moving the i possition to the first character of the word
            i=j+1
            #getting the word from the string which is between i and + lenght from befor hash
            word=s[i:i+length]
            #adding the word to the array 
            strs.append(word)
            #jumping to net word 
            i+=length
        return strs

            


