module Main (main) where
import GHC.Environment

primes = 2:3:[n | x<-[1..], y<-[-1,1], let n=6*x+y, isPrime n]
isPrime n = all (\x -> n `mod` x /= 0) $ takeWhile (\x -> x*x <= n) primes

getNumPrimesOrUseDefault :: [String] -> Int
getNumPrimesOrUseDefault [] = 100000
getNumPrimesOrUseDefault (x:xs) = 1000 * read x

sumPrimes :: Int -> Int
sumPrimes n = sum $ take n primes

main = do
    args <- getFullArgs
    let n = getNumPrimesOrUseDefault args
    print $ sumPrimes n
