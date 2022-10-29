''' BIG O
Best case - O(n)
Medium case - O(n^2)
Worst case - O(n^2)
'''


def insertion_sort(arr):
    p = 1
    sort_list = arr
    n = len(sort_list)
    while (p < n):
        temp = sort_list[p]
        j = p
        while (j > 0 and temp < sort_list[j - 1]):
            sort_list[j] = sort_list[j - 1]
            j -= 1
        sort_list[j] = temp
        p += 1

    return sort_list

if __name__ == "__main__":
    print(insertion_sort([4, 2, 3, 1]))