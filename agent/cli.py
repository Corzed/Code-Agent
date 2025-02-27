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

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='assistant.log'
)

class SimpleCLI:
    def __init__(self):
        self.console = Console()
        self.messages = []
        logging.info("SimpleCLI initialized")

    def display_messages(self):
        """Safely display all messages"""
        try:
            self.console.clear()
            self.console.print("[blue]CodingAssistant[/]\n")
            for msg in self.messages:
                self.console.print(msg)
        except Exception as e:
            logging.error(f"Error displaying messages: {str(e)}")

    def run(self):
        logging.info("Starting CLI")
        self.console.clear()
        self.console.print("[blue]CodingAssistant[/]\n")
        
        while True:
            try:
                user_input = input("\n> ")
                logging.debug(f"Received user input: {user_input}")
                
                if user_input.lower() in ['q', 'quit', 'exit']:
                    logging.info("User requested exit")
                    self.console.print("[yellow]Goodbye![/]")
                    break

                self.messages.append(user_input)
                self.console.print("[blue]Thinking...[/]")
                
                try:
                    logging.debug("Processing user input")
                    response = code_agent.run_conversation(user_input)
                    self.messages.append(f"[blue]Assistant:[/]")
                    # Convert Markdown to string for display
                    if isinstance(response, str):
                        self.messages.append(Markdown(response))
                    else:
                        self.messages.append(response)
                except Exception as e:
                    logging.error(f"Error during conversation: {str(e)}", exc_info=True)
                    self.messages.append(f"[red]Error:[/] {str(e)}")
                
                self.display_messages()
                
            except KeyboardInterrupt:
                logging.info("Received KeyboardInterrupt")
                self.console.print("\n[yellow]Goodbye![/]")
                break
            except Exception as e:
                logging.error(f"Unexpected error: {str(e)}", exc_info=True)
                self.console.print(f"[red]Unexpected error:[/] {str(e)}")

if __name__ == "__main__":
    SimpleCLI().run()
