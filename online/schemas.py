from __future__ import annotations

from pydantic import BaseModel, Field


class FeatureRecord(BaseModel):
    feature_name: str = Field(min_length=1)
    feature_description: str = Field(min_length=1)


class WorkflowOutput(BaseModel):
    feature_name: str
    feature_description: str
    needs_geo_compliance: bool
    reasoning: str
    citations: list[str]
    confidence: float
    needs_hitl: bool
    hitl_reason: str
    audit_trail: list[str]
