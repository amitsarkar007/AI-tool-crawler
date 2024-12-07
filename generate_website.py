import pandas as pd

# Load the CSV file
input_csv = "ai_tools_google.csv"  # Replace with your CSV file name
data = pd.read_csv(input_csv)

# Modern HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Tools Directory</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>AI Tools Directory</h1>
        <p>Your go-to place for discovering the latest AI tools!</p>
    </header>
    <main>
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Website</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
    </main>
    <footer>
        <p>&copy; 2024 AI Tools Directory. Built with ❤️ for AI enthusiasts.</p>
    </footer>
</body>
</html>
"""

# Modern CSS template
CSS_TEMPLATE = """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #444;
    background: #f9fafb;
    margin: 0;
    padding: 0;
}

header {
    background: #4CAF50;
    color: #fff;
    padding: 20px 10px;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

header h1 {
    font-size: 2.5rem;
    margin-bottom: 10px;
}

header p {
    font-size: 1.2rem;
}

main {
    padding: 20px;
}

.table-container {
    overflow-x: auto;
    margin: 20px auto;
    max-width: 1200px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
}

table th, table td {
    padding: 15px;
    border-bottom: 1px solid #e5e5e5;
}

table th {
    background: #f4f4f4;
    font-weight: bold;
    text-transform: uppercase;
    font-size: 0.9rem;
    letter-spacing: 0.05em;
}

table tr:hover {
    background: #f9f9f9;
}

a {
    color: #4CAF50;
    text-decoration: none;
    font-weight: bold;
}

a:hover {
    text-decoration: underline;
}

footer {
    text-align: center;
    padding: 15px;
    background: #333;
    color: #fff;
    margin-top: 20px;
    font-size: 0.9rem;
}
"""

# Generate table rows
def generate_table_rows(data):
    rows = ""
    for _, row in data.iterrows():
        rows += f"""
        <tr>
            <td>{row['Name']}</td>
            <td>{row['Description']}</td>
            <td><a href="{row['Website']}" target="_blank">Visit</a></td>
        </tr>
        """
    return rows

# Create the HTML file
def create_html_file(data):
    table_rows = generate_table_rows(data)
    html_content = HTML_TEMPLATE.format(table_rows=table_rows)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

# Create the CSS file
def create_css_file():
    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(CSS_TEMPLATE)

# Generate the website
create_html_file(data)
create_css_file()
print("Modern website generated successfully: index.html and styles.css")
