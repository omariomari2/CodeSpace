# Escape Game Score

**Company:** Microsoft

## Problem

In an escape game, one puzzle hands you an array of integers `elements`. You score points by repeating these two steps until the array is empty:

1. Pick a value `v` that's still in the array. Remove every occurrence of `v` and add their sum to your score.
2. Remove every element equal to `v - 1` or `v + 1`. These give no points.

Return the maximum score you can end up with.

## Function

```python
def max_escape_score(elements: list[int]) -> int:
```

## Constraints

- `1 <= len(elements) <= 10^5`
- `1 <= elements[i] <= 10^5`

## Examples

**Example 1**

```
elements = [5, 6, 6, 4, 11]
output: 27
```

Take `11` for 11 points. Take both `6`s for 12 points, which wipes out the `5`. Take `4` for 4 points. Total 11 + 12 + 4 = 27.

**Example 2**

```
elements = [3, 4, 2]
output: 6
```

Take `4` for 4 points, which removes the `3`. Then take `2` for 2 more. Total 6.

## More test cases

| elements | output |
|---|---|
| `[1]` | `1` |
| `[7, 7, 7]` | `21` |
| `[1, 2]` | `2` |
| `[2, 2, 3, 3, 3, 4]` | `9` |
| `[1, 2, 3, 4, 5]` | `9` |
| `[10, 20, 30]` | `60` |
| `[1, 1, 1, 2, 4, 5, 5, 5, 6]` | `18` |
| `[100000, 99999, 1]` | `100001` |
| `[3, 1, 2, 3, 1, 2]` | `8` |
| `[8, 10, 9, 9, 10]` | `28` |
| `[4, 4, 4, 5, 6, 6]` | `24` |
| `[1, 3, 5, 7, 2]` | `16` |
| `[50, 51, 52, 53, 54, 55]` | `159` |
