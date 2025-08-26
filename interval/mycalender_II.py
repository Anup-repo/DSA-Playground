class MyCalendarTwo:

    def __init__(self):
        self.overall_bookings = []
        self.double_bookings = []

    def isOverlap(self, first, second, start, end):
        return max(start, first) < min(end, second)

    def overlapRegion(self, first, second, start, end):
        return max(start, first), min(end, second)

    def book(self, start: int, end: int) -> bool:
        # check if triple booking is created or not
        for s, e in self.double_bookings:
            if self.isOverlap(s, e, start, end):
                return False

        # check if double booking is created or not
        for s, e in self.overall_bookings:
            if self.isOverlap(s, e, start, end):
                self.double_bookings.append(self.overlapRegion(s, e, start, end))

        self.overall_bookings.append((start, end))
        return True


# https://leetcode.com/problems/my-calendar-ii/
# example 1
cal = MyCalendarTwo()
print(cal.book(10, 20))
print(cal.book(50, 60))
print(cal.book(10, 40))
print(cal.book(5, 15))
print(cal.book(5, 10))
print(cal.book(25, 55))
