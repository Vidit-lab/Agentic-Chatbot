from configparser import ConfigParser

class Config:
    #All the constants thar are used in the UI are stored in a configuration file

    #As soon as I create an instance of this class, it will read the configuration file
    def __init__(self,config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config=ConfigParser() 
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")