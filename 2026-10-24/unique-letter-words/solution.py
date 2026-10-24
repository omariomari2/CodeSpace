def max_unique_length(words: list[str]) -> int:
    """words: list of lowercase words. Return the max length of a concatenation of some subset of words in which no letter repeats."""
    return 0


# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    ((['un', 'iq', 'ue'],), 4),
    ((['cha', 'r', 'act', 'ers'],), 6),
    ((['aa', 'bc'],), 2),
    (([],), 0),
    ((['abcdefghijklmnopqrstuvwxyz'],), 26),
    ((['a', 'b', 'c'],), 3),
    ((['aa', 'bb'],), 0),
    ((['ab', 'ba', 'cd'],), 4),
    ((['abc', 'def', 'abd', 'gh'],), 8),
    ((['a', 'abc', 'd', 'de', 'def'],), 6),
    ((['xyz', 'x', 'y', 'z', 'w'],), 4),
    ((['abcdefghijklm', 'nopqrstuvwxyz', 'a'],), 26),
    ((['ab', 'cd', 'ef', 'gh', 'ij', 'aj'],), 10),
    ((['zz', 'qq', 'x'],), 1),
    ((['yy', 'bkhwmpbiisbldzknpm'],), 0),
]


def _run_tests():
    import copy, random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = max_unique_length(*copy.deepcopy(inp))
        except Exception as e:
            got = f"error: {type(e).__name__}: {e}"
        if got == expected:
            passed += 1
        else:
            print(f"case {i} failed: input={str(inp)[:80]} expected={expected} got={got}")
    print(f"{passed}/{len(TEST_CASES)} passed")

    # speed check: 16 words should finish well under 2 seconds
    random.seed(7)
    letters = "abcdefghijklmnopqrstuvwxyz"
    big = (["".join(random.sample(letters, random.randint(1, 2))) for _ in range(16)],)
    start = time.time()
    try:
        max_unique_length(*big)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (16 words): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
