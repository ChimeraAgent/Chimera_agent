import torch
from transformers import AutoTokenizer, AutoModel

class PerceptionModule:
    def __init__(self, model_name="bert-base-uncased"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def process_text(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state

    # Add image and other modalities processing here
    def process_image(self,image):
        # Image processing logic
        pass