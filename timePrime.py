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
  timestr = timestr.strip()
  valid = re.match("\d+\.\d\d real +\d+\.\d\d user +\d+\.\d\d sys", timestr)
  assert(valid != None)
  times = re.findall("\d+\.?\d+", timestr)
  real = float(times[0])
  user = float(times[1])
  sys = float(times[2])
  return (real, user, sys)

def timeLang(primeSequence, lang):
  result = []
  for p in primeSequence:
    try:
      r = measureTime(p, lang)
      print(lang + ", " + str(p) +": " + str(r))
      result.append(r)
      if r > 3600:
        break
    except (AssertionError, s.CalledProcessError) as e:
      print("Failed on " + lang + "," + str(p))
      print(e)
      result.append("NaN")
      break
  return result

def main():
  powers = range(6)
  multiples = [1,2,5]
  numPrimesInThousands = [mult * 10 ** powr for powr in powers for mult in multiples]
  numPrimes = [n * 1000 for n in numPrimesInThousands]
  langs = ["c", "python", "java", "haskell"]
  # The order is significant, since first result is treated as canonical by the cache.
  # Since python turns everything into bigints, as necessary, it won't suffer from overflow
  # errors, so it should run first.
  results = {"numPrimes": numPrimes}
  for lang in langs:
    results[lang] = timeLang(numPrimesInThousands, lang)
  with open("results.json", "w") as f:
    json.dump(results, f)


main()
