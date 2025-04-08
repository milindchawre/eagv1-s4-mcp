# Math Agent with Microsoft Word Integration

A Python-based mathematical agent that solves problems iteratively using various mathematical tools and visualizes results using Microsoft Word.

## Features

- Mathematical Operations
  - Basic arithmetic (add, subtract, multiply, divide)
  - Advanced operations (power, square root, cube root)
  - Trigonometric functions (sin, cos, tan)
  - Logarithmic calculations
  - Factorial computation
  - Fibonacci sequence generation
  - ASCII value conversion
  - Exponential sum calculations

- AI Integration
  - Google Gemini Pro model for intelligent problem-solving
  - Iterative problem-solving approach
  - Automatic tool selection and execution

- Word Integration
  - Automatic Word document creation
  - Rectangle drawing with results
  - Automated result visualization
  - Configurable text placement

## Prerequisites

- Python 3.7+
- Microsoft Word for macOS
- macOS 10.15 or later
- Google Cloud API key (for Gemini Pro)

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip3 install -r requirements.txt
```
3. Create a .env file in the project root and add your Gemini API key:
```bash
GEMINI_API_KEY=your_api_key_here
```

## Usage
1. Start the MCP server:
```bash
python math_agent_server.py
```
2. Run the client:
```bash
python math_agent_client.py
```

The agent will:

- Connect to the MCP server
- Process mathematical queries using Gemini AI
- Execute calculations using available tools
- Create a Word document with the result
- Draw a rectangle containing the final answer

## Example Queries
```plaintext
- Find the ASCII values of characters in INDIA and then return sum of exponentials of those values
- Calculate the factorial of 5
- Find the sum of first 10 Fibonacci numbers
```

## Architecture
- `math_agent_client.py` : Main client handling:
    - Gemini AI integration
    - Query processing
    - Tool execution
    - Word visualization

- `math_agent_server.py` : Server providing:
    - Mathematical tools
    - Word integration tools
    - Resource handlers

## Error Handling
- Timeout protection for AI generation
- Robust error handling for tool execution
- Automatic state reset
- Debug logging

## Limitations
- Requires macOS environment
- Microsoft Word for macOS must be installed
- Maximum 3 iterations per problem
- Requires Google Cloud API access
