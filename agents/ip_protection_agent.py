from .base_agent import BaseAgent

class IPProtectionAgent(BaseAgent):
    def __init__(self, vdb):
        super().__init__("IP Protection Agent", vdb)