class Primes {
    private static boolean isPrime(int n, int[] primes) {
        int i = 0;
        while (true) {
            int p = primes[i];
            if ((n%p) == 0) {
                return false;
            }
            if (p*p > n) {
                return true;
            }
            i++;
        }
    }
    private static int[] primes(int n) {
        int[] result = new int[n];
        result[0] = 2; result[1] = 3;
        int found = 2;
        int i = 2;
        int next;
        while (found < n) {
            next = 6 * (i/2) + 2 * (i%2) - 1;
            if (Primes.isPrime(next, result)) {
                result[found] = next;
                found++;
            }
            i++;
        }
        return result;
    }
    private static long primesum(int n) {
        long sum = 0;
        int[] primelist = Primes.primes(n);
        for (int i=0; i<n; i++){
            sum += primelist[i];
        }
        return sum;
    }
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]) * 1000;
        System.out.println(primesum(n));
    }
}
