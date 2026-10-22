def min_cut_cost(left_child: list[int], right_child: list[int],
                 left_cost: list[int], right_cost: list[int]) -> int:
    """left_child[i] / right_child[i]: children of node i, or -1. left_cost[i] / right_cost[i]: cost of those edges (0 if absent). Node 0 is the root. Return the minimum total cost of edges to cut so the root reaches no original leaf."""
    return 0


# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    (([1, 3, 5, -1, -1, -1, -1], [2, 4, 6, -1, -1, -1, -1], [4, 1, 6, 0, 0, 0, 0], [7, 5, 2, 0, 0, 0, 0]), 11),
    (([1, 2, 3, -1], [-1, -1, -1, -1], [8, 3, 5, 0], [0, 0, 0, 0]), 3),
    (([-1], [-1], [0], [0]), 0),
    (([], [], [], []), 0),
    (([1, -1], [-1, -1], [9, 0], [0, 0]), 9),
    (([1, -1, -1], [2, -1, -1], [0, 0, 0], [5, 0, 0]), 5),
    (([-1, -1], [1, -1], [0, 0], [4, 0]), 4),
    (([1, -1, 3, -1], [2, -1, -1, -1], [10, 0, 1, 0], [2, 0, 0, 0]), 11),
    (([1, 3, -1, -1, -1], [2, 4, -1, -1, -1], [100, 1, 0, 0, 0], [3, 1, 0, 0, 0]), 5),
    (([2, -1, 3, -1], [1, -1, -1, -1], [6, 0, 2, 0], [5, 0, 0, 0]), 7),
    (([1, 2, -1, -1], [3, -1, -1, -1], [7, 7, 0, 0], [1, 0, 0, 0]), 8),
    (([1, 3, 5, -1, -1, -1], [2, 4, -1, -1, -1, -1], [9, 2, 3, 0, 0, 0], [9, 2, 0, 0, 0, 0]), 7),
    (([1, -1, -1], [2, -1, -1], [0, 0, 0], [0, 0, 0]), 0),
    (([3, -1, 1, -1, -1], [2, -1, 4, -1, -1], [5, 0, 4, 0, 0], [1, 0, 4, 0, 0]), 6),
    (([1, 2, 3, 4, -1], [-1, -1, -1, -1, -1], [2147483647, 6, 9, 4, 0], [0, 0, 0, 0, 0]), 4),
]


def _run_tests():
    import copy, random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = min_cut_cost(*copy.deepcopy(inp))
        except Exception as e:
            got = f"error: {type(e).__name__}: {e}"
        if got == expected:
            passed += 1
        else:
            print(f"case {i} failed: input={str(inp)[:80]} expected={expected} got={got}")
    print(f"{passed}/{len(TEST_CASES)} passed")

    # speed check: n=100,000, one long path should finish well under 2 seconds
    random.seed(7)
    n = 100_000
    left, right = [-1] * n, [-1] * n
    lcost, rcost = [0] * n, [0] * n
    for v in range(1, n):  # one long path down from the root
        if random.random() < 0.5:
            left[v - 1], lcost[v - 1] = v, random.randint(0, 10_000)
        else:
            right[v - 1], rcost[v - 1] = v, random.randint(0, 10_000)
    big = (left, right, lcost, rcost)
    start = time.time()
    try:
        min_cut_cost(*big)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (n=100,000, one long path): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
