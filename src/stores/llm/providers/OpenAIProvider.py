from ..LLMinterface import LLMInterface
from openai import OpenAI
import logging

class OpenAIProvider(LLMInterface):
    
    def __init__(self, api_key: str, api_url: str=None,
                 default_input_max_characters: int=1000, 
                 default_generation_output_tokens: int=1000,
                 default_generation_temperature: float=0.1,):
        
        self.api_key = api_key
        self.api_url = api_url
        self.default_input_max_characters = default_input_max_characters
        self.default_generation_output_tokens = default_generation_output_tokens
        self.default_generation_temperature=default_generation_temperature
        
        self.genearation_model_id = None
        self.embedding_model_id = None
        self.embedding_size = None
        
        self.client = OpenAI(
            api_key=self.api_key,
            api_url=self.api_url
        )
        
        self.logger = logging.getLogger(__name__)
    
    
    def set_generation_model(self, model_id: str):
        self.genearation_model_id = model_id
        
    def set_embedding_model(self, model_id, embedding_size):
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size
    
    def generate_text(self, prompt, max_output_tokens,
                      temperature = None):
        raise NotImplementedError
    
    def embed_text(self, text, document_type):
        
        if not self.client:
            
        
        
        