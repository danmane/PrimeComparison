def isPrime(n, plist):
    for p in plist:
        if n%p == 0: return False
        elif p*p > n: return True

def potentialPrimeGen():
    i=2
    while True:
        yield i//2 * 6 + i%2 * 2 - 1
        i+=1

def primes(nPrimes):
    primes = [2,3]
    for p in potentialPrimeGen():
        if isPrime(p, primes):
            primes.append(p)
        if len(primes) == nPrimes:
            return primes

def main():
    print sum(primes(1000))

main()
