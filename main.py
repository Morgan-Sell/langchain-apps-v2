from dotenv import load_dotenv
from langchain.agent.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool

load_dotenv()


def main():
    print("Start...")
    # initializes an agent w/ a prompt that is designed to execute Python code
    python_agent_executor = create_python_agent(llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo"), tool=PythonREPLTool)


if __name__ == "__main__":
    main()
