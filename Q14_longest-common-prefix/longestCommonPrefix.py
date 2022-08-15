class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        output = ""   

        # Get shortest word length

        shortestWord = strs[0]

        for element in strs:
            if len(element) < len(shortestWord):
                shortestWord = element
        
        # Empty string detected quick exit
        if shortestWord == "":
            return ""

        # base index on shortest word

        for index in range(len(shortestWord) + 1):
            output = shortestWord[:index]

            for word in strs:
                if output != word[:index]:
                    return output[:index-1]
        
        return output


