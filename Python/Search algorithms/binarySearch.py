binarySearch = lambda a, n, b = 0, t = None: b if a[b] == n else -1 if b == t else binarySearch(a, n, b, len(a) - 1) if t == None else binarySearch(a, n, b, b + int(((t - b) / 2))) if n <= a[b + int(((t - b) / 2))] else binarySearch(a, n, b + int(((t - b) / 2)) + 1, t)