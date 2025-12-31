from pathlib import Path

def main():
  here = Path(__file__).parent
  relnames = [path.name for path in here.glob("*.html")]
  li_elements = [f'<li><a href="{relname}">{relname}</a></li>' for relname in relnames]

  with open(here / "index.html", "w") as f:
    f.write(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Main</title>
    </head>
    <body>
      <h1>Main</h1>
      <ul>
        {"\n".join(li_elements)}
      </ul>
    </body>
    </html>
    """)

if __name__ == "__main__":
  main()