# import hypercli
from hypercli import hypercli

# create an instance of hypercli
cli = hypercli()

# configure the instance
cli.config["banner_text"] = "HYPERCLI"
cli.config["intro_title"] = "Intro"
cli.config["intro_content"] = "Generate enhanced menu-driven CLI programs with ease!"
cli.config["show_menu_table_header"] = True

# add navigation options to the menu
cli.link("Main Menu", "Mathematics Menu")
cli.link("Main Menu", "String Menu")


@cli.entry(menu="Main Menu", option="Greeter")
def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")


@cli.entry(menu="Mathematics Menu", option="Add two numbers")
def add(num1=1, num2=1):
    a = int(input(f"Enter first number (default {num1}): ") or num1)
    b = int(input(f"Enter second number (default {num2}): ") or num2)
    print(f"{a} + {b} = {a + b}")


@cli.entry(menu="Mathematics Menu", option="Subtract two numbers")
def sub(num1=1, num2=1):
    a = int(input(f"Enter first number (default {num1}): ") or num1)
    b = int(input(f"Enter second number (default {num2}): ") or num2)
    print(f"{a} - {b} = {a - b}")


@cli.entry(menu="String Menu", option="Reverse a string")
def reverse():
    string = input("Enter a string: ")
    print(string[::-1])


@cli.entry(menu="String Menu", option="Show length of a string")
def str_length():
    string = input("Enter a string: ")
    print(f"Length of string is {len(string)}")


# run the cli
cli.run()
