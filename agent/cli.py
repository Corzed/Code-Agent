import logging
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.markdown import Markdown
from rich.tree import Tree
from agent import code_agent

# Load environment variables
load_dotenv()
if not os.getenv('OPENAI_API_KEY'):
    raise EnvironmentError("OPENAI_API_KEY not found in environment variables")

class SimpleCLI:
    def __init__(self):
        self.console = Console()
        self.messages = []

    def display_messages(self):
        """Safely display all messages"""
        try:
            self.console.clear()
            self.console.print("[blue]CodingAssistant[/]\n")
            for msg in self.messages:
                self.console.print(msg)
        except Exception as e:
            self.console.print(f"[red]Error displaying messages:[/] {str(e)}")

    def run(self):
        self.console.clear()
        self.console.print("[blue]CodingAssistant[/]\n")
        
        while True:
            try:
                user_input = input("\n> ")
                
                if user_input.lower() in ['q', 'quit', 'exit']:
                    self.console.print("[yellow]Goodbye![/]")
                    break

                self.messages.append(user_input)
                self.console.print("[blue]Thinking...[/]")
                
                try:
                    response = code_agent.run_conversation(user_input)
                    self.messages.append(f"[blue]Assistant:[/]")
                    # Convert Markdown to string for display
                    if isinstance(response, str):
                        self.messages.append(Markdown(response))
                    else:
                        self.messages.append(response)
                except Exception as e:
                    self.messages.append(f"[red]Error:[/] {str(e)}")
                
                self.display_messages()
                
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Goodbye![/]")
                break
            except Exception as e:
                self.console.print(f"[red]Unexpected error:[/] {str(e)}")

if __name__ == "__main__":
    SimpleCLI().run()
