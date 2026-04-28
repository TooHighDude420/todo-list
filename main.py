from pathlib import Path
from rich.console import Console

BASE_DIR = Path(__file__).parent
TODO_DIR = BASE_DIR / "TODO"

if not TODO_DIR.exists():
    TODO_DIR.mkdir(exist_ok=True)

console = Console(color_system='truecolor')

title = console.input("Enter todo title:\n")
items = []

def generate_file(items: list[str], title):
    file_cont = f"# {title}"

    title = "_".join(title.split(' '))

    for item in items:
        file_cont += f"\n- [] {item}"

    with open(TODO_DIR / f"TODO.{title}.md", mode='w') as todolist:
        todolist.write(file_cont)

    console.print(f"generated TODO.{title}.md")

running = True
cont = False

while(running):
    current = []
    current.append("current todo list:\n")

    for i in items:
        current.append(f"- {i}\n")

    if cont:
        title = console.input("Enter todo title:\n")
        items = []

        cont = False

    console.print(*current)
    input = console.input("enter list item, q to generate and exit, c to generate and continue\n")
    console.clear()

    match input:
        case 'q':
            generate_file(items, title)
            cont = False
            running = False
        
        case 'c':
            generate_file(items, title)
            cont = True

        case _:
            items.append(input)