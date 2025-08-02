from colorama import Fore, Back, Style
print('default color text')
print(Fore.RED + 'red text' + Style.RESET_ALL)
print(Back.GREEN + 'black with green background' + Style.RESET_ALL)
print(Fore.YELLOW + Back.BLACK + 'yellow text with black background' + Style.RESET_ALL)
print('default color text')

print(Fore.RED)
print('red text')
print(Back.BLACK)
print('red text black background')

print(Style.RESET_ALL)
print('back to default color')
