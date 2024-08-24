class Star_Cinema:
    hall_list = []
    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = [] 
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {self._hall_no: [['free' for _ in range(cols)] for _ in range(rows)]}
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self._show_list.append((id, movie_name, time))
        self._seats[id] = [['free' for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, show_id, seat_list):
        show_exists = any(show_id == show[0] for show in self._show_list)
        if not show_exists:
           print(f"Show with ID {show_id} does not exist.")
        for row, col in seat_list:
            if not (0 <= row < self._rows and 0 <= col < self._cols):
               print(f"Seat ({row}, {col}) is out of range.")
            if self._seats[show_id][row][col] != 'free':
               print(f"Seat ({row}, {col}) is already booked.")
            self._seats[show_id][row][col] = 'booked'

    def view_show_list(self):
        return self._show_list

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print(f"Show with ID {show_id} does not exist.")
        available_seats = []
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[show_id][row][col] == 'free':
                    available_seats.append((row, col))
        return available_seats

start=True
while start:
    hall1 = Hall(5, 5, 1)
    hall1.entry_show(101, "Superman", "12:00 PM")
    hall1.entry_show(102, "BatMan", "3:00 PM")
    hall2 = Hall(4,6,2)
    hall2.entry_show(201, "SpiderMan", "6:00 PM")
    while start:
        print("\nMenu:")
        print("1. View Show List")
        print("2. View Available Seats")
        print("3. Book Tickets")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            for hall in Star_Cinema.hall_list:
                shows = hall.view_show_list()
                for show in shows:
                    print(f"Hall {hall._hall_no}: ID {show[0]}, Movie {show[1]}, Time {show[2]}")  
        elif choice == '2':
            show_id = int(input("Enter show ID: "))
            try:
                for hall in Star_Cinema.hall_list:
                    available_seats = hall.view_available_seats(show_id)
                    if available_seats:
                        print(f"Available seats for show ID {show_id}: {available_seats}")
                        break
                else:
                    print("Show ID not found.")
            except ValueError as e:
                print(e)
        
        elif choice == '3':
            show_id = int(input("Enter show ID: "))
            seats_to_book = input("Enter seats to book (row,col) separated by commas (e.g., 0,1 1,2): ")
            seat_list = [tuple(map(int, seat.split(','))) for seat in seats_to_book.split()]
            try:
                for hall in Star_Cinema.hall_list:
                    hall.book_seats(show_id, seat_list)
                    print(f"Seats {seat_list} booked for show ID {show_id}.")
                    break
                else:
                    print("Show ID not found.")
            except:
                print("Error!")
        elif choice == '4':
            start=False
        else:
            print("Invalid choice. Please try again.")
