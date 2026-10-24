# Unique Letter Words

**Company:** Meta

## Problem

You're given a list of lowercase words. Pick any subset of them so that, once you glue the picked words together, no letter appears more than once.

A word that already repeats a letter on its own can never be picked. Order doesn't matter, and picking nothing is allowed.

Return the longest possible length of the glued-together string.

## Function

```python
def max_unique_length(words: list[str]) -> int:
```

## Constraints

- `0 <= len(words) <= 16`
- `1 <= len(words[i]) <= 26`
- every word contains only lowercase English letters

## Examples

**Example 1**

```
words = ["un", "iq", "ue"]
output: 4
```

`"un"` + `"iq"` gives four different letters. Adding `"ue"` would repeat `u`.

**Example 2**

```
words = ["cha", "r", "act", "ers"]
output: 6
```

`"cha"` + `"ers"` gives `"chaers"`, six different letters.

**Example 3**

```
words = ["aa", "bc"]
output: 2
```

`"aa"` repeats a letter, so the best you can do is `"bc"`.

## More test cases

| words | output |
|---|---|
| `[]` | `0` |
| `["abcdefghijklmnopqrstuvwxyz"]` | `26` |
| `["a", "b", "c"]` | `3` |
| `["aa", "bb"]` | `0` |
| `["ab", "ba", "cd"]` | `4` |
| `["abc", "def", "abd", "gh"]` | `8` |
| `["a", "abc", "d", "de", "def"]` | `6` |
| `["xyz", "x", "y", "z", "w"]` | `4` |
| `["abcdefghijklm", "nopqrstuvwxyz", "a"]` | `26` |
| `["ab", "cd", "ef", "gh", "ij", "aj"]` | `10` |
| `["zz", "qq", "x"]` | `1` |
| `["yy", "bkhwmpbiisbldzknpm"]` | `0` |
