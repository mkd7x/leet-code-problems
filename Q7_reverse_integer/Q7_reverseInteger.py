class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        
        output = 0
        makePositive = False
        
        if x < 0:
            x = x * -1
            makePositive = True

        maxNumbersList = [7,4,6,3,8,4,7,4,1,2]

        numbersList = []

        while x != 0:
            numbersList.append(x % 10)
            x = x // 10

        if len(numbersList) == len(maxNumbersList):
            for index in range(len(numbersList)):
                if index == 9:
                    # Note: only need to check if appending the final digit will cause overflow
                    if output > 147483648 and numbersList[-1] > 1 and makePositive == True:
                        return 0
                    if output > 147483647 and numbersList[-1] > 1 and makePositive == False:
                        return 0
                    
                output += numbersList.pop() * (10 ** index)
        else:
            for index in range(len(numbersList)):
                output += numbersList.pop() * (10 ** index)
        

        if makePositive == True:
            output = output * -1

        return output