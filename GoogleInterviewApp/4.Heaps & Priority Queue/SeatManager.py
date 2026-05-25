# https://leetcode.com/problems/seat-reservation-manager/
import heapq


class SeatManager:

    def __init__(self, n: int):
        self.seats = [i for i in range(1, n+1)]

    def reserve(self) -> int:
        seat_number = heapq.heappop(self.seats)
        return seat_number

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)

seat_manager = SeatManager(5)
seat_manager.reserve()
seat_manager.reserve()
seat_manager.unreserve(2)
seat_manager.reserve()
seat_manager.reserve()
seat_manager.reserve()
seat_manager.reserve()
seat_manager.unreserve(5)