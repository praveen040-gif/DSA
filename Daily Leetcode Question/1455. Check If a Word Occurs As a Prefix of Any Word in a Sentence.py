class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split()
        print(sentence)
        i=1
        for word in sentence:
            s=""
            for ch in word:
                s=s+ch
                if s==searchWord:
                    return i
            i+=1
        return -1
        