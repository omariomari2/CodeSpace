# Min Moves

**Company:** Google
**Topic:** Prefix Sums / Greedy
**Difficulty:** Easy

## Problem

You start with an array of zeros the same length as `a`. In one move, you pick any contiguous range and add 1 to every number in it.

Return the fewest moves it takes to turn the zeros into `a`.

## Function

```python
def min_moves(a: list[int]) -> int:
```

## Constraints

- `1 <= len(a) <= 10^5`
- `0 <= a[i] <= 10^4`

## Examples

**Example 1**

```
a = [2, 1, 3]
output: 4
```

One way to do it:

```
[0, 0, 0] -> [1, 1, 1] -> [2, 1, 1] -> [2, 1, 2] -> [2, 1, 3]
```

You can't do it in 3.

## More test cases

| a | output |
|---|---|
| `[0]` | `0` |
| `[5]` | `5` |
| `[0, 0, 0]` | `0` |
| `[1, 1, 1, 1]` | `1` |
| `[1, 2, 3, 4]` | `4` |
| `[4, 3, 2, 1]` | `4` |
| `[3, 0, 3]` | `6` |
| `[1, 0, 1, 0, 1]` | `3` |
| `[0, 2, 0, 2, 0]` | `4` |
| `[10000]` | `10000` |
| `[5, 5, 0, 5, 5]` | `10` |
| `[1, 3, 2, 4, 1, 5]` | `9` |
| `[2, 2, 1, 2, 2]` | `3` |

Hidden tests include arrays with 10^5 elements, so aim for O(n).
