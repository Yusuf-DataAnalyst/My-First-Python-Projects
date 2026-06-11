# 📊 My Python Data Analysis & Automation Projects

This repository serves as a showcase for my initial journey into Python programming. Every project here was conceptualized, coded, and tested entirely on a **mobile device** using Pydroid 3, reflecting my deep commitment to learning despite hardware limitations. These projects demonstrate my progression from basic scripting to creating practical tools that solve real-world problems.

---

## 🚀 Projects Portfolio

### 1️⃣ El Prince Kitchen Management System (`elprince_kitchen_system.py`) 👨‍🍳
* **Problem:** Managing inventory efficiency and timing during high-pressure shifts in a busy restaurant environment.
* **Solution:** A smart logistics system I developed for "El Prince" restaurant. 
* **Key Functionality:** The script dynamically calculates the exact number of rice pots needed based on daily customer volume, reducing food waste. Additionally, it integrates a countdown timer to monitor the time remaining until Iftar, ensuring smooth operations during peak service hours.

### 2️⃣ Sales Analysis & Optimization Tool (`sales_analysis.py`) 📈
* **Problem:** Difficulty in identifying high-value products and tracking overall business performance manually.
* **Solution:** A robust data processing script that ingests sales data to generate actionable business intelligence.
* **Key Functionality:** It calculates total revenue, identifies the "King of Sales" (top-selling product), and provides a breakdown of performance metrics, enabling data-driven decisions for inventory stocking.

### 3️⃣ Personal Expense Tracker (`expense_tracker.py`) 💰
* **Problem:** Lack of visibility into daily spending habits and difficulty in managing personal budgets.
* **Solution:** An automated financial monitoring tool to enforce fiscal discipline.
* **Key Functionality:** Users can input daily expenses, which are tracked against a budget. The script includes an automated "High-Price Alert" system that warns users when spending exceeds specific, predefined thresholds, helping users maintain better control over their finances.

### 4️⃣ Asset Goal & Investment Calculator (`asset_calculator.py`) 🏦
* **Problem:** Uncertainty regarding financial timelines for long-term investments like purchasing property or gold.
* **Solution:** A complex financial modeling tool that simulates future growth.
* **Key Functionality:** This script calculates the exact time required to reach financial targets by factoring in compounding investment returns and annual inflation rates. It helps in planning for major life purchases by providing a realistic projection of capital accumulation over time.



5️⃣ Automated File Organizer (`file_organizer.py`)

Automated File Organizer
​An automated Python script designed to clean, sort, and manage cluttered directories by filtering and moving files into specific folders based on their extensions.
​As a Data Analyst, keeping data environments structured is essential. This project automates the initial Data Triage and file organization process, saving time and establishing a reliable pipeline before the data extraction and transformation (ETL) phases.
​🧠 Logic & Workflow
​The script executes through three logical phases:
​Directory Scanning: It reads the specified path and gathers a comprehensive list of all contained files using the os module.
​Directory Creation: It checks for the existence of target folders (csv_files, image_files, text_files). If they do not exist, it dynamically creates them.
​File Sorting & Routing: It loops through each file, identifies its format (e.g., .csv, .png, .txt), and safely transfers it to its designated folder utilizing the shutil library.
​🚀 Key Features
​Dynamic Folder Checking: Prevents script crashes by verifying folder existence before creation.
​Automated File Routing: Uses conditional logic to sort files instantly.
​Robust Path Handling: Implements os.path.join to ensure cross-platform compatibility and avoid path string syntax errors.
​Streamlined Efficiency: Eliminates manual file sorting, allowing more focus on core data analysis tasks.
________________________________________________________________-

6️⃣ Web Scraping and Data Extraction Project: Books to Scrape(`web_scraping.py)
​Project Overview
​This project focuses on automated data extraction and collection from the web using Python. The primary objective is to scrape a multi-page e-commerce website to extract book details, including their full titles and prices. Instead of relying on pre-existing static datasets, this project demonstrates the ability to gather live, raw data from the web, which is a foundational step in any data analysis workflow.
​Core Features
​Automated HTTP requests to retrieve website source code.
​Parsing HTML structures to locate and isolate specific data points.
​Extraction of nested attributes and text elements from web pages.
​Data structuring capabilities for future analysis.
​Technologies Used
​Python: The core programming language.
​Jupyter Notebook: The development environment used for writing and testing the code interactively.
​BeautifulSoup4 (bs4): For parsing HTML documents and navigating the DOM tree structure.
​Requests: For handling HTTP requests to fetch webpage data.
​Technical Challenges and Solutions
​1. Scope and Variable Overwriting in Loops
​Challenge: An initial logical error occurred when separating the iteration logic from the extraction output across different notebook cells. The printing function was placed outside the execution block of the loop, causing the program to output only the final record of the scraped dataset due to continuous variable overwriting.
​Solution: Restructured the notebook execution sequence by encapsulating both the data parsing and the output printing within a single unified for loop block, maintaining strict indentation integrity.
​2. Python Reserved Keyword Conflicts
​Challenge: A SyntaxError was encountered when trying to filter HTML elements by their CSS class names using the standard class keyword, which is reserved for object-oriented programming in native Python.
​Solution: Resolved the syntax conflict by utilizing the BeautifulSoup-specific class_ argument, allowing the script to target specific HTML element classes smoothly.
​3. Character Encoding Issues
​Challenge: The extracted price data contained unexpected corrupted characters (e.g., Â£) preceding the currency symbol. This happened due to a mismatch between the website's character encoding format and the default parsing interpretation.
​Solution: Identified the encoding discrepancy and introduced proper text decoding mechanisms to clean the textual output, ensuring a standardized and accurate dataset.


## 🖼️ Results & Preview

### El Prince Kitchen System:
![Kitchen Result](El_Prince.jpg)

### Sales & Expenses:
![Sales Result](sales_result.jpg)
![Expense Result](expense_result.jpg)

### Asset Goal Calculator: 
![Asset Result](AssetGoalCalculator.jpg) 


### file organizer :
![file organizer](file_organizer.png) 


#### web scraping :
![web scraping](web_scraping.png) 

---

## 🛠️ Technical Foundation
* **Programming Language:** Python 3
* **Primary Environment:** Pydroid 3 (Mobile Development) & Laptop (Post-Development)
* **Core Skills:** Algorithmic logic, data input/output handling, automated conditional alerts, and financial modeling.
* **Professional Goal:** To transition my analytical mindset into a full-time Data Analysis career, leveraging my ability to build automated solutions from scratch.
