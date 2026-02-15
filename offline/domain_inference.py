from __future__ import annotations

from pathlib import Path


KNOWN_DOMAINS = [
    "data_privacy",
    "youth_safety",
    "consumer_protection",
]

GENERAL_DOMAIN = "general_compliance"


DOMAIN_KEYWORDS = {
    "data_privacy": {
        "privacy",
        "personal data",
        "consent",
        "tracking",
        "retention",
        "gdpr",
        "pdpa",
        "pdpl",
        "controller",
        "processor",
    },
    "youth_safety": {
        "minor",
        "child",
        "children",
        "teen",
        "juvenile",
        "parent",
        "guardian",
        "age",
        "cybertipline",
        "ncmec",
    },
    "consumer_protection": {
        "consumer",
        "deceptive",
        "dark pattern",
        "subscription",
        "refund",
        "advertising",
        "manipulative",
        "transparency",
    },
}


def infer_domain(source_path: Path, title: str, body: str) -> str:
    parts = {part.lower() for part in source_path.parts}
    for domain in KNOWN_DOMAINS:
        if domain in parts:
            return domain

    text = f"{title}\n{body}".lower()
    scores: dict[str, int] = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        scores[domain] = sum(1 for keyword in keywords if keyword in text)

    best_domain = max(scores, key=scores.get)
    if scores[best_domain] <= 0:
        return GENERAL_DOMAIN
    return best_domain


def all_domains() -> list[str]:
    return sorted(KNOWN_DOMAINS + [GENERAL_DOMAIN])
