# **E-Library Data Insights Dashboard**

---

## **Project Overview**

The **E-Library Data Insights Dashboard** is a **Python-based application** to manage, analyze, and visualize library borrowing data.
It helps librarians explore borrowing patterns, generate reports, filter transactions, and gain actionable insights for better library management.

---

## **Features**

* **Data Management:** Load CSV datasets and automatically clean & validate data.
* **Statistics & Analysis:** Compute average borrowing duration, most borrowed books, busiest days, etc.
* **Filtering:** Filter transactions by **genre**, **date range**, or **borrowing duration**.
* **Reports:** Generate summary reports with **top books**, **late returns**, and **user statistics**.
* **Visualization:**

  * **Bar charts** for top borrowed books
  * **Line charts** for monthly borrowing trends
  * **Pie charts** for genre distribution
  * **Heatmaps** for day & hour borrowing activity
* **Interactive Menu:** Easy-to-use command-line interface for all features.

---

## **Functions**

* **`load_data(file_path=None)`** – Loads CSV data, cleans missing/duplicate values, and computes extra columns like `Frequent Borrower` & `Late Return`.
* **`calculate_statistics()`** – Shows statistics like **most borrowed book**, **average borrowing duration**, **std deviation**, and **busiest day**.
* **`filter_transactions()`** – Filter transactions by **genre**, **date range**, or **borrowing duration**. Optionally saves filtered data.
* **`generate_report()`** – Summarizes **total transactions**, **unique users**, **late returns**, and **top 3 borrowed books**.
* **`visualize()`** – Generates **bar charts**, **line charts**, **pie charts**, and **heatmaps** with proper titles, labels, and legends.

---

## **Classes**

### `LibraryDashboard`

Main class managing all library operations:

* **Attribute:** `self.data` → stores transactions as a pandas DataFrame.
* **Methods:** `load_data()`, `calculate_statistics()`, `filter_transactions()`, `generate_report()`, `visualize()`.

---

## **Libraries Used**

* **pandas** → Data manipulation & analysis
* **numpy** → Numerical computations
* **matplotlib** → Plotting charts
* **seaborn** → Professional visualizations
* **datetime** → Handling dates & times

---

## **Dataset**

The CSV file **`library_transactions.csv`** contains:

* `Transaction ID`
* `Date` (YYYY-MM-DD)
* `User ID`
* `Book Title`
* `Genre`
* `Borrowing Duration (Days)`

**Example row:**

```csv
T001,2024-01-01,U101,The Alchemist,Fiction,7
```

---

## **Folder Structure**

```
E-Library-Dashboard/
│
├── library_dashboard.py       # Main Python script
├── library_transactions.csv   # Sample dataset
└── README.md                  # Project documentation
```

---

## **How to Run**

1. Ensure **Python 3.x** is installed.
2. Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn
```

3. Run the script:

```bash
python library_dashboard.py
```

4. Use the interactive menu to view **statistics**, **filter data**, **generate reports**, and **visualize trends**.

---

## **Quick Start Example**

**Sample Run:**

```
==== Load Data Menu ====
1. Use default CSV file (library_transactions.csv)
2. Enter CSV file path manually
Enter choice: 1
Data loaded and cleaned successfully!

==== E-Library Dashboard ====
1. View Statistics
2. Filter Transactions
3. Generate Report
4. Visualize Data
5. Exit
Enter your choice: 1

------ Library Statistics ------
Most Borrowed Book       : The Alchemist
Average Borrow Duration  : 8.5 days
Borrow Duration Std Dev  : 2.3
Busiest Day              : Wednesday

Enter your choice: 2
Filter Options
1. Filter by Genre
2. Filter by Date Range
3. Filter by Borrowing Duration (>days)
Enter choice: 1
Enter Genre: Fiction

Filtered Data (Top 5 rows):
  Transaction ID       Date User ID      Book Title    Genre  Borrowing Duration (Days) Frequent Borrower Late Return
0           T001 2024-01-01   U101  The Alchemist  Fiction                       7                3          No

Do you want to save filtered data to CSV? (y/n): n

Enter your choice: 4
==== Visualization Menu ====
1. Bar Chart: Top 5 Most Borrowed Books
2. Line Chart: Borrowing Trends Over Months
3. Pie Chart: Distribution by Genre
4. Heatmap: Borrowing Activity by Day & Hour
5. Return to Main Menu
Enter your choice: 1
# Displays bar chart with top 5 most borrowed books
```

---

## **Author**

**Patel Tej**

---

