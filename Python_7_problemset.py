#!/usr/bin/env python
import re

with open("Python_07_nobody.txt", "r") as Python_07_read, open("Alice.txt", "w") as Python_07_write:
  for line in Python_07_read:
    line = line.rstrip()
    list_of_matches =   [(m.start(), m.end()) for m in re.finditer(r"Nobody", line)]
    #print(list_of_matches)
    line = re.sub(r"Nobody", "Alice", line)
    print(line)
    Python_07_write.write(f"{line}")
