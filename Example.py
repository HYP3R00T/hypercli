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
