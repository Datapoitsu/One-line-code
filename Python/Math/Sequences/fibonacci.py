fibonacci = lambda n,i = 1,h = [0,1] : fibonacci(n,i+1,[h[1],h[0]+h[1]]) if i < n else h[n-i+1]