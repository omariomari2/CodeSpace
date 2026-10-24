# Substring Frequency

**Company:** Microsoft

## Problem

You're given a lowercase string `text` and three integers `max_distinct`, `min_length`, and `max_length`.

A substring counts as valid if its length is between `min_length` and `max_length` (inclusive) and it uses at most `max_distinct` different letters.

Return the highest number of times any single valid substring shows up in `text`. Occurrences are allowed to overlap. If there's no valid substring at all, return 0.

## Function

```python
def max_substring_frequency(text: str, max_distinct: int, min_length: int, max_length: int) -> int:
```

## Constraints

- `1 <= len(text) <= 10^5`
- `text` contains only lowercase English letters
- `1 <= max_distinct <= 26`
- `1 <= min_length <= max_length <= min(26, len(text))`

## Examples

**Example 1**

```
text = "aababcaab", max_distinct = 2, min_length = 3, max_length = 4
output: 2
```

`"aab"` shows up twice and only uses `a` and `b`.

**Example 2**

```
text = "aaaa", max_distinct = 1, min_length = 3, max_length = 3
output: 2
```

Both length-3 windows are `"aaa"`, and overlapping counts.

**Example 3**

```
text = "abcde", max_distinct = 2, min_length = 3, max_length = 3
output: 0
```

Every length-3 substring has three different letters, so nothing is valid.

## More test cases

| text | max_distinct | min_length | max_length | output |
|---|---|---|---|---|
| `"a"` | `1` | `1` | `1` | `1` |
| `"ab"` | `1` | `2` | `2` | `0` |
| `"abab"` | `2` | `2` | `2` | `2` |
| `"abcabcabc"` | `3` | `3` | `9` | `3` |
| `"zzzzzz"` | `1` | `1` | `6` | `6` |
| `"abcdabcd"` | `2` | `2` | `4` | `2` |
| `"aabbaabb"` | `1` | `2` | `3` | `2` |
| `"xyzxyzx"` | `26` | `1` | `2` | `3` |
| `"bbbbb"` | `3` | `5` | `5` | `1` |
| `"abacabadabacaba"` | `2` | `3` | `3` | `4` |
| `"qwerty"` | `6` | `6` | `6` | `1` |
| `"mississippi"` | `2` | `2` | `4` | `2` |
