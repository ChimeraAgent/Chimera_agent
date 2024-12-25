from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class CognitionModule:
    def __init__(self, openai_api_key):
        self.llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

    def generate_response(self, prompt, context=None):
        if context:
            prompt = f"{prompt}\nContext:{context}"
        return self.llm(prompt)

    def plan_actions(self,goal, current_state):
        #Logic for action planning
        prompt = f"Given the goal:{goal} and current state:{current_state} what is the next action to take?"
        return self.llm(prompt)