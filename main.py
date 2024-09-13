import pandas as pd

from IPython.display import Markdown, HTML, display
from langchain.schema import HumanMessage
from langchain_openai import AzureChatOpenAI 

model = AzureChatOpenAI(
    openai_api_version="API_VERSION",
    azure_deployment="MODEL_NAME",
    azure_endpoint="YOUR_AZUREOPENAI_ENDPOINT",
    api_key="YOUR_AZURE_API_KEY"
)

df = pd.read_csv("csv_file_path").fillna(value = 0)

from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
agent = create_pandas_dataframe_agent(
    llm=model,
    df=df,
    verbose=True,
    allow_dangerous_code=True,
)

agent.invoke("can you give me the first row of the dataframe?")
