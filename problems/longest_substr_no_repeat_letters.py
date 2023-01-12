# A given string has letters, and
# this code find a longest length substring
# without repeat of letters

sample_str = "abcdabeudgzeui"
def longest_substr(string):
    l_s = ""
    temp = ""
    for ele in string:
        if ele in temp:
            print(f"Letter repeated {ele} and substr {temp}")
            if len(temp) > len(l_s):
                l_s = temp
            else:
                temp = ""
        else:
            temp += ele
    return l_s
print(longest_substr(sample_str))
