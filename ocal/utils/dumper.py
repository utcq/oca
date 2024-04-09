from core.challenge import Challenge
from utils.colors import Colors

def finds(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def find_line(s, index):
    return next((i + 1 for i, line in enumerate(s.split('\n')) if sum(map(len, s.split('\n')[:i + 1])) >= index), None)

def print_chall(chall: Challenge)->None:
    newdesc = chall.description.replace("\n\n", "\n")
    nedesc = []
    newdesc = newdesc.split("\n")
    for line in newdesc:
        if ("Sito: " in line):
            pass
        elif ("`nc " in line and line.startswith("`")):
            pass
        elif (line.startswith("Nota: ")):
            pass
        elif (line.startswith("Leggi la [writeup]")):
            pass
        elif "Puoi collegarti al servizio remoto con" in line:
            pass
        else:
            nedesc.append(line)
    newdesc = ' '.join(nedesc).replace("`", "")

    print(Colors.BOLD + Colors.CYAN + "━" * 50 + Colors.END)
    print("\t{}Name:  {}{} [{}]{}".format(Colors.CYAN, Colors.GREEN, chall.name, chall.id, Colors.END))
    print("\t{}Score: {}{} {}".format(Colors.CYAN, Colors.GREEN, chall.score, Colors.END))
    print("\t{}Tags:  {}{} {}".format(Colors.CYAN, Colors.GREEN, ', '.join(chall.categories).capitalize(), Colors.END))
    print("\t{}URLs:  {}{} {}".format(Colors.CYAN, Colors.GREEN, '\n\t       '.join(chall.urls), Colors.END))
    print("\t{}Hosts: {}{} {}".format(Colors.CYAN, Colors.GREEN, '\n\t       '.join(' '.join(tup) for tup in chall.hosts), Colors.END))
    print(newdesc)
    print(Colors.BOLD + Colors.CYAN + "━" * 50 + Colors.END)

def print_plugin(plugin: str)->None:
    print("{}[PLUGIN] Loaded {}{}{}".format(Colors.CYAN, Colors.LIGHT_GREEN, plugin, Colors.END))

def print_plugin_run(plugin: str)->None:
    print("{}[PLUGIN] {}Executing {}{}{}\n".format(Colors.CYAN, Colors.BLUE, Colors.LIGHT_GREEN, plugin, Colors.END))

def print_downloading(file: str)->None:
    print("{}[FILE] {}Downloading {}{}{}".format(Colors.CYAN, Colors.RED, Colors.CYAN, file, Colors.END))