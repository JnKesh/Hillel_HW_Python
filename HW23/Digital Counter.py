class Counter:
    def __init__(self, start, stop, pr_val):
        self.start = start
        self.stop = stop
        self.pr_val = pr_val
        if self.pr_val is None or self.pr_val < self.start or self.pr_val > self.stop:
            self.pr_val = self.start

    def check(self):
        if self.pr_val < self.stop:
            self.pr_val += 1
        return self.pr_val


a = int(input("set start value: "))
b = int(input("set stop value: "))
c = input("set present value: ")

if c == "":
    c = a
else:
    c = int(c)

if c < a:
    c = a
elif c > b:
    c = b

x = Counter(start=a, stop=b, pr_val=c)

print(c)
for _ in range(b - c):
    print(x.check())