from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from rich.spinner import Spinner
import asyncio

class SimpleCLI:
    def __init__(self):
        self.console = Console()
        self.messages = []

    def run(self):
        self.console.clear()
        self.console.print("[blue]CodingAssistant[/]\n")
        
        while True:
            try:
                # Show all past messages
                for msg in self.messages:
                    self.console.print(msg)

                user_input = input("\n> ")
                
                if user_input.lower() in ['q', 'quit', 'exit']:
                    self.console.print("[yellow]Goodbye![/]")
                    break

                # Store raw user input
                self.messages.append(user_input)
                
                # Get response with loading spinner
                with Live(Spinner("dots", style="blue"), refresh_per_second=10):
                    try:
                        response = coding_agent.run_conversation(user_input)
                        # Render the agent's response with markdown
                        self.messages.append(f"[blue]Assistant:[/]\n{Markdown(response)}")
                    except Exception as e:
                        self.messages.append(f"[red]Error:[/] {str(e)}")

                self.console.clear()
                self.console.print("[blue]CodingAssistant[/]\n")
                
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Goodbye![/]")
                break

if __name__ == "__main__":
    SimpleCLI().run()
