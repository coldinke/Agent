#!/usr/bin/env python3
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.syntax import Syntax
import argparse
import sys

# Create a rich console for pretty output
console = Console()

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process queries for the DeepSeek API.')
    parser.add_argument('-q', '--query', nargs='*', 
                        help='Query to send to the model. If no other flags follow, all remaining arguments are treated as part of the query.')
    parser.add_argument('-k', '--api-key', default="", 
                        help='API key for DeepSeek API')
    parser.add_argument('-u', '--base-url', default="https://api.deepseek.com", 
                        help='Base URL for the API')
    
    # Parse known args first to handle -q specially
    args, unknown = parser.parse_known_args()
    
    # If -q is provided but has no values and there are unknown args, 
    # assume all remaining arguments belong to -q
    if hasattr(args, 'query') and args.query == [] and unknown:
        args.query = unknown
    
    # Convert list of words to a single string
    if hasattr(args, 'query') and args.query:
        args.query = ' '.join(args.query)
    
    return args

def query_deepseek(query_text, api_key="", base_url="https://api.deepseek.com"):
    # Initialize the client
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    # Prepare the message
    messages = [{"role": "user", "content": query_text}]
    
    # Make the API call
    console.print("\n[bold blue]Sending query to DeepSeek API...[/bold blue]")
    console.print(Panel(query_text, title="Your Query", border_style="cyan"))
    
    try:
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=messages
        )
        
        # Extract the responses
        reasoning_content = response.choices[0].message.reasoning_content
        content = response.choices[0].message.content
        
        # Display the results with nice formatting
        console.print(Panel(Markdown(reasoning_content), title="💭 Reasoning Process", border_style="green"))
        console.print(Panel(Markdown(content), title="✅ Final Answer", border_style="yellow"))
        
    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {str(e)}")
        
        # Provide more helpful error message for common issues
        if "unauthorized" in str(e).lower():
            console.print("[yellow]Hint:[/yellow] You may need to provide a valid API key using the -k option.")
        elif "connection" in str(e).lower():
            console.print("[yellow]Hint:[/yellow] Check your internet connection or the API base URL.")

def main():
    args = parse_arguments()
    
    if not hasattr(args, 'query') or not args.query:
        console.print("\n[bold red]Error:[/bold red] No query provided.")
        console.print("\n[bold]Usage examples:[/bold]")
        console.print("  ./main.py -q 9.11 and 9.8, which is greater?")
        console.print("  cat ./examples/deepseek_example.py | ./main.py -q explain this code")
        sys.exit(1)
    
    query_deepseek(args.query, api_key=args.api_key, base_url=args.base_url)

if __name__ == "__main__":
    main()