class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        def toMorse(word):
            ans=''
            for w in word:
                ans+=morse[ord(w)-97]
            return ans
        return len(set(map(toMorse,words)))
        
