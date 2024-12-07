import requests
import pandas as pd
import os

# Google Custom Search API credentials
API_KEY = "AIzaSyDwrG2bQHmVaWv2708gQ4p5yS6obT7cPlQ"  # Replace with your API key
SEARCH_ENGINE_ID = "5297313f5794e4436"  # Replace with your search engine ID
QUERY = "site:.ai"  # Search query to find .ai domains
MAX_RESULTS = 100  # Limit total results in the CSV
RESULTS_PER_PAGE = 10  # Google API returns 10 results per page
OUTPUT_FILE = "ai_tools_google.csv"  # File to save results

# Function to load already captured results from the CSV
def load_existing_results(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return pd.DataFrame(columns=["Name", "Website", "Description"])

# Function to perform Google search
def search_google(query, start_index):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query,
        "start": start_index,  # Pagination
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Function to extract metadata from search results
def extract_metadata(item):
    try:
        name = item["title"]
        description = item.get("snippet", "No description available.")
        link = item["link"]
        return {"Name": name, "Website": link, "Description": description}
    except KeyError:
        return None

# Main function
def crawl_google():
    existing_results = load_existing_results(OUTPUT_FILE)
    existing_websites = set(existing_results["Website"])

    tools = []
    start_index = 1  # Start with the first result

    while len(existing_results) + len(tools) < MAX_RESULTS:
        print(f"Fetching results starting from index {start_index}...")
        if start_index > 91:  # Google API pagination limit
            print("Reached maximum pagination limit (91).")
            break

        results = search_google(QUERY, start_index)
        if not results or "items" not in results:
            break

        for item in results["items"]:
            metadata = extract_metadata(item)
            if metadata and metadata["Website"] not in existing_websites:
                tools.append(metadata)
                existing_websites.add(metadata["Website"])
                if len(existing_results) + len(tools) >= MAX_RESULTS:
                    break

        start_index += RESULTS_PER_PAGE  # Increment to fetch the next page

    # Combine existing results with new tools
    new_results_df = pd.DataFrame(tools)
    final_results = pd.concat([existing_results, new_results_df], ignore_index=True)

    # Save results to the CSV file
    final_results.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
    print(f"Data saved to {OUTPUT_FILE}. Total records: {len(final_results)}")

if __name__ == "__main__":
    crawl_google()
