import getch

from src.options_dict import option_dict

def job():
    option = getOption()

def getOption():
    entry = getch.getch()
    print(f"Selected Move: {option_dict[entry][0]}")
    option_dict[entry][1]()
    return entry