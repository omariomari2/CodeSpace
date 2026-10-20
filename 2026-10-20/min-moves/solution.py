def min_moves(a: list[int]) -> int:
    """Return the fewest range +1 moves needed to build `a` from an all-zero array."""
    return 0


# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    ([2, 1, 3], 4),
    ([0], 0),
    ([5], 5),
    ([0, 0, 0], 0),
    ([1, 1, 1, 1], 1),
    ([1, 2, 3, 4], 4),
    ([4, 3, 2, 1], 4),
    ([3, 0, 3], 6),
    ([1, 0, 1, 0, 1], 3),
    ([0, 2, 0, 2, 0], 4),
    ([10000], 10000),
    ([5, 5, 0, 5, 5], 10),
    ([1, 3, 2, 4, 1, 5], 9),
    ([2, 2, 1, 2, 2], 3),
    ([6, 1, 4, 5, 0, 0], 10),
    ([2, 3, 0, 2, 5, 3, 0, 0, 1, 4, 2], 12),
]


def _run_tests():
    import random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = min_moves(list(inp))
        except Exception as e:
            got = f"error: {type(e).__name__}: {e}"
        if got == expected:
            passed += 1
        else:
            print(f"case {i} failed: input={str(inp)[:80]} expected={expected} got={got}")
    print(f"{passed}/{len(TEST_CASES)} passed")

    # speed check: n = 100,000 should finish well under 2 seconds
    random.seed(7)
    big = [random.randint(0, 10**4) for _ in range(100_000)]
    start = time.time()
    try:
        min_moves(big)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (n=100,000): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
