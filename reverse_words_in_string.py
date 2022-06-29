class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        letters = []
        temp = []
        for word in words:
            letters.append(list(word)) 
            
        for letter in letters:
            letter.reverse()
        words = []
        for letter in letters:
            words.append("".join(letter))
        res = " ".join(words)
        return res