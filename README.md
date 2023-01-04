```
 _                               _ _
| |                             | (_)
| |__  _   _ _ __   ___ _ __ ___| |_
| '_ \| | | | '_ \ / _ \ '__/ __| | |
| | | | |_| | |_) |  __/ | | (__| | |
|_| |_|\__, | .__/ \___|_|  \___|_|_|
        __/ | |
       |___/|_|               v 0.1.4
```


# hypercli

`hypercli` is a Python library for creating a good looking command line interface. Primarily it can generate menu with very simple steps. We can also create some banners as well. Everything one need to create create interactive command line interface. 

## Installation

Use the package manager [pip](https://pypi.org/project/hypercli/) to install `hypercli`.

```bash
pip install hypercli
```

## Usage

```python
from hypercli import cli
import webbrowser


def author_name():
    print("HYP3R00T")


def open_website():
    webbrowser.open("https://hyperoot.live")


hyper = cli()

hyper.create_banner("hypercli")
hyper.create_intro("Intro", "An elegant solution to interact\n with command line tools")

hyper.create_menu("Main Menu", "Enter your choice")
hyper.add_option("Main Menu", "Checkout the Sub Menu", "Sub Menu")
hyper.add_option("Main Menu", "Print Author Name", author_name)

hyper.create_menu("Sub Menu", "Enter your choice")
hyper.add_option("Sub Menu", "Go Back to Main Menu", "Main Menu")
hyper.add_option("Sub Menu", "Checkout the Website (hyperoot.live)", open_website)

response = hyper.show_cli()
response()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
