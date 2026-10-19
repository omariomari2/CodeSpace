def find_largest_number(nums: list[int]) -> int:
    """Pick three digits in their original order and return the biggest 3-digit number they make."""
    return 0


# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    ([7, 4, 3, 8, 2], 782),
    ([1, 2, 3], 123),
    ([0, 0, 0], 0),
    ([3, 2, 1], 321),
    ([9, 9, 9, 9], 999),
    ([0, 0, 5], 5),
    ([3, 0, 0, 0], 300),
    ([1, 9, 1, 9, 1], 991),
    ([5, 1, 9, 2, 8], 928),
    ([2, 9, 8, 7, 9], 989),
    ([9, 0, 0, 1], 901),
    ([1, 0, 0, 9, 9], 199),
    ([4, 4, 1, 4], 444),
    ([2, 7, 6, 1, 3, 3, 8, 3, 0, 6, 7, 0, 4, 0, 4, 5, 6, 2, 5, 5, 2], 876),
    ([2, 2, 1, 2, 5, 1, 5, 0], 550),
    ([1, 5, 2, 5, 7, 4, 2, 3, 5, 6, 0, 6, 2, 6, 4, 6, 4, 7, 7], 777),
    ([6, 4, 2, 1, 1, 6, 2, 2, 7, 7, 0, 6, 7, 7, 2, 7], 777),
]


def _run_tests():
    import random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = find_largest_number(list(inp))
        except Exception as e:
            got = f"error: {type(e).__name__}: {e}"
        if got == expected:
            passed += 1
        else:
            print(f"case {i} failed: input={str(inp)[:80]} expected={expected} got={got}")
    print(f"{passed}/{len(TEST_CASES)} passed")

    # speed check: n = 100,000 should finish well under 2 seconds
    random.seed(7)
    big = [random.randint(0, 9) for _ in range(100_000)]
    start = time.time()
    try:
        find_largest_number(big)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (n=100,000): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
