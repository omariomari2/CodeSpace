def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Given a list of [start, end] intervals, return the merged list of [start, end] intervals sorted by start."""
    pass


# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    (([[1, 3], [2, 6], [8, 10], [15, 18]],), [[1, 6], [8, 10], [15, 18]]),
    (([[1, 4], [4, 5]],), [[1, 5]]),
    (([[8, 10], [1, 4], [2, 3], [15, 18], [6, 9], [3, 7], [17, 20], [12, 12]],), [[1, 10], [12, 12], [15, 20]]),
    (([[5, 5]],), [[5, 5]]),
    (([[0, 0], [0, 0]],), [[0, 0]]),
    (([[1, 2], [3, 4]],), [[1, 2], [3, 4]]),
    (([[1, 10], [2, 3], [4, 5]],), [[1, 10]]),
    (([[0, 10000]],), [[0, 10000]]),
    (([[3, 4], [1, 2], [2, 3]],), [[1, 4]]),
    (([[1, 1], [2, 2], [1, 2]],), [[1, 2]]),
    (([[6, 8], [1, 9], [2, 4], [4, 7]],), [[1, 9]]),
    (([[10, 12], [0, 1], [5, 6], [1, 5]],), [[0, 6], [10, 12]]),
    (([[7, 7], [7, 7], [8, 8]],), [[7, 7], [8, 8]]),
    (([[0, 3], [5, 9], [3, 5]],), [[0, 9]]),
    (([[2, 3], [4, 6], [1, 1], [10, 11], [6, 10]],), [[1, 1], [2, 3], [4, 11]]),
]


def _run_tests():
    import copy, random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = merge(*copy.deepcopy(inp))
        except Exception as e:
            got = f"error: {type(e).__name__}: {e}"
        if got == expected:
            passed += 1
        else:
            print(f"case {i} failed: input={str(inp)[:80]} expected={expected} got={got}")
    print(f"{passed}/{len(TEST_CASES)} passed")

    # speed check: n = 100,000 should finish well under 2 seconds
    random.seed(7)
    big = []
    for _ in range(100_000):
        s = random.randint(0, 10**4)
        big.append([s, min(10**4, s + random.randint(0, 50))])
    big = (big,)
    start = time.time()
    try:
        merge(*big)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (n=100,000): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
