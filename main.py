import os
import pickle
from googletrans import Translator
import googletrans
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
import platform
import sys
from rich.table import Table
from rich.theme import Theme


class App:

    def __init__(self):
        self.configfile = open("./config.pkl", "rb")
        self.userconfig = pickle.load(self.configfile)
        self.LANGUAGE_CODE_LIST = []
        self.THEME = Theme({
            "input": "#00FF00 italic bold",
            "error": "#FFFF00 italic bold",
            "instruction": "#00FFFF italic bold"
        })
        self.console = Console(theme=self.THEME)
        try:
            self.LANGUAGES = googletrans.LANGUAGES
        except ConnectionError:
            self.console.print("Internet error! [instruction]Check your Network[/instruction]", style="error")
            sys.exit(0)

        self.entrance()

    def config(self):
        md = Markdown("# Thanks for choosing this software!")
        self.console.print(md)
        self.console.print("For it's you [error]FIRST[/error] time to use this software", style="instruction")
        self.console.print("Here are some questions to ask you for a better personal using experience",
                           style="instruction")
        self.console.print("If you want just keeping the default value, just press [error]ENTER[/error] to ignore",
                           style="instruction")
        self.console.print(
            "Set the [error]DEFAULT TARGET LANGUAGE[/error]"
            "([instruction]type {langs} to show the language list[/instruction]): ",
            style="input",
            end="")
        dtl = self.console.input()
        if dtl != "{langs}":
            pass
        else:
            self.console.print(
                "TIPS: You can use {langs} to check the Language Code everywhere in this software since now")

    def language_code(self):
        table = Table(title="Language Code List")
        table.add_column("Language Name", style='#00FF00')
        table.add_column("Language Code", style='#FFFF00')
        for i in self.LANGUAGES:
            table.add_row(self.LANGUAGES[i], i)
            self.LANGUAGE_CODE_LIST.append(i)
        system_type = platform.system()
        if system_type == "Windows":
            os.system("cls")
        if system_type == "Linux":
            os.system("clear")
        self.console.print(table)

    def make_language_code_list(self):
        for i in self.LANGUAGES:
            self.LANGUAGE_CODE_LIST.append(i)

    def entrance(self):
        if self.userconfig["used"] == 0:
            self.config()
        else:
            self.make_language_code_list()
            self.mainloop()

    def hr(self):
        terminal_size = os.get_terminal_size()
        for i in range(terminal_size.columns):
            self.console.print("-", end="")
        self.console.print("\n")

    def mainloop(self):
        while True:
            try:
                words = []
                self.console.print("Input something:", style="input")
                while True:
                    source = self.console.input()
                    if source == "":
                        break
                    else:
                        words.append(source)
            except ConnectionError:
                self.console.print("Internet error! [instruction]Check your Network[/instruction]", style="error")
                self.console.print("\n")
                continue


if __name__ == "__main__":
    try:
        App()
    except KeyboardInterrupt:
        console = Console()
        console.print("You Interrupt the programme!", style="#FFFF00 italic bold")
        console.print("\n")
        sys.exit(0)
