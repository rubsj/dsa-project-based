"""
Retail system alerts if stock of any item falls below threshold in any 3-day period.
Prompt:
Given a list of item counts per day for n products:
restocks = [[5, 3, 2], [6, 7, 1], [3, 4, 5]]
and a threshold (say 5),
Return a list of product indices that triggered an alert in any 3-day window where any day’s stock was ≤ threshold.
"""

def inventory_restock_alert(restocks, thresold) :
    alerts = []
    for i, stocks in enumerate(restocks) :
        for stock in stocks:
            if stock <= thresold:
                alerts.append(i)
                break
    return alerts

restocks = [
    [5, 3, 2],  # Product 0
    [6, 7, 1],  # Product 1
    [3, 4, 5],  # Product 2
]
threshold = 2


result = inventory_restock_alert(restocks=restocks, thresold=threshold)
print(result)