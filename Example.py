from hypercli import hypercli

cli = hypercli()
cli.link("main", "main2")


@cli.entry(menu="main", option="multiply")
def multiply(num1=1, num2=1):
    a = int(input(f"Enter first number (default {num1}): ") or num1)
    b = int(input(f"Enter second number (default {num2}): ") or num2)
    print(f"{a} * {b} = {a * b}")


@cli.entry(menu="main", option="greet")
def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")


@cli.entry(menu="main2", option="add")
def add(num1=1, num2=1):
    a = int(input(f"Enter first number (default {num1}): ") or num1)
    b = int(input(f"Enter second number (default {num2}): ") or num2)
    print(f"{a} + {b} = {a + b}")


@cli.entry(menu="main3", option="subtract")
def sub(num1=1, num2=1):
    a = int(input(f"Enter first number (default {num1}): ") or num1)
    b = int(input(f"Enter second number (default {num2}): ") or num2)
    print(f"{a} - {b} = {a - b}")


cli.run("main")
