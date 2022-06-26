import re
from collections import Counter

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

a = Counter(words)

print(a.most_common(1)[0][0])