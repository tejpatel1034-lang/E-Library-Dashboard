import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class LibraryDashboard:

    def __init__(self):
        self.data = None

    # Load and validate Data 
    def load_data(self, file_path=None):
        try:
            print("\nLoad Data Menu")
            print("1. Use default CSV file (library_transactions.csv)")
            print("2. Enter CSV file path manually")

            if file_path is None:
                try:
                    option = int(input("Enter choice: "))
                except ValueError:
                    print("Invalid input, please enter a number")
                    return False
            else:
                option = 1

            match option:
                case 1:
                    if file_path is None:
                        file_path = "C:/Users/tejpa/OneDrive/Documents/R & W Projects/Pr 10 E-Library-Dashboard/library_transactions.csv"
                    self.data = pd.read_csv(file_path)
                case 2:
                    file_path = input("Enter CSV file path: ")
                    self.data = pd.read_csv(file_path)
                case _:
                    print("Invalid choice")
                    return False

            # Required columns check
            required_columns = [
                "Transaction ID",
                "Date",
                "User ID",
                "Book Title",
                "Genre",
                "Borrowing Duration (Days)"
            ]
            for col in required_columns:
                if col not in self.data.columns:
                    print(f"Missing Column: {col}")
                    return False

            # Data cleaning
            self.data.dropna(inplace=True)
            self.data.drop_duplicates(inplace=True)
            self.data["Date"] = pd.to_datetime(self.data["Date"], errors='coerce')
            self.data = self.data.dropna(subset=["Date"])
            
            # Extra computed columns
            self.data["Frequent Borrower"] = self.data["User ID"].map(
                self.data["User ID"].value_counts()
            )
            self.data["Late Return"] = self.data["Borrowing Duration (Days)"].apply(lambda x: "Yes" if x > 14 else "No")

            print("Data loaded and cleaned successfully!")
            return True

        except Exception as e:
            print("Error loading file:", e)
            return False

    # Statistics
    def calculate_statistics(self):
        durations = np.array(self.data["Borrowing Duration (Days)"])
        avg_duration = np.mean(durations)
        std_duration = np.std(durations)
        most_borrowed = self.data["Book Title"].value_counts().idxmax()
        busiest_day = self.data["Date"].dt.day_name().value_counts().idxmax()

        print("\n Library Statistics ")
        print(f"Most Borrowed Book       : {most_borrowed}")
        print(f"Average Borrow Duration  : {round(avg_duration,2)} days")
        print(f"Borrow Duration Std Dev  : {round(std_duration,2)}")
        print(f"Busiest Day              : {busiest_day}")

    # Filter Transactions 
    def filter_transactions(self):
        print("\nFilter Options")
        print("1. Filter by Genre")
        print("2. Filter by Date Range")
        print("3. Filter by Borrowing Duration (>days)")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input!")
            return

        filtered = self.data.copy()

        if choice == 1:
            genre = input("Enter Genre: ")
            filtered = filtered[filtered["Genre"] == genre]

        elif choice == 2:
            start = input("Start Date (YYYY-MM-DD): ")
            end = input("End Date (YYYY-MM-DD): ")
            try:
                start = pd.to_datetime(start)
                end = pd.to_datetime(end)
            except:
                print("Invalid date format!")
                return
            filtered = filtered[(filtered["Date"] >= start) & (filtered["Date"] <= end)]

        elif choice == 3:
            try:
                days = int(input("Enter minimum borrowing days: "))
            except:
                print("Invalid input!")
                return
            filtered = filtered[filtered["Borrowing Duration (Days)"] >= days]

        else:
            print("Invalid choice")
            return

        print("\nFiltered Data (Top 5 rows):")
        print(filtered.head())
        save = input("Do you want to save filtered data to CSV? (y/n): ").lower()
        if save == "y":
            filtered.to_csv("filtered_transactions.csv", index=False)
            print("Filtered data saved as filtered_transactions.csv")

    #  Generate Report 
    def generate_report(self):
        total_transactions = len(self.data)
        unique_users = self.data["User ID"].nunique()
        top_books = self.data["Book Title"].value_counts().head(3)
        late_returns = self.data["Late Return"].value_counts().get("Yes",0)

        print("\n------ Library Report ------")
        print(f"Total Transactions : {total_transactions}")
        print(f"Unique Users       : {unique_users}")
        print(f"Late Returns (>14d): {late_returns}")
        print("\nTop 3 Borrowed Books:")
        print(top_books)

    # Visualizations 
    def visualize(self):
        while True:
            print("\n==== Visualization Menu ====")
            print("1. Bar Chart: Top 5 Most Borrowed Books")
            print("2. Line Chart: Borrowing Trends Over Months")
            print("3. Pie Chart: Distribution by Genre")
            print("4. Heatmap: Borrowing Activity by Day & Hour")
            print("5. Return to Main Menu")

            try:
                choice = int(input("Enter your choice: "))
            except:
                print("Invalid input!")
                continue

            match choice:
                case 1:
                    top_books = self.data["Book Title"].value_counts().head(5)
                    plt.figure(figsize=(8,5))
                    sns.barplot(x=top_books.index, y=top_books.values, palette="viridis")
                    plt.title("Top 5 Most Borrowed Books")
                    plt.xlabel("Book Title")
                    plt.ylabel("Borrow Count")
                    plt.xticks(rotation=45)
                    plt.show()

                case 2:
                    self.data["Month"] = self.data["Date"].dt.month
                    monthly = self.data.groupby("Month").size()
                    plt.figure(figsize=(8,5))
                    sns.lineplot(x=monthly.index, y=monthly.values, marker="o")
                    plt.title("Borrowing Trends Over Months")
                    plt.xlabel("Month")
                    plt.ylabel("Total Borrowings")
                    plt.show()

                case 3:
                    genre = self.data["Genre"].value_counts()
                    plt.figure(figsize=(6,6))
                    plt.pie(genre, labels=genre.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
                    plt.title("Books Borrowed by Genre")
                    plt.show()
                    
                case 4:
                    self.data["Day"] = self.data["Date"].dt.day_name()
                    if "Hour" not in self.data.columns:
                        self.data["Hour"] = 0  
                    heat = self.data.pivot_table(index="Day", columns="Hour", values="Transaction ID", aggfunc="count").fillna(0)
                    # reorder days
                    heat = heat.reindex(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
                    plt.figure(figsize=(12,6))
                    sns.heatmap(heat, cmap="YlGnBu", annot=True, fmt=".0f")
                    plt.title("Borrowing Activity Heatmap")
                    plt.show()

                case 5:
                    break
                case _:
                    print("Invalid choice")

# Main Program 
def main():
    dashboard = LibraryDashboard()

    if not dashboard.load_data():
        return

    while True:
        print("\n==== E-Library Dashboard ====")
        print("1. View Statistics")
        print("2. Filter Transactions")
        print("3. Generate Report")
        print("4. Visualize Data")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input!")
            continue

        match choice:
            case 1:
                dashboard.calculate_statistics()
            case 2:
                dashboard.filter_transactions()
            case 3:
                dashboard.generate_report()
            case 4:
                dashboard.visualize()
            case 5:
                print("Exiting Dashboard. Goodbye!")
                break
            case _:
                print("Invalid choice")
                
if __name__ == "__main__":
    main()
