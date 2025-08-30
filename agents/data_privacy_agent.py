from .base_agent import BaseAgent

class DataPrivacyAgent(BaseAgent):
    def __init__(self, vdb):
        super().__init__("Data Privacy Agent", vdb)