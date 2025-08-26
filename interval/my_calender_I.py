class MyCalendar:

    def __init__(self):
        self.bookings = []

    def isOverlap(self, first, second, start, end):
        return max(start, first) < min(end, second)

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if self.isOverlap(s, e, start, end):
                return False
        self.bookings.append((start, end))
        return True

cal = MyCalendar()
print(cal.book(10, 20))  # True cal.book(10, 20)  # True
print(cal.book(15, 25))  # False cal.book(5, 9)  # Should be True, but your code will return False
print(cal.book(20, 30))  # True cal.book(25, 30)