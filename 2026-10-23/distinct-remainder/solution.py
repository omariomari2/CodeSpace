def min_deletion_for_distinct(text: str) -> int:
    """text: string of printable ASCII characters. Return the minimum length of one contiguous substring to delete so every remaining character is unique."""
    return 0


# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    (('abca',), 1),
    (('abc',), 0),
    (('',), 0),
    (('a',), 0),
    (('aa',), 1),
    (('aaa',), 2),
    (('abab',), 2),
    (('abcabc',), 3),
    (('abcdba',), 2),
    (('aAbBa',), 1),
    (('xyzzyx',), 3),
    (('hello world',), 3),
    (('abcdefgha',), 1),
    (('zabcz',), 1),
    (('mississippi',), 8),
]


def _run_tests():
    import copy, random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = min_deletion_for_distinct(*copy.deepcopy(inp))
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
    chars = [chr(c) for c in range(32, 127)]
    random.shuffle(chars)
    head, tail = "".join(chars[:47]), "".join(chars[47:])
    big = (head + "".join(random.choice(chars) for _ in range(n - 95)) + tail,)
    start = time.time()
    try:
        min_deletion_for_distinct(*big)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (n=100,000): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
