#!/usr/bin/env python3

## Note - this is python3 not python2
## Normally I write python2 but I wanted subprocess.DEVNULL and it seemed like a good time
## to take the plunge

import subprocess as s
import re

l2process = {
  "haskell": ["./primes"],
  "python": ["python", "primes.py"],
  "c": ["./a.out"],
  "java": ["java", "Primes"]}

def measureTime(numPrimes, lang):
  cmd = ["time"] + l2process[lang] + [str(numPrimes)]
  with open(".timePrime_temp", "w") as f:
    result = s.check_output(cmd, stderr=f)
  with open(".timePrime_temp", "r") as f:
    t = readTimes(f.read())
  return t[0]

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

def main():
  powers = range(3)
  multiples = [1,2,5]
  numPrimes = [mult * 10 ** powr for powr in powers for mult in multiples]
  langs = {"haskell": [], "java": [], "c": [], "python": []}
  for lang, result in langs.items():
    for num in numPrimes:
      real = measureTime(num, lang)
      result.append(real)
  print(langs)


main()
