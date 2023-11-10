class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        if isinstance(hall, Hall):
            cls.__hall_list.append(hall)
        else:
            print("Invalid Hall object")


class Hall:

    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)

        # create 2d list

        self._seats[id] = []
        for i in range(self._rows):
            row = [0] * self._cols
            self._seats[id].append(row)

        # print(self._rows)
        # for i in range(self._rows):
        #     for j in range(self._cols):
        #         print( end=' * ')
        #     print()

    def book_seats(self, id, seat_list):
        # Check if the given id is valid or not.
        if id not in self._seats:
            print(f"Invalid show ID: {id}")
            return

        for row, col in seat_list:
            # Check seat validity
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print(f"Invalid seat: ({row}, {col})")
                continue

            if self._seats[id][row][col] == 1:
                print(f"Seat ({row}, {col}) is already booked")
            else:
                self._seats[id][row][col] = 1
                print(f"Booked seat ({row}, {col}) for show {id}")

    def view_show_list(self):
        for show in self._show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        # Check if the given id is valid or not.

        if id not in self._seats:
            print(f'Invalid show ID: {id}')
            return

        # Show all available seats as tuples
        for row in range(self._rows):
            for col in range(self._cols):
                # check this seat is bocked or not.
                if self._seats[id][row][col] == 0:
                    print(f"Seat: {row, col}")

        # Show all available seats in matrix form.
        print("\nUpdate seats matrix\n")
        for i in self._seats[id]:
            print(i)


if __name__ == "__main__":
    hall1 = Hall(5, 7, 1)
    hall1.entry_show(1, 'avengers', '5:30 PM')
    hall1.entry_show(2, "Moon knight", "8:00 PM")
    hall1.entry_show(3, "The Batman", "9:00 PM")

    current_hall = hall1
    while True:
        print('1. View all shows')
        print('2. View available seats')
        print('3. Book ticket')
        print("4. Exit")
        op = int(input("Enter option: "))

        match op:
            case 1:
                print(
                    '\n---------------------- View all shows -------------------------\n'
                )
                current_hall.view_show_list()
            case 2:
                show_id = int(input("Enter show ID: "))
                print(
                    '\n---------------------- View available seats -------------------------\n'
                )
                current_hall.view_available_seats(show_id)
            case 3:
                show_id = int(input("Enter the show id: "))
                num_tickets = int(input("Number of Tickets?: "))
                if num_tickets < 0:
                    print(f'{num_tickets} Ticket number you provided is too low, minimum ticket number is 1')
                ticket_list = [(int(input("Enter Seat Row: ")),
                                int(input("Enter Seat Col: ")))
                               for i in range(num_tickets)]
                print(
                    '\n--------------------------------------------------------\n'
                )
                current_hall.book_seats(show_id, ticket_list)
            case 4:
                break
        print('\n--------------------------------------------------------')
