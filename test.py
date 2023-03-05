from rich.console import Console
from rich.syntax import Syntax

console = Console()
syntax = Syntax("""{\n\t"used": 0, \n\t"default_target_lang": "zh-cn", \n\t"tts": "False"\n}""", "json")
console.print(syntax)