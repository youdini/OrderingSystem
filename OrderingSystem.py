from textual.app import App, ComposeResult
from textual.widgets import Button, Static, Footer
from textual.containers import Container, Horizontal, Vertical

class Menu(Static):
    
    def compose(self) -> ComposeResult:
        yield Static("Menu")


class AbdulApp(App):

    def compose(self) -> ComposeResult:
        yield Footer()
        yield Button("Hi")
        yield Static("New changes")
        
# update
        
if __name__ == "__main__":
    AbdulApp().run()
