import simpy
import os
import openai
from dotenv import load_dotenv
from use_cases import BusinessUseCase

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

startse = BusinessUseCase()

# name = input("What is your business name? ")
# keywords = input("Before we get started let me know what are the keywords that define your business: ").split(",")
name = "StartSe"
keywords = ["technology", "management", "executive education", "market"]

startse.start_business(name, keywords)
startse.init_key_roles()
startse.init_business_description()
print(startse.get_business_info())
