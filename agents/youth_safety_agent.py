from .base_agent import BaseAgent

class YouthSafetyAgent(BaseAgent):
    def __init__(self, vdb):
        super().__init__("Youth Safety Agent", vdb)