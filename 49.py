from collections import defaultdict

a = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = defaultdict(list)

for i in a:
    result[''.join(sorted(i))].append(i)

print(list(result.values()))