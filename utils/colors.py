"""Improve console output by adding color to them."""

import shutil


class Colors:
    """Output colorful message in terminal"""

    def __init__(self) -> None:
        self.c_blue = "\033[94m"
        self.c_cyan = "\033[96m"
        self.c_success = "\033[92m"
        self.c_warning = "\033[93m"
        self.c_error = "\033[91m"
        self.c_bold = "\033[1m"
        self.c_underline = "\033[4m"
        self.endc = "\033[0m"

    def blue(self, text) -> str:
        """Print text in blue color"""
        return f"{self.c_blue}{text}{self.endc}"

    def cyan(self, text) -> str:
        """Print text in cyan color"""
        return f"{self.c_cyan}{text}{self.endc}"

    def success(self, text) -> str:
        """Print text in green color"""
        return f"{self.c_success}{text}{self.endc}"

    def warning(self, text) -> str:
        """Print text in yellow color"""
        return f"{self.c_warning}{text}{self.endc}"

    def error(self, text) -> str:
        """Print text in red color"""
        return f"{self.c_error}{text}{self.endc}"

    def bold(self, text) -> str:
        """Print text in bold"""
        return f"{self.c_bold}{text}{self.endc}"

    def underline(self, text) -> str:
        """Print text in underline"""
        return f"{self.c_underline}{text}{self.endc}"

    def bold_underline(self, text) -> str:
        """Print text in green color"""
        return f"{self.c_bold}{self.c_underline}{text}{self.endc}"

    def bold_blue(self, text) -> str:
        """Print text in bold and blue color"""
        return f"{self.c_bold}{self.c_blue}{text}{self.endc}"

    def bold_cyan(self, text) -> str:
        """Print text in bold and cyan color"""
        return f"{self.c_bold}{self.c_cyan}{text}{self.endc}"

    def bold_success(self, text) -> str:
        """Print text in bold and green color"""
        return f"{self.c_bold}{self.c_success}{text}{self.endc}"

    def bold_warning(self, text) -> str:
        """Print text in bold and yellow color"""
        return f"{self.c_bold}{self.c_warning}{text}{self.endc}"

    def bold_error(self, text) -> str:
        """Print text in bold and red color"""
        return f"{self.c_bold}{self.c_error}{text}{self.endc}"

    def bold_underline_blue(self, text) -> str:
        """Print text in bold and underline and blue color"""
        return f"{self.c_bold}{self.c_underline}{self.c_blue}{text}{self.endc}"

    def print_result(self, result: bool, message: str) -> None:
        """Print the quiz result in green or red color

        Args:
            result (bool): True if the quiz is correct, False otherwise
            message (str): The message to print
        """

        if result:
            print(f"{self.bold_success(f'✔ {message}')}", "\n")
        else:
            print(f"{self.bold_error(f'✘ {message}')}")

    def print_warning(self, message: str) -> None:
        """Print text in yellow color with a warning sign"""

        print(f"{self.warning('⚠')} {message}")

    def print_error(self, message: str) -> None:
        """Print text in red color with an error sign"""

        print(f"{self.error(f'✘ {message}')}")

    def print_centre(self, text: str) -> None:
        """Print text in centre of the terminal"""

        print(text.center(int(shutil.get_terminal_size().columns)))

    def print_final_result(
        self,
        scores_msg: str,
        percentage_msg: str,
        pattern_char: str = "=",
        pattern_len: int = 20,
        result_boundary: str = "#",
        padding: bool = False,
    ) -> None:
        """Print the final quiz result

        Args:
            scores_msg (str): The number of correct answers with message
            percentage_msg (str): The percentage of correct answers with message
            pattern_char (str, optional): The character to use for the pattern. Defaults to "=".
            pattern_len (int, optional): The length of the pattern. Defaults to 20.
            result_boundary (str, optional): The character for result boundary. Defaults to "#".
            padding (bool, optional): If True, print padding arround the result. Defaults to False.
        """

        main_pattern: str = pattern_char * pattern_len
        msg_pattern: str = "{0}{msg}{0}"
        scores_msg: str = msg_pattern.format(
            result_boundary, msg=scores_msg.center(pattern_len - 2)
        )
        percentage_msg: str = msg_pattern.format(
            result_boundary, msg=percentage_msg.center(pattern_len - 2)
        )

        print()
        self.print_centre("Your final result:")
        print(self.c_cyan, end="")
        self.print_centre(main_pattern)

        if padding:
            self.print_centre(
                msg_pattern.format(result_boundary, msg=" " * (pattern_len - 2))
            )
            self.print_centre(scores_msg)
            self.print_centre(percentage_msg)
            self.print_centre(
                msg_pattern.format(result_boundary, msg=" " * (pattern_len - 2))
            )
        else:
            self.print_centre(scores_msg)
            self.print_centre(percentage_msg)

        self.print_centre(main_pattern)
        print(self.endc)
        print(self.c_bold, self.c_blue)
        self.print_centre("Thank you for playing!")
        print(self.endc)
        print(self.c_cyan)
        self.print_centre("To play again, click on the 'RUN PROGRAM' button.")
        print(self.endc)

    def print_heading(self, *args) -> None:
        """Print a heading with a line of dashes"""

        print(self.c_bold, self.c_success)
        for heading in args:
            self.print_centre(heading)
        print(self.endc, end="")
        self.print_centre(50 * "*")
        print()
