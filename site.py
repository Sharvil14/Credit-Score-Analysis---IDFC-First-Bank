# generate_site.py
import os

# Create a directory for the static site
os.makedirs("docs", exist_ok=True)

# Generate HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>My Python Site</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome to My Python-Generated Site!</h1>
    <p>This site was created using Python.</p>
</body>
</html>
"""

# Save HTML file
with open("docs/index.html", "w") as file:
    file.write(html_content)

# Create a CSS file
css_content = """
body {
    font-family: Arial, sans-serif;
    background: #f0f0f0;
    text-align: center;
    padding: 50px;
}
h1 {
    color: #333;
}
"""

with open("docs/styles.css", "w") as file:
    file.write(css_content)

print("Static site generated in 'docs/' directory.")
