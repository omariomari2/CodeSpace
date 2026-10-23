def max_escape_score(elements: list[int]) -> int:
    """elements: list of positive integers. Return the maximum total score reachable under the game rules."""
    return 0


# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    (([5, 6, 6, 4, 11],), 27),
    (([3, 4, 2],), 6),
    (([1],), 1),
    (([7, 7, 7],), 21),
    (([1, 2],), 2),
    (([2, 2, 3, 3, 3, 4],), 9),
    (([1, 2, 3, 4, 5],), 9),
    (([10, 20, 30],), 60),
    (([1, 1, 1, 2, 4, 5, 5, 5, 6],), 18),
    (([100000, 99999, 1],), 100001),
    (([3, 1, 2, 3, 1, 2],), 8),
    (([8, 10, 9, 9, 10],), 28),
    (([4, 4, 4, 5, 6, 6],), 24),
    (([1, 3, 5, 7, 2],), 16),
    (([50, 51, 52, 53, 54, 55],), 159),
]


def _run_tests():
    import copy, random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = max_escape_score(*copy.deepcopy(inp))
        except Exception as e:
            got = f"error: {type(e).__name__}: {e}"
        if got == expected:
            passed += 1
        else:
            print(f"case {i} failed: input={str(inp)[:80]} expected={expected} got={got}")
    print(f"{passed}/{len(TEST_CASES)} passed")

    # speed check: n=100,000 should finish well under 2 seconds
    random.seed(7)
    n = 100_000
    big = ([random.randint(1, 100_000) for _ in range(n)],)
    start = time.time()
    try:
        max_escape_score(*big)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (n=100,000): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
