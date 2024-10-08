import numpy as np
import matplotlib.pyplot as plt

#Enter TS DATA
time_series = np.array([[3459, 3458, 4002, 4564, 4221, 4529, 4466, 4137, 4126, 4259, 4240, 4936, 
     3031, 3261, 4160, 4377, 4307, 4696, 4458, 4457, 4364, 4236, 4500, 4974, 
     3075, 3377, 4443, 4261, 4460, 4985, 4324, 4719, 4374, 4248, 4784, 4971, 
     3370, 3484, 4269, 3994, 4715, 4974, 4223, 5000, 4235, 4554, 4851, 4826, 
     3699, 3983, 4262, 4619, 5219, 4836, 4941, 5062, 4365, 5012, 4850, 5097, 
     3758, 3825, 4454, 4635, 5210, 5057, 5231, 5034, 4970, 5342, 4831, 5965, 
     3796, 4019, 4898, 5090, 5237, 5447, 5435, 5107, 5515, 5583, 5346, 6286, 
     4032, 4435, 5479, 5483, 5587, 6176, 5621, 5889, 5828, 5849, 6180, 6771, 
     4243, 4952, 6008, 5353, 6435, 6673, 5636, 6630, 5887, 6322, 6520, 6678, 
     5082, 5216, 5893, 5894, 6799, 6667, 6374, 6840, 5575, 6545, 6789, 7180, 
     5117, 5442, 6337, 6525, 7216, 6761, 6958, 7070, 6148, 6924, 6716, 7975, 
     5326, 5609, 6414, 6741, 7144, 7133, 7568, 7266, 6634, 7626, 6843, 8540, 
     5629, 5898, 7045, 7094, 7333, 7918, 7289, 7396, 7259, 7268, 7731, 9058, 
     5557, 6237, 7723, 7262, 8241, 8757, 7352, 8496, 7741, 7710, 8247, 8902, 
     6066, 6590, 7923, 7335, 8843, 9327, 7792, 9156, 8037, 8640, 9128, 9545, 
     6627, 6743, 8195, 7828, 9570, 9484, 8608, 9543, 8123, 9649, 9390, 10065, 
     7093, 7483, 8365, 8895, 9794, 9977, 9553, 9375, 9225, 9948, 8758, 10839])

q = int(input("Enter value of q: "))

n = len(time_series)
Tline = np.zeros(n)

#Calc Mk values
#Odd
if len(time_series) % 2 == 1:
    for i in range(q, n - q):
        Tline[i] = np.mean(time_series[i - q:i + q + 1])
#Even
else:
    d = 2 * q
    for i in range(q, n - q):
        Tline[i] = (0.5 * time_series[i - q] + np.sum(time_series[i - q + 1:i + q]) + 0.5 * time_series[i + q]) / d


seasonal_effect = np.zeros(n)
for i in range(n):
    sum_diff = 0
    count = 0
    for j in range(-(n // q), n // q):
        if 0 <= i + j * q < n:
            sum_diff += time_series[i + j * q] - Tline[i + j * q]
            count += 1
    if count > 0:
        seasonal_effect[i] = sum_diff / count

avg_seasonality = np.mean(seasonal_effect)
adjusted_seasonal = seasonal_effect - avg_seasonality

print("Calculated Trend:", Tline)
print("Extracted Seasonality:", adjusted_seasonal)

plt.figure(figsize=(10, 6))

plt.subplot(311)
plt.plot(time_series, label="Original Data")
plt.legend(loc='upper left')

plt.subplot(312)
plt.plot(Tline, label="Trend", color='orange')
plt.legend(loc='upper left')

plt.subplot(313)
plt.plot(adjusted_seasonal, label="Seasonality", color='green')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
