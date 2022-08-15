class Solution:

    @staticmethod
    def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        
        list1Length = len(nums1)
        list2Length = len(nums2)
        combinedLength = list1Length + list2Length

        if (combinedLength == 0):
            return 0

        count = 0
        list1Index = 0
        list2Index = 0
        
        if combinedLength % 2 == 1:
            medianNum1 = None
            maxCount = (combinedLength // 2) + 1

            while(count < maxCount - 1):
                if list1Index < list1Length and list2Index < list2Length:
                    if nums1[list1Index] < nums2[list2Index]:
                        list1Index += 1
                        count += 1
                    else:
                        list2Index += 1
                        count += 1
                elif list1Index >= list1Length:
                    list2Index += 1
                    count += 1
                else:
                    list1Index += 1
                    count += 1
            

            if list1Index < list1Length and list2Index < list2Length:
                if nums1[list1Index] < nums2[list2Index]:
                    medianNum1 = nums1[list1Index]
                    list1Index += 1
                    count += 1
                else:
                    medianNum1 = nums2[list2Index]
                    list2Index += 1
                    count += 1
            elif list1Index >= list1Length:
                medianNum1 = nums2[list2Index]
                list2Index += 1
                count += 1
            else:
                medianNum1 = nums1[list1Index]
                list1Index += 1
                count += 1


            return medianNum1

        else:
            medianNum1 = None
            medianNum2 = None
            maxCount = (combinedLength / 2) + 1

            while(count < maxCount - 2):
                if list1Index < list1Length and list2Index < list2Length:
                    if nums1[list1Index] < nums2[list2Index]:
                        list1Index += 1
                        count += 1
                    else:
                        list2Index += 1
                        count += 1
                elif list1Index >= list1Length:
                    list2Index += 1
                    count += 1
                else:
                    list1Index += 1
                    count += 1
            

            if list1Index < list1Length and list2Index < list2Length:
                if nums1[list1Index] < nums2[list2Index]:
                    medianNum1 = nums1[list1Index]
                    list1Index += 1
                    count += 1
                else:
                    medianNum1 = nums2[list2Index]
                    list2Index += 1
                    count += 1
            elif list1Index >= list1Length:
                medianNum1 = nums2[list2Index]
                list2Index += 1
                count += 1
            else:
                medianNum1 = nums1[list1Index]
                list1Index += 1
                count += 1

            if list1Index < list1Length and list2Index < list2Length:
                if nums1[list1Index] < nums2[list2Index]:
                    medianNum2 = nums1[list1Index]
                    list1Index += 1
                    count += 1
                else:
                    medianNum2 = nums2[list2Index]
                    list2Index += 1
                    count += 1
            elif list1Index >= list1Length:
                medianNum2 = nums2[list2Index]
                list2Index += 1
                count += 1
            else:
                medianNum2 = nums1[list1Index]
                list1Index += 1
                count += 1

            return (medianNum1 + medianNum2) / 2