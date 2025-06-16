import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import openai


def profile_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("\n Columns:\n", df.columns)
        print("\n Summary Stats:\n", df.describe(include='all'))
        sns.pairplot(df.select_dtypes(include='number').dropna())
        plt.show()
    except Exception as e:
        print(f"Error profiling data: {e}")


def scrape_website(url, tag, class_name=None):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        if class_name:
            results = soup.find_all(tag, class_=class_name)
        else:
            results = soup.find_all(tag)
        return [res.get_text(strip=True) for res in results]
    except Exception as e:
        return f"Error during scraping: {e}"


def chat_loop(api_key):
    openai.api_key = api_key
    print("\n AIChatCLI ready! Type 'exit' to quit.")
    while True:
        msg = input("You: ")
        if msg.lower() == 'exit':
            break
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": msg}]
            )
            print("AI:", response['choices'][0]['message']['content'].strip())
        except Exception as e:
            print(f"Chat error: {e}")


def menu():
    print("""
Welcome to PyPowerTools 
1. Data Analyzer
2. Auto Scraper
3. AI Chat CLI
4. Exit
""")
    while True:
        choice = input("Choose tool [1-4]: ")
        if choice == '1':
            file_path = input("CSV path: ")
            profile_data(file_path)
        elif choice == '2':
            url = input("URL: ")
            tag = input("HTML tag to extract (e.g. p, h1): ")
            class_name = input("Optional class name: ")
            results = scrape_website(url, tag, class_name or None)
            if isinstance(results, list):
                for i, text in enumerate(results):
                    print(f"[{i+1}] {text}")
            else:
                print(results)
        elif choice == '3':
            api_key = input("OpenAI API key: ")
            chat_loop(api_key)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
