# First and Last Digit Pairs

**Company:** Microsoft
**Topic:** Hashing
**Difficulty:** Easy

## Problem

You're given a list of non-negative integers. Two numbers count as a matching pair if they start with the same digit and also end with the same digit as each other. For example, 36 and 306 match (both start with 3 and end with 6), and 45 and 415 match (both start with 4 and end with 5).

Pick two numbers at different positions in the list that match, and return the largest sum you can get from any such pair. If no two numbers match, return -1.

A single-digit number starts and ends with the same digit, so 7 matches with 7, 77, 707, and so on.

## Function

```python
def max_pair_sum(nums: list[int]) -> int:
```

## Constraints

- `1 <= len(nums) <= 10^5`
- `0 <= nums[i] <= 10^9`
- Numbers have no leading zeros (0 itself is just "0").

## Examples

**Example 1**

```
nums = [2, 36, 45, 306, 415]
output: 460
```

36 + 306 = 342 and 45 + 415 = 460. The bigger one is 460.

**Example 2**

```
nums = [1, 2, 3]
output: -1
```

No two numbers start and end with the same digits.

## More test cases

| nums | output |
|---|---|
| `[7]` | `-1` |
| `[11, 11]` | `22` |
| `[5, 5, 5]` | `10` |
| `[0, 0]` | `0` |
| `[10, 100, 1000]` | `1100` |
| `[121, 101, 1]` | `222` |
| `[909, 99, 9, 999]` | `1908` |
| `[12, 21, 102, 201]` | `222` |
| `[1000000000, 1000000000, 100000000]` | `2000000000` |

Hidden tests include lists of 10^5 numbers, so an O(n^2) check of every pair will be too slow.
