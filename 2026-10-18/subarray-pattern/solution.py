def count_matching_subarrays(numbers: list[int], pattern: list[int]) -> int:
    count = 0
    n = len(numbers)
    m = len(pattern)
    count = 0

    def is_match(candidate, l1):
        comp = 1
        for i in range(len(l1)):
            p = pattern[i]
            if l1[i] > candidate:
                comp = 1
            elif l1[i] == candidate:
                comp = 0
            else:
                comp = -1

            if p != comp:
                return False
            
            candidate = l1[i]

        return True

    for i in range(n - m):
        if is_match(numbers[i], numbers[i + 1: i + m + 1]):
            count += 1

    return count


    return 0


TEST_CASES = [
    (([4, 1, 3, 4, 4, 5, 5, 1], [1, 0, -1]), 1),
    (([1, 2, 3, 4, 5, 6], [1, 1]), 4),
    (([1, 4, 4, 1, 3, 5, 5, 3], [1, 0, -1]), 2),
    (([5, 5], [0]), 1),
    (([5, 6], [-1]), 0),
    (([3, 2, 1], [-1, -1]), 1),
    (([7, 7, 7, 7, 7], [0, 0]), 3),
    (([1, 3, 2, 4, 3, 5], [1, -1]), 2),
    (([1, 3, 2, 4, 3, 5], [1, -1, 1, -1, 1]), 1),
    (([2, 1], [1]), 0),
    (([10, 20, 20, 10, 20, 20, 10], [1, 0, -1]), 2),
    (([1, 2, 1, 2, 1, 2, 1], [1, -1, 1]), 2),
    (([1000000000, 1, 1000000000], [-1, 1]), 1),
    (([2, 3, 5, 3, 4, 2, 1, 5, 3, 5, 1, 1, 4, 1, 1, 4, 2, 2, 3, 4, 5, 1, 2, 4, 2, 5, 3, 5, 1, 4, 5, 3, 1, 2, 5, 2, 2, 3, 1, 4], [0, 0]), 0),
    (([4, 4, 3, 4, 2, 3, 2, 3, 4, 5, 5, 1, 4, 3, 4, 5, 4, 3, 5, 5, 3, 2, 2, 5, 3, 3, 4, 5, 2, 3, 1], [-1, 0]), 2),
    (([5, 2, 4, 1, 4, 5, 4, 5, 5, 3, 3, 1, 5, 2, 2, 1, 4], [1, 1, 0]), 0),
    (([2, 4, 1, 2, 1, 1, 3, 2, 1, 2, 2, 1, 3, 3, 2, 4, 1], [-1, -1]), 1),
]


def _run_tests():
    import random, time
    passed = 0
    for i, ((numbers, pattern), expected) in enumerate(TEST_CASES, 1):
        try:
            got = count_matching_subarrays(list(numbers), list(pattern))
        except Exception as e:
            got = f"error: {type(e).__name__}: {e}"
        if got == expected:
            passed += 1
        else:
            print(f"case {i} failed: numbers={str(numbers)[:60]} pattern={pattern} expected={expected} got={got}")
    print(f"{passed}/{len(TEST_CASES)} passed")

    # speed check: n = 100,000 should finish well under 2 seconds
    random.seed(7)
    big = [random.randint(1, 10**9) for _ in range(100_000)]
    big_pattern = [1, -1, 1]
    start = time.time()
    try:
        count_matching_subarrays(big, big_pattern)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (n=100,000): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")

if __name__ == "__main__":
    _run_tests()
