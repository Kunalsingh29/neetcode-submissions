from collections import defaultdict

class TimeMap:

    def __init__(self):
        # Dictionary to store: key -> list of (timestamp, value) pairs
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the (timestamp, value) to the list for the key
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        left, right = 0, len(values) - 1
        res = ""

        while left <= right:
            mid = left + (right - left) // 2
            mid_time, mid_value = values[mid]

            if mid_time == timestamp:
                return mid_value
            elif mid_time < timestamp:
                res = mid_value
                left = mid + 1
            else:
                right = mid - 1

        return res


# Example usage:
# obj = TimeMap()
# obj.set("foo", "bar", 1)
# print(obj.get("foo", 1))   # Output: "bar"
# print(obj.get("foo", 3))   # Output: "bar"
# obj.set("foo", "bar2", 4)
# print(obj.get("foo", 4))   # Output: "bar2"
# print(obj.get("foo", 5))   # Output: "bar2"
