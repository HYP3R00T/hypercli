from os import get_terminal_size, name, system

from pyfiglet import Figlet
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from termcolor import cprint

try:
    width = get_terminal_size()[0]
except Exception:
    width = 80


class Hypercli:
    def __init__(self) -> None:
        """
        The above function is the initialization method for a class that sets up various configuration
        options and properties.
        """
        self.menu_wrapper = {}
        self.console = Console()
        self.config = {
            "show_banner": True,
            "show_intro": True,
            "show_exit": True,
            "show_menu_table_header": False,
            "exit_text": "Quit ✗",
            "banner_text": "hypercli",
            "banner_color": "cyan",
            "banner_font": "big",
            "banner_justify": "center",
            "banner_width": width,
            "intro_title": "Welcome to hypercli!",
            "intro_title_color": "red bold",
            "intro_content": "A simple menu-driven CLI program generator",
            "intro_content_color": "magenta",
            "intro_justify": "center",
            "menu_context_color": "blue",
            "menu_option_color": "green",
            "menu_exit_color": "red bold",
            "menu_border_style": box.SQUARE,
            "menu_table_header_color": "bright_black",
            "error_message_title": "\u26a0  ERROR \u26a0 ",
            "error_message": "Invalid input\nProgram is terminated",
            "error_message_title_color": "red bold",
            "error_message_color": "magenta",
            "error_message_justify": "center",
            "exit_message_title": "\u263a BYE \u263a ",
            "exit_message": "Have a great day\nProgram is terminated",
            "exit_message_title_color": "green bold",
            "exit_message_color": "blue",
            "exit_message_justify": "center",
        }
        self.banner = Figlet(
            font=self.config["banner_font"],
            justify=self.config["banner_justify"],
            width=self.config["banner_width"],
        )

    def link(self, from_menu, to_menu, option_text="Go to", reverse=True):
        """
        The function `link` creates a link between two menus by adding an option to navigate from one
        menu to another.

        :param from_menu: The menu from which the link is being created
        :param to_menu: The menu that the link will lead to
        :param option_text: The `option_text` parameter is a string that represents the text that will
        be displayed for the link option in the menu. By default, it is set to "Go to", defaults to Go
        to (optional)
        :param reverse: The "reverse" parameter is a boolean value that determines whether or not to
        create a reverse link between the menus. If set to True, a link will be created from the
        "to_menu" to the "from_menu" with the option text "Go to". If set to False, no reverse, defaults
        to True (optional)
        """
        if from_menu not in self.menu_wrapper:
            self.menu_wrapper[from_menu] = {}
        if to_menu not in self.menu_wrapper:
            self.menu_wrapper[to_menu] = {}
        self.menu_wrapper[from_menu][f"{option_text} {to_menu}"] = to_menu
        if reverse:
            self.menu_wrapper[to_menu][f"{option_text} {from_menu}"] = from_menu

    def entry(
        self,
        menu,
        option,
        menu_context_color=None,
        menu_option_color=None,
        menu_exit_color=None,
    ):
        """
        The `entry` function is a decorator that adds a menu option to a menu wrapper and allows for
        customization of menu colors.

        :param menu: The "menu" parameter is a string that represents the name of the menu. It is used
        to group related options together
        :param option: The "option" parameter is used to specify the option within a menu. It is used to
        identify a specific function that will be executed when that option is selected from the menu
        :param menu_context_color: The `menu_context_color` parameter is used to specify the color of
        the menu context text
        :param menu_option_color: The parameter `menu_option_color` is used to specify the color of the
        menu option text
        :param menu_exit_color: The `menu_exit_color` parameter is an optional parameter that specifies
        the color of the menu exit option. It is used to customize the appearance of the menu exit
        option in the user interface
        :return: The `decorator` function is being returned.
        """

        def decorator(func):
            if menu not in self.menu_wrapper:
                self.menu_wrapper[menu] = {}
            if option not in self.menu_wrapper[menu]:
                self.menu_wrapper[menu][option] = func
            if menu_context_color:
                self.config[menu]["menu_context_color"] = menu_context_color
            if menu_option_color:
                self.config[menu]["menu_option_color"] = menu_option_color
            if menu_exit_color:
                self.config[menu]["menu_exit_color"] = menu_exit_color
            return func

        return decorator

    def enter_choice(self, menu_name):
        """
        The function takes a menu name as input and prompts the user for a choice, then executes the
        corresponding function based on the choice.

        :param menu_name: The `menu_name` parameter is a string that represents the name of the menu. It
        is used to access the corresponding menu dictionary in the `self.menu_wrapper` attribute
        :return: different values based on the conditions met. The possible return values are:
        """
        choice = input("\u279d ")
        for index, (_k, v) in enumerate(self.menu_wrapper[menu_name].items()):
            if choice == "q" or choice == "Q":
                return self.exit()
            elif choice.isalnum() and not choice.isnumeric():
                return self.error()
            elif int(choice) <= len(self.menu_wrapper[menu_name]):
                if int(choice) == index + 1:
                    function = v
                    if isinstance(function, str):
                        return self.run(function)
                    elif function is not None:
                        return function()
                    else:
                        return self.error()
            else:
                return self.error()

    def run(self, menu_name=None):
        """
        The `run` function displays a menu with options and allows the user to make a choice.

        :param menu_name: The `menu_name` parameter is used to specify the name of the menu that should
        be displayed. If no `menu_name` is provided, the code will default to the first menu in the
        `menu_wrapper` dictionary
        :return: the result of the `enter_choice()` method, which is called with the `menu_name`
        argument.
        """
        self.clear()
        if self.config["show_banner"]:
            cprint(
                self.banner.renderText(self.config["banner_text"]),
                color=self.config["banner_color"],
            )
        if self.config["show_intro"]:
            self.console.print(
                Panel(
                    f"{self.config['intro_content']}",
                    style=f"{self.config['intro_content_color']} bold",
                    title=f"[{self.config['intro_title_color']}]{self.config['intro_title']}",
                ),
                justify=self.config["intro_justify"],
            )
        if menu_name is None:
            for menu, _options in self.menu_wrapper.items():
                menu_name = menu
                break
        table = Table(
            show_header=self.config["show_menu_table_header"],
            style=self.config["menu_table_header_color"],
            box=self.config["menu_border_style"],
        )
        if self.config["show_menu_table_header"]:
            table.add_column("Choice", justify="center")
            table.add_column("Option", justify="left")
        for index, (option, _option_value) in enumerate(self.menu_wrapper[menu_name].items()):
            table.add_row(str(index + 1), str(option), style=self.config["menu_option_color"])
        table.add_section()
        if self.config["show_exit"]:
            table.add_row("q", self.config["exit_text"], style=self.config["menu_exit_color"])
        self.console.print(table, justify="left")
        return self.enter_choice(menu_name)

    def exit(self):
        """
        The above function clears the console and prints an exit message with specified formatting
        before exiting the program.
        :return: The `exit` function is returning the `exit` keyword, which is used to exit the program.
        """
        self.clear()
        self.console.print(
            Panel(
                self.config["exit_message"],
                style=self.config["exit_message_color"],
                title=f"[{self.config['exit_message_title_color']}]{self.config['exit_message_title']}",
            ),
            justify=self.config["exit_message_justify"],
        )
        return exit

    def error(self):
        """
        The function `error` clears the console and prints an error message with a specified title and
        color.
        :return: the exit keyword.
        """
        self.clear()
        self.console.print(
            Panel(
                self.config["error_message"],
                style=self.config["error_message_color"],
                title=f"[{self.config['error_message_title_color']}]{self.config['error_message_title']}",
            ),
            justify=self.config["error_message_justify"],
        )
        return exit

    def clear(self):
        """
        The function clears the console screen.
        """
        system("cls" if name == "nt" else "clear")
