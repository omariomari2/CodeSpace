def max_substring_frequency(text: str, max_distinct: int, min_length: int, max_length: int) -> int:
    """text: lowercase string. max_distinct, min_length, max_length: ints. Return the highest occurrence count (overlaps allowed) of any substring with length in [min_length, max_length] and at most max_distinct different letters, or 0 if none."""
    return 0


# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    (('aababcaab', 2, 3, 4), 2),
    (('aaaa', 1, 3, 3), 2),
    (('abcde', 2, 3, 3), 0),
    (('a', 1, 1, 1), 1),
    (('ab', 1, 2, 2), 0),
    (('abab', 2, 2, 2), 2),
    (('abcabcabc', 3, 3, 9), 3),
    (('zzzzzz', 1, 1, 6), 6),
    (('abcdabcd', 2, 2, 4), 2),
    (('aabbaabb', 1, 2, 3), 2),
    (('xyzxyzx', 26, 1, 2), 3),
    (('bbbbb', 3, 5, 5), 1),
    (('abacabadabacaba', 2, 3, 3), 4),
    (('qwerty', 6, 6, 6), 1),
    (('mississippi', 2, 2, 4), 2),
]


def _run_tests():
    import copy, random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = max_substring_frequency(*copy.deepcopy(inp))
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
    big = ("".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n)), 26, 1, 26)
    start = time.time()
    try:
        max_substring_frequency(*big)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (n=100,000): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
