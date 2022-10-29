''' BIG O
Best case - O(n log(n))
Medium case - O(n log(n))
Worst case - O(n log(n))
'''


def merge_sort(arr):
    obj = arr

    if len(obj) > 1:
        mid = int(len(obj) / 2)
        left = obj[:mid]
        right = obj[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                obj[k] = left[i]
                i += 1
            else:
                obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            obj[k] = right[j]
            j += 1
            k += 1

    return obj

if __name__ == "__main__":
    print(merge_sort([4, 2, 3, 1]))