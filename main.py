import os
import pickle

from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.theme import Theme


class App:

    def __init__(self):
        self.configfile = open("./config.pkl", "rb")
        self.configfile = None
        self.LOG_THEME = Theme({
            "info": "#00FF00",
            "error": "#FFFF00 italic",
            "instruction": "#00FFFF italic"
        })
        self.console = Console(theme=self.LOG_THEME)
        self.entrance()

    def firstTime(self):
        md = Markdown("# Thanks for choosing this software!")
        self.console.print(md)
        self.console.print("For it's you [error]first[/error] time to use this software")
        self.console.print("Here are some questions to ask you for a better personal using experience")
        self.console.print("If you want just keep ")

    def entrance(self):
        config = pickle.load(self.configfile)
        if config["used"] == 0:
            self.firstTime()
        else:
            self.mainloop()

    def hr(self):
        terminal_size = os.get_terminal_size()
        for i in range(terminal_size.columns):
            self.console.print("-", end='')
        self.console.print("\n")

    def mainloop(self):
        while True:
            try:
                words = []
                self.console.print("Input something:", style="info")
                while True:
                    source = self.console.input()
                    if source == "":
                        break
                    else:
                        words.append(source)

            except KeyboardInterrupt:
                self.console.print("You Interrupt the programme!", style="error")
                self.console.print("\n")
                break
            except ConnectionError:
                self.console.print("Internet error! [instruction]Check your Network[/instruction]", style="error")
                self.console.print("\n")
                continue


if __name__ == "__main__":
    App()
