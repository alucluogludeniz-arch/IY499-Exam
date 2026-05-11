'''
Programmer: Deniz Alucluoglu
Date: 2026
Program: Data Analysis Program

Description:
This program allows the user to enter numerical data,
save the data into a CSV file, read the data back,
display statistics, group data into classes,
search and sort values, create graphs,
and save reports to a text file.
'''

import pandas as pd
import matplotlib.pyplot as plt


# ---------- Function: Enter Data ----------
def enter_data():
    """
    Allows user to enter numerical data
    and saves it into data.csv
    """

    numbers = []

    print("\nEnter numbers one at a time.")
    print("Type 'done' to finish.\n")

    while True:

        user_input = input("Enter number: ")

        if user_input.lower() == "done":
            break

        try:
            number = float(user_input)
            numbers.append(number)

        except ValueError:
            print("Invalid input. Please enter a number.")

    if len(numbers) == 0:
        print("No data entered.")
        return

    data = pd.DataFrame(numbers, columns=["Values"])

    try:
        data.to_csv("data.csv", index=False)
        print("Data successfully saved to data.csv")

    except Exception as error:
        print("Error saving data:", error)


# ---------- Function: Read Data ----------
def read_data():
    """
    Reads data from CSV file.
    """

    try:

        data = pd.read_csv("data.csv")

        if data.empty:
            print("Error: CSV file is empty.")
            return None

        return data

    except FileNotFoundError:
        print("Error: data.csv not found.")
        return None

    except Exception as error:
        print("Error reading file:", error)
        return None


# ---------- Function: Show Statistics ----------
def show_statistics(data):
    """
    Displays statistics.
    """

    if data is None:
        return

    values = data.iloc[:, 0]

    print("\n===== DATA TABLE =====")
    print(data)

    print("\n===== STATISTICS =====")
    print("Count:", values.count())
    print("Mean:", round(values.mean(), 2))
    print("Median:", values.median())
    print("Minimum:", values.min())
    print("Maximum:", values.max())
    print("Standard Deviation:", round(values.std(), 2))


# ---------- Function: Group Data Into Classes ----------
def group_data(data):
    """
    Groups data into classes using user class width.
    """

    if data is None:
        return

    values = data.iloc[:, 0]

    try:

        class_width = float(input("Enter class width: "))

        if class_width <= 0:
            print("Class width must be greater than 0.")
            return

        minimum = values.min()
        maximum = values.max()

        bins = []

        current = minimum

        while current <= maximum:
            bins.append(current)
            current += class_width

        bins.append(maximum + class_width)

        grouped = pd.cut(values, bins=bins)

        frequency = grouped.value_counts().sort_index()

        print("\n===== GROUPED DATA =====")
        print(frequency)

    except ValueError:
        print("Invalid class width.")


# ---------- Function: Draw Histogram ----------
def draw_histogram(data):
    """
    Draws histogram graph.
    """

    if data is None:
        return

    values = data.iloc[:, 0]

    plt.hist(values, bins=10, edgecolor='black')

    plt.title("Histogram")
    plt.xlabel("Values")
    plt.ylabel("Frequency")

    plt.show()


# ---------- Function: Draw Line Graph ----------
def draw_line_graph(data):
    """
    Draws line graph.
    """

    if data is None:
        return

    values = data.iloc[:, 0]

    plt.plot(values, marker='o')

    plt.title("Line Graph")
    plt.xlabel("Index")
    plt.ylabel("Values")

    plt.grid(True)

    plt.show()


# ---------- Function: Sort Data ----------
def sort_data(data):
    """
    Sorts data in ascending order.
    """

    if data is None:
        return

    values = data.iloc[:, 0]

    sorted_values = values.sort_values()

    print("\n===== SORTED DATA =====")
    print(sorted_values.to_string(index=False))


# ---------- Function: Search Value ----------
def search_value(data):
    """
    Searches for a value in dataset.
    """

    if data is None:
        return

    try:

        target = float(input("Enter value to search: "))

        values = data.iloc[:, 0]

        if target in values.values:
            print("Value found in dataset.")
        else:
            print("Value not found.")

    except ValueError:
        print("Invalid number entered.")


# ---------- Function: Save Report ----------
def save_report(data):
    """
    Saves statistics into report.txt
    """

    if data is None:
        return

    values = data.iloc[:, 0]

    try:

        with open("report.txt", "w") as file:

            file.write("===== DATA REPORT =====\n")
            file.write(f"Count: {values.count()}\n")
            file.write(f"Mean: {round(values.mean(), 2)}\n")
            file.write(f"Median: {values.median()}\n")
            file.write(f"Minimum: {values.min()}\n")
            file.write(f"Maximum: {values.max()}\n")
            file.write(f"Standard Deviation: {round(values.std(), 2)}\n")

        print("Report saved to report.txt")

    except Exception as error:
        print("Error writing report:", error)


# ---------- Main Menu ----------
def main():

    while True:

        print("\n===================================")
        print("      DATA ANALYSIS PROGRAM")
        print("===================================")
        print("1 - Enter Data")
        print("2 - Show Statistics")
        print("3 - Group Data Into Classes")
        print("4 - Draw Histogram")
        print("5 - Draw Line Graph")
        print("6 - Sort Data")
        print("7 - Search Value")
        print("8 - Save Report")
        print("9 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            enter_data()

        elif choice == "2":
            data = read_data()
            show_statistics(data)

        elif choice == "3":
            data = read_data()
            group_data(data)

        elif choice == "4":
            data = read_data()
            draw_histogram(data)

        elif choice == "5":
            data = read_data()
            draw_line_graph(data)

        elif choice == "6":
            data = read_data()
            sort_data(data)

        elif choice == "7":
            data = read_data()
            search_value(data)

        elif choice == "8":
            data = read_data()
            save_report(data)

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# ---------- Run Program ----------
main()
