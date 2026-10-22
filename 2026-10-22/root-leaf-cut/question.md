# Root-to-Leaf Cut

**Company:** Google

## Problem

You're given a rooted binary tree with `n` nodes, numbered `0` to `n - 1`. Node `0` is the root. Every edge has a non-negative cost.

The tree comes as four arrays of length `n`. For node `i`, `left_child[i]` and `right_child[i]` are its children, or `-1` if that child doesn't exist. `left_cost[i]` and `right_cost[i]` are the costs of the edges to those children, and they're `0` when the child doesn't exist.

You want to cut some edges so that the root can no longer reach any leaf of the original tree. A leaf is a node that has no children in the original tree. Nodes that only become childless because of your cuts don't count as leaves.

Return the minimum total cost of the edges you cut.

If the tree is empty (all arrays are empty) or it's just the root, return `0`.

## Function

```python
def min_cut_cost(left_child: list[int], right_child: list[int],
                 left_cost: list[int], right_cost: list[int]) -> int:
```

## Constraints

- `0 <= n <= 10^5`
- All four arrays have length `n`
- When `n > 0`, the arrays describe one valid binary tree rooted at node `0`: every node other than `0` is a child of exactly one node, and every node is reachable from the root
- Each child index is `-1` or in `[0, n - 1]`
- `0 <= cost <= 2^31 - 1` for every existing edge, and the sum of all edge costs is at most `2^31 - 1`
- The tree is not guaranteed to be balanced. It can be a single path of length `n`.

## Examples

**Example 1**

```
left_child  = [1, 3, 5, -1, -1, -1, -1]
right_child = [2, 4, 6, -1, -1, -1, -1]
left_cost   = [4, 1, 6, 0, 0, 0, 0]
right_cost  = [7, 5, 2, 0, 0, 0, 0]
output: 11
```

Cut the edge 0 to 1 (cost 4) and the edge 0 to 2 (cost 7). Total 11.

**Example 2**

```
left_child  = [1, 2, 3, -1]
right_child = [-1, -1, -1, -1]
left_cost   = [8, 3, 5, 0]
right_cost  = [0, 0, 0, 0]
output: 3
```

There's one path from the root to the only leaf. Cutting the edge 1 to 2 costs 3, the cheapest edge on it.

**Example 3**

```
left_child = [-1], right_child = [-1], left_cost = [0], right_cost = [0]
output: 0
```

## More test cases

| left_child | right_child | left_cost | right_cost | output |
|---|---|---|---|---|
| `[]` | `[]` | `[]` | `[]` | `0` |
| `[1, -1]` | `[-1, -1]` | `[9, 0]` | `[0, 0]` | `9` |
| `[1, -1, -1]` | `[2, -1, -1]` | `[0, 0, 0]` | `[5, 0, 0]` | `5` |
| `[-1, -1]` | `[1, -1]` | `[0, 0]` | `[4, 0]` | `4` |
| `[1, -1, 3, -1]` | `[2, -1, -1, -1]` | `[10, 0, 1, 0]` | `[2, 0, 0, 0]` | `11` |
| `[1, 3, -1, -1, -1]` | `[2, 4, -1, -1, -1]` | `[100, 1, 0, 0, 0]` | `[3, 1, 0, 0, 0]` | `5` |
| `[2, -1, 3, -1]` | `[1, -1, -1, -1]` | `[6, 0, 2, 0]` | `[5, 0, 0, 0]` | `7` |
| `[1, 2, -1, -1]` | `[3, -1, -1, -1]` | `[7, 7, 0, 0]` | `[1, 0, 0, 0]` | `8` |
| `[1, 3, 5, -1, -1, -1]` | `[2, 4, -1, -1, -1, -1]` | `[9, 2, 3, 0, 0, 0]` | `[9, 2, 0, 0, 0, 0]` | `7` |
| `[1, -1, -1]` | `[2, -1, -1]` | `[0, 0, 0]` | `[0, 0, 0]` | `0` |
| `[3, -1, 1, -1, -1]` | `[2, -1, 4, -1, -1]` | `[5, 0, 4, 0, 0]` | `[1, 0, 4, 0, 0]` | `6` |
| `[1, 2, 3, 4, -1]` | `[-1, -1, -1, -1, -1]` | `[2147483647, 6, 9, 4, 0]` | `[0, 0, 0, 0, 0]` | `4` |
