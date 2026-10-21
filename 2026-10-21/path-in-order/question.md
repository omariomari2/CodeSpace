# Path In Order

**Company:** Microsoft

## Problem

You're given an undirected graph with `N` vertices numbered `1` to `N`, and `M` edges. The edges are described by two arrays `A` and `B` of length `M`: for each `K`, there's an edge between `A[K]` and `B[K]`.

Check whether the graph has a path that starts at vertex `1`, ends at vertex `N`, and visits every vertex one by one in increasing order (`1, 2, 3, ..., N`). Every step on the path has to be a direct edge.

Return `1` if that path exists, otherwise `0`.

## Function

```python
def check_path_presence(n: int, a: list[int], b: list[int]) -> int:
```

## Constraints

- `2 <= N <= 10^5`
- `1 <= M <= 10^5`
- `1 <= A[K], B[K] <= N`
- Edges can repeat, and `A[K]` can equal `B[K]`

(The original listing didn't give constraints, so these are the ones the tests use.)

## Examples

**Example 1**

```
N = 4
A = [1, 2, 4, 4, 3]
B = [2, 3, 1, 3, 1]
output: 1
```

The path `1-2-3-4` uses the edges `(1,2)`, `(2,3)`, and `(4,3)`.

## More test cases

| N | A | B | output |
|---|---|---|---|
| `2` | `[1]` | `[2]` | `1` |
| `2` | `[2]` | `[1]` | `1` |
| `3` | `[1, 1]` | `[2, 3]` | `0` |
| `3` | `[2, 3]` | `[1, 2]` | `1` |
| `5` | `[1, 2, 3]` | `[2, 3, 4]` | `0` |
| `5` | `[5, 3, 2, 1]` | `[4, 4, 3, 2]` | `1` |
| `4` | `[1, 2, 3, 1]` | `[3, 4, 4, 2]` | `0` |
| `3` | `[1, 1, 2]` | `[2, 2, 1]` | `0` |
| `4` | `[4, 3, 2]` | `[3, 2, 1]` | `1` |
| `6` | `[1, 2, 3, 4, 5, 1]` | `[2, 3, 4, 5, 6, 6]` | `1` |
| `6` | `[1, 2, 4, 5, 1]` | `[2, 3, 5, 6, 6]` | `0` |
| `2` | `[1, 1]` | `[1, 2]` | `1` |
| `3` | `[3, 3]` | `[3, 2]` | `0` |
| `7` | `[2, 1, 4, 3, 6, 5]` | `[3, 2, 5, 4, 7, 6]` | `1` |
