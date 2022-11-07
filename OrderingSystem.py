from textual.app import App, ComposeResult
from textual.widgets import Button, Static, Footer
from textual.containers import Container, Horizontal, Vertical

class Menu(Static):
    
    def compose(self) -> ComposeResult:
        yield Button("Menu")


class AbdulApp(App):

    def compose(self) -> ComposeResult:
        yield Footer()
        yield Container (
            Button("Hello"),
            Horizontal(
                Button("1st Button"),
                Button("2nd Button"),
                Button("3rd Button")
            ),
            id="container"
        )
        
if __name__ == "__main__":
    AbdulApp().run()
