# array1 = [0,1,0,3,12]
# array2 = [1,7,0,0,8,0,10,12,0,4]
# array2 = [1,7,0,0,8,0,10,12,0,4]



sample = [10,0,0,0,0,2,0,3]


def search(arr):
    for idx, ele in enumerate(arr):
        if ele != 0:
            return idx

def sort(arr):
    for idx, ele in enumerate(arr):
        if ele == 0:
            next_non_zero = search(arr[idx:])
            if not next_non_zero:
                break
            arr[idx], arr[next_non_zero + idx] = arr[next_non_zero + idx], arr[idx]    

# sort(sample)
# print(sample)



# Computer, utercomp —— true

# tercompu
# ercompot
# rcompute
# Computer, uterocmp —— false
# computer

def prob2(string, str_to_search):
    possible_words = []
    for i in range(len(string)):
        possible_words.append(string[i:] + string[0:i])
        
    print(f"possible_words:{possible_words}")
    if str_to_search in possible_words:
        return True
    return False

print(prob2("computer", "utercomp"))

print(prob2("computer", "uterocmp"))

