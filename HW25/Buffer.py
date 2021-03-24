class Buffer:
    def __init__(self):
        self.nums = []

    def add(self, *a):
        self.nums += a
        while len(self.nums) >= 5:
            print(sum(self.nums[:5]))
            self.nums = self.nums[5:]

    def get_current_part(self):
        return self.nums


buf = Buffer()
buf.add(3, 1, 2, 1, 4, 1, 1)
buf.get_current_part()
buf.add(1)
buf.get_current_part()
buf.add(12, 1, 2, 1, 3)
buf.get_current_part()
buf.add(1, 45)
buf.get_current_part()