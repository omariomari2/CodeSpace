# Connect Ropes

**Company:** Amazon
**Topic:** Heaps / greedy
**Difficulty:** Medium

## Problem

A warehouse has a pile of loose ropes, and the crew needs to tie them all into one long rope before a shipment goes out. `ropes[i]` is the length of the i-th rope.

Each time the crew ties two ropes together, it costs the sum of their two lengths, and the result is a single rope of that combined length. They can pick any two ropes at each step.

Return the minimum total cost to end up with exactly one rope. If there's only one rope to begin with, nothing needs tying, so the cost is 0.

## Function

```python
def min_cost_to_connect(ropes: list[int]) -> int:
```

## Constraints

- `1 <= len(ropes) <= 10^5`
- `1 <= ropes[i] <= 10^4`
- The answer fits in a 64-bit signed integer.

## Examples

**Example 1**

```
ropes = [4, 3, 2, 6]
output: 29
```

Tie 2 and 3 (cost 5), then 4 and 5 (cost 9), then 6 and 9 (cost 15). Total is 5 + 9 + 15 = 29.

**Example 2**

```
ropes = [4, 2, 7, 6, 9]
output: 62
```

One best order costs 6, 12, 16, then 28, for 62 total.

**Example 3**

```
ropes = [10]
output: 0
```

Only one rope, so there's nothing to tie.

## More test cases

| ropes | output |
|---|---|
| `[5, 5]` | `10` |
| `[1, 1, 1, 1]` | `8` |
| `[1, 2, 3, 4, 5]` | `33` |
| `[7, 7, 7, 7, 7, 7, 7, 7]` | `168` |
| `[10000, 10000, 10000]` | `50000` |
| `[1, 10000]` | `10001` |

Hidden tests include inputs at the full 10^5 size, so aim for better than O(n^2).
