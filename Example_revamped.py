from hypercli import cli
import webbrowser


def author_name():
    print("HYP3R00T")


def open_website():
    webbrowser.open("https://hyperoot.dev")


def greet(*args):
    if len(args) > 0:
        name = args[0]
        print(f"Hello, {name}!")
    else:
        print("Hello!")


def add_numbers(*args):
    if len(args) > 1:
        num1 = int(args[0])
        num2 = int(args[1])
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")
    else:
        print("Invalid input! Please provide two numbers.")


hyper = cli()

# Set up the banner
hyper.create_banner("hypercli", figlet_font='slant', banner_color='yellow', justify='center')

# Set up the intro
hyper.create_intro("Intro", "An elegant solution to interact\n with command line tools",
                   intro_title_color='blue', intro_color='white', justify='center')

# Set up the main menu
hyper.create_menu("Main Menu", "Enter your choice", context_color='cyan', option_color='magenta',
                   exit_color='red', show_border=True)

# Add options to the main menu
hyper.add_option("Main Menu", "Checkout the Sub Menu", "Sub Menu")
hyper.add_option("Main Menu", "Greet", greet, "John")
hyper.add_option("Main Menu", "Print Author Name", author_name)
hyper.add_option("Main Menu", "Perform Math Operations", "Math Operations")

# Set up the math operations menu
hyper.create_menu("Math Operations", "Select an operation", context_color='green', option_color='yellow',
                   exit_color='red', show_border=False)

# Add options to the math operations menu
hyper.add_option("Math Operations", "Addition", add_numbers, 10, 20)
hyper.add_option("Math Operations", "Multiplication", None)

# Set up the sub menu
hyper.create_menu("Sub Menu", "Enter your choice", context_color='blue', option_color='white',
                   exit_color='red', show_border=True)

# Add options to the sub menu
hyper.add_option("Sub Menu", "Go Back to Main Menu", "Main Menu")
hyper.add_option("Sub Menu", "Checkout the Website (hyperoot.dev)", open_website)

# Show the CLI
response = hyper.show_cli()
