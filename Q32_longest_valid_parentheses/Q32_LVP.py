class Solution:

    @staticmethod
    def longestValidParentheses(s: str) -> int:
        stack = [None]
        stringList = list(s)
        parenthesesMap = []

        currentRunIndex = 0

        for element in stringList:
            if element == "(":
                stack.append(currentRunIndex)
                parenthesesMap.append(0)
            elif element == ")":
                if stack[-1] != None:
                    parenthesesMap[stack.pop()] = 1
                    parenthesesMap.append(1)
                else:
                    parenthesesMap.append(0)
            
            currentRunIndex += 1
        
        # print(parenthesesMap)

        longest = 0
        currentCount = 0

        for element in parenthesesMap:
            if element == 1:
                currentCount += 1
            elif currentCount > longest:
                longest = currentCount
                currentCount = 0
            else:
                currentCount = 0
        
        if currentCount > longest:
            return currentCount
        else:
            return longest
                    
                


    def longestValidParenthesesOld(s: str) -> int:
        stack = [None]

        stringList = list(s)

        longest = 0
        current = 0

        openParentheses = 0
        closedParentheses = 0

        for element in stringList:
            if element == "(":
                stack.append("(")
                openParentheses += 1
            elif element == ")":
                if stack[-1] == "(":
                    stack.pop()
                    current += 2
                    openParentheses -= 1
                    closedParentheses += 1
                    if longest < current and openParentheses == 0:
                        longest = current
                else:
                    # stack.append(")")
                    openParentheses = 0
                    closedParentheses = 0
                    if current > longest:
                        longest = current
                    
                    current = 0

        if closedParentheses * 2 > longest:
            return closedParentheses * 2

        return longest
