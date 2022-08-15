class Solution:
    def romanToInt(self, s: str) -> int:
        # I - V X, X - L C, C - D M
        
        total = 0
        
        def numeralPair(numerals):
            match numerals:
                case ['I', 'V']:
                    return 4
                case ['I', 'X']:
                    return 9
                case ['X', 'L']:
                    return 40
                case ['X', 'C']:
                    return 90
                case ['C', 'D']:
                    return 400
                case ['C', 'M']:
                    return 900
                case _:
                    return False
                
        def numeralMatch(letter):
            match letter:
                case 'I':
                    return 1
                case 'V':
                    return 5
                case 'X':
                    return 10
                case 'L':
                    return 50
                case 'C':
                    return 100
                case 'D':
                    return 500
                case 'M':
                    return 1000
                
        if len(s) < 2:
            return numeralMatch(s)

        numeralQueue = list(s)

        slidingWindow = [numeralQueue[0], numeralQueue[1]]

        del numeralQueue[0]
        del numeralQueue[0]
        
        while (len(numeralQueue) > 0):
            if len(slidingWindow) < 2:
                slidingWindow.append(numeralQueue[0])
                del numeralQueue[0]
            else:
            
                if numeralPair(slidingWindow) == False:
                    total += numeralMatch(slidingWindow[0])
                    del slidingWindow[0]
                else:
                    total += numeralPair(slidingWindow)
                    slidingWindow = []
        
        while len(slidingWindow) > 0:
            
            if numeralPair(slidingWindow) == False:
                total += numeralMatch(slidingWindow[0])
                del slidingWindow[0]
            else:
                total += numeralPair(slidingWindow)
                slidingWindow = []
        
        return total



    def romanToInt2(self, s: str) -> int:
        # I - V X, X - L C, C - D M
        
        total = 0
        
        def edge(numerals):
            match numerals:
                case ['I', 'V']:
                    return 4
                case ['I', 'X']:
                    return 9
                case ['X', 'L']:
                    return 40
                case ['X', 'C']:
                    return 90
                case ['C', 'D']:
                    return 400
                case ['C', 'M']:
                    return 900
                case _:
                    return False
                
        def numeralMatch(letter):
            match letter:
                case 'I':
                    return 1
                case 'V':
                    return 5
                case 'X':
                    return 10
                case 'L':
                    return 50
                case 'C':
                    return 100
                case 'D':
                    return 500
                case 'M':
                    return 1000
                
        
        numeralSplit = list(s)
        #print(numeralSplit)
        
        if len(numeralSplit) < 2:
            return numeralMatch(s)
            
        
        slidingWindow = [numeralSplit[0], numeralSplit[1]]
        
        
        index = 1

        while(index < len(numeralSplit) + 2):
            if len(slidingWindow) < 2:
                if index < len(numeralSplit):
                    slidingWindow.append(numeralSplit[index])
                    if len(slidingWindow) == 1 and index + 1 < len(numeralSplit) + 2:
                        slidingWindow.append(numeralSplit[index + 1])
                        index += 1
                    #index += 1
                else:
                    if len(slidingWindow) == 0:
                        break
                    total += numeralMatch(slidingWindow[0])
                    break
                    #index += 1
                
            
            if edge(slidingWindow) == False:
                total += numeralMatch(slidingWindow[0])
                del slidingWindow[0]
                index += 1
            else:
                total += edge(slidingWindow)
                slidingWindow = []
                index += 1
        
        return total
        
#test = Solution()

#res = test.romanToInt("MCMXCIV")

#print(res)