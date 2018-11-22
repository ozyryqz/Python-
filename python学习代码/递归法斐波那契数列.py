def fobi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fobi(n - 1) + fobi(n - 2)
    
