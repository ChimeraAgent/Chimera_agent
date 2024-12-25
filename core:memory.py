class MemoryModule:
    def __init__(self):
        self.short_term_memory = {}
        self.long_term_memory = {}

    def store_short_term(self, key, value):
        self.short_term_memory[key] = value

    def retrieve_short_term(self, key):
        return self.short_term_memory.get(key)
    
    def store_long_term(self,key,value):
        self.long_term_memory[key] = value
    
    def retrieve_long_term(self,key):
        return self.long_term_memory.get(key)