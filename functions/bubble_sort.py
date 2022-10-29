''' BIG O
Best case - O(n)
Medium case - O(n^2)
Worst case - O(n^2)
'''


def bubble_sort(arr):
    i = 0
    sort_list = arr
    n = len(sort_list)
    while (i < n - 1):
        j = n - 1
        while (j > i):
            if (sort_list[j] < sort_list[j - 1]):
                sort_list[j - 1], sort_list[j] = sort_list[j], sort_list[j - 1]
            j -= 1
        i += 1

    return sort_list

if __name__ == "__main__":
    print(bubble_sort([4, 2, 3, 1]))