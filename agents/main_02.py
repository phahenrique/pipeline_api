from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.postgres import PostgresTools
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize PostgresTools with connection details
postgres_tools = PostgresTools(
    host="pg-d0loaoidbo4c73ar7vgg-a.oregon-postgres.render.com",
    port=5432,
    db_name="dbname_5q13",
    user="dbname_5q13_user",
    password="dcSkOc3ssPkIGPXSdD4GJDhHMQPd4gj3",
    table_schema="public",
)

# Create an agent with the PostgresTools
agent = Agent(tools=[postgres_tools],
        model=Groq(id="llama-3.3-70b-versatile"))
            

agent.print_response("Fale todas as tabelas do banco de dados", markdown=True)

agent.print_response("""
Faça uma query para pegas todas as cotações de bitcoin na tabela bitcoin_dados""")

agent.print_response("""
Faça uma análise sobre o bitcoin usando os dados da tabela bitcoin_dados""")