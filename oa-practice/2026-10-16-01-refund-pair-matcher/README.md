# Refund Pair Matcher

**Difficulty:** Medium  
**Topic:** Hashing  
**Time:** 25 minutes

A payment service stores pending refund amounts in cents. Finance wants pairs of those refunds that sum exactly to a target amount. Each refund may be used in at most one pair. Return the maximum number of such disjoint pairs.

## Signature

```ts
function countRefundPairs(amounts: number[], target: number): number
```

## Constraints

- `1 <= n <= 1e5`, where `n` is `amounts.length`
- `1 <= amounts[i], target <= 1e9`

## Samples

**Example 1**

Input: `amounts = [100, 200, 300, 400, 100]`, `target = 500`  
Output: `2`

**Example 2**

Input: `amounts = [50, 50, 50, 50]`, `target = 100`  
Output: `2`
