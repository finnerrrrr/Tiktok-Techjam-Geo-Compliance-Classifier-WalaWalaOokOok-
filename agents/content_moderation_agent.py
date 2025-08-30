from .base_agent import BaseAgent

class ContentModerationAgent(BaseAgent):
    def __init__(self, vdb):
        super().__init__("Content Moderation Agent", vdb)