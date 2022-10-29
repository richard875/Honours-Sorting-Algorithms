''' BIG O
Best case - O(n)
Medium case - O((n log(n)) ^ 2)
Worst case - O((n log(n)) ^ 2)
'''

def shell_sort(sort_arr):
    array = sort_arr
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
    
    return array

if __name__ == "__main__":
    print(shell_sort([4, 2, 3, 1]))