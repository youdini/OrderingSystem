from textual.app import App, ComposeResult
from textual.widgets import Button, Static, Footer
from textual.containers import Container, Horizontal, Vertical

class AbdulApp(App):

    def compose(self) -> ComposeResult:
        yield Footer()
        yield Button("Hi")
        
if __name__ == "__main__":
    AbdulApp().run()
