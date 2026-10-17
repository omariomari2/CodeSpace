# Tax Season Streak Bonus

**Difficulty:** Medium-hard  
**Topic:** Dynamic programming  
**Time:** 25 minutes

Closing a case on day `i` earns `points[i]`. If you close day `i`, you must skip day `i + 1`. Return the maximum total points you can earn over the season.

## Signature

```ts
function maxSeasonPoints(points: number[]): number
```

## Constraints

- `1 <= n <= 1e5`, where `n` is `points.length`
- `0 <= points[i] <= 1e4`

## Samples

**Example 1**

Input: `points = [3, 2, 5, 10, 7]`  
Output: `15`

**Example 2**

Input: `points = [1, 100, 1, 1, 100]`  
Output: `200`
