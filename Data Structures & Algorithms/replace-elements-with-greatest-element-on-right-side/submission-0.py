class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max = 0
            for r in range(i+1, len(arr)):
                if max < arr[r]:
                    max = arr[r]
            arr[i] = max
        arr[-1] = -1
        return arr