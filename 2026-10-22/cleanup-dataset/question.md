# Cleanup Dataset

**Company:** Amazon

## Problem

A team is cleaning up a dataset stored as a string `dataset` of lowercase English letters. The length of the string is always even.

You clean it by repeatedly picking any two characters (from any positions) and removing both. Each removal has a cost:

- `x` if the two removed characters are the same letter
- `y` if they're different letters

Keep going until the string is empty. Return the minimum total cost to remove every character.

## Function

```python
def cleanup_dataset(dataset: str, x: int, y: int) -> int:
```

## Constraints

- `2 <= len(dataset) <= 10^5`
- `len(dataset)` is even
- `dataset` contains only lowercase English letters
- `1 <= x, y <= 10^4`

## Examples

**Example 1**

```
dataset = "aaabca", x = 3, y = 2
output: 7
```

Remove two `a`s for 3, leaving `"abca"`. Remove `a` and `c` for 2, leaving `"ba"`. Remove those for 2. Total 3 + 2 + 2 = 7.

**Example 2**

```
dataset = "ouio", x = 2, y = 4
output: 6
```

Remove both `o`s for 2, then `u` and `i` for 4. Total 6.

## More test cases

| dataset | x | y | output |
|---|---|---|---|
| `"ab"` | `5` | `1` | `1` |
| `"aa"` | `5` | `1` | `5` |
| `"aaaa"` | `1` | `10` | `2` |
| `"aaaaaa"` | `10` | `1` | `30` |
| `"aaaabb"` | `10` | `1` | `12` |
| `"aaaaab"` | `10` | `1` | `21` |
| `"abcdef"` | `1` | `7` | `21` |
| `"aabbcc"` | `3` | `3` | `9` |
| `"abab"` | `2` | `9` | `4` |
| `"zzzzzzyx"` | `4` | `2` | `12` |
| `"abcabc"` | `1` | `2` | `3` |
| `"qqqqqqqqqqqqqqqqqqqp"` | `7` | `3` | `66` |
| `"mississippim"` | `6` | `5` | `30` |
