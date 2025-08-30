from .base_agent import BaseAgent

class AIGovernanceAgent(BaseAgent):
    def __init__(self, vdb):
        super().__init__("AI Governance Agent", vdb)