![human_typer](https://socialify.git.ci/UnMars/human_typer/image?forks=1&language=1&name=1&owner=1&stargazers=1&theme=Light)

# Human Typer

Python package to simulate human keyboard typing

## Installation

Use the package manager [pip](https://pypi.org/project/human_typer/) to install human_typer.

```bash
pip install human_typer
```

For Playwright support:

```bash
pip install human_typer[playwright]
```

## Usage

```python
from human_typer import Human_typer

My_Typer = Human_typer(keyboard_layout = "qwerty", average_cpm = 190)

# Directly with keyboard
My_Typer.keyboard_type("my text")

# With a Selenium element
my_element = driver.find_element_by_id("ID")
My_Typer.type_in_element("my text", my_element)

# With a Playwright element (requires: pip install human_typer[playwright])
from playwright.sync_api import sync_playwright

My_Typer = Human_typer(element_type="playwright")
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    element = page.locator("#my-input")
    My_Typer.type_in_element("my text", element)
    browser.close()
```

## Contributing

Pull requests are welcome 😊

## License

[MIT](https://choosealicense.com/licenses/mit/)
