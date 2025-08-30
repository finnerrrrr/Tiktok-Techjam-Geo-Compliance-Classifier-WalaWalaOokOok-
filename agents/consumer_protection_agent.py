from .base_agent import BaseAgent

class ConsumerProtectionAgent(BaseAgent):
    def __init__(self, vdb):
        super().__init__("Consumer Protection Agent", vdb)