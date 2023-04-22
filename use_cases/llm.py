import openai
from entities import LLMEntity


class LLMUseCase:
    def __init__(self, model):
        self.__llm = LLMEntity(model)

    def add_message(self, role, message):
        self.__llm.messages.append({"role": role, "content": message})

    def clear_messages(self):
        self.__llm.messages = []

    def run(self):
        request = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.__llm.messages
        )

        result = request["choices"][0]["message"]["content"]

        if result:
            return result.strip()

        return "I'm sorry, I couldn't understand your question"
