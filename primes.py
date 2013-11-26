import sys

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
    try:
        n = int(sys.argv[1]) * 1000
    except:
        n = 100000
    print sum(primes(n))

main()
