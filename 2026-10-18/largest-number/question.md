# Largest Number

**Company:** Google
**Topic:** Greedy
**Difficulty:** Easy

## Problem

You're given a list of single digits, `nums`. Pick exactly three of them, keeping them in the same left-to-right order they appear in the list, and glue them together into a three-digit number.

Return the largest number you can make. If the number starts with zeros, just return its integer value (for example, picking `0, 0, 5` gives `5`).

## Function

```python
def find_largest_number(nums: list[int]) -> int:
```

## Constraints

- `3 <= len(nums) <= 10^5`
- `0 <= nums[i] <= 9`

## Examples

**Example 1**

```
nums = [7, 4, 3, 8, 2]
output: 782
```

Pick `7`, then `8`, then `2`. You can't use `8` first and then `7`, because `7` comes before `8` in the list.

**Example 2**

```
nums = [1, 2, 3]
output: 123
```

There are only three digits, so you have to use all of them in order.

**Example 3**

```
nums = [0, 0, 0]
output: 0
```

## More test cases

| nums | output |
|---|---|
| `[3, 2, 1]` | `321` |
| `[9, 9, 9, 9]` | `999` |
| `[0, 0, 5]` | `5` |
| `[3, 0, 0, 0]` | `300` |
| `[1, 9, 1, 9, 1]` | `991` |
| `[5, 1, 9, 2, 8]` | `928` |
| `[2, 9, 8, 7, 9]` | `989` |
| `[9, 0, 0, 1]` | `901` |
| `[1, 0, 0, 9, 9]` | `199` |
| `[4, 4, 1, 4]` | `444` |

Hidden tests include inputs at the full 10^5 size, so aim for O(n).
