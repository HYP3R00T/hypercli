from os import system, name, get_terminal_size
from termcolor import cprint
from pyfiglet import Figlet
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich import box

try:
    width = get_terminal_size()[0]
except:
    width = 80


class cli:
    def __init__(self) -> None:
        """
        It initializes the menu, context, and visual dictionaries, sets the show_banner, show_intro, and
        show_context variables to False, and initializes the common_func and console variables
        """
        self.menu = {}
        self.context = {}
        self.visual = {}

        self.show_banner = False
        self.show_intro = False
        self.show_context = False

        self.common_func = Common_func()
        self.console = Console()

    def create_banner(self, banner, figlet_font='big', banner_color='green', justify='center'):
        """
        This function takes in a string, a figlet font, a color, and a justification and returns a
        banner object
        
        :param banner: The text to be displayed in the banner
        :param figlet_font: The font to use for the banner, defaults to big (optional)
        :param banner_color: The color of the banner, defaults to green (optional)
        :param justify: left, center, right, defaults to center (optional)
        """
        self.show_banner = True
        self.banner = Banner(
            banner, figlet_font=figlet_font, banner_color=banner_color, justify=justify)

    def create_intro(self, intro_title, intro, intro_title_color='red', intro_color='blue', justify='center'):
        """
        This function creates an intro object and sets the show_intro variable to True
        
        :param intro_title: The title of the intro
        :param intro: The text of the intro
        :param intro_title_color: The color of the title of the intro, defaults to red (optional)
        :param intro_color: The color of the text in the intro, defaults to blue (optional)
        :param justify: 'left', 'center', 'right', defaults to center (optional)
        """
        self.show_intro = True
        self.intro = Intro(
            intro=intro, intro_title=intro_title, intro_title_color=intro_title_color, intro_color=intro_color, justify=justify)

    def create_menu(self, menu_name, detail=None, context_color="yellow", option_color="white", exit_color="red", show_border=False, show_exit=True):
        """
        This function creates a menu with a name, a detail, a context color, an option color, an exit
        color, a show border boolean, and a show exit boolean
        
        :param menu_name: The name of the menu
        :param detail: This is the text that will be displayed at the top of the menu
        :param context_color: The color of the menu's context, defaults to yellow (optional)
        :param option_color: The color of the options in the menu, defaults to white (optional)
        :param exit_color: The color of the exit option, defaults to red (optional)
        :param show_border: If True, a border will be drawn around the menu, defaults to False
        (optional)
        :param show_exit: If True, the exit option will be shown, defaults to True (optional)
        """
        self.menu[f"{menu_name}"] = {}
        self.context[f"{menu_name}"] = detail
        self.visual[f"{menu_name}"] = {}
        self.visual[f"{menu_name}"]["context_color"] = context_color
        self.visual[f"{menu_name}"]["option_color"] = option_color
        self.visual[f"{menu_name}"]["exit_color"] = exit_color
        self.visual[f"{menu_name}"]["show_border"] = show_border
        self.visual[f"{menu_name}"]["show_exit"] = show_exit

    def add_option(self, menu_name, option, function=None):
        """
        It adds an option to a menu
        
        :param menu_name: The name of the menu you want to add the option to
        :param option: The name of the option to add to the menu
        :param function: The function to be called when the option is selected
        """
        self.menu[menu_name][option] = function

    def show_cli(self, menu_name=None):
        """
        It prints a menu to the console
        
        :param menu_name: The name of the menu to show
        :return: The return value is the value of the option that was selected.
        """
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
        """
        It takes a menu name, and a boolean value, and returns a function based on the user's choice
        
        :param menu_name: The name of the menu you want to display
        :param show_exit: If True, the user can exit the menu by entering 0
        :return: The return value is the function that is being called.
        """
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
        """
        This function is used to print a banner in the terminal
        
        :param banner: The text you want to display
        :param figlet_font: The font you want to use
        :param banner_color: The color of the banner
        :param justify: left, center, right
        """
        self.banner = banner
        self.banner_color = banner_color
        self.justify = justify

        self.common_func = Common_func()
        self.f = Figlet(font=figlet_font, justify=self.justify, width=width)

    def show_banner(self):
        """
        It takes a string, and prints it to the screen in a fancy way
        """
        cprint(self.f.renderText(self.banner), color=self.banner_color)


class Intro:
    def __init__(self, intro, intro_title, intro_title_color, intro_color, justify) -> None:
        """
        This function is used to create a new instance of the class
        
        :param intro: The text that will be displayed
        :param intro_title: The title of the intro
        :param intro_title_color: The color of the title of the intro
        :param intro_color: The color of the text in the intro
        :param justify: left, right, center
        """
        self.intro = intro
        self.intro_title = intro_title
        self.intro_color = intro_color
        self.intro_title_color = intro_title_color
        self.justify = justify

        self.c = Console()

    def show_intro(self):
        """
        It prints a panel with a title and a style
        """
        self.c.print(Panel(f"{self.intro}",
                     style=f"{self.intro_color} bold", title=f"[{self.intro_title_color}]{self.intro_title}"), justify=self.justify)


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
        self.c.print(Panel("Have a great day\nProgram is terminated", style="blue",
                     title=f"[green bold]\u263A BYE \u263A"), justify="center")
        return exit

    def error(self):
        """
        It prints an error message and exits the program
        :return: The exit function is being returned.
        """
        self.clear()
        self.c.print(Panel("Invalid input\nProgram is terminated", style="blue",
                     title=f"[red bold]\u26A0  ERROR \u26A0 "), justify="center")
        return exit

    def clear(self):
        """
        If the operating system is Windows, clear the screen using the cls command, otherwise clear the
        screen using the clear command
        """
        system('cls' if name == 'nt' else 'clear')
