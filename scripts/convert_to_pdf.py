import markdown
from weasyprint import HTML

# Lees het markdown bestand
with open('menu/boodschappen-voorgerecht-oefenen.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Converteer markdown naar HTML
html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

# Maak complete HTML met styling
html = f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 2cm;
            line-height: 1.6;
            color: #333;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 1.5em;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 5px;
        }}
        h3 {{
            color: #7f8c8d;
            margin-top: 1em;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        ul, ol {{
            margin-left: 1.5em;
        }}
        li {{
            margin: 0.3em 0;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
        }}
        strong {{
            color: #2c3e50;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 1em;
            margin-left: 0;
            color: #7f8c8d;
        }}
    </style>
</head>
<body>
{html_body}
</body>
</html>
'''

# Converteer naar PDF
HTML(string=html).write_pdf('menu/boodschappen-voorgerecht-oefenen.pdf')

print("PDF succesvol aangemaakt: menu/boodschappen-voorgerecht-oefenen.pdf")
