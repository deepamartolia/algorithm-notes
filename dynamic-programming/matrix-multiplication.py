# Recurrence Formula:
# For i <= k < j, cost[i, j] = min(cost[i,k] + cost[k+1, j] + (di-1 * dk * dj)).

# Example: A1 * A2 * A3 * A4 => (d0, d1) * (d1, d2) * (d2, d3) * (d3, d4).
# To find the recurrence formula for i = 1 and j = 4, where 1 <= k < 4. we have:
# cost[1, 4] = min((cost[1, 1] + cost[2, 4] + (d0 * d1 * d4)), (cost[1, 2] + cost[3, 4] + (d0 * d2 * d4)), (cost[1, 3] + cost[4, 4] + (d0 * d3 * d4))), 

# Base Case:
# When i == j, cost[i, j] = 0. So, cost[1, 1] = cost[2, 2] = cost[3, 3] = cost[4, 4] = 0.

# For other cases, we have:
# cost[1, 3] = min((cost[1, 1] + cost[2, 3] + (d0 * d1 * d3)), (cost[1, 2] + cost[3, 3] + (d0 * d2 * d3))), where 1 <= k < 3.
# cost[2, 4] = min((cost[2, 2] + cost[3, 4] + (d1 * d2 * d4)), (cost[2, 3] + cost[4, 4] + (d1 * d3 * d4))), where 2 <= k < 4.
# cost[1, 2] = cost[1, 1] + cost[2, 2] + (d0 * d1 * d2), where 1 <= k < 2.
# cost[3, 4] = cost[3, 3] + cost[4, 4] + (d2 * d3 * d4), where 3 <= k < 4.
