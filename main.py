from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain_experimental.agents.agent_toolkits import create_python_agent, create_csv_agent
from langchain.chat_models import ChatOpenAI
from langchain_experimental.tools import PythonREPLTool

load_dotenv()


def main():
    print("Start...")
    # initializes an agent w/ a prompt that is designed to execute Python code
    # python_agent_executor = create_python_agent(
    #     llm=ChatOpenAI(temperature=0, model="gpt-4"),
    #     tool=PythonREPLTool(),
    #     agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    #     verbose=True,
    #     handle_parsing_errors=True,
    # )
    #
    # python_agent_executor.run(
    #     """generate and save in the working directory 15 QR codes that points to
    #     www.udemy.com/course/langchain. you have qrcode package already installed""")

    csv_agent = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        path="episode_info.csv",
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        )

    csv_agent.run("print seasons in ascending order of the number of seasons")


if __name__ == "__main__":
    main()
