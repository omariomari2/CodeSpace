# Distinct Remainder

**Company:** Google

## Problem

You're given a string `text`. Delete exactly one contiguous substring from it (possibly empty, possibly the whole string) so that every character left over appears only once.

Characters are case-sensitive, so `"a"` and `"A"` are different, and spaces count as characters too.

Return the minimum number of characters you have to delete.

## Function

```python
def min_deletion_for_distinct(text: str) -> int:
```

## Constraints

- `0 <= len(text) <= 10^5`
- `text` contains printable ASCII characters (codes 32 to 126)

## Examples

**Example 1**

```
text = "abca"
output: 1
```

Delete either `a` and you're left with three different characters.

**Example 2**

```
text = "abc"
output: 0
```

Nothing repeats, so you don't need to delete anything.

## More test cases

| text | output |
|---|---|
| `""` | `0` |
| `"a"` | `0` |
| `"aa"` | `1` |
| `"aaa"` | `2` |
| `"abab"` | `2` |
| `"abcabc"` | `3` |
| `"abcdba"` | `2` |
| `"aAbBa"` | `1` |
| `"xyzzyx"` | `3` |
| `"hello world"` | `3` |
| `"abcdefgha"` | `1` |
| `"zabcz"` | `1` |
| `"mississippi"` | `8` |
