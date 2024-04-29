from IPython.display import display, HTML

def show_html(file: str):
    with open(file, "r") as f:
        plot = f.read()
    display(HTML(plot))