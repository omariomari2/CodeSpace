import heapq

def min_cost_to_connect(ropes: list[int]) -> int:
    if len(ropes) < 2:
        return 0
    # REVIEW: Good call on a min-heap, O(n log n) time is right for n=1e5.
    # REVIEW: heapify mutates the caller's list. Fine here, but in an OA would you copy first? When does it matter?
    heapq.heapify(ropes)
    # REVIEW: `power` is a vague name for a running cost. Name it after what it is.
    power = 0

    # REVIEW: Given the len<2 guard above, can the loop ever pop a single rope alone? Two of the `if ropes:` checks look dead.
    # REVIEW: What loop condition would make each iteration exactly "pop two, push one"?
    while ropes:
        # REVIEW: Delete leftover debug prints before submitting.
        # print('yes')
        merged = heapq.heappop(ropes)
        if ropes:
            merged += heapq.heappop(ropes)

        if ropes:
            heapq.heappush(ropes, merged)
        power += merged 

    return power 




# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    ([4, 3, 2, 6], 29),
    ([4, 2, 7, 6, 9], 62),
    ([10], 0),
    ([5, 5], 10),
    ([1, 1, 1, 1], 8),
    ([1, 2, 3, 4, 5], 33),
    ([7, 7, 7, 7, 7, 7, 7, 7], 168),
    ([10000, 10000, 10000], 50000),
    ([1, 10000], 10001),
    ([7980, 8193, 2051, 8450, 6663, 3567, 5751, 1675, 2005, 3611, 7946, 6933, 5393, 1733, 204, 8451, 6171, 2957, 5809, 308, 3064, 7547, 2219, 7676, 4631, 9061, 8124, 7956, 7821, 2195, 7999, 2497, 5277, 9402, 4653, 7718, 2358, 3331, 3969, 1036, 3297, 7854], 1119138),
    ([6069, 5089, 9384, 4175, 5899, 7556, 1099, 2384, 8627, 1871, 3698, 169, 8251, 2569, 2710, 1922, 4598, 8422, 6675, 4694, 2669, 2334, 6288, 3021, 8722, 4841, 3807, 6136, 7149, 8815, 7409, 3295, 9499, 5841, 6632, 1722, 3877, 1913, 5343, 7027, 9153], 1098018),
    ([1008, 8025, 3001, 3808, 3518, 7807, 1313, 7830, 2779, 291, 6023, 74, 5723, 4396, 1969, 8773, 2861, 146, 5584, 6401, 1920, 5861, 7149, 5913, 4052, 2037, 8472, 8342, 7039, 1497, 7294, 9144, 2025, 666, 2947, 7850, 9007, 5430, 9233, 2936, 2883, 1893, 6023, 2818, 6522, 2010], 1114693),
    ([7284, 9419, 622, 6178, 526, 8135, 4055, 4741, 1069, 9038, 6532, 5652, 4893, 9167, 9079, 2413, 2929, 5941, 5599, 9066, 8129, 4592, 4967, 5588, 144, 5082, 5968, 2985, 3472, 2927, 9809, 3755, 6065, 8630, 6195, 2402, 1163, 9292], 1029767),
    ([8556, 3664, 2751, 8112, 1759, 5459, 6962, 8505, 766, 1676, 2463, 2177, 4815, 2589, 5935, 2198, 2594, 9448, 6682, 1938, 988, 4297, 1060, 4031, 8180, 7519, 4465, 6694, 7589, 5927, 4041, 6876, 1790, 7631, 9989, 3929, 1738, 4762, 797, 2351, 5154, 4817], 1003977),
    ([2116, 3743, 1284, 4518, 3268, 4046, 3190, 7963, 1930, 9988, 9811, 9154, 4614, 5086, 7085, 4480, 9074, 1064, 5150, 1735, 9341, 671, 2859], 481793),
    ([5449, 5341, 8942], 30522),
    ([8075, 2438, 4267, 276, 8290, 4597, 4728, 1430, 3836, 3715, 3046, 4919, 8425, 7171, 8504, 7248], 311157),
]


def _run_tests():
    import random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = min_cost_to_connect(list(inp))
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
        min_cost_to_connect(big)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (n=100,000): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
