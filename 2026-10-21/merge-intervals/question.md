# Merge Intervals

**Company:** Amazon

## Problem

You're given a list of closed intervals, where `intervals[i] = [start_i, end_i]`. Merge every pair of intervals that overlap, and return the non-overlapping intervals that cover everything in the input, sorted by start.

Two intervals that share an endpoint count as overlapping. The input isn't guaranteed to be sorted.

## Function

```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
```

Return a list of `[start, end]` lists.

## Constraints

- `1 <= len(intervals) <= 10^5`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Examples

**Example 1**

```
intervals = [[1,3],[2,6],[8,10],[15,18]]
output: [[1,6],[8,10],[15,18]]
```

`[1,3]` and `[2,6]` overlap, so they become `[1,6]`.

**Example 2**

```
intervals = [[1,4],[4,5]]
output: [[1,5]]
```

They share the endpoint 4, so they merge.

**Example 3**

```
intervals = [[8,10],[1,4],[2,3],[15,18],[6,9],[3,7],[17,20],[12,12]]
output: [[1,10],[12,12],[15,20]]
```

## More test cases

| intervals | output |
|---|---|
| `[[5, 5]]` | `[[5, 5]]` |
| `[[0, 0], [0, 0]]` | `[[0, 0]]` |
| `[[1, 2], [3, 4]]` | `[[1, 2], [3, 4]]` |
| `[[1, 10], [2, 3], [4, 5]]` | `[[1, 10]]` |
| `[[0, 10000]]` | `[[0, 10000]]` |
| `[[3, 4], [1, 2], [2, 3]]` | `[[1, 4]]` |
| `[[1, 1], [2, 2], [1, 2]]` | `[[1, 2]]` |
| `[[6, 8], [1, 9], [2, 4], [4, 7]]` | `[[1, 9]]` |
| `[[10, 12], [0, 1], [5, 6], [1, 5]]` | `[[0, 6], [10, 12]]` |
| `[[7, 7], [7, 7], [8, 8]]` | `[[7, 7], [8, 8]]` |
| `[[0, 3], [5, 9], [3, 5]]` | `[[0, 9]]` |
| `[[2, 3], [4, 6], [1, 1], [10, 11], [6, 10]]` | `[[1, 1], [2, 3], [4, 11]]` |
