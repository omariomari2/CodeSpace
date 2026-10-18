# Subarray Pattern

**Company:** Meta
**Topic:** Sliding window
**Difficulty:** Easy

## Problem

You're looking at a list of daily readings, `numbers`, and a short `pattern` that describes how the readings should move from one day to the next. Each value in `pattern` is one of:

- `1` means the next reading goes up
- `-1` means the next reading goes down
- `0` means the next reading stays the same

A pattern of length `m` describes a stretch of `m + 1` consecutive readings. The stretch starting at index `i` matches when, for every `k` from `0` to `m - 1`, the move from `numbers[i + k]` to `numbers[i + k + 1]` is exactly what `pattern[k]` says.

Return how many stretches of `numbers` match the pattern. Stretches can overlap.

## Function

```python
def count_matching_subarrays(numbers: list[int], pattern: list[int]) -> int:
```

## Constraints

- `2 <= len(numbers) <= 10^5`
- `1 <= len(pattern) < len(numbers)`
- `1 <= numbers[i] <= 10^9`
- `pattern[k]` is `-1`, `0`, or `1`
- A solution around O(n * m) is accepted, but O(n) is possible.

## Examples

**Example 1**

```
numbers = [4, 1, 3, 4, 4, 5, 5, 1]
pattern = [1, 0, -1]
output: 1
```

The stretch `[4, 5, 5, 1]` goes up, stays the same, then goes down. No other stretch of 4 readings does that.

**Example 2**

```
numbers = [1, 2, 3, 4, 5, 6]
pattern = [1, 1]
output: 4
```

Every 3-reading stretch keeps going up: `[1, 2, 3]`, `[2, 3, 4]`, `[3, 4, 5]`, and `[4, 5, 6]`.

**Example 3**

```
numbers = [1, 4, 4, 1, 3, 5, 5, 3]
pattern = [1, 0, -1]
output: 2
```

`[1, 4, 4, 1]` and `[3, 5, 5, 3]` both match.

## More test cases

| numbers | pattern | output |
|---|---|---|
| `[5, 5]` | `[0]` | `1` |
| `[5, 6]` | `[-1]` | `0` |
| `[3, 2, 1]` | `[-1, -1]` | `1` |
| `[7, 7, 7, 7, 7]` | `[0, 0]` | `3` |
| `[1, 3, 2, 4, 3, 5]` | `[1, -1]` | `2` |
| `[1, 3, 2, 4, 3, 5]` | `[1, -1, 1, -1, 1]` | `1` |
| `[2, 1]` | `[1]` | `0` |
| `[10, 20, 20, 10, 20, 20, 10]` | `[1, 0, -1]` | `2` |
| `[1, 2, 1, 2, 1, 2, 1]` | `[1, -1, 1]` | `2` |
| `[1000000000, 1, 1000000000]` | `[-1, 1]` | `1` |

Hidden tests include inputs at the full 10^5 size.
