# Wiki

## The list of configs and relevant resources

### Configs

| Config                    | Type | Default                                      |
| ------------------------- | ---- | -------------------------------------------- |
| show_banner               | bool | True                                         |
| show_intro                | bool | True                                         |
| show_exit                 | bool | True                                         |
| show_menu_table_header    | bool | False                                        |
| exit_text                 | str  | "Quit ✗"                                     |
| banner_text               | str  | "hypercli"                                   |
| banner_color              | str  | "cyan"                                       |
| banner_font               | str  | "big"                                        |
| banner_justify            | str  | "center"                                     |
| banner_width              | int  | width                                        |
| intro_title               | str  | "Welcome to hypercli!"                       |
| intro_title_color         | str  | "red bold"                                   |
| intro_content             | str  | "A simple menu-driven CLI program generator" |
| intro_content_color       | str  | "magenta"                                    |
| intro_justify             | str  | "center"                                     |
| menu_context_color        | str  | "blue"                                       |
| menu_option_color         | str  | "green"                                      |
| menu_exit_color           | str  | "red bold"                                   |
| menu_border_style         | str  | box.SQUARE                                   |
| menu_table_header_color   | str  | "bright_black"                               |
| error_message_title       | str  | "\u26A0  ERROR \u26A0 "                      |
| error_message             | str  | "Invalid input\nProgram is terminated"       |
| error_message_title_color | str  | "red bold"                                   |
| error_message_color       | str  | "magenta"                                    |
| error_message_justify     | str  | "center"                                     |
| exit_message_title        | str  | "\u263A BYE \u263A "                         |
| exit_message              | str  | "Have a great day\nProgram is terminated"    |
| exit_message_title_color  | str  | "green bold"                                 |
| exit_message_color        | str  | "blue"                                       |
| exit_message_justify      | str  | "center"                                     |

### Resources

- Link to rich color palette: https://rich.readthedocs.io/en/stable/appendix/colors.html
- Link to rich box styles: https://rich.readthedocs.io/en/stable/appendix/box.html
- Link to pyfiglet font list: http://www.figlet.org/

## The list of methods

### Methods

| Method | Description                             |
| ------ | --------------------------------------- |
| link   | Add a navigation option to the menu     |
| entry  | Decorator to add a function to the menu |
| run    | Run the CLI program                     |

## Notes

- The `link` method is used to add a navigation option to the menu. It takes two arguments: `menu` and `option`. The `menu` argument is the name of the menu to which the navigation option is added. The `option` argument is the name of the navigation option. The `link` method can be called multiple times to add multiple navigation options to the menu.
- The `entry` method is a decorator that is used to add a function to the menu. It takes two arguments: `menu` and `option`. The `menu` argument is the name of the menu to which the function is added. The `option` argument is the name of the function. The `entry` method can be called multiple times to add multiple functions to the menu.
- The `run` method is used to run the CLI program. It takes no arguments. It is called after all the navigation options and functions have been added to the menu.
- `banner_color` has limited color options as it is not rendered by the rich module. The available options are `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, and `white`.
