nh, nm, ns = map(int, input().split(":"))

sh, sm, ss = map(int, input().split(":"))


n = nh*60*60 + nm*60 + ns
s = sh*60*60 + sm*60 + ss

rst = s - n

h = rst // 3600

m = (rst % 3600) // 60

s = (rst % 3600) % 60

if h < 0:
    h = str(24 + h)
elif h < 10:
    h = '0' + str(h)

if m < 10:
    m = '0' + str(m)

if s < 10:
    s = '0' + str(s)

h = str(h)
m = str(m)
s = str(s)

print(h + ":" + m + ":" + s)

