class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest = 0
        i = 1
        while i < len(arr) - 1:
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                l = i - 1
                r = i + 1

                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1

                while r < len(arr) - 1 and arr[r] > arr[r + 1]:
                    r += 1

                longest = max(longest, r - l + 1)
                i = r
            else:
                i += 1

        return longest
        

# Time: O(n)
# Space: O(1)