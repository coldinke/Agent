# from rich import print
import sys

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.text import Text
from rich.prompt import Prompt

# print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

console = Console()

# console.print("\n[bold blue]Sending query to DeepSeek API...[/bold blue]")
# console.print(Panel("query test", title="Your Query", border_style="cyan"))

reasoning_content = """
Okay, so I need to figure out whether 9.11 is greater than 9.8 or if 9.8 is greater than 9.11. Hmm, let's start by looking at both numbers. They both have a 9 before the decimal point, so the whole number parts are the same. That means the difference has to be in the decimal parts. 

First, let me write them out with the same number of decimal places to make it easier to compare. So, 9.11 is the same as 9.11, and 9.8 can be written as 9.80. Now, when I look at them side by side, it's 9.11 versus 9.80. 

Comparing the tenths place first. In 9.11, the tenths digit is 1, and in 9.80, the tenths digit is 8. Since 8 is greater than 1, that would mean 9.80 is larger than 9.11, right? Wait, but maybe I need to check the hundredths place too? Let me think. 

In 9.11, after the tenths place, there's another 1 in the hundredths place. In 9.80, after the tenths place, there's a 0 in the hundredths place. But since the tenths place in 9.80 is already higher (8 vs. 1), the hundredths place doesn't matter here. It's like when you compare numbers digit by digit from left to right. Once a digit is larger in one number, the rest don't affect the comparison. 

So, even though 9.11 has a 1 in the hundredths place and 9.80 has a 0 there, the 8 in the tenths place of 9.80 makes it bigger overall. Therefore, 9.8 (or 9.80) is greater than 9.11. Let me verify this by converting them to fractions or maybe subtracting one from the other.

If I subtract 9.11 from 9.8, what do I get? Let's see: 9.8 minus 9.11. That's 0.69. Since the result is positive, that means 9.8 is indeed larger by 0.69. Alternatively, if I subtract 9.8 from 9.11, I would get a negative number, which also confirms that 9.11 is smaller. 

Another way to think about it is by considering money. If these numbers were amounts of money, $9.11 versus $9.80. Which is more? $9.80 is 80 cents, which is more than 11 cents, so $9.80 is more. Yeah, that makes sense. 

Or maybe using a number line. Visualizing the numbers on a number line, 9.11 is just a little past 9.1, while 9.8 is much closer to 10. So, 9.8 would be further to the right, indicating a larger value. 

I think that's solid. The key here is recognizing that even though 9.11 has more decimal places, the value of each digit position decreases by a factor of 10 as you move to the right. So the tenths place is worth more than the hundredths place, hence 8 tenths outweigh 1 tenth plus 1 hundredth. 

Wait, let me break that down. In 9.11, the decimal part is 0.11, which is 1 tenth and 1 hundredth. In 9.8, which is 9.80, the decimal part is 0.80, which is 8 tenths and 0 hundredths. Comparing 0.80 and 0.11, clearly 0.80 is larger. Therefore, 9.8 is greater. 

Just to ensure I haven't made a mistake, let me convert both to fractions over 100. 

9.11 is 9 + 11/100 = 911/100. 

9.8 is 9 + 8/10 = 9 + 80/100 = 980/100. 

Comparing 911/100 and 980/100, obviously 980 is greater than 911, so 980/100 (which is 9.8) is greater. 

Yep, that checks out. So, 9.8 is greater than 9.11. 

I guess another common mistake might be thinking that because 11 is more than 8, 9.11 is more than 9.8, but that's incorrect because the decimal places are fractions. The first decimal place is tenths, so 0.8 is equivalent to 0.80, which is much larger than 0.11. 

So in summary, when comparing decimals, you start from the leftmost digit after the decimal and move right, comparing each corresponding place value. The first place where they differ determines which number is larger. In this case, the tenths place differs with 8 being greater than 1, so 9.8 is greater than 9.11.

**Final Answer**
The greater number is \boxed{9.8}.
content:  To determine whether 9.11 or 9.8 is greater, we start by comparing the whole number parts. Both numbers have the same whole number part, which is 9. Next, we compare the decimal parts.

First, we write 9.8 as 9.80 to have the same number of decimal places as 9.11:
- 9.11
- 9.80

We compare the tenths place:
- In 9.11, the tenths digit is 1.
- In 9.80, the tenths digit is 8.

Since 8 is greater than 1, we can conclude that 9.80 is greater than 9.11 without needing to compare the hundredths place. 

To verify, we can subtract:
- \( 9.80 - 9.11 = 0.69 \) (a positive result, confirming 9.80 is greater).

Converting to fractions:
- 9.11 as a fraction is \( \frac{911}{100} \).
- 9.80 as a fraction is \( \frac{980}{100} \).

Since \( 980 \) is greater than \( 911 \), \( \frac{980}{100} \) (which is 9.80) is greater.

Thus, the greater number is \boxed{9.8}.
"""

content = """
 To determine whether 9.11 or 9.8 is greater, we start by comparing the whole number parts. Both numbers have the same whole number part, which is 9. Next, we compare the decimal parts.

First, we write 9.8 as 9.80 to have the same number of decimal places as 9.11:
- 9.11
- 9.80

We compare the tenths place:
- In 9.11, the tenths digit is 1.
- In 9.80, the tenths digit is 8.

Since 8 is greater than 1, we can conclude that 9.80 is greater than 9.11 without needing to compare the hundredths place. 

To verify, we can subtract:
- \( 9.80 - 9.11 = 0.69 \) (a positive result, confirming 9.80 is greater).

Converting to fractions:
- 9.11 as a fraction is \( \frac{911}{100} \).
- 9.80 as a fraction is \( \frac{980}{100} \).

Since \( 980 \) is greater than \( 911 \), \( \frac{980}{100} \) (which is 9.80) is greater.

Thus, the greater number is \boxed{9.8}.
"""

# console.print(Panel(Markdown(reasoning_content), title="💭 Reasoning Process", border_style="green"))
# console.print(Markdown(content))

# def display_user_message(message):
#     """Displays the user's message in a styled panel."""
#     panel = Panel(Text(f"^D:\n{message}", style="green"), title="User", border_style="green")
#     console.print(panel)

# def display_llm_message(message, title="Deepseek"):
#     """Displays the LLM's message in a styled panel."""
#     panel = Panel(Text(message, style="blue"), title=title, border_style="blue")
#     console.print(panel)


USER_PROMPT_PREFIX = ":robot ^D:\n"
# LLM_PROMPT_PREFIX = f":robot {}: {}"

def display_user_message():
    """Displays the user's message with a prefix."""
    console.print(Text(f"{USER_PROMPT_PREFIX}", style="green"))
    sys.stdin.read()

def display_llm_message(message):
    """Displays the LLM's message with a prefix."""
    console.print(Text(f"{LLM_PROMPT_PREFIX}{message}", style="blue"))

display_user_message()