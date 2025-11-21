from pathlib import Path
from typing import Annotated
import typer

app = typer.Typer()


@app.command()
def main(paths: Annotated[list[Path], typer.Argument()]):
    for path in paths:
        if path.name == "checkable.txt":
            content = path.read_text()
            if content != "checkable\n":
                path.write_text("checkable\n")
                raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
