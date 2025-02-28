from OrchestrAI import Agent, AgentManager
from tools import FILE_TOOLS

# Initialize the agent manager
manager = AgentManager()

# Create the coding agent
code_agent = Agent(
    name="Programmer",
    role="""You are a coding assistant that can help with file operations and code management.
You can read, write, edit, create, rename, and delete files, as well as execute terminal commands.
Always confirm before making destructive changes (delete, overwrite).
When editing files, provide clear explanations of the changes being made.
Always write/run unit tests with files.""",
    description="An AI agent specialized in code and file manipulation",
    manager=manager,
    verbose=False, # Set to True for logging
    tools=FILE_TOOLS,
    model="gpt-4o-mini",  # Make sure to use a capable model
)
