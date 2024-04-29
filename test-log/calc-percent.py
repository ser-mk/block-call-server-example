import re

# Sample data
data = """

size 40 loop 1
======================= Slow =========================
Time taken for tests:   33.185 seconds
======================= Fast =========================
Time taken for tests:   30.434 seconds
size 41 loop 1
======================= Slow =========================
Time taken for tests:   29.607 seconds
======================= Fast =========================
Time taken for tests:   27.767 seconds
size 42 loop 1
======================= Slow =========================
Time taken for tests:   35.306 seconds
======================= Fast =========================
Time taken for tests:   31.334 seconds
size 43 loop 1
======================= Slow =========================
Time taken for tests:   33.220 seconds
======================= Fast =========================
Time taken for tests:   30.711 seconds
size 44 loop 1
======================= Slow =========================
Time taken for tests:   42.805 seconds
======================= Fast =========================
Time taken for tests:   33.820 seconds
size 45 loop 1
======================= Slow =========================
Time taken for tests:   37.331 seconds
======================= Fast =========================
Time taken for tests:   32.021 seconds
size 46 loop 1
======================= Slow =========================
Time taken for tests:   38.098 seconds
======================= Fast =========================
Time taken for tests:   33.707 seconds
size 47 loop 1
======================= Slow =========================
Time taken for tests:   41.676 seconds
======================= Fast =========================
Time taken for tests:   33.266 seconds
size 48 loop 1
======================= Slow =========================
Time taken for tests:   43.217 seconds
======================= Fast =========================
Time taken for tests:   35.037 seconds
size 49 loop 1
======================= Slow =========================
Time taken for tests:   46.836 seconds
======================= Fast =========================
Time taken for tests:   36.926 seconds
size 50 loop 1
======================= Slow =========================
Time taken for tests:   49.725 seconds
======================= Fast =========================
Time taken for tests:   39.994 seconds
size 51 loop 1
======================= Slow =========================
Time taken for tests:   51.844 seconds
======================= Fast =========================
Time taken for tests:   39.678 seconds
size 52 loop 1
======================= Slow =========================
Time taken for tests:   52.958 seconds
======================= Fast =========================
Time taken for tests:   41.287 seconds
size 53 loop 1
======================= Slow =========================
Time taken for tests:   53.737 seconds
======================= Fast =========================
Time taken for tests:   43.400 seconds
size 54 loop 1
======================= Slow =========================
Time taken for tests:   58.740 seconds
======================= Fast =========================
Time taken for tests:   42.533 seconds
size 55 loop 1
======================= Slow =========================
Time taken for tests:   57.596 seconds
======================= Fast =========================
Time taken for tests:   47.222 seconds
size 56 loop 1
======================= Slow =========================
Time taken for tests:   61.743 seconds
======================= Fast =========================
Time taken for tests:   48.366 seconds
size 57 loop 1
======================= Slow =========================
Time taken for tests:   64.779 seconds
======================= Fast =========================
Time taken for tests:   50.639 seconds
size 58 loop 1
======================= Slow =========================
Time taken for tests:   67.104 seconds
======================= Fast =========================
Time taken for tests:   53.127 seconds
size 59 loop 1
======================= Slow =========================
Time taken for tests:   69.706 seconds
======================= Fast =========================
Time taken for tests:   53.523 seconds
size 60 loop 1
======================= Slow =========================
Time taken for tests:   71.329 seconds
======================= Fast =========================
Time taken for tests:   56.027 seconds
size 61 loop 1
======================= Slow =========================
Time taken for tests:   74.366 seconds
======================= Fast =========================
Time taken for tests:   59.038 seconds
size 62 loop 1
======================= Slow =========================
Time taken for tests:   74.600 seconds
======================= Fast =========================
Time taken for tests:   61.439 seconds
size 63 loop 1
======================= Slow =========================
Time taken for tests:   78.912 seconds
======================= Fast =========================
Time taken for tests:   62.151 seconds
size 64 loop 1
======================= Slow =========================
Time taken for tests:   80.877 seconds
======================= Fast =========================
Time taken for tests:   64.891 seconds
size 65 loop 1
======================= Slow =========================
Time taken for tests:   85.651 seconds
======================= Fast =========================
Time taken for tests:   67.843 seconds
size 66 loop 1
======================= Slow =========================
Time taken for tests:   87.128 seconds
======================= Fast =========================
Time taken for tests:   69.703 seconds
size 67 loop 1
======================= Slow =========================
Time taken for tests:   89.212 seconds
======================= Fast =========================
Time taken for tests:   72.091 seconds
size 68 loop 1
======================= Slow =========================
Time taken for tests:   93.846 seconds
======================= Fast =========================
Time taken for tests:   75.870 seconds
size 69 loop 1
======================= Slow =========================
Time taken for tests:   98.189 seconds
======================= Fast =========================
Time taken for tests:   79.305 seconds
size 70 loop 1
======================= Slow =========================
Time taken for tests:   100.750 seconds
======================= Fast =========================
Time taken for tests:   81.100 seconds
size 71 loop 1
======================= Slow =========================
Time taken for tests:   105.772 seconds
======================= Fast =========================
Time taken for tests:   85.675 seconds
size 72 loop 1
======================= Slow =========================
Time taken for tests:   109.013 seconds
======================= Fast =========================
Time taken for tests:   86.463 seconds
size 73 loop 1
======================= Slow =========================
Time taken for tests:   111.337 seconds
======================= Fast =========================
Time taken for tests:   90.073 seconds
size 74 loop 1
======================= Slow =========================
Time taken for tests:   113.703 seconds
======================= Fast =========================
Time taken for tests:   94.159 seconds
size 75 loop 1
======================= Slow =========================
Time taken for tests:   132.407 seconds
======================= Fast =========================
Time taken for tests:   108.293 seconds
size 76 loop 1
======================= Slow =========================
Time taken for tests:   135.505 seconds
======================= Fast =========================
Time taken for tests:   112.825 seconds
size 77 loop 1
======================= Slow =========================
Time taken for tests:   141.466 seconds
======================= Fast =========================
Time taken for tests:   114.683 seconds
size 78 loop 1
======================= Slow =========================
Time taken for tests:   144.510 seconds
======================= Fast =========================
Time taken for tests:   119.606 seconds
size 79 loop 1
======================= Slow =========================
Time taken for tests:   149.688 seconds
======================= Fast =========================
Time taken for tests:   122.317 seconds
size 80 loop 1
======================= Slow =========================
Time taken for tests:   152.583 seconds
======================= Fast =========================
Time taken for tests:   126.455 seconds
size 81 loop 1
======================= Slow =========================
Time taken for tests:   160.404 seconds
======================= Fast =========================
Time taken for tests:   130.464 seconds
size 82 loop 1
======================= Slow =========================
Time taken for tests:   163.196 seconds
======================= Fast =========================
Time taken for tests:   134.158 seconds
size 83 loop 1
======================= Slow =========================
Time taken for tests:   168.651 seconds
======================= Fast =========================
Time taken for tests:   138.304 seconds
size 84 loop 1
======================= Slow =========================
Time taken for tests:   175.353 seconds
======================= Fast =========================
Time taken for tests:   142.254 seconds
size 85 loop 1
======================= Slow =========================
Time taken for tests:   180.888 seconds
======================= Fast =========================
Time taken for tests:   147.144 seconds
size 86 loop 1
======================= Slow =========================
Time taken for tests:   186.115 seconds
======================= Fast =========================
Time taken for tests:   153.260 seconds
size 87 loop 1
======================= Slow =========================
Time taken for tests:   191.021 seconds
======================= Fast =========================
Time taken for tests:   159.315 seconds
size 88 loop 1
======================= Slow =========================
Time taken for tests:   197.212 seconds
======================= Fast =========================
Time taken for tests:   163.664 seconds
size 89 loop 1
======================= Slow =========================
Time taken for tests:   203.507 seconds
======================= Fast =========================
Time taken for tests:   168.532 seconds
size 90 loop 1
======================= Slow =========================
Time taken for tests:   211.527 seconds
======================= Fast =========================
Time taken for tests:   175.027 seconds
size 91 loop 1
======================= Slow =========================
Time taken for tests:   215.033 seconds
======================= Fast =========================
Time taken for tests:   180.843 seconds
size 92 loop 1
======================= Slow =========================
Time taken for tests:   201.775 seconds
======================= Fast =========================
Time taken for tests:   165.466 seconds
size 93 loop 1
======================= Slow =========================
Time taken for tests:   208.944 seconds
======================= Fast =========================
Time taken for tests:   172.113 seconds
size 94 loop 1
======================= Slow =========================
Time taken for tests:   213.897 seconds
======================= Fast =========================
Time taken for tests:   177.587 seconds
size 95 loop 1
======================= Slow =========================
Time taken for tests:   233.025 seconds
======================= Fast =========================
Time taken for tests:   195.590 seconds
size 96 loop 1
======================= Slow =========================
Time taken for tests:   242.280 seconds
======================= Fast =========================
Time taken for tests:   201.922 seconds
size 97 loop 1
======================= Slow =========================
Time taken for tests:   246.858 seconds
======================= Fast =========================
Time taken for tests:   208.586 seconds
size 98 loop 1
======================= Slow =========================
Time taken for tests:   250.345 seconds
======================= Fast =========================
Time taken for tests:   206.360 seconds
size 99 loop 1
======================= Slow =========================
Time taken for tests:   256.726 seconds
======================= Fast =========================
Time taken for tests:   212.220 seconds
size 100 loop 1
======================= Slow =========================
Time taken for tests:   264.485 seconds
======================= Fast =========================
Time taken for tests:   219.934 seconds
size 40 loop 2
======================= Slow =========================
Time taken for tests:   53.680 seconds
======================= Fast =========================
Time taken for tests:   46.603 seconds
size 41 loop 2
======================= Slow =========================
Time taken for tests:   48.262 seconds
======================= Fast =========================
Time taken for tests:   41.836 seconds
size 42 loop 2
======================= Slow =========================
Time taken for tests:   60.329 seconds
======================= Fast =========================
Time taken for tests:   50.339 seconds
size 43 loop 2
======================= Slow =========================
Time taken for tests:   54.316 seconds
======================= Fast =========================
Time taken for tests:   46.576 seconds
size 44 loop 2
======================= Slow =========================
Time taken for tests:   70.784 seconds
======================= Fast =========================
Time taken for tests:   55.782 seconds
size 45 loop 2
======================= Slow =========================
Time taken for tests:   60.736 seconds
======================= Fast =========================
Time taken for tests:   50.341 seconds
size 46 loop 2
======================= Slow =========================
Time taken for tests:   63.874 seconds
======================= Fast =========================
Time taken for tests:   52.877 seconds
size 47 loop 2
======================= Slow =========================
Time taken for tests:   68.578 seconds
======================= Fast =========================
Time taken for tests:   56.072 seconds
size 48 loop 2
======================= Slow =========================
Time taken for tests:   74.474 seconds
======================= Fast =========================
Time taken for tests:   57.462 seconds
size 49 loop 2
======================= Slow =========================
Time taken for tests:   78.285 seconds
======================= Fast =========================
Time taken for tests:   61.222 seconds
size 50 loop 2
======================= Slow =========================
Time taken for tests:   82.667 seconds
======================= Fast =========================
Time taken for tests:   62.660 seconds
size 51 loop 2
======================= Slow =========================
Time taken for tests:   86.369 seconds
======================= Fast =========================
Time taken for tests:   65.701 seconds
size 52 loop 2
======================= Slow =========================
Time taken for tests:   89.640 seconds
======================= Fast =========================
Time taken for tests:   69.389 seconds
size 53 loop 2
======================= Slow =========================
Time taken for tests:   92.713 seconds
======================= Fast =========================
Time taken for tests:   73.244 seconds
size 54 loop 2
======================= Slow =========================
Time taken for tests:   97.768 seconds
======================= Fast =========================
Time taken for tests:   76.623 seconds
size 55 loop 2
======================= Slow =========================
Time taken for tests:   102.789 seconds
======================= Fast =========================
Time taken for tests:   82.151 seconds
size 56 loop 2
======================= Slow =========================
Time taken for tests:   108.654 seconds
======================= Fast =========================
Time taken for tests:   84.505 seconds
size 57 loop 2
======================= Slow =========================
Time taken for tests:   113.763 seconds
======================= Fast =========================
Time taken for tests:   87.758 seconds
size 58 loop 2
======================= Slow =========================
Time taken for tests:   119.657 seconds
======================= Fast =========================
Time taken for tests:   93.126 seconds
size 59 loop 2
======================= Slow =========================
Time taken for tests:   121.687 seconds
======================= Fast =========================
Time taken for tests:   96.480 seconds
size 60 loop 2
======================= Slow =========================
Time taken for tests:   126.559 seconds
======================= Fast =========================
Time taken for tests:   99.715 seconds
size 61 loop 2
======================= Slow =========================
Time taken for tests:   131.321 seconds
======================= Fast =========================
Time taken for tests:   105.592 seconds
size 62 loop 2
======================= Slow =========================
Time taken for tests:   137.710 seconds
======================= Fast =========================
Time taken for tests:   110.730 seconds
size 63 loop 2
======================= Slow =========================
Time taken for tests:   141.979 seconds
======================= Fast =========================
Time taken for tests:   115.137 seconds
size 64 loop 2
======================= Slow =========================
Time taken for tests:   148.329 seconds
======================= Fast =========================
Time taken for tests:   120.773 seconds
size 65 loop 2
======================= Slow =========================
Time taken for tests:   154.765 seconds
======================= Fast =========================
Time taken for tests:   125.679 seconds
size 66 loop 2
======================= Slow =========================
Time taken for tests:   161.197 seconds
======================= Fast =========================
Time taken for tests:   129.703 seconds
size 67 loop 2
======================= Slow =========================
Time taken for tests:   166.791 seconds
======================= Fast =========================
Time taken for tests:   134.449 seconds
size 68 loop 2
======================= Slow =========================
Time taken for tests:   169.620 seconds
======================= Fast =========================
Time taken for tests:   137.867 seconds
size 69 loop 2
======================= Slow =========================
Time taken for tests:   178.016 seconds
======================= Fast =========================
Time taken for tests:   142.641 seconds
size 70 loop 2
======================= Slow =========================
Time taken for tests:   182.810 seconds
======================= Fast =========================
Time taken for tests:   148.905 seconds
size 71 loop 2
======================= Slow =========================
Time taken for tests:   190.160 seconds
======================= Fast =========================
Time taken for tests:   153.615 seconds
size 72 loop 2
======================= Slow =========================
Time taken for tests:   197.732 seconds
======================= Fast =========================
Time taken for tests:   161.120 seconds
size 73 loop 2
======================= Slow =========================
Time taken for tests:   205.920 seconds
======================= Fast =========================
Time taken for tests:   166.899 seconds
size 74 loop 2
======================= Slow =========================
Time taken for tests:   212.493 seconds
======================= Fast =========================
Time taken for tests:   173.954 seconds
size 75 loop 2
======================= Slow =========================
Time taken for tests:   247.327 seconds
======================= Fast =========================
Time taken for tests:   202.784 seconds
size 76 loop 2
======================= Slow =========================
Time taken for tests:   256.267 seconds
======================= Fast =========================
Time taken for tests:   209.747 seconds
size 77 loop 2
======================= Slow =========================
Time taken for tests:   263.610 seconds
======================= Fast =========================
Time taken for tests:   219.671 seconds
size 78 loop 2
======================= Slow =========================
Time taken for tests:   275.869 seconds
======================= Fast =========================
Time taken for tests:   226.335 seconds
size 79 loop 2
======================= Slow =========================
Time taken for tests:   283.874 seconds
======================= Fast =========================
Time taken for tests:   233.446 seconds
size 80 loop 2
======================= Slow =========================
Time taken for tests:   293.773 seconds
======================= Fast =========================
Time taken for tests:   242.365 seconds
size 81 loop 2
======================= Slow =========================
Time taken for tests:   306.506 seconds
======================= Fast =========================
Time taken for tests:   252.547 seconds
size 82 loop 2
======================= Slow =========================
Time taken for tests:   316.492 seconds
======================= Fast =========================
Time taken for tests:   259.494 seconds
size 83 loop 2
======================= Slow =========================
Time taken for tests:   323.944 seconds
======================= Fast =========================
Time taken for tests:   261.032 seconds
size 84 loop 2
======================= Slow =========================
Time taken for tests:   333.615 seconds
======================= Fast =========================
Time taken for tests:   272.741 seconds
size 85 loop 2
======================= Slow =========================
Time taken for tests:   343.955 seconds
======================= Fast =========================
Time taken for tests:   281.832 seconds
size 86 loop 2
======================= Slow =========================
Time taken for tests:   361.009 seconds
======================= Fast =========================
Time taken for tests:   293.662 seconds
size 87 loop 2
======================= Slow =========================
Time taken for tests:   369.533 seconds
======================= Fast =========================
Time taken for tests:   305.166 seconds
size 88 loop 2
======================= Slow =========================
Time taken for tests:   382.069 seconds
======================= Fast =========================
Time taken for tests:   314.244 seconds
size 89 loop 2
======================= Slow =========================
Time taken for tests:   393.064 seconds
======================= Fast =========================
Time taken for tests:   325.981 seconds
size 90 loop 2
======================= Slow =========================
Time taken for tests:   407.492 seconds
======================= Fast =========================
Time taken for tests:   339.055 seconds
size 91 loop 2
======================= Slow =========================
Time taken for tests:   419.396 seconds
======================= Fast =========================
Time taken for tests:   351.393 seconds
size 92 loop 2
======================= Slow =========================
Time taken for tests:   389.561 seconds
======================= Fast =========================
Time taken for tests:   321.377 seconds
size 93 loop 2
======================= Slow =========================
Time taken for tests:   396.476 seconds
======================= Fast =========================
Time taken for tests:   322.772 seconds
size 94 loop 2
======================= Slow =========================
Time taken for tests:   410.164 seconds
======================= Fast =========================
Time taken for tests:   333.572 seconds
size 95 loop 2
======================= Slow =========================
Time taken for tests:   448.111 seconds
======================= Fast =========================
Time taken for tests:   373.359 seconds
size 96 loop 2
======================= Slow =========================
Time taken for tests:   460.533 seconds
======================= Fast =========================
Time taken for tests:   386.070 seconds
size 97 loop 2
======================= Slow =========================
Time taken for tests:   474.407 seconds
======================= Fast =========================
Time taken for tests:   396.709 seconds
size 98 loop 2
======================= Slow =========================
Time taken for tests:   490.087 seconds
======================= Fast =========================
Time taken for tests:   410.683 seconds
size 99 loop 2
======================= Slow =========================
Time taken for tests:   502.691 seconds
======================= Fast =========================
Time taken for tests:   422.452 seconds
size 100 loop 2
======================= Slow =========================
Time taken for tests:   518.889 seconds
======================= Fast =========================
Time taken for tests:   430.753 seconds
size 40 loop 3
======================= Slow =========================
Time taken for tests:   72.413 seconds
======================= Fast =========================
Time taken for tests:   62.345 seconds
size 41 loop 3
======================= Slow =========================
Time taken for tests:   64.791 seconds
======================= Fast =========================
Time taken for tests:   54.017 seconds
size 42 loop 3
======================= Slow =========================
Time taken for tests:   81.809 seconds
======================= Fast =========================
Time taken for tests:   67.416 seconds
size 43 loop 3
======================= Slow =========================
Time taken for tests:   72.761 seconds
======================= Fast =========================
Time taken for tests:   61.259 seconds
size 44 loop 3
======================= Slow =========================
Time taken for tests:   97.830 seconds
======================= Fast =========================
Time taken for tests:   77.060 seconds
size 45 loop 3
======================= Slow =========================
Time taken for tests:   83.148 seconds
======================= Fast =========================
Time taken for tests:   68.869 seconds
size 46 loop 3
======================= Slow =========================
Time taken for tests:   88.586 seconds
======================= Fast =========================
Time taken for tests:   69.546 seconds
size 47 loop 3
======================= Slow =========================
Time taken for tests:   94.863 seconds
======================= Fast =========================
Time taken for tests:   74.653 seconds
size 48 loop 3
======================= Slow =========================
Time taken for tests:   102.252 seconds
======================= Fast =========================
Time taken for tests:   78.423 seconds
size 49 loop 3
======================= Slow =========================
Time taken for tests:   109.011 seconds
======================= Fast =========================
Time taken for tests:   84.050 seconds
size 50 loop 3
======================= Slow =========================
Time taken for tests:   114.185 seconds
======================= Fast =========================
Time taken for tests:   88.995 seconds
size 51 loop 3
======================= Slow =========================
Time taken for tests:   118.973 seconds
======================= Fast =========================
Time taken for tests:   93.076 seconds
size 52 loop 3
======================= Slow =========================
Time taken for tests:   122.491 seconds
======================= Fast =========================
Time taken for tests:   97.667 seconds
size 53 loop 3
======================= Slow =========================
Time taken for tests:   128.356 seconds
======================= Fast =========================
Time taken for tests:   102.880 seconds
size 54 loop 3
======================= Slow =========================
Time taken for tests:   136.769 seconds
======================= Fast =========================
Time taken for tests:   108.128 seconds
size 55 loop 3
======================= Slow =========================
Time taken for tests:   142.352 seconds
======================= Fast =========================
Time taken for tests:   114.298 seconds
size 56 loop 3
======================= Slow =========================
Time taken for tests:   153.325 seconds
======================= Fast =========================
Time taken for tests:   121.522 seconds
size 57 loop 3
======================= Slow =========================
Time taken for tests:   160.228 seconds
======================= Fast =========================
Time taken for tests:   126.895 seconds
size 58 loop 3
======================= Slow =========================
Time taken for tests:   167.898 seconds
======================= Fast =========================
Time taken for tests:   132.790 seconds
size 59 loop 3
======================= Slow =========================
Time taken for tests:   175.131 seconds
======================= Fast =========================
Time taken for tests:   136.553 seconds
size 60 loop 3
======================= Slow =========================
Time taken for tests:   180.363 seconds
======================= Fast =========================
Time taken for tests:   144.723 seconds
size 61 loop 3
======================= Slow =========================
Time taken for tests:   187.869 seconds
======================= Fast =========================
Time taken for tests:   152.740 seconds
size 62 loop 3
======================= Slow =========================
Time taken for tests:   195.600 seconds
======================= Fast =========================
Time taken for tests:   158.653 seconds
size 63 loop 3
======================= Slow =========================
Time taken for tests:   203.765 seconds
======================= Fast =========================
Time taken for tests:   165.370 seconds
size 64 loop 3
======================= Slow =========================
Time taken for tests:   211.866 seconds
======================= Fast =========================
Time taken for tests:   172.564 seconds
size 65 loop 3
======================= Slow =========================
Time taken for tests:   220.381 seconds
======================= Fast =========================
Time taken for tests:   180.309 seconds
size 66 loop 3
======================= Slow =========================
Time taken for tests:   229.449 seconds
======================= Fast =========================
Time taken for tests:   183.556 seconds
size 67 loop 3
======================= Slow =========================
Time taken for tests:   235.981 seconds
======================= Fast =========================
Time taken for tests:   190.826 seconds
size 68 loop 3
======================= Slow =========================
Time taken for tests:   246.834 seconds
======================= Fast =========================
Time taken for tests:   198.316 seconds
size 69 loop 3
======================= Slow =========================
Time taken for tests:   254.942 seconds
======================= Fast =========================
Time taken for tests:   206.792 seconds
size 70 loop 3
======================= Slow =========================
Time taken for tests:   266.018 seconds
======================= Fast =========================
Time taken for tests:   216.099 seconds
size 71 loop 3
======================= Slow =========================
Time taken for tests:   276.697 seconds
======================= Fast =========================
Time taken for tests:   225.877 seconds
size 72 loop 3
======================= Slow =========================
Time taken for tests:   286.690 seconds
======================= Fast =========================
Time taken for tests:   234.688 seconds
size 73 loop 3
======================= Slow =========================
Time taken for tests:   299.925 seconds
======================= Fast =========================
Time taken for tests:   247.128 seconds
size 74 loop 3
======================= Slow =========================
Time taken for tests:   313.841 seconds
======================= Fast =========================
Time taken for tests:   255.707 seconds
size 75 loop 3
======================= Slow =========================
Time taken for tests:   362.107 seconds
======================= Fast =========================
Time taken for tests:   298.569 seconds
size 76 loop 3
======================= Slow =========================
Time taken for tests:   375.214 seconds
======================= Fast =========================
Time taken for tests:   311.927 seconds
size 77 loop 3
======================= Slow =========================
Time taken for tests:   390.008 seconds
======================= Fast =========================
Time taken for tests:   323.798 seconds
size 78 loop 3
======================= Slow =========================
Time taken for tests:   404.656 seconds
======================= Fast =========================
Time taken for tests:   323.381 seconds
size 79 loop 3
======================= Slow =========================
Time taken for tests:   415.283 seconds
======================= Fast =========================
Time taken for tests:   336.688 seconds
size 80 loop 3
======================= Slow =========================
Time taken for tests:   432.296 seconds
======================= Fast =========================
Time taken for tests:   352.178 seconds
size 81 loop 3
======================= Slow =========================
Time taken for tests:   448.186 seconds
======================= Fast =========================
Time taken for tests:   368.489 seconds
size 82 loop 3
======================= Slow =========================
Time taken for tests:   462.133 seconds
======================= Fast =========================
Time taken for tests:   380.490 seconds
size 83 loop 3
======================= Slow =========================
Time taken for tests:   476.550 seconds
======================= Fast =========================
Time taken for tests:   396.504 seconds




"""

# Regular expression patterns
size_pattern = re.compile(r"size (\d+) loop (\d+)")
time_pattern = re.compile(r"Time taken for tests:\s+(\d+\.\d+) seconds")

# Parse the data
lines = data.strip().split('\n')
results = []
for i in range(0, len(lines), 5):
    size_match = size_pattern.search(lines[i])
    slow_time_match = time_pattern.search(lines[i + 2])
    fast_time_match = time_pattern.search(lines[i + 4])
    if size_match and slow_time_match and fast_time_match:
        size = int(size_match.group(1))
        loop = int(size_match.group(2))
        slow_time = float(slow_time_match.group(1))
        fast_time = float(fast_time_match.group(1))
        div_percent = ((slow_time - fast_time) / fast_time) * 100
        results.append((size, loop, div_percent))

# Print the results
for result in results:
    size, loop, div_percent = result
    print(f"Size: {size}, Loop: {loop}, Diff Percent: {div_percent:.2f}%")
