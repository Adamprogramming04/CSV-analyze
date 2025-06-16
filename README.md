# PyPowerTools 

A single, powerful Python script that combines:

-  CSV Data Analyzer
-  HTML Web Scraper
-  OpenAI ChatGPT CLI

---

## 💻 Features

| Tool          | Description                                           |
|---------------|-------------------------------------------------------|
| Data Analyzer | Loads a CSV file, displays stats, plots correlations |
| Web Scraper   | Extracts text from a website by tag and class        |
| ChatGPT CLI   | Talks with OpenAI’s GPT-4 from your terminal         |

---

##  How to Use

### 1. Install Dependencies

```bash
pip install pandas seaborn matplotlib requests beautifulsoup4 openai
```

### 2. Run the Tool

```bash
python main.py
```

You'll see:

```
Welcome to PyPowerTools 
1. Data Analyzer
2. Auto Scraper
3. AI Chat CLI
4. Exit
```

### 3. Tool Descriptions

####  Data Analyzer

- Input: CSV file path
- Output:
  - Column list
  - Summary statistics
  - Seaborn pairplot of numeric columns

####  Auto Scraper

- Input: URL, HTML tag, optional class name
- Output: List of text elements matching criteria

####  AI Chat CLI

- Input: Your OpenAI API key
- Chat directly with GPT-4 from your terminal

---

## Notes

- Keep your OpenAI key private.
- Avoid scraping websites you don't have permission to access.

---

## Single-File Structure

Only one file needed:

```
main.py
```

Put it in any folder and you're good to go!

---

##  License

MIT License © 2025 [ProgrammingAdam]

---

##  Contributing

Pull requests welcome! Feel free to fork and upgrade.

---
