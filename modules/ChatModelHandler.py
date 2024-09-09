from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from modules.DataHandler import LoadData
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

class LLMLoader:
    """
    Class responsible for loading the LLM and determining the correct table 
    to which a given prompt belongs, based on a list of columns from extracted from the data.
    
    Attributes:
        model_name (str): The name of the language model to load, using ChatOpenAI options.
    """
    
    def __init__(self, model_name: str):
        self.model_name = model_name

    def load_llm(self):
        return ChatOpenAI(temperature=0, model_name=self.model_name)
    
    def determine_table_from_prompt(self, prompt: str) -> str:
        """
        Determines the appropriate table to use in the flow based on the given prompt.
        
        Parameters:
            prompt (str): The prompt or question to analyze.
        
        Returns:
            str: The name of the CSV file corresponding to the table, or 'no_valid' if no match is found.
        """
        
        ld = LoadData()

        columns_str = str(ld.get_column_names()).replace('[','').replace('],',';').replace('{','').replace('}','').replace("'","")
        
        prompt_template = f"""
        Given this question/request: {prompt}, respond with a single word (file+.csv) indicating which table you think it belongs to. These are the tables with their respective columns:
        {columns_str}
        If you think it is not a question related to tables or is not related to the task, answer with the token no_valid
        """
        
        formated_prompt_template = PromptTemplate(input_variables=["request"], template=prompt_template)
        
        llm = self.load_llm()
        chain = formated_prompt_template | llm
        
        try:
            res = chain.invoke(input={"request": prompt})
            result = res.content.strip()
            if not result.endswith(".csv"):
                result+=".csv"
            logging.info(f"Table selected: {result}")
            return result
        
        except Exception as e:
            logging.error(f"Error during LLM processing: {e}")
            return "Error"



