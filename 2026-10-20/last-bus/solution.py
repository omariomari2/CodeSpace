def bustling_town_buses(time_table: list[str], moment: str) -> int:
    def normalize(time):
        return int(time[:2] + time[3:])

    def hh_to_mm(num):
        mm, hh  = num % 100, num // 100
        return hh * 60  + mm

    moment = normalize(moment)
    ans = -1
    for t in time_table:
        time = normalize(t)
        if time < moment:
            ans = max(time, ans)

    if ans == -1:
        return ans
    return hh_to_mm(moment) - hh_to_mm(ans)     

# ---- test cases (run: python solution.py) ----
TEST_CASES = [
    ((["12:30", "14:00", "19:55"], "14:30"), 30),
    ((["00:00", "14:00", "19:55"], "00:00"), -1),
    ((["12:30", "14:00", "19:55"], "14:00"), 90),
    ((["08:15"], "08:16"), 1),
    ((["08:15"], "08:15"), -1),
    ((["08:15"], "07:00"), -1),
    ((["23:59"], "23:59"), -1),
    ((["00:00"], "23:59"), 1439),
    ((["10:00", "10:00", "10:00"], "10:01"), 1),
    ((["19:55", "12:30", "14:00"], "20:00"), 5),
    ((["06:00", "09:45", "13:10", "17:20"], "23:59"), 399),
    ((["06:00", "09:45", "13:10", "17:20"], "09:44"), 224),
    ((["00:01", "00:02"], "00:02"), 1),
    ((["13:05", "01:50", "22:40", "07:07"], "13:05"), 358),
    ((["22:14", "10:42", "07:15", "16:25", "02:07", "22:12"], "16:54"), 29),
    ((["05:03", "01:05", "11:00"], "17:21"), 381),
]


def _run_tests():
    import random, time
    passed = 0
    for i, (inp, expected) in enumerate(TEST_CASES, 1):
        try:
            got = bustling_town_buses(list(inp[0]), inp[1])
        except Exception as e:
            got = f"error: {type(e).__name__}: {e}"
        if got == expected:
            passed += 1
        else:
            print(f"case {i} failed: input={str(inp)[:80]} expected={expected} got={got}")
    print(f"{passed}/{len(TEST_CASES)} passed")

    # speed check: n = 100,000 should finish well under 2 seconds
    random.seed(7)
    big_table = [f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}" for _ in range(100_000)]
    big_moment = "12:00"
    start = time.time()
    try:
        bustling_town_buses(big_table, big_moment)
    except Exception as e:
        print(f"speed check crashed: {type(e).__name__}: {e}")
        return
    took = time.time() - start
    print(f"speed check (n=100,000): {took:.2f}s {'ok' if took < 2 else 'TOO SLOW'}")


if __name__ == "__main__":
    _run_tests()
