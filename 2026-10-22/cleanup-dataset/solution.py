def cleanup_dataset(dataset: str, x: int, y: int) -> int:
    """dataset: even-length string of lowercase letters. x: cost to remove two equal characters. y: cost to remove two different characters. Return the minimum total cost to empty the string."""
    return 0


# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    (('aaabca', 3, 2), 7),
    (('ouio', 2, 4), 6),
    (('ab', 5, 1), 1),
    (('aa', 5, 1), 5),
    (('aaaa', 1, 10), 2),
    (('aaaaaa', 10, 1), 30),
    (('aaaabb', 10, 1), 12),
    (('aaaaab', 10, 1), 21),
    (('abcdef', 1, 7), 21),
    (('aabbcc', 3, 3), 9),
    (('abab', 2, 9), 4),
    (('zzzzzzyx', 4, 2), 12),
    (('abcabc', 1, 2), 3),
    (('qqqqqqqqqqqqqqqqqqqp', 7, 3), 66),
    (('mississippim', 6, 5), 30),
]


def _run_tests():
    import copy, random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = cleanup_dataset(*copy.deepcopy(inp))
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
    big = ("".join(random.choice("ab") if random.random() < 0.5 else "a" for _ in range(n)), 9, 4)
    start = time.time()
    try:
        cleanup_dataset(*big)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (n=100,000): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
