# Human Typer

Python package to simulate human keyboard typing

## Installation

Use the package manager [pip](https://pypi.org/project/human_typer/) to install human-typer.

```bash
pip install human_typer
```

## Usage

```python
from human_typer import Human_typer

My_Typer = Human_typer(keyboard_layout = "qwerty", average_cpm = 190)

# Directly with keyboard 
My_Typer.keyboard_type("my text")

# With an Selenium element
my_element = driver.find_element_by_id("ID")
My_Typer.type_in_element("my text", my_element)
```

## Contributing
Pull requests are welcome 😊

## License
[MIT](https://choosealicense.com/licenses/mit/)
