def comb_sort(sort_arr):
    num = sort_arr
    gap = len(num)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(num) - gap):
            j = i+gap
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
                swaps = True
                
    return num
 
if __name__ == "__main__":
    print(comb_sort([4, 2, 3, 1]))