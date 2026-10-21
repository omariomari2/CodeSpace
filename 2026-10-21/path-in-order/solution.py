def check_path_presence(n: int, a: list[int], b: list[int]) -> int:
    """Given n vertices and edges (a[k], b[k]), return 1 if the path 1, 2, ..., n exists using direct edges, else 0."""
    return 0


# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    ((4, [1, 2, 4, 4, 3], [2, 3, 1, 3, 1]), 1),
    ((2, [1], [2]), 1),
    ((2, [2], [1]), 1),
    ((3, [1, 1], [2, 3]), 0),
    ((3, [2, 3], [1, 2]), 1),
    ((5, [1, 2, 3], [2, 3, 4]), 0),
    ((5, [5, 3, 2, 1], [4, 4, 3, 2]), 1),
    ((4, [1, 2, 3, 1], [3, 4, 4, 2]), 0),
    ((3, [1, 1, 2], [2, 2, 1]), 0),
    ((4, [4, 3, 2], [3, 2, 1]), 1),
    ((6, [1, 2, 3, 4, 5, 1], [2, 3, 4, 5, 6, 6]), 1),
    ((6, [1, 2, 4, 5, 1], [2, 3, 5, 6, 6]), 0),
    ((2, [1, 1], [1, 2]), 1),
    ((3, [3, 3], [3, 2]), 0),
    ((7, [2, 1, 4, 3, 6, 5], [3, 2, 5, 4, 7, 6]), 1),
]


def _run_tests():
    import copy, random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = check_path_presence(*copy.deepcopy(inp))
        except Exception as e:
            got = f"error: {type(e).__name__}: {e}"
        if got == expected:
            passed += 1
        else:
            print(f"case {i} failed: input={str(inp)[:80]} expected={expected} got={got}")
    print(f"{passed}/{len(TEST_CASES)} passed")

    # speed check: n = 100,000 should finish well under 2 seconds
    random.seed(7)
    n = 100_000
    edges = [(i, i + 1) for i in range(1, n)] + [(random.randint(1, n), random.randint(1, n)) for _ in range(1)]
    random.shuffle(edges)
    big = (n, [x for x, _ in edges], [y for _, y in edges])
    start = time.time()
    try:
        check_path_presence(*big)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (n=100,000): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
