#!/usr/bin/env python3

## Note - this is python3 not python2
## Normally I write python2 but I wanted subprocess.DEVNULL and it seemed like a good time
## to take the plunge

import subprocess as s
import re
import json

l2process = {
  "haskell": ["./primes"],
  "python": ["python", "primes.py"],
  "c": ["./a.out"],
  "java": ["java", "Primes"]}

cachedPrimes = {}

def allDigits(x):
  try:
    int(x)
    return True
  except ValueError:
    return False

def measureTime(numPrimes, lang):
  cmd = ["time"] + l2process[lang] + [str(numPrimes)]
  with open(".timePrime_temp", "w") as f:
    output = s.check_output(cmd, stderr=f)
    output = output.strip()
    try:
      output = int(output)
    except ValueError:
      print("Got non-digit output")
      print(output)
      raise AssertionError

    if numPrimes not in cachedPrimes:
      cachedPrimes[numPrimes] = output
    elif cachedPrimes[numPrimes] != output:
      print("Expected " + str(cachedPrimes[numPrimes]) + " got " + str(output))
      raise AssertionError

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

def timeLang(primeSequence, lang):
  result = []
  for p in primeSequence:
    try:
      r = measureTime(p, lang)
      result.append(r)
    except AssertionError as e:
      print("Failed on " + lang + "," + str(p))
      result.append("NaN")
      break
  return result

def main():
  powers = range(1)
  multiples = [1,2,5]
  numPrimes = [mult * 10 ** powr for powr in powers for mult in multiples]
  langs = ["python", "c", "java", "haskell"]
  results = {"numPrimes": numPrimes}
  for lang in langs:
    results[lang] = timeLang(numPrimes, lang)
  with open("results.json", "w") as f:
    json.dump(results, f)


main()
