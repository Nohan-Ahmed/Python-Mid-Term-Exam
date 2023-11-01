class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:

    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self._show_list.append((id, movie_name, time))
        self._seats[id] = [[0 for _ in range(self._cols)]
                           for _ in range(self._rows)]

    def book_seats(self, id, seat_list):
        if id not in self._seats:
            print('Invalid show ID')

        for row, col in seat_list:
            if not (1 <= row <= self._rows) or not (1 <= col <= self._cols):
                print("Invalid seat")

            if self._seats[id][row - 1][col - 1] == 0:
                self._seats[id][row - 1][col - 1] = 1
            else:
                print("Seat is already booked")

    def view_show_list(self):
        for i in self.show_list:
            print(i)

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid show ID")
        try:
            for i in self._seats[id]:
                print(i)
        except Exception as e:
            print("Invalid show ID")


hall1 = Hall(5, 6, 1)

hall1.entry_show(121, "Moon knight", "10:00 AM")

hall1.book_seats(121, [(1, 2)])

hall1.view_available_seats(121)
