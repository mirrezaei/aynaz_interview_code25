#You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

# the idea is to take advantage of merge sort.
# the reason is that if a number moves from right to left, then it means thr right number has been smaller than the left number, and we call it inversion count
#this inversion should be counted for the current number in the left array and all the numbers located after the current number  in the left array
# so we keep increadsing the inversion count as we move forward
# once we are done with the current left number (which means the current left number is greater than the current right number), we add the conversion count  for it

#Time complexity: O(nlogn). This is the same as conventional merge sort. You can google it if you want to understand why this complexity. Space complexity: O(n). This comes from the temp list that we initialized to temporarily store the sorted array segment.
class Solution(object):
    def countSmaller(self, nums):

        res = [0] * len(nums)  # final output
        enum = list(enumerate(nums))  # we initialize another list of tuple to have each tuple stores the index and value as (index, nums[index]). This list serves as the bridge to link the array element which is under the sorting process
        # we use a list of tuples instead on a list for sorting process, the reason is that when we are sorting we need to know elemens from which positions are moving

        self.mergeSort(enum, 0, len(nums) - 1, res)
        return res

    def mergeSort(self, enum, start, end, res):
        if start >= end: return

        mid = start + (end - start) // 2
        self.mergeSort(enum, start, mid, res)
        self.mergeSort(enum, mid + 1, end, res)
        self.merge(enum, start, mid, end, res)

    def merge(self, enum, start, mid, end, res):
        p, q = start, mid + 1
        inversion_count = 0  # we create a variable to count the how many numbers from the right half is smaller than the current number from the left half.
        temp = []

        while p <= mid and q <= end:
            if enum[p][1] <= enum[q][1]:
                temp.append(enum[p])# basically when we add a number to the temp, it means it has been finalized and we need to update its inversion count
                res[enum[p][0]] += inversion_count  # enum[p] has been finalized and we update its inversion count.
                p += 1
            else:
                temp.append(enum[q])
                inversion_count += 1  # when we find that nums[left_index] > nums[right_index], we add 1 to the inversion_count, but we dont add the current inversion_count to the final result yet. Because it is still possible that the next number(s) in the right half is still smaller than this current left number.
                q += 1

        while p <= mid:
            temp.append(enum[p])
            res[enum[p][0]] += inversion_count  # when we finish iterating the numbers in the right half but there are still numbers left in the left half, we know that the number in the remaining left half should be bigger than all numbers in the right half, thus we need to add the current inversion_count to the corresponding index of all remaining left numbers. To help you understand this better, you can also use end-mid which gives the length of the right half array instead of inversion_count in this step.
            p += 1

        while q <= end:# there is no smaller number in the right side, so we do not  need to update the inversion
            temp.append(enum[q])
            q += 1

        enum[start:end + 1] = temp


so=Solution()
inp=[5,2,6,1]
print(so.countSmaller(inp))

#2025