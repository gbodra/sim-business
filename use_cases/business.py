import time
import datetime
import animation
from faker import Faker
from termcolor import cprint
from entities import BusinessEntity, EmployeeEntity
from use_cases.llm import LLMUseCase


class BusinessUseCase:
    def __init__(self):
        self.__business = None

    @animation.wait()
    def start_business(self, name, keywords):
        print("Getting your business started", end="")
        time.sleep(5)
        self.__business = BusinessEntity()
        self.__business.name = name
        self.__business.keywords = keywords
        self.__business.foundation_date = datetime.date.today()
        self.__business.employees = 0
        self.__business.revenue = 0
        self.__business.products = []
        self.__business.services = []
        self.__business.employees = []
        cprint(" DONE!", "green")

    @animation.wait()
    def init_key_roles(self):
        print("Initializing key roles", end="")
        time.sleep(5)
        key_roles = ["CEO", "CFO", "COO", "CTO", "CHRO", "CRO", "CPO", "CMO"]
        fake = Faker()
        for role in key_roles:
            self.__business.employees.append(EmployeeEntity(fake.name(), [role]))

        cprint(" DONE!", "green")

    @animation.wait()
    def init_business_description(self):
        print("Initializing business description", end="")
        time.sleep(5)
        llm = LLMUseCase(model="gpt-3.5-turbo")
        llm.add_message(role="system", message="You will help the user to describe their businesses based on a few "
                                               "keywords")
        llm.add_message(role="user", message=f"Please create a description for my business which is named "
                                             f"{self.__business.name}. These are the keywords that represent my "
                                             f"business: {self.__business.keywords}")

        result = llm.run()
        self.__business.description = result
        cprint(" DONE!", "green")

    def get_business_info(self):
        info = f"Business name: {self.__business.name}\n" \
               f"Established: {self.__business.foundation_date}\n" \
               f"Description: {self.__business.description}\n" \
               f"Revenue: {self.__business.revenue}"
        return info
