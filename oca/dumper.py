from challenge import Challenge

def finds(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def find_line(s, index):
    return next((i + 1 for i, line in enumerate(s.split('\n')) if sum(map(len, s.split('\n')[:i + 1])) >= index), None)

class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""

def print_chall(chall: Challenge)->None:
    newdesc = chall.description.replace("\n\n", "\n")
    if ("Sito: " in newdesc.split("\n")[-1]):
        newdesc = '\n'.join(newdesc.split("\n")[:-1])
    elif (newdesc.split("\n")[-1].startswith("`")):
        newdesc = '\n'.join(newdesc.split("\n")[:-1])


    print(Colors.BOLD + Colors.CYAN + "━" * 50 + Colors.END)
    print("\t{}Name:  {}{} [{}]{}".format(Colors.CYAN, Colors.GREEN, chall.name, chall.id, Colors.END))
    print("\t{}Score: {}{} {}".format(Colors.CYAN, Colors.GREEN, chall.score, Colors.END))
    print("\t{}Tags:  {}{} {}".format(Colors.CYAN, Colors.GREEN, ', '.join(chall.categories).capitalize(), Colors.END))
    print(newdesc)
    print(Colors.BOLD + Colors.CYAN + "━" * 50 + Colors.END)

def print_plugin(plugin: str)->None:
    print("{}[PLUGIN] Loaded {}{}{}".format(Colors.CYAN, Colors.LIGHT_GREEN, plugin, Colors.END))

def print_plugin_run(plugin: str)->None:
    print("{}[PLUGIN] {}Executing {}{}{}\n".format(Colors.CYAN, Colors.BLUE, Colors.LIGHT_GREEN, plugin, Colors.END))

def print_downloading(file: str)->None:
    print("{}[FILE] {}Downloading {}{}{}".format(Colors.CYAN, Colors.RED, Colors.CYAN, file, Colors.END))