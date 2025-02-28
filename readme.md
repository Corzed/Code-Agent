# Code-Agent

## Overview

Code-Agent is an AI agent designed to help with file operations and code management. Built on top of the [OrchestrAI](https://github.com/Corzed/OrchestrAI) library, it provides an ai agent with a suite of tools for reading, writing, editing, creating, renaming, and deleting files, as well as executing terminal commands.

## Features

- **File Operations:** Code agent can Read, list, write, edit file segments, create, rename, and delete files/directories.
- **Command Execution:** Code agent can Run terminal commands and capture their output.
- **Interactive CLI:** A rich, interactive command-line interface for a seamless user experience.


## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Corzed/Code-Agent.git
    cd Code-Agent
    ```

2. **Install dependencies:**
    ```bash
    pip install -r agent/requirements.txt
    ```

3. **Set up environment variables:**  
   Create a `.env` file in the project root and add your OpenAI API key:
    ```dotenv
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## Usage

### Running the CLI

Launch the interactive command-line interface:
```bash
python cli.py
