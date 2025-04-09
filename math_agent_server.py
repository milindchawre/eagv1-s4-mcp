# basic import 
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import Tool, types
from PIL import Image as PILImage
import math
import sys
from appscript import app, k
import pyautogui
import time
import subprocess  # Add this import
import asyncio  # Add this import at the top
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
import logging

# After imports, before tools
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# instantiate an MCP server client
mcp = FastMCP("Calculator")

# DEFINE TOOLS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# mine tool
@mcp.tool()
def mine(a: int, b: int) -> int:
    """special mining tool"""
    print("CALLED: mine(a: int, b: int) -> int:")
    return int(a - b - b)

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    print("CALLED: create_thumbnail(image_path: str) -> Image:")
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")

@mcp.tool()
def strings_to_chars_to_int(string: str) -> list[int]:
    """Return the ASCII values of the characters in a word"""
    print("CALLED: strings_to_chars_to_int(string: str) -> list[int]:")
    return [int(ord(char)) for char in string]

@mcp.tool()
def int_list_to_exponential_sum(int_list: list) -> float:
    """Return sum of exponentials of numbers in a list"""
    print("CALLED: int_list_to_exponential_sum(int_list: list) -> float:")
    return sum(math.exp(i) for i in int_list)

@mcp.tool()
def fibonacci_numbers(n: int) -> list:
    """Return the first n Fibonacci Numbers"""
    print("CALLED: fibonacci_numbers(n: int) -> list:")
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

@mcp.tool()
async def open_word() -> dict:
    """Open Microsoft Word and create new document"""
    try:
        import subprocess
        
        apple_script = '''
        tell application "Microsoft Word"
            activate
            make new document
            delay 1
            return "success"
        end tell
        '''
        
        result = subprocess.run(['osascript', '-e', apple_script], capture_output=True, text=True)
        time.sleep(1)
        
        if result.returncode == 0:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Word document created successfully"
                    )
                ]
            }
        else:
            raise Exception(f"AppleScript error: {result.stderr}")
            
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error creating Word document: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def draw_word_rectangle_with_text(text: str) -> dict:
    """Draw rectangle and add text inside that rectangle in Word document"""
    try:
        async def execute_drawing():
            apple_script = f'''
            tell application "Microsoft Word"
                activate
                delay 1
                
                -- Make sure we have a document open
                if (count of documents) is 0 then
                    make new document
                end if
                delay 0.5
                
                tell application "System Events"
                    tell process "Microsoft Word"
                        -- Click Insert menu
                        click menu bar item "Insert" of menu bar 1
                        delay 0.5
                        
                        -- Click Shape from Insert menu's popup menu
                        tell menu 1 of menu bar item "Insert" of menu bar 1
                            click menu item "Shape"
                            delay 0.3
                            
                            -- Click Rectangle from Shape submenu
                            tell menu 1 of menu item "Shape"
                                click menu item "Rectangle"
                            end tell
                        end tell
                    end tell
                end tell
            end tell
            '''
            
            result = subprocess.run(['osascript', '-e', apple_script], capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"AppleScript error: {result.stderr}")
                
            # Reduced wait time for menu to close
            time.sleep(1)
            
            # Get screen size and calculate center offset
            screen_width, screen_height = pyautogui.size()
            center_x = screen_width // 2
            
            # Adjust coordinates relative to center of screen
            start_x = center_x - 200  # Starting point left of center
            start_y = 300
            end_x = center_x + 200    # Ending point right of center
            end_y = 400
            text_x = center_x         # Text position at center
            text_y = 350
            
            # Draw rectangle
            pyautogui.moveTo(start_x, start_y)
            time.sleep(0.2)
            pyautogui.mouseDown()
            pyautogui.keyDown('shift')
            pyautogui.moveTo(end_x, end_y, duration=0.3)
            pyautogui.mouseUp()
            pyautogui.keyUp('shift')
            time.sleep(0.2)
            
            # Add text with reduced delays
            pyautogui.click(text_x, text_y)
            time.sleep(0.2)
            pyautogui.write(text)
            time.sleep(0.2)
            
            pyautogui.click(end_x + 100, end_y + 100)
            
            return {
                "content": [
                    TextContent(
                        type="text",
                        text=f"Shape created with text: {text}"
                    )
                ]
            }

        # Reduced timeout to 20 seconds
        return await asyncio.wait_for(execute_drawing(), timeout=20)
            
    except asyncio.TimeoutError:
        return {
            "content": [
                TextContent(
                    type="text",
                    text="Operation timed out after 30 seconds"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error adding text to document: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def send_email_report(recipient: str, logs: list, final_result: str) -> dict:
    """Sends an email report with execution logs and final result"""
    try:
        # Email configuration with direct environment access
        sender_email = os.environ.get("GMAIL_USER")
        sender_password = os.environ.get("GMAIL_APP_PASSWORD")
        
        if not sender_email or not sender_password:
            logger.error("Email credentials not found in environment")
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Email credentials not found. Please ensure environment variables are set:\n"
                             "export GMAIL_USER=your.email@gmail.com\n"
                             "export GMAIL_APP_PASSWORD=your16digitpassword"
                    )
                ]
            }

        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = "Math Agent Execution Report"
        
        body = f"""
Math Agent Execution Report

Final Result: {final_result}

Execution Logs:
{chr(10).join(log for log in logs)}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Create SMTP session with debug level
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(1)  # Enable debug output
        
        try:
            server.ehlo()  # Identify ourselves to SMTP Gmail
            server.starttls()  # Secure the connection
            server.ehlo()  # Re-identify ourselves over TLS connection
            server.login(sender_email, sender_password)  # Login to the server
            server.send_message(msg)  # Send email
            
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Email report sent successfully"
                    )
                ]
            }
        finally:
            server.quit()  # Always close the connection
            
    except smtplib.SMTPAuthenticationError as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Gmail authentication failed. Error: {str(e)}. Please ensure:\n"
                         "1. GMAIL_USER is your full email address\n"
                         "2. GMAIL_APP_PASSWORD is the 16-character app password\n"
                         "3. 2-Step Verification is enabled in your Google Account"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Failed to send email. Error: {str(e)}"
                )
            ]
        }

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"


# DEFINE AVAILABLE PROMPTS
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
    print("CALLED: review_code(code: str) -> str:")


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution
