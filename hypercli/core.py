from os import get_terminal_size, name, system

from pyfiglet import Figlet
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from termcolor import cprint

try:
    width = get_terminal_size()[0]
except:
    width = 80


class hypercli:
    def __init__(self) -> None:
        self.menu_wrapper = dict()
        self.common_func = Common_func()
        self.console = Console()
        self.config = {
            "show_banner": True,
            "show_intro": True,
            "banner": "hypercli",
            "banner_color": "red",
            "banner_font": "slant",
            "banner_justify": "center",
            "banner_width": width,
            "intro_title": "Welcome to hypercli!",
            "intro_title_color": "green",
            "intro_content": "A simple menu-driven CLI program generator",
            "intro_content_color": "yellow",
            "intro_justify": "center",
            "menu_context_color": "blue",
            "menu_option_color": "cyan",
            "menu_exit_color": "red",
            "menu_show_border": True,
            "menu_border_style": box.HEAVY_HEAD,
        }

    def entry(
        self,
        menu,
        option,
        menu_context_color=None,
        menu_option_color=None,
        menu_exit_color=None,
    ):
        def decorator(func):
            if menu not in self.menu_wrapper:
                self.menu_wrapper[menu] = dict()
            if option not in self.menu_wrapper[menu]:
                self.menu_wrapper[menu][option] = func
            if menu_context_color:
                self.config["menu_context_color"] = menu_context_color
            if menu_option_color:
                self.config["menu_option_color"] = menu_option_color
            if menu_exit_color:
                self.config["menu_exit_color"] = menu_exit_color
            return func

        return decorator

    def enter_choice(self, menu_name):
        choice = input("\u279D ")
        for index, (k, v) in enumerate(self.menu_wrapper[menu_name].items()):
            if int(choice) <= len(self.menu_wrapper[menu_name]):
                if int(choice) == index + 1:
                    function = v
                    if isinstance(function, str):
                        return self.run(function)
                    elif function is not None:
                        return function()
                    else:
                        return self.common_func.error()
                elif int(choice) == 0:
                    return self.common_func.exit()
            else:
                return self.common_func.error()

    def run(self, menu_name=None):
        if menu_name == None:
            for menu, options in self.menu_wrapper.items():
                menu_name = menu
                break
        table = Table(show_header=False)
        for index, (option, option_value) in enumerate(
            self.menu_wrapper[menu_name].items()
        ):
            table.add_row(str(index + 1), str(option))
        table.add_section()
        self.console.print(table)
        return self.enter_choice(menu_name)

    def link(self, from_menu, to_menu, option_text="Go to", reverse=True):
        if from_menu not in self.menu_wrapper:
            self.menu_wrapper[from_menu] = dict()
        if to_menu not in self.menu_wrapper:
            self.menu_wrapper[to_menu] = dict()
        self.menu_wrapper[from_menu][f"{option_text} {to_menu}"] = to_menu
        if reverse:
            self.menu_wrapper[to_menu][f"{option_text} {from_menu}"] = from_menu


class Common_func:
    def __init__(self) -> None:
        """
        This function is a constructor that initializes the Console class
        """
        self.c = Console()

    def exit(self):
        """
        It clears the screen, prints a message, and exits the program
        :return: The exit function is being returned.
        """
        self.clear()
        self.c.print(
            Panel(
                "Have a great day\nProgram is terminated",
                style="blue",
                title=f"[green bold]\u263A BYE \u263A",
            ),
            justify="center",
        )
        return exit

    def error(self):
        """
        It prints an error message and exits the program
        :return: The exit function is being returned.
        """
        self.clear()
        self.c.print(
            Panel(
                "Invalid input\nProgram is terminated",
                style="blue",
                title=f"[red bold]\u26A0  ERROR \u26A0 ",
            ),
            justify="center",
        )
        return exit

    def clear(self):
        """
        If the operating system is Windows, clear the screen using the cls command, otherwise clear the
        screen using the clear command
        """
        system("cls" if name == "nt" else "clear")
