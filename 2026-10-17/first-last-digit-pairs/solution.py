"""
PseudoCode
Bruteforce
first pass through all and rewrite into dict 
dict will have entries with two/more digits, and if it does then the key will be first last digits with value being a list of actual entries 

eg: nums = [2, 36, 45, 306, 415]
dict = {2: [2], 45: [45, 415], 36: [36, 306]}

initialize ans variable to -1
pass through the dict, for each element in the dict if the value has two or more len, we add the two largest elements 
ans = max(ans, (value[n - 1] + value[n - 2])) where n = len(value)
return ans 

time complexity = O(N) for the nums pass + O(N) for the dict pass + O(NlogN) for sorting the dict values
"""

def max_pair_sum(nums: list[int]) -> int:
    matches = dict()
    for num in nums:
        n = str(num)
        if len(n) > 1:
            k = n[0] + n[-1] 
        else:
            k = n
        matches[k] = matches.get(k, []) + [num]

    ans = -1
    for entry in matches:
        if len(matches[entry]) < 2:
            continue 

        vals = matches[entry].sort()
        n = len(vals) - 1
        largest_sum = vals[n] + vals[n - 1]
        ans = max(ans, largest_sum)

    return ans