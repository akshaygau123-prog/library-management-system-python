import datetime

books = {}
issued_books = {}

def add_books():
    name = input("Enter book name: ")
    try:
        qty = int(input("Enter quantity: "))
    except:
        print("Invalid input")
        return

    books[name] = books.get(name, 0) + qty
    print(f"{qty} copies of {name} added.\n")


def show_books():
    if not books:
        print("No books available\n")
        return
    for book, qty in books.items():
        print(f"{book} -> {qty} copies")
    print()


def issue_books():
    show_books()
    name = input("Enter book name: ")

    if name not in books or books[name] == 0:
        print("Book not available\n")
        return

    student = input("Enter student name: ")
    duration = int(input("Enter duration (days): "))

    issue_date = datetime.date.today()

    if name not in issued_books:
        issued_books[name] = []

    issued_books[name].append({
        "student": student,
        "issue_date": issue_date,
        "duration": duration
    })

    books[name] -= 1

    print(f"{name} issued to {student} on {issue_date}\n")


def return_book():
    name = input("Enter book name: ")

    if name not in issued_books or len(issued_books[name]) == 0:
        print("No record found\n")
        return

    student = input("Enter student name: ")

    for record in issued_books[name]:
        if record["student"] == student:

            return_date = datetime.date.today()
            issue_date = record["issue_date"]
            duration = record["duration"]

            days_used = (return_date - issue_date).days

            fine = 0
            if days_used > duration:
                extra_days = days_used - duration
                weeks_late = (extra_days // 7) + 1
                fine = weeks_late * 20

            books[name] += 1
            issued_books[name].remove(record)

            print("\nReturn Details:")
            print(f"Student: {student}")
            print(f"Issued on: {issue_date}")
            print(f"Returned on: {return_date}")
            print(f"Days used: {days_used}")

            if fine > 0:
                print(f"Fine: ₹{fine}")
            else:
                print("Returned on time")

            print("Book returned successfully\n")
            return

    print("Student record not found\n")


def library():
    while True:
        print("1. Add Books")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Invalid input\n")
            continue

        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank you!")
            break
        else:
            print("Invalid choice\n")


library()