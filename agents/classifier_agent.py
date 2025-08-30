class ClassifierAgent:
    def __init__(self):
        self.labelled_samples = [
            {
                "feature": "To comply with the Utah Social Media Regulation Act, we are implementing a curfew-based login restriction for users under 18. The system uses ASL to detect minor accounts and routes enforcement through GH to apply only within Utah boundaries. The feature activates during restricted night hours and logs activity using EchoTrace for auditability. This allows parental control to be enacted without user-facing alerts, operating in ShadowMode during initial rollout.",
                "flag": "YES",
                "reasoning": "Explicitly references Utah Social Media Regulation Act; geo-specific compliance logic required.",
                "regulations": ["Utah Social Media Regulation Act"]
            },
            {
                "feature": "As part of compliance with California’s SB976, the app will disable PF by default for users under 18 located in California. This default setting is considered NR to override, unless explicit parental opt-in is provided. Geo-detection is handled via GH, and rollout is monitored with FR logs. The design ensures minimal disruption while meeting the strict personalization requirements imposed by the law.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "In line with the US federal law requiring providers to report child sexual abuse content to NCMEC, this feature scans uploads and flags suspected materials tagged as T5. Once flagged, the CDS auto-generates reports and routes them via secure channel APIs. The logic runs in real-time, supports human validation, and logs detection metadata for internal audits. Regional thresholds are governed by LCP parameters in the backend.",
                "flag": "YES",
                "reasoning": "Explicitly references US NCMEC reporting requirements; geo-specific compliance logic required.",
                "regulations": ["US NCMEC reporting requirements"]
            },
            {
                "feature": "To meet the transparency expectations of the EU Digital Services Act, we are introducing a visibility lock for flagged user-generated content labeled under NSP. When such content is detected, a soft Softblock is applied and GH ensures enforcement is restricted to the EU region only. EchoTrace supports traceability, and Redline status can be triggered for legal review. This feature enhances accountability and complies with Article 16’s removal mechanisms.",
                "flag": "YES",
                "reasoning": "Explicitly references EU Digital Services Act (DSA); geo-specific compliance logic required.",
                "regulations": ["EU Digital Services Act (DSA)"]
            },
            {
                "feature": "To support Florida's Online Protections for Minors law, this feature extends the Jellybean parental control framework. Notifications are dispatched to verified parent accounts when a minor attempts to access restricted features. Using IMT, the system checks behavioral anomalies against BB models. If violations are detected, restrictions are applied in ShadowMode with full audit logging through CDS. Glow flags ensure compliance visibility during rollout phases.",
                "flag": "YES",
                "reasoning": "Description indicates a legal requirement (e.g., age-gating/minors/copyright/consent) that needs geo-specific logic.",
                "regulations": []
            },
            {
                "feature": "Introduce a data retention feature using DRT thresholds, ensuring automatic log deletion across all regions. CDS will continuously audit retention violations, triggering EchoTrace as necessary. Spanner logic ensures all platform modules comply uniformly.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "This feature will automatically detect and tag content that violates NSP policy. Once flagged, Softblock is applied and a Redline alert is generated if downstream sharing is attempted.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "When users report content containing high-risk information, it is tagged as T5 for internal routing. CDS then enforces escalation. The system is universal and does not rely on regional toggles or GH routes.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "Snowcap is activated for all underage users platform-wide, applying ASL to segment accounts. Actions taken under this logic are routed to CDS and monitored using BB to identify deviations in usage.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "By default, PF will be turned off for all uses browsing in guest mode.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "Enable users to reshare stories from others, with auto-expiry after 48 hours. This feature logs resharing attempts with EchoTrace and stores activity under BB.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "Introduce a creator leaderboard updated weekly using internal analytics. Points and rankings are stored in FR metadata and tracked using IMT.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "Adjust PF recommendations based on inferred mood signals from emoji usage. This logic is soft-tuned using BB and undergoes quiet testing in ShadowMode.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "At onboarding, users will receive NR-curated profiles to follow for faster network building. A/B testing will use Spanner.",
                "flag": "NO",
                "reasoning": "Description indicates business-driven geofence/experiment without legal basis.",
                "regulations": []
            },
            {
                "feature": "Monetization events will be tracked through CDS to detect anomalies in creator payouts. DRT rules apply for log trimming.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "Roll out video reply functionality to users in EEA only. GH will manage exposure control, and BB is used to baseline feedback.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "Launch a PF variant in CA as part of early experimentation. Spanner will isolate affected cohorts and Glow flags will monitor feature health.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "A new chat layout will be tested in the following regions: CA, US, BR, ID. GH will ensure location targeting and ShadowMode will collect usage metrics without user impact.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "Enable video autoplay only for users in US. GH filters users, while Spanner logs click-through deltas.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "A/B test dark theme accessibility for users in South Korea. Rollout is limited via GH and monitored with FR flags.",
                "flag": "NO",
                "reasoning": "Description indicates business-driven geofence/experiment without legal basis.",
                "regulations": []
            },
            {
                "feature": "Notifications will be tailored by age using ASL, allowing us to throttle or suppress push alerts for minors. EchoTrace will log adjustments, and CDS will verify enforcement across rollout waves.",
                "flag": "YES",
                "reasoning": "Description indicates a legal requirement (e.g., age-gating/minors/copyright/consent) that needs geo-specific logic.",
                "regulations": []
            },
            {
                "feature": "Enforce message content constraints by injecting LCP rules on delivery. ShadowMode will initially deploy the logic for safe validation. No explicit mention of legal requirements, but privacy context is implied.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "Introduce limits on video uploads from new accounts. IMT will trigger thresholds based on BB patterns. These limitations are partly for platform safety but without direct legal mapping.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "A flow that detects high-risk comment content and routes it via CDS with Redline markers. The logic applies generally and is monitored through EchoTrace, with no mention of regional policies.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "Behavioral scoring via Spanner will be used to gate access to certain tools. The feature tracks usage and adjusts gating based on BB divergence.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "We are expanding chat features, but for users flagged by Jellybean, certain functions (e.g., media sharing) will be limited. BB and ASL will monitor compliance posture.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "New suggestion logic uses PF to recommend friends, but minors are excluded from adult pools using ASL and CDS logic. EchoTrace logs interactions in case future policy gates are needed.",
                "flag": "YES",
                "reasoning": "Description indicates a legal requirement (e.g., age-gating/minors/copyright/consent) that needs geo-specific logic.",
                "regulations": []
            },
            {
                "feature": "Enable GIFs in comments, while filtering content deemed inappropriate for minor accounts. Softblock will apply if a flagged GIF is used by ASL-flagged profiles.",
                "flag": "YES",
                "reasoning": "Description indicates a legal requirement (e.g., age-gating/minors/copyright/consent) that needs geo-specific logic.",
                "regulations": []
            },
            {
                "feature": "Longform post creation is now open to all. However, moderation for underage authors is stricter via Snowcap.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "Users can now design custom avatars. For safety, T5 triggers block adult-themed assets from use by underage profiles. Age detection uses ASL and logs flow through GH.",
                "flag": "UNCERTAIN",
                "reasoning": "No explicit regulation or clear legal obligation detected; needs human evaluation.",
                "regulations": []
            },
            {
                "feature": "Test a new recommendation algorithm for video content in Japan, using Spanner to isolate test cohorts and Glow flags to monitor engagement metrics.",
                "flag": "NO",
                "reasoning": "Description indicates business-driven experiment without legal basis.",
                "regulations": []
            },
            {
                "feature": "Introduce a premium subscription tier with exclusive filters, rolled out globally with A/B testing via Spanner and tracked using FR logs.",
                "flag": "NO",
                "reasoning": "Description indicates business-driven feature without legal basis.",
                "regulations": []
            },
            {
                "feature": "Enable a new emoji reaction set for posts, with regional rollout in Brazil controlled by GH and monitored via EchoTrace for user engagement.",
                "flag": "NO",
                "reasoning": "Description indicates business-driven geofence/experiment without legal basis.",
                "regulations": []
            },
            {
                "feature": "Launch a gamified badge system for active users, with points tracked via IMT and displayed in FR metadata. Limited to US users during initial testing.",
                "flag": "NO",
                "reasoning": "Description indicates business-driven geofence/experiment without legal basis.",
                "regulations": []
            },
            {
                "feature": "Test a new search interface in India, using ShadowMode to collect usage data via Spanner without affecting user experience.",
                "flag": "NO",
                "reasoning": "Description indicates business-driven geofence/experiment without legal basis.",
                "regulations": []
            },
            {
                "feature": "Roll out a live streaming feature in select regions (AU, NZ) with GH managing access and BB tracking engagement metrics.",
                "flag": "NO",
                "reasoning": "Description indicates business-driven geofence/experiment without legal basis.",
                "regulations": []
            },
            {
                "feature": "Introduce a story highlight feature for creators, with analytics stored in CDS and A/B testing conducted via Spanner.",
                "flag": "NO",
                "reasoning": "Description indicates business-driven feature without legal basis.",
                "regulations": []
            },
            {
                "feature": "Enable a new profile customization option globally, with usage tracked via EchoTrace and performance monitored using Glow flags.",
                "flag": "NO",
                "reasoning": "Description indicates business-driven feature without legal basis.",
                "regulations": []
            },
            {
                "feature": "Test a simplified onboarding flow in the EU, with GH ensuring regional targeting and Spanner logging user retention metrics.",
                "flag": "NO",
                "reasoning": "Description indicates business-driven geofence/experiment without legal basis.",
                "regulations": []
            },
            {
                "feature": "Launch a content discovery carousel in Canada, with engagement tracked via BB and isolated testing via Spanner.",
                "flag": "NO",
                "reasoning": "Description indicates business-driven geofence/experiment without legal basis.",
                "regulations": []
            },
            {
                "feature": "Implement age verification for users in Germany to comply with the Jugendmedienschutz-Staatsvertrag, using ASL to identify minors and GH to enforce restrictions within Germany. EchoTrace logs compliance checks, and CDS ensures auditability.",
                "flag": "YES",
                "reasoning": "Explicitly references Jugendmedienschutz-Staatsvertrag; geo-specific compliance logic required.",
                "regulations": ["Jugendmedienschutz-Staatsvertrag"]
            },
            {
                "feature": "Introduce mandatory cookie consent banners for UK users to comply with the UK GDPR. GH restricts enforcement to the UK, and Softblock applies to non-compliant sessions. FR logs track user interactions.",
                "flag": "YES",
                "reasoning": "Explicitly references UK GDPR; geo-specific compliance logic required.",
                "regulations": ["UK GDPR"]
            },
            {
                "feature": "Enforce data breach notification rules for Canadian users under PIPEDA, using CDS to generate alerts and GH to limit enforcement to Canada. Redline markers flag incidents for legal review.",
                "flag": "YES",
                "reasoning": "Explicitly references PIPEDA; geo-specific compliance logic required.",
                "regulations": ["PIPEDA"]
            },
            {
                "feature": "Restrict targeted advertising for minors in Australia per the Australian Privacy Principles. ASL identifies underage users, and GH ensures enforcement within Australia. EchoTrace logs ad-serving decisions.",
                "flag": "YES",
                "reasoning": "Explicitly references Australian Privacy Principles; geo-specific compliance logic required.",
                "regulations": ["Australian Privacy Principles"]
            },
            {
                "feature": "Apply content moderation for hate speech in France under the Loi Avia, with NSP-tagged content receiving Softblock via GH routing. CDS logs moderation actions for transparency.",
                "flag": "YES",
                "reasoning": "Explicitly references Loi Avia; geo-specific compliance logic required.",
                "regulations": ["Loi Avia"]
            },
            {
                "feature": "Enable parental consent mechanisms for users under 16 in the EU to comply with GDPR Article 8. GH enforces regional targeting, and Jellybean framework verifies consent. EchoTrace logs compliance.",
                "flag": "YES",
                "reasoning": "Explicitly references GDPR Article 8; geo-specific compliance logic required.",
                "regulations": ["GDPR Article 8"]
            },
            {
                "feature": "Implement data localization for Indian users under the Personal Data Protection Bill, using DRT to manage storage and GH to restrict data to Indian servers. CDS audits compliance.",
                "flag": "YES",
                "reasoning": "Explicitly references Personal Data Protection Bill; geo-specific compliance logic required.",
                "regulations": ["Personal Data Protection Bill"]
            },
            {
                "feature": "Restrict access to certain content categories in Saudi Arabia per the Anti-Cyber Crime Law, with GH ensuring regional enforcement and BB monitoring user interactions. Softblock applies to restricted content.",
                "flag": "YES",
                "reasoning": "Explicitly references Anti-Cyber Crime Law; geo-specific compliance logic required.",
                "regulations": ["Anti-Cyber Crime Law"]
            },
            {
                "feature": "Enable transparency reports for content takedowns in Brazil to comply with Marco Civil da Internet, using CDS to log actions and GH to limit enforcement to Brazil. Redline alerts trigger legal review.",
                "flag": "YES",
                "reasoning": "Explicitly references Marco Civil da Internet; geo-specific compliance logic required.",
                "regulations": ["Marco Civil da Internet"]
            },
            {
                "feature": "Apply mandatory age-gating for South Korean users under the Personal Information Protection Act, with ASL detecting minors and GH enforcing restrictions. EchoTrace logs compliance for audits.",
                "flag": "YES",
                "reasoning": "Explicitly references Personal Information Protection Act; geo-specific compliance logic required.",
                "regulations": ["Personal Information Protection Act"]
            }
        ]

    def classify(self, aggregated, query):
        """Mock classification: Flag, reasoning, regulations based on aggregated context"""
        chunks = aggregated['chunks']
        audit_trail = aggregated.get('audit_trail', [])

        # Mock logic: Check for keywords to determine flag
        content_combined = ' '.join([chunk['content'].lower() for chunk in chunks])
        regulations = list(set([chunk['citation'] for chunk in chunks if chunk['citation'] != 'No Citation']))

        if 'law' in content_combined or 'regulation' in content_combined or 'compliance' in content_combined:
            flag = "YES"
            reasoning = "Feature requires geo-specific logic due to legal obligations identified in chunks."
        elif 'business' in content_combined or 'market' in content_combined or 'testing' in content_combined:
            flag = "NO"
            reasoning = "Appears business-driven, no legal geo-specific requirement."
        else:
            flag = "UNCERTAIN"
            reasoning = "Uncertain; no clear legal or business indicators."

        # Incorporate HITL override if present
        if 'hitl_override' in aggregated:
            override = aggregated['hitl_override']
            if override['flag']:
                flag = override['flag']
            if override['rationale']:
                reasoning = override['rationale'] + " (HITL override)"

        # Add labelled samples comparison to reasoning
        reasoning += "\nBased on similar examples:\n"
        for sample in self.labelled_samples:
            reasoning += f"- {sample['feature']}: {sample['flag']} ({sample['reasoning']})\n"

        # Audit trail
        audit_trail.append(f"Classification: {flag}, Reasoning: {reasoning[:50]}..., Regulations: {regulations}")
        audit_trail.append("Labelled samples used for comparison.")

        return {
            'flag': flag,
            'reasoning': reasoning,
            'regulations': regulations,
            'audit_trail': audit_trail
        }
