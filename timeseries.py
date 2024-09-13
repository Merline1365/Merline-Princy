import matplotlib.pyplot as plt

def estimate_trend(y, d):
    n = len(y)
    trend = [0]*n
    for t in range(n):
        if d % 2 == 1:  # odd d
            sum_y = sum(y[max(0, t-d//2):min(n, t+d//2+1)])
            count = min(t+1, n-t, d)
        else:  # even d
            sum_y = sum(y[max(0, t-d//2+1):min(n, t+d//2+1)])
            count = min(t+1, n-t, d)
        trend[t] = sum_y / count
    return trend

def estimate_seasonality(y, d, trend):
    n = len(y)
    seasonality = [0]*n
    for t in range(n):
        seasonality[t] = y[t] / trend[t]
    return seasonality

# Example usage:
y = [3459,
3458,
4002,
4564,
4221,
4529,
4466,
4137,
4126,
4259,
4240,
4936,
3031,
3261,
4160,
4377,
4307,
4696,
4458,
4457,
4364,
4236,
4500,
4974,
3075,
3377,
4443,
4261,
4460,
4985,
4324,
4719,
4374,
4248,
4784,
4971,
3370,
3484,
4269,
3994,
4715,
4974,
4223,
5000,
4235,
4554,
4851,
4826,
3699,
3983,
4262,
4619,
5219,
4836,
4941,
5062,
4365,
5012,
4850,
5097,
3758,
3825,
4454,
4635,
5210,
5057,
5231,
5034,
4970,
5342,
4831,
5965,
3796,
4019,
4898,
5090,
5237,
5447,
5435,
5107,
5515,
5583,
5346,
6286,
4032,
4435,
5479,
5483,
5587,
6176,
5621,
5889,
5828,
5849,
6180,
6771,
4243,
4952,
6008,
5353,
6435,
6673,
5636,
6630,
5887,
6322,
6520,
6678,
5082,
5216,
5893,
5894,
6799,
6667,
6374,
6840,
5575,
6545,
6789,
7180,
5117,
5442,
6337,
6525,
7216,
6761,
6958,
7070,
6148,
6924,
6716,
7975,
5326,
5609,
6414,
6741,
7144,
7133,
7568,
7266,
6634,
7626,
6843,
8540,
5629,
5898,
7045,
7094,
7333,
7918,
7289,
7396,
7259,
7268,
7731,
9058,
5557,
6237,
7723,
7262,
8241,
8757,
7352,
8496,
7741,
7710,
8247,
8902,
6066,
6590,
7923,
7335,
8843,
9327,
7792,
9156,
8037,
8640,
9128,
9545,
6627,
6743,
8195,
7828,
9570,
9484,
8608,
9543,
8123,
9649,
9390,
10065,
7093,
7483,
8365,
8895,
9794,
9977,
9553,
9375,
9225,
9948,
8758,
10839,
7266,
7578,
8688,
9162,
9369,
10167,
9507,
8923,
9272,
9075,
8949,
10843,
6558,
7481,
9475,
9424,
9351,
10552,
9077,
9273,
9420,
9413,
9866,
11455,
6901,
8014,
9832,
9281,
9967,
11344,
9106,
10469,
10085,
9612,
10328,
11483,
7486,
8641,
9709,
9423,
11342,
11274,
9845,
11163,
9532,
10754,
10953,
11922,
8395,
8888,
10110,
10493,
12218,
11385,
11186,
11462,
10494,
11540,
11138,
12709,
8557,
9059,
10055,
10977,
11792,
11904,
10965,
10981,
10828,
11817,
10470,
13310,
8400,
9062,
10722,
11107,
11508,
12904,
11869,
11224,
12022,
11983,
11506,
14183,
8648,
10321,
12107,
11420,
12238,
13681,
10950,
12700,
12272,
11905,
13016,
14421,
9043,
10452,
12481,
11491,
13545,
14730,
11416,
13402,
11907,
12711,
13261,
14265,
9564,
10415,
12683,
11919,
14138,
14583,
12640,
14257,
12396,
13914,
14174,
15504,
10718,
]
 # Time series data
d = 3  # Number of seasons (odd)
# d = 4  # Number of seasons (even)

trend = estimate_trend(y, d)
seasonality = estimate_seasonality(y, d, trend)

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(y, label='Original Time Series')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(trend, label='Trend Component')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(seasonality, label='Seasonality Component')
plt.legend()

plt.tight_layout()
plt.show()

