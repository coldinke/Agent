import argparse
import os
import sys
import tomli

from openai import OpenAI
from openai import ChatCompletion
from rich.console import Console
from rich.markdown import Markdown


class Config:
    model: str
    model_base_url: str
    api_key: str
    system_prompt: str

    def __init__(self) -> None:
        self.model = "deepseek-reasoner"
        self.model_base_url = "https://api.deepseek.com"
        self.api_key = ""

        self.load_config()

    def load_config(self, config_path=None):
        if config_path is None:
            home_dir = os.path.expanduser("~")
            defalut_paths = [
                os.path.join(home_dir, ".config", "ag", "config.toml"),
                os.path.join(os.getcwd(), "config.toml"),
            ]

        for path in defalut_paths:
            if os.path.exists(path):
                config_path = path
                break

        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, "rb") as f:
                    config_data = tomli.load(f)

                if "model" in config_data:
                    self.model = config_data["model"]
                if "model_base_url" in config_data:
                    self.model_base_url = config_data["model_base_url"]
                if "api_key" in config_data:
                    self.api_key = config_data["api_key"]

            except Exception as e:
                print(f"load config file {config_path} failed!, error is {str(e)}")


class Agent:
    """An agent for V1nci"""

    model: str
    model_base_url: str
    model_api_key: str
    system_prompt: str

    def __init__(self, config):
        self.model = getattr(config, "model", "deepseek-reasoner")
        self.model_base_url = getattr(
            config, "model_base_url", "https://api.deepseek.com"
        )
        self.system_prompt = getattr(
            config, "system_prompt", "You are a helpful assistant."
        )
        api_key = getattr(config, "api_key", "")

        # Initialize OpenAI client
        self.client = OpenAI(api_key=api_key, base_url=self.model_base_url)

    def _get_response(self, messages) -> ChatCompletion:
        """ get response from LLM api use user's input"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        # print(response)
        # print("----------------------------")
        return response

    def email(self, email_content: str):
        """ translate email to English"""
        pass
    def query(self, questions: str):
        messages = [
            {"role": "system", "content": "abc"},
            {"role": "user", "content": questions},
        ]
        response = self._get_response(messages)
        print_markdown(response.model, response.choices[0].message.content)


console = Console()


def print_markdown(model: str, data: str):
    console.print(f":vampire: {model}:")
    console.print(Markdown(data))

def main():
    parser = argparse.ArgumentParser(description="(LLM) Agent for everything.")

    parser.add_argument(
        "instruct", nargs=argparse.REMAINDER, help="All remaining arguments"
    )
    parser.add_argument(
        "-c", "--cot", action="store_true", help="With chain-of-thought reasoning."
    )
    parser.add_argument(
        "-q", "--query", action="store_true", help="Query stdin contents with argv."
    )
    parser.add_argument(
        "-s", "--slides", action="store_true", help="Generate and play slides."
    )
    parser.add_argument(
        "-a",
        "--agent",
        action="store_true",
        help="Chat with agent (more powerful, but slower).",
    )
    parser.add_argument(
        "-e",
        "--email",
        action="store_true",
        help="Revise email (translate to English).",
    )
    parser.add_argument(
        "-r",
        "--revise",
        action="store_true",
        help="Revise the content; produces diff from.",
    )

    args = parser.parse_args()

    config = Config()
    agent = Agent(config=config)

    # print(args.instruct)
    if args.query:
        stdin_contents = sys.stdin.read()
        query_data = f"{args.query}\n{stdin_contents}"
        agent.query(query_data)


if __name__ == "__main__":
    main()
