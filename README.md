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

- Enhanced Logging
  - Detailed execution logs
  - Debug information for tool operations
  - Error tracking and reporting
  - Comprehensive email reports with execution history

- Email Integration
  - Automatic email reports after completion
  - Detailed execution logs in email body
  - Final result summary
  - Gmail SMTP integration

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
3. Set up environment variables:

Option 1: Export in terminal (recommended for testing):
```bash
export GEMINI_API_KEY=your_api_key_here
export GMAIL_USER=your.email@gmail.com
export GMAIL_APP_PASSWORD=your16digitpassword
```
Option 2: Create a .env file:
```bash
GEMINI_API_KEY=your_api_key_here
GMAIL_USER=your.email@gmail.com
GMAIL_APP_PASSWORD=your16digitpassword
```

## Usage
Recommended Method: Run the client (automatically starts the server):
```bash
python math_agent_client.py
```
Alternative Method (for debugging): Run server and client separately:
1. Start the MCP server:
```bash
# Terminal 1
python math_agent_server.py

# Terminal 2
python math_agent_client.py
```

The agent will:

- Start the MCP server internally
- Process mathematical queries using Gemini AI
- Execute calculations using available tools
- Create a Word document with the result
- Draw a rectangle containing the final answer
- Send an email report with execution logs

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

## Logging
- All operations are logged with timestamps
- Log levels: INFO, DEBUG, ERROR
- Logs are included in email reports
- Console output for real-time monitoring

## Troubleshooting

### Email Configuration
- Ensure GMAIL_USER is your full email address
- GMAIL_APP_PASSWORD must be a 16-character app password
- Enable 2-Step Verification in your Google Account
- Check execution logs for detailed error messages

### Word Integration
- Ensure Microsoft Word is installed and running
- Allow automation permissions if prompted
- Check execution logs for any automation errors

### Common Issues
- If environment variables are not detected, try restarting your terminal
- For Word automation issues, ensure Word is not in full-screen mode
- Check console output for detailed error messages and stack traces

## Limitations
- Requires macOS environment
- Microsoft Word for macOS must be installed
- Maximum 8 iterations per problem
- Requires Google Cloud API access
