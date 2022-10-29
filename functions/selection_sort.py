''' BIG O
Best case - O(n^2)
Medium case - O(n^2)
Worst case - O(n^2)
'''

def selection_sort(sort_arr):
    arr = sort_arr
    i = 0
    n = len(arr)
    while(i<n):
        j=i+1
        min = i
        while(j<n):
            if(arr[j] < arr[min]):
                min = j 
            j+=1

        arr[i], arr[min] = arr[min], arr[i]
        i+=1
    
    return arr

if __name__ == "__main__":
    print(selection_sort([4, 2, 3, 1]))