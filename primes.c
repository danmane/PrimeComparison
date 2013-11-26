#include <stdio.h>
#include <stdlib.h>

int isPrime(int n, int primes[]){
    int p;
    for (int i=0; ; i++){
        p = primes[i];
        if (n % p == 0){
            return 0;
        }
        if (p * p > n) {
            return 1;
        }
    }
}

int * primes(int num){
    int *primes = malloc(sizeof(int) * num);
    primes[0] = 2; primes[1] = 3;
    int found = 2;
    int i = 2;
    int next;
    while (found < num) {
        next = 6 * (i>>1) + (i & 1) * 2 - 1;
        if (isPrime(next, primes)){
            primes[found] = next;
            found++;
        }
        i++;
    }
    return primes;
}

long primesum(int num){
    int *list_of_primes;
    list_of_primes = primes(num);
    int i;
    long sum = 0;
    for (i=0; i<num; i++){
        sum+=list_of_primes[i];
    }
    return sum;
}

int main(int argc, char *argv[]){
    int num;
    num = atoi(argv[1]) * 1000;
    if (num == 0){ num = 100000;}
    long x = primesum(num);
    printf("%ld\n", x);
}
