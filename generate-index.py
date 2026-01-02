from pathlib import Path

def main():
  here = Path(__file__).parent
  relnames = [path.name for path in here.glob("*.html") if path.name not in ("index.html", "index-template.html")]

  li_elements = []
  for relname in sorted(relnames):
    # Generate icon filename (e.g., "antisniff.html" -> "antisniff-icon.png")
    icon_name = relname.replace(".html", "-icon.png")
    li_elements.append(
      f'<li><a href="{relname}"><img src="{icon_name}" class="icon" alt=""> {relname}</a></li>'
    )

  # Read template
  with open(here / "index-template.html", "r") as f:
    template = f.read()

  # Replace placeholder with generated list items
  html_content = template.replace("{LIST_ITEMS}", "\n".join(li_elements))

  # Write output
  with open(here / "index.html", "w") as f:
    f.write(html_content)

if __name__ == "__main__":
  main()