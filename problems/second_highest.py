## Code to find second highest
def second_highest(arr):
	high = arr[0]
	s_high = arr[0]
	for ele in arr[1:]:
		if ele > high:
			s_high = high
			high = ele
	return high, s_high

h, sh = second_highest(sample)
print(h, sh)
