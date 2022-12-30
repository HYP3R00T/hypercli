from os import system, name, get_terminal_size
from termcolor import cprint
from pyfiglet import Figlet
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich import box


width = get_terminal_size()[0]


class cli:
    def __init__(self) -> None:
        self.menu = {}
        self.context = {}
        self.visual = {}

        self.show_banner = False
        self.show_intro = False
        self.show_context = False

        self.common_func = Common_func()
        self.console = Console()

    def create_banner(self, banner, figlet_font='big', banner_color='green', justify='center'):
        self.show_banner = True
        self.banner = Banner(
            banner, figlet_font=figlet_font, banner_color=banner_color, justify=justify)

    def create_intro(self, intro_title, intro, intro_title_color='red', intro_color='blue', justify='center'):
        self.show_intro = True
        self.intro = Intro(
            intro=intro, intro_title=intro_title, intro_title_color=intro_title_color, intro_color=intro_color, justify=justify)

    def create_menu(self, menu_name, detail=None, context_color="yellow", option_color="white", exit_color="red", show_border=False, show_exit=True):
        self.menu[f"{menu_name}"] = {}
        self.context[f"{menu_name}"] = detail
        self.visual[f"{menu_name}"] = {}
        self.visual[f"{menu_name}"]["context_color"] = context_color
        self.visual[f"{menu_name}"]["option_color"] = option_color
        self.visual[f"{menu_name}"]["exit_color"] = exit_color
        self.visual[f"{menu_name}"]["show_border"] = show_border
        self.visual[f"{menu_name}"]["show_exit"] = show_exit

    def add_option(self, menu_name, option, function=None):
        self.menu[menu_name][option] = function

    def show_cli(self, menu_name=None):
        self.common_func.clear()
        if self.show_banner:
            self.banner.show_banner()
        if self.show_intro:
            self.intro.show_intro()
        if menu_name == None:
            for k, v in self.menu.items():
                menu_name = k
                break
        context_color = self.visual[f"{menu_name}"]["context_color"]
        option_color = self.visual[f"{menu_name}"]["option_color"]
        exit_color = self.visual[f"{menu_name}"]["exit_color"]
        if self.visual[f"{menu_name}"]["show_border"] == False:
            show_border = box.SIMPLE
        else:
            show_border = box.HEAVY_HEAD
        show_exit = self.visual[f"{menu_name}"]["show_exit"]
        if self.context[f"{menu_name}"] != None:
            self.console.print(
                "\n"+self.context[f"{menu_name}"], style=context_color)
        table = Table(show_header=False, box=show_border)
        for (index, (k, v)) in enumerate(self.menu[menu_name].items()):
            table.add_row(str(index+1), str(k), style=option_color)
        table.add_section()
        if show_exit == True:
            table.add_row("0", "exit", style=exit_color)
        self.console.print(table)
        return self.enter_choice(menu_name, show_exit)

    def enter_choice(self, menu_name, show_exit):

        choice = input("\u279D ")
        for (index, (k, v)) in enumerate(self.menu[menu_name].items()):
            if int(choice) <= len(self.menu[menu_name]):
                if int(choice) == index + 1:
                    if isinstance(v, str):
                        return self.show_cli(v)
                    elif v != None:
                        return v
                    else:
                        return self.common_func.error()
                elif int(choice) == 0 and show_exit == True:
                    return self.common_func.exit()
            else:
                return self.common_func.error()


class Banner:
    def __init__(self, banner, figlet_font, banner_color, justify) -> None:
        self.banner = banner
        self.banner_color = banner_color
        self.justify = justify

        self.common_func = Common_func()
        self.f = Figlet(font=figlet_font, justify=self.justify, width=width)

    def show_banner(self):
        cprint(self.f.renderText(self.banner), color=self.banner_color)


class Intro:
    def __init__(self, intro, intro_title, intro_title_color, intro_color, justify) -> None:
        self.intro = intro
        self.intro_title = intro_title
        self.intro_color = intro_color
        self.intro_title_color = intro_title_color
        self.justify = justify

        self.c = Console()

    def show_intro(self):
        self.c.print(Panel(f"{self.intro}",
                     style=f"{self.intro_color} bold", title=f"[{self.intro_title_color}]{self.intro_title}"), justify=self.justify)


class Common_func:
    def __init__(self) -> None:
        self.c = Console()

    def exit(self):
        self.clear()
        self.c.print(Panel("Have a great day\nProgram is terminated", style="blue",
                     title=f"[green bold]\u263A BYE \u263A"), justify="center")
        return exit

    def error(self):
        self.clear()
        self.c.print(Panel("Invalid input\nProgram is terminated", style="blue",
                     title=f"[red bold]\u26A0  ERROR \u26A0 "), justify="center")
        return exit

    def clear(self):
        system('cls' if name == 'nt' else 'clear')
