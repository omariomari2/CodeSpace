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

# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    ([2, 36, 45, 306, 415], 460),
    ([7], -1),
    ([1, 2, 3], -1),
    ([11, 11], 22),
    ([5, 5, 5], 10),
    ([0, 0], 0),
    ([10, 100, 1000], 1100),
    ([121, 101, 1], 222),
    ([1, 1], 2),
    ([909, 99, 9, 999], 1908),
    ([12, 21, 102, 201], 222),
    ([1000000000, 1000000000, 100000000], 2000000000),
    ([5, 55], 60),
    ([3, 303, 33], 336),
    ([1, 11, 101], 112),
]


def _run_tests():
    import random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = max_pair_sum(list(inp))
        except Exception as e:
            got = f"error: {type(e).__name__}: {e}"
        if got == expected:
            passed += 1
        else:
            print(f"case {i} failed: input={str(inp)[:80]} expected={expected} got={got}")
    print(f"{passed}/{len(TEST_CASES)} passed")

    # speed check: n = 100,000 should finish well under 2 seconds
    random.seed(7)
    big = [random.randint(1, 10**9) for _ in range(100_000)]
    start = time.time()
    try:
        max_pair_sum(big)
    except Exception as e:
        print(f\"speed check crashed: {type(e).__name__}: {e}\")
        return
    took = time.time() - start
    print(f"speed check (n=100,000): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
