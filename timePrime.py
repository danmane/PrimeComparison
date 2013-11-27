#!/usr/bin/env python3

## Note - this is python3 not python2
## Normally I write python2 but I wanted subprocess.DEVNULL and it seemed like a good time
## to take the plunge

import subprocess as s
import re

def measureTime(numPrimes, lang, numRuns=1):
  l2process = {
    "haskell": ["./primes"],
    "python": ["python", "primes.py"],
    "c": ["./a.out"],
    "java": ["java", "Primes"],
  }
  cmd = ["time"] + l2process[lang] + [str(numPrimes)]
  times = (0,0,0)
  for i in range(numRuns):
    with open(".timePrime_temp", "w") as f:
      s.call(cmd, stdout=s.DEVNULL, stderr=f)
    with open(".timePrime_temp", "r") as f:
      t = readTimes(f.read())
      times = sumTriplet(times, t)
  times = divideTriplet(times, numRuns)
  return times[0]

def readTimes(timestr):
  times = re.findall("\d+\.?\d+", timestr)
  if len(times) != 3:
    print(times)
    print(timestr)
    assert False
  real = float(times[0])
  user = float(times[1])
  sys = float(times[2])
  return (real, user, sys)

def sumTriplet(a,b):
  return (a[0]+b[0], a[1]+b[1], a[2]+b[2])

def divideTriplet(a,div):
  return (a[0]/div, a[1]/div, a[2]/div)

def main():
  numPrimes = []
  for powr in [0,1]:
    for mult in [1,2,5]:
      numPrimes.append(mult * 10**powr)
  langs = {"haskell": [], "java": [], "c": [], "python": []}
  for lang, result in langs.items():
    for num in numPrimes:
      real = measureTime(num, lang)
      result.append(real)
  print(langs)


main()
