def equalsum(arr):
    n = len(arr)
    # Left and Right pointer
    i = 0
    j = n-1
    found = False

    # Left Sum & Right Sum
    ls = arr[0]
    rs = arr[n-1]

    while i <= j:
        if ls < rs:
            i += 1
            ls += arr[i]
        elif rs < ls:
            j -= 1
            rs += arr[j]

        if ls == rs:
            if j - i == 2:
                found = True
                break
            else:
                i += 1
                ls += arr[i]
                j -= 1
                ls -= arr[j]

    if found:
        print(arr[i+1])
    else:
        print("Nothing found")

equalsum([1,4,2,5])
