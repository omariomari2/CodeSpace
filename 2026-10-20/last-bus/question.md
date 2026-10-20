# Last Bus

**Company:** Meta
**Topic:** Binary Search / Time Parsing
**Difficulty:** Easy

## Problem

You're standing at a bus stop and you've got the day's bus schedule, `time_table`, as a list of departure times in `"HH:MM"` (24-hour) format. You also know the current time, `moment`, in the same format.

Return how many minutes ago the most recent bus left. A bus scheduled at exactly `moment` hasn't left yet, so it doesn't count. If no bus has left yet today, return `-1`.

Everything happens within one day, so don't wrap around midnight. The schedule isn't guaranteed to be sorted.

## Function

```python
def bustling_town_buses(time_table: list[str], moment: str) -> int:
```

## Constraints

- `1 <= len(time_table) <= 10^5`
- Every time is a valid `"HH:MM"` between `"00:00"` and `"23:59"`
- Times can repeat

(The original listing didn't give constraints, so these are the ones the tests use.)

## Examples

**Example 1**

```
time_table = ["12:30", "14:00", "19:55"]
moment = "14:30"
output: 30
```

The last bus before 14:30 left at 14:00, which was 30 minutes ago.

**Example 2**

```
time_table = ["00:00", "14:00", "19:55"]
moment = "00:00"
output: -1
```

The 00:00 bus is leaving right now, so it hasn't departed. Nothing left before it.

**Example 3**

```
time_table = ["12:30", "14:00", "19:55"]
moment = "14:00"
output: 90
```

The 14:00 bus hasn't left yet, so the most recent one is 12:30, 90 minutes ago.

## More test cases

| time_table | moment | output |
|---|---|---|
| `["08:15"]` | `"08:16"` | `1` |
| `["08:15"]` | `"08:15"` | `-1` |
| `["08:15"]` | `"07:00"` | `-1` |
| `["23:59"]` | `"23:59"` | `-1` |
| `["00:00"]` | `"23:59"` | `1439` |
| `["10:00", "10:00", "10:00"]` | `"10:01"` | `1` |
| `["19:55", "12:30", "14:00"]` | `"20:00"` | `5` |
| `["06:00", "09:45", "13:10", "17:20"]` | `"23:59"` | `399` |
| `["06:00", "09:45", "13:10", "17:20"]` | `"09:44"` | `224` |
| `["00:01", "00:02"]` | `"00:02"` | `1` |
| `["13:05", "01:50", "22:40", "07:07"]` | `"13:05"` | `358` |

Hidden tests include schedules with 10^5 entries, so aim for O(n) (or O(n log n) if you sort).
