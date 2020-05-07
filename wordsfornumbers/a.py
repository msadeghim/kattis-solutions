import re
import sys


ls = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ls2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

mp = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
      8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
      15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
      30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

for i in range(8):
    for j in range(9):
        mp[(i+2) * 10 + (j+1)] = ls2[i] + '-' + ls[j]


for line in sys.stdin:
    print(re.sub(r'\d+', lambda m: mp[int(m.group())], line).capitalize())
