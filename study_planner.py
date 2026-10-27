
def show_welcome():
    print("\n=== STUDENT STUDY PLANNER ===")
    print("Plan your day, one task at a time!")


def main():
    tasks = []

    while True:
        print("\n1. Add a study task")
        print("2. View tasks")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter your study task: ")
            tasks.append(task)
            print("Task added!")

        elif choice == "2":
            if tasks:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("No tasks added yet.")

        elif choice == "3":
            print("Good luck with your studies!")
            break

        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    show_welcome()
    main()
