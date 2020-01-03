class Solution:
    def median(self, list1):
        if len(list1) % 2 == 0:
            med1 = list1[len(list1) // 2]
            med2 = list1[len(list1) // 2 - 1]
            return (med1 + med2) / 2
        else:
            med = list1[len(list1) // 2]
            return med

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1 = []
        tot = len(nums1) + len(nums2)
        count1 = count2 = i = j = 0
        if all(v == 0 for v in nums1) and all(v == 0 for v in nums2):
            return 0
        if nums1 == []:
            return self.median(nums2)
        if nums2 == []:
            return self.median(nums1)
        k=0
        while k < tot:
            if count1 < len(nums1) and nums1[i] == 0:
                list1.append(0)
                i+=1
                count1+=1
            elif count2 < len(nums2) and nums2[j] == 0:
                list1.append(0)
                j+=1
                count2+=1
            elif count1 < len(nums1) and count2 < len(nums2):
                if (nums1[i] < nums2[j]) and count1 < len(nums1):
                    list1.append(nums1[i])
                    count1 += 1
                    i += 1
                elif (nums1[i] > nums2[j]) and count2 < len(nums2):
                    list1.append(nums2[j])
                    count2 += 1
                    j += 1
                elif (nums1[i] == nums2[j]) and count1 < len(nums1) and count2 < len(nums2):
                    list1.append(nums1[i])
                    list1.append(nums2[j])
                    i += 1
                    j += 1
                    k += 1
                    count1 += 1
                    count2 += 1
            elif count2 == len(nums2):
                list1.append(nums1[i])
                i += 1
            elif count1 == len(nums1):
                list1.append(nums2[j])
                j += 1
            k+=1
        return self.median(list1)

#------------------------------------------------------------------------

        list1 = []
        for i in nums1:
            list1.append(i)
        for i in nums2:
            list1.append(i)
        list1 = sorted(list1)
        if len(list1)%2 != 0:
            med1 = len(list1)//2
            med11 = list1[med1]
        else:
            med1 = len(list1)//2
            med2 = len(list1)//2 - 1
            med11 = (list1[med1] + list1[med2])/2
        return med11
