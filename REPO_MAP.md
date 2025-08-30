
Format: HTML
max tokens
50000

All Extensions

Base path: root
±8411 tokens


Copy
├── README.md
├── agents
    ├── base_agent.py
    └── youth_safety_agent.py
├── assets
    └── agent_workflow.png
├── kb
    ├── consumer_protection
    │   └── EU_DSA_A25.txt
    ├── data_privacy
    │   └── SG_PDPA2012.txt
    └── youth_safety
    │   ├── CA_SB976.txt
    │   ├── EU_DSA_A28.txt
    │   └── FL_HB3.txt
├── pilot.py
└── utils
    ├── rag.py
    └── semanticchunker.py


/README.md:
--------------------------------------------------------------------------------
 1 | 
 2 | # GeoLogicClassifer123
 3 | 
 4 | ![Alt text](assets/agent_workflow.png)
 5 | 
 6 | 
 7 | # From Guesswork to Governance — High-Level Agent Overview
 8 | 
 9 | ## Pipeline (at a glance)
10 | Query Prep → Domain Agents → Reranker → Verifier → (HITL if needed) → Aggregator → Classifier → Output & Audit
11 | 
12 | ---
13 | 
14 | ## 1) Query Prep Agent
15 | **What:** Normalize feature artifacts and extract key signals.  
16 | **Task:** Clean text, resolve codenames/jargon, detect intent & geo, add synonyms/triggers, emit an enriched query.
17 | 
18 | ## 2) Domain Agents (xN)
19 | **What:** Per-domain retrieval (e.g., youth safety, reporting/CSAM, EU DSA).  
20 | **Task:** Pull top candidate law chunks with citations and jurisdiction tags using hybrid lexical+semantic search.
21 | 
22 | ## 3) Reranker Agent
23 | **What:** Precision pass over the candidates.  
24 | **Task:** Re-rank with a cross-encoder and apply diversity (MMR) to select a small, high-signal, non-redundant set.
25 | 
26 | ## 4) Verifier Agent
27 | **What:** Turn “relevant text” into grounded evidence.  
28 | **Task:** Check geo/citation alignment, score evidence quality, decide **verified** vs **low confidence**, and surface supporting/conflicting snippets.
29 | 
30 | ## 5) HITL (Human-in-the-Loop)
31 | **What:** Fast human review for edge cases.  
32 | **Task:** Present top evidence and suggested label; capture overrides/rationales when confidence is low or geo/citation is unclear.
33 | 
34 | ## 6) Aggregator Agent
35 | **What:** Build the final context bundle.  
36 | **Task:** Deduplicate citations, balance facets (regs/jurisdictions), and assemble a compact context + audit metadata for classification.
37 | 
38 | ## 7) Classifier Agent
39 | **What:** Produce the final triage label with traceability.  
40 | **Task:** Output **YES/NO/UNCERTAIN** with a short reason, referenced regulations, and citation IDs; include a self-confidence score.
41 | 
42 | ## 8) Outputs & Audit Trail
43 | **What:** Submission artifacts and compliance evidence.  
44 | **Task:** Write CSV/JSONL containing the decision, reasoning, citations, sentence indices, scores, thresholds, and any HITL overrides.
45 | 


--------------------------------------------------------------------------------
/agents/base_agent.py:
--------------------------------------------------------------------------------
 1 | # agents/base_agent.py
 2 | from abc import ABC, abstractmethod
 3 | from langchain.schema import BaseRetriever
 4 | 
 5 | class BaseAgent(ABC):
 6 |     def __init__(self, name, retriever: BaseRetriever):
 7 |         self.name = name
 8 |         self.retriever = retriever
 9 | 
10 |     @abstractmethod
11 |     def analyze_feature(self, feature_description: str) -> dict:
12 |         """
13 |         Analyze a feature description. Must return a dict with:
14 |         {
15 |             "requires_geo_compliance": bool,
16 |             "reasoning": str,
17 |             "related_regulations": list
18 |         }
19 |         """
20 |         pass
21 | 
22 |     def _retrieve_context(self, query: str, k: int = 5) -> str:
23 |         """Retrieves relevant context from the agent's knowledge base."""
24 |         docs = self.retriever.get_relevant_documents(query)
25 |         context = "\n\n".join([doc.page_content for doc in docs])
26 |         sources = [{"chunk text": doc.page_content, "source": doc.metadata.get("source", "unknown"), 
27 |                    "chunk_number": doc.metadata.get("chunk_number", "unknown")} 
28 |                   for doc in docs]
29 |         return context, sources
30 | 
31 |     def _create_optimized_query(self, feature_description: str) -> str:
32 |         """Simple query optimization. Override this in child classes for more sophistication."""
33 |         # For a robust version, you'd use an LLM here as discussed.
34 |         # This is a simple placeholder.
35 |         return f"{feature_description} legal compliance regulation law"


--------------------------------------------------------------------------------
/agents/youth_safety_agent.py:
--------------------------------------------------------------------------------
 1 | # agents/youth_safety_agent.py
 2 | from .base_agent import BaseAgent
 3 | # Use the updated, non-deprecated import:
 4 | from langchain_openai import ChatOpenAI  # <- FIXED IMPORT
 5 | from langchain.prompts import ChatPromptTemplate
 6 | 
 7 | 
 8 | 
 9 | 
10 | class YouthSafetyAgent(BaseAgent):
11 |     def __init__(self, retriever):
12 |         super().__init__("Youth Safety Agent", retriever)
13 |         # Define the prompt template here
14 |         self.prompt_template = ChatPromptTemplate.from_messages([
15 |             ("system", "You are a meticulous youth safety and protection compliance officer. Your goal is to prevent harm to minors. Analyze the following feature description using ONLY the context provided from relevant laws. If a feature could potentially harm minors or violate protections, you MUST flag it."),
16 |             ("human", """
17 |             **Feature Description to Analyze:**
18 |             {feature_description}
19 | 
20 |             **Relevant Legal Context:**
21 |             {context}
22 | 
23 |             **Your Task:**
24 |             1. Determine if this feature requires geo-specific compliance logic due to youth safety concerns.
25 |             2. If yes, list every country/region and cite the specific law and article that triggers the requirement.
26 |             3. Provide clear, auditable reasoning for your decision.
27 |             4. If no issues are found based on the context, state that.
28 | 
29 |             Output your final analysis in the following structured format:
30 |             - Requires Geo-Compliance Logic: [Yes/No/Unclear]
31 |             - Reasoning: [Your reasoning here]
32 |             - Related Regulations: [List of laws or 'None']
33 |             """)
34 |         ])
35 | 
36 |     def analyze_feature(self, feature_description: str) -> dict:
37 |         # Create the LLM object HERE, when the method is called
38 |         llm = ChatOpenAI(model="gpt-3.5-turbo")
39 |         
40 |         # Step 1: Create an optimized query
41 |         query = self._create_optimized_query(feature_description)
42 |         # Step 2: Retrieve relevant context and source metadata
43 |         context, sources = self._retrieve_context(query, k=5)
44 |         # Step 3: Fill in the prompt template
45 |         prompt = self.prompt_template.format_messages(
46 |             feature_description=feature_description,
47 |             context=context
48 |         )
49 |         # Step 4: Get the analysis from the LLM
50 |         analysis_result = llm.invoke(prompt).content
51 | 
52 |         # Step 5: Parse the result and add source information
53 |         result = self._parse_llm_output(analysis_result)
54 |         # Add source metadata to the reasoning
55 |         source_info = f"\nSources: {sources}"
56 |         result["reasoning"] = result["reasoning"] + source_info
57 |         return result
58 | 
59 |     def _parse_llm_output(self, text: str) -> dict:
60 |         """Parses the LLM's text output into a structured dict."""
61 |         lines = text.split('\n')
62 |         result = {
63 |             "requires_geo_compliance": "Yes" in lines[0],
64 |             "reasoning": lines[1].replace("- Reasoning: ", "").strip(),
65 |             "related_regulations": lines[2].replace("- Related Regulations: ", "").strip()
66 |         }
67 |         return result


--------------------------------------------------------------------------------
/assets/agent_workflow.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/51fc399a7b060eee06832cdae3e07660cba6487b/assets/agent_workflow.png


--------------------------------------------------------------------------------
/kb/consumer_protection/EU_DSA_A25.txt:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/finnerrrrr/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-/51fc399a7b060eee06832cdae3e07660cba6487b/kb/consumer_protection/EU_DSA_A25.txt


--------------------------------------------------------------------------------
/kb/data_privacy/SG_PDPA2012.txt:
--------------------------------------------------------------------------------
  1 | Personal Data Protection
  2 | Act 2012
  3 | 2020 REVISED EDITION
  4 | This revised edition incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021
  5 | An Act to govern the collection, use and disclosure of personal data by organisations, and to establish the Do Not Call Register and to provide for its administration, and for matters connected therewith.
  6 | [22/2016]
  7 | [2 January 2013: Parts I, II, VIII, IX (except sections 36 to 38, 41 and 43 to 48) and X (except section 67(1)), and the First, Seventh and Ninth Schedules ;
  8 | 2 December 2013: Sections 36, 37, 38 and 41 ;
  9 | 2 January 2014: Sections 43 to 48 and 67(1) and the Eighth Schedule ;
 10 | 2 July 2014: Parts III to VII, and the Second to Sixth Schedules ]
 11 | PART 1
 12 | PRELIMINARY
 13 | Short title
 14 | 1.  This Act is the Personal Data Protection Act 2012.
 15 | Interpretation
 16 | 2.—(1)  In this Act, unless the context otherwise requires —
 17 | “advisory committee” means an advisory committee appointed under section 7;
 18 | “Appeal Committee” means a Data Protection Appeal Committee constituted under section 48P(4), read with the Seventh Schedule;
 19 | “Appeal Panel” means the Data Protection Appeal Panel established by section 48P(1);
 20 | “authorised officer”, in relation to the exercise of any power or performance of any function or duty under any provision of this Act, means a person to whom the exercise of that power or performance of that function or duty under that provision has been delegated under section 38 of the Info‑communications Media Development Authority Act 2016;
 21 | “Authority” means the Info‑communications Media Development Authority established by section 3 of the Info‑communications Media Development Authority Act 2016;
 22 | “benefit plan” means an insurance policy, a pension plan, an annuity, a provident fund plan or other similar plan;
 23 | “business” includes the activity of any organisation, whether or not carried on for purposes of gain, or conducted on a regular, repetitive or continuous basis, but does not include an individual acting in his or her personal or domestic capacity;
 24 | “business contact information” means an individual’s name, position name or title, business telephone number, business address, business electronic mail address or business fax number and any other similar information about the individual, not provided by the individual solely for his or her personal purposes;
 25 | “Chief Executive”, in relation to the Authority, means the Chief Executive of the Authority appointed under section 40(2) of the Info‑communications Media Development Authority Act 2016, and includes any individual acting in that capacity;
 26 | “Commission” means the person designated as the Personal Data Protection Commission under section 5 to be responsible for the administration of this Act;
 27 | “Commissioner” means the Commissioner for Personal Data Protection appointed under section 8(1)(a), and includes any Deputy Commissioner for Personal Data Protection or Assistant Commissioner for Personal Data Protection appointed under section 8(1)(b);
 28 | “credit bureau” means an organisation which —
 29 | (a)	provides credit reports for gain or profit; or
 30 | (b)	provides credit reports on a routine, non‑profit basis as an ancillary part of a business carried on for gain or profit;
 31 | “credit report” means a communication, whether in written, oral or other form, provided to an organisation to assess the creditworthiness of an individual in relation to a transaction between the organisation and the individual;
 32 | “data intermediary” means an organisation which processes personal data on behalf of another organisation but does not include an employee of that other organisation;
 33 | “derived personal data”  —
 34 | (a)	means personal data about an individual that is derived by an organisation in the course of business from other personal data, about the individual or another individual, in the possession or under the control of the organisation; but
 35 | (b)	does not include personal data derived by the organisation using any prescribed means or method;
 36 | “document” includes information recorded in any form;
 37 | “domestic” means related to home or family;
 38 | “education institution” means an organisation that provides education, including instruction, training or teaching, whether by itself or in association or collaboration with, or by affiliation with, any other person;
 39 | “employee” includes a volunteer;
 40 | “employment” includes working under an unpaid volunteer work relationship;
 41 | “evaluative purpose” means —
 42 | (a)	the purpose of determining the suitability, eligibility or qualifications of the individual to whom the data relates —
 43 | (i)	for employment or for appointment to office;
 44 | (ii)	for promotion in employment or office or for continuance in employment or office;
 45 | (iii)	for removal from employment or office;
 46 | (iv)	for admission to an education institution;
 47 | (v)	for the awarding of contracts, awards, bursaries, scholarships, honours or other similar benefits;
 48 | (vi)	for selection for an athletic or artistic purpose; or
 49 | (vii)	for grant of financial or social assistance, or the delivery of appropriate health services, under any scheme administered by a public agency;
 50 | (b)	the purpose of determining whether any contract, award, bursary, scholarship, honour or other similar benefit should be continued, modified or cancelled;
 51 | (c)	the purpose of deciding whether to insure any individual or property or to continue or renew the insurance of any individual or property; or
 52 | (d)	such other similar purposes as the Minister may prescribe;
 53 | “individual” means a natural person, whether living or deceased;
 54 | “inspector” means an individual appointed as an inspector under section 8(1)(b);
 55 | “investigation” means an investigation relating to —
 56 | (a)	a breach of an agreement;
 57 | (b)	a contravention of any written law, or any rule of professional conduct or other requirement imposed by any regulatory authority in exercise of its powers under any written law; or
 58 | (c)	a circumstance or conduct that may result in a remedy or relief being available under any law;
 59 | “national interest” includes national defence, national security, public security, the maintenance of essential services and the conduct of international affairs;
 60 | “organisation” includes any individual, company, association or body of persons, corporate or unincorporated, whether or not —
 61 | (a)	formed or recognised under the law of Singapore; or
 62 | (b)	resident, or having an office or a place of business, in Singapore;
 63 | “personal data” means data, whether true or not, about an individual who can be identified —
 64 | (a)	from that data; or
 65 | (b)	from that data and other information to which the organisation has or is likely to have access;
 66 | “prescribed healthcare body” means a healthcare body prescribed for the purposes of the Second Schedule by the Minister charged with the responsibility for health;
 67 | “prescribed law enforcement agency” means an authority charged with the duty of investigating offences or charging offenders under written law, prescribed for the purposes of sections 21(4) and 26D(6) and the Second Schedule by the Minister charged with the responsibility for that authority;
 68 | “private trust” means a trust for the benefit of one or more designated individuals who are the settlor’s friends or family members;
 69 | “proceedings” means any civil, criminal or administrative proceedings by or before a court, tribunal or regulatory authority that is related to the allegation of —
 70 | (a)	a breach of an agreement;
 71 | (b)	a contravention of any written law or any rule of professional conduct or other requirement imposed by any regulatory authority in exercise of its powers under any written law; or
 72 | (c)	a wrong or a breach of a duty for which a remedy is claimed under any law;
 73 | “processing”, in relation to personal data, means the carrying out of any operation or set of operations in relation to the personal data, and includes any of the following:
 74 | (a)	recording;
 75 | (b)	holding;
 76 | (c)	organisation, adaptation or alteration;
 77 | (d)	retrieval;
 78 | (e)	combination;
 79 | (f)	transmission;
 80 | (g)	erasure or destruction;
 81 | “public agency” includes —
 82 | (a)	the Government, including any ministry, department, agency, or organ of State;
 83 | (b)	any tribunal appointed under any written law; or
 84 | (c)	any statutory body specified under subsection (2);
 85 | “publicly available”, in relation to personal data about an individual, means personal data that is generally available to the public, and includes personal data which can be observed by reasonably expected means at a location or an event —
 86 | (a)	at which the individual appears; and
 87 | (b)	that is open to the public;
 88 | “relevant body” means the Commission, the Appeal Panel or any Appeal Committee;
 89 | “tribunal” includes a judicial or quasi‑judicial body or a disciplinary, an arbitral or a mediatory body;
 90 | “user activity data”, in relation to an organisation, means personal data about an individual that is created in the course or as a result of the individual’s use of any product or service provided by the organisation;
 91 | “user‑provided data”, in relation to an organisation, means personal data provided by an individual to the organisation.
 92 | [22/2016; 40/2020]
 93 | (2)  The Minister may, by notification in the Gazette, specify any statutory body established under a public Act for a public function to be a public agency for the purposes of this Act.
 94 | Purpose
 95 | 3.  The purpose of this Act is to govern the collection, use and disclosure of personal data by organisations in a manner that recognises both the right of individuals to protect their personal data and the need of organisations to collect, use or disclose personal data for purposes that a reasonable person would consider appropriate in the circumstances.
 96 | Application of Act
 97 | 4.—(1)  Parts 3, 4, 5, 6, 6A and 6B do not impose any obligation on —
 98 | (a)	any individual acting in a personal or domestic capacity;
 99 | (b)	any employee acting in the course of his or her employment with an organisation;
100 | (c)	any public agency; or
101 | (d)	any other organisations or personal data, or classes of organisations or personal data, prescribed for the purposes of this provision.
102 | [40/2020]
103 | (2)  Parts 3, 4, 5, 6 (except sections 24 and 25), 6A (except sections 26C(3)(a) and 26E) and 6B do not impose any obligation on a data intermediary in respect of its processing of personal data on behalf of and for the purposes of another organisation pursuant to a contract which is evidenced or made in writing.
104 | [40/2020]
105 | (3)  An organisation has the same obligation under this Act in respect of personal data processed on its behalf and for its purposes by a data intermediary as if the personal data were processed by the organisation itself.
106 | (4)  This Act does not apply in respect of —
107 | (a)	personal data about an individual that is contained in a record that has been in existence for at least 100 years; or
108 | (b)	personal data about a deceased individual, except that the provisions relating to the disclosure of personal data and section 24 (protection of personal data) apply in respect of personal data about an individual who has been dead for 10 years or less.
109 | (5)  Except where business contact information is expressly mentioned, Parts 3, 4, 5, 6 and 6A do not apply to business contact information.
110 | [40/2020]
111 | (6)  Unless otherwise expressly provided in this Act —
112 | (a)	nothing in Parts 3, 4, 5, 6, 6A and 6B affects any authority, right, privilege or immunity conferred, or obligation or limitation imposed, by or under the law, including legal privilege, except that the performance of a contractual obligation is not an excuse for contravening this Act; and
113 | (b)	the provisions of other written law prevail to the extent that any provision of Parts 3, 4, 5, 6, 6A and 6B is inconsistent with the provisions of that other written law.
114 | [40/2020]
115 | 


--------------------------------------------------------------------------------
/kb/youth_safety/CA_SB976.txt:
--------------------------------------------------------------------------------
 1 | California Senate Bill No. 967 2024
 2 | 
 3 | 
 4 | Senate Bill No. 976
 5 | CHAPTER 321
 6 | 
 7 | An act to add Chapter 24 (commencing with Section 27000) to Division 20 of the Health and Safety Code, relating to youth addiction.
 8 | 
 9 | [ Approved by Governor  September 20, 2024. Filed with Secretary of State  September 20, 2024. ]
10 | 
11 | LEGISLATIVE COUNSEL'S DIGEST
12 | 
13 | SB 976, Skinner. Protecting Our Kids from Social Media Addiction Act.
14 | Existing law, the California Age-Appropriate Design Code Act, requires, beginning July 1, 2024, a business that provides an online service, product, or feature likely to be accessed by children to comply with certain requirements. The act requires the business to complete a data protection impact assessment addressing, among other things, whether the design could harm children and whether and how the online product, service, or feature uses system design features to increase, sustain, or extend use of the online product, service, or feature by children, including the automatic playing of media, rewards for time spent, and notifications. Existing law prohibits the business from using the personal information of any child in a way that the business knows, or has reason to know, is materially detrimental to the physical health, mental health, or well-being of a child.
15 | Existing law, the Privacy Rights for California Minors in the Digital World, prohibits an operator of an internet website, online service, online application, or mobile application from specified conduct when minors are involved, including the marketing or advertising of alcoholic beverages, firearms, or certain other products or services. Existing law sets forth other related protections for minors, including under the California Consumer Privacy Act of 2018 and the California Privacy Rights Act of 2020.
16 | This bill, the Protecting Our Kids from Social Media Addiction Act, would make it unlawful for the operator of an addictive internet-based service or application, as defined, to provide an addictive feed to a user, unless the operator does not have actual knowledge that the user is a minor; commencing January 1, 2027, has reasonably determined that the user is not a minor; or has obtained verifiable parental consent to provide an addictive feed to the user who is a minor.
17 | The bill would define “addictive feed” as an internet website, online service, online application, or mobile application, in which multiple pieces of media generated or shared by users are recommended, selected, or prioritized for display to a user based on information provided by the user, or otherwise associated with the user or the user’s device, as specified, unless any of certain conditions are met.
18 | The bill would make it unlawful for the operator of an addictive internet-based service or application, between the hours of 12 a.m. and 6 a.m., in the user’s local time zone, and between the hours of 8 a.m. and 3 p.m., Monday through Friday from September through May in the user’s local time zone, to send notifications to a user if the operator has actual knowledge that the user is a minor or, commencing January 1, 2027, has not reasonably determined that the user is not a minor, unless the operator has obtained verifiable parental consent to send those notifications, as specified. The bill would set forth related provisions for certain access controls determined by the verified parent through a mechanism provided by the operator.
19 | Under the bill, a parent’s provision of consent or use of a mechanism, as described above, would not waive, release, otherwise limit, or serve as a defense to, any claim that the parent, or that the user who is a minor or was a minor at the time of using the internet-based service or application, might have against the operator regarding any harm to the mental health or well-being of the user.
20 | The bill would require an operator to annually disclose the number of minor users of its addictive internet-based service or application, and of that total the number for whom the operator has received verifiable parental consent to provide an addictive feed, and the number of minor users as to whom the access controls are or are not enabled.
21 | Under the bill, these provisions would only be enforced in a civil action brought in the name of the people of the State of California by the Attorney General. The bill would require the Attorney General to adopt regulations to further the purposes of these provisions, including regulations regarding age assurance and parental consent by January 1, 2027. The bill would authorize the Attorney General to adopt regulations that provide for exceptions to these provisions, but only if those exceptions further the purpose of protecting minors. The bill would require the Attorney General, in promulgating regulations, to solicit public comment regarding the impact that any regulation might have based on certain nondiscrimination characteristics set forth in existing law.


--------------------------------------------------------------------------------
/kb/youth_safety/EU_DSA_A28.txt:
--------------------------------------------------------------------------------
 1 | EU Digital Services Act Article 28 2022
 2 | 
 3 | 
 4 | Article 28, Online protection of minors - the Digital Services Act (DSA)
 5 | 
 6 | 
 7 | 1. Providers of online platforms accessible to minors shall put in place appropriate and proportionate measures to ensure a high level of privacy, safety, and security of minors, on their service.
 8 | 
 9 | 
10 | 2. Providers of online platform shall not present advertisements on their interface based on profiling as defined in Article 4, point (4), of Regulation (EU) 2016/679 using personal data of the recipient of the service when they are aware with reasonable certainty that the recipient of the service is a minor.
11 | 
12 | 
13 | 3. Compliance with the obligations set out in this Article shall not oblige providers of online platforms to process additional personal data in order to assess whether the recipient of the service is a minor.
14 | 
15 | 
16 | 4. The Commission, after consulting the Board, may issue guidelines to assist providers of online platforms in the application of paragraph 1.


--------------------------------------------------------------------------------
/kb/youth_safety/FL_HB3.txt:
--------------------------------------------------------------------------------
 1 | Florida House Bill 3 2024
 2 | 
 3 | 
 4 | THE FLORIDA SENATE 
 5 | 2024 SUMMARY OF LEGISLATION PASSED 
 6 | Committee on Judiciary 
 7 | CS/CS/HB 3 — Online Protections for Minors 
 8 | by Judiciary Committee; Regulatory Reform & Economic Development Subcommittee; and 
 9 | Reps. Tramont, Overdorf, Sirois, McFarland, Rayner, and others (CS/SB 1792 by Judiciary 
10 | Committee and Senators Grall and Garcia) 
11 | 
12 | 
13 | The bill requires regulated social media platforms to prohibit minors younger than 14 years of 
14 | age from entering into contracts with social media platforms to become account holders. It 
15 | allows minors who are 14 or 15 years of age to become account holders, but only with the 
16 | consent of a parent or guardian. Social media platforms are regulated under the bill if they:  
17 | • Allow users to upload content or view the content or activity of other users.  
18 | • Satisfy certain daily active user metrics identified in the bill. 
19 | • Employ algorithms that analyze user data or information on users to select content for 
20 | users.  
21 | • Have certain addictive features.  
22 | With respect to all accounts belonging to minors younger than 14, and to those accounts 
23 | belonging to minors who are 14 or 15 years of age but for whom parents or guardians have not 
24 | provided consent, the bill requires regulated social media platforms to terminate them and also 
25 | allows the account holders or their parents or guardians to terminate them. Social media 
26 | platforms must permanently delete all personal information held by them relating to terminated 
27 | accounts unless otherwise required by law to maintain the personal information.  
28 | The bill also requires regulated commercial entities that knowingly and intentionally publish or 
29 | distribute material harmful to minors on a website or application to prohibit access to such 
30 | material by any person younger than 18 years of age, if their website or application contains a 
31 | substantial portion of material that is harmful to minors. Such commercial entities must verify, 
32 | using either an anonymous or standard age verification method, that the age of a person 
33 | attempting to access the material harmful to minors satisfies the bill’s age requirements. If an 
34 | anonymous age verification method is used, the verification must be conducted by a 
35 | nongovernmental, independent third party organized under the laws of a state of the U.S. Any 
36 | information used to verify age must be deleted once the age is verified. 
37 | Regulated social media platforms, commercial entities, and third parties performing age 
38 | verification for commercial entities that knowingly and recklessly violate the bill’s requirements 
39 | are subject to enforcement under the Florida Deceptive and Unfair Trade Practices Act. The 
40 | Department of Legal Affairs may collect civil penalties of up to $50,000 per violation, 
41 | reasonable attorney fees and court costs, and (under certain conditions) punitive damages. 
42 | Account holders who are minors may also pursue up to $10,000 in damages. 


--------------------------------------------------------------------------------
/pilot.py:
--------------------------------------------------------------------------------
 1 | # pilot.py
 2 | from agents.youth_safety_agent import YouthSafetyAgent
 3 | # from agents.data_privacy_agent import DataPrivacyAgent  # You'll create this similarly
 4 | from utils.rag import get_vector_db, embedding_model
 5 | import os
 6 | 
 7 | # Initialize all agents with their respective knowledge bases
 8 | def initialize_agents():
 9 |     agents = []
10 |     
11 |     # Initialize Youth Safety Agent
12 |     youth_safety_db_path = "./kb/youth_safety_chromadb" # Path to store/load the vector DB
13 |     youth_safety_kb_path = "./kb/youth_safety"          # Path to raw .txt files
14 |     
15 |     # Check if vector DB exists, if not, create it
16 |     if not os.path.exists(youth_safety_db_path):
17 |         from utils.rag import create_vector_db_from_dir
18 |         youth_vectordb = create_vector_db_from_dir(
19 |             youth_safety_kb_path, youth_safety_db_path, embedding_model
20 |         )
21 |     else:
22 |         youth_vectordb = get_vector_db(youth_safety_db_path, embedding_model)
23 |     
24 |     youth_retriever = youth_vectordb.as_retriever(search_kwargs={"k": 5})
25 |     agents.append(YouthSafetyAgent(youth_retriever))
26 |     
27 |     # Initialize Data Privacy Agent (Repeat the same process)
28 |     # data_privacy_db_path = "./kb/data_privacy_chromadb"
29 |     # data_privacy_kb_path = "./kb/data_privacy"
30 |     # ... [Create/get vector DB]
31 |     # agents.append(DataPrivacyAgent(data_retriever))
32 |     
33 |     return agents
34 | 
35 | def main():
36 |     # 1. Initialize all specialist agents
37 |     print("Initializing agents and loading knowledge bases...")
38 |     specialist_agents = initialize_agents()
39 |     
40 |     # 2. Get the feature description (this could be from user input, a file, etc.)
41 |     feature_description = """
42 |     Feature Title: Mood-based personalized feed enhancements
43 |     Description: Adjust personalized feed recommendations based on inferred mood signals from emoji usage. This logic is soft-tuned using baseline behaviour and undergoes quiet testing in a non-user-impact way to collect analytics only.
44 |     """
45 |     
46 |     print(f"\nAnalyzing feature: {feature_description}")
47 |     
48 |     # 3. Send the feature to EVERY agent for analysis
49 |     all_results = {}
50 |     for agent in specialist_agents:
51 |         print(f"\n--- Consulting {agent.name} ---")
52 |         result = agent.analyze_feature(feature_description)
53 |         all_results[agent.name] = result
54 |         print(f"Result: {result}")
55 |     
56 |     # 4. Consolidate and present the final results
57 |     print("\n=== FINAL COMPLIANCE ASSESSMENT ===")
58 |     for agent_name, result in all_results.items():
59 |         print(f"\n{agent_name}:")
60 |         print(f"  Requires Geo-Compliance Logic: {result['requires_geo_compliance']}")
61 |         print(f"  Reasoning: {result['reasoning']}")
62 |         print(f"  Related Regulations: {result['related_regulations']}")
63 | 
64 | if __name__ == "__main__":
65 |     main()


--------------------------------------------------------------------------------
/utils/rag.py:
--------------------------------------------------------------------------------
 1 | # utils/rag.py
 2 | from langchain.text_splitter import RecursiveCharacterTextSplitter
 3 | from langchain_community.vectorstores import Chroma
 4 | from langchain_community.embeddings import HuggingFaceEmbeddings
 5 | from langchain.schema import Document
 6 | import os
 7 | from . import semanticchunker as sc
 8 | 
 9 | def create_vector_db_from_dir(directory_path, persist_directory, embedding_model):
10 |     documents = []
11 |     for filename in os.listdir(directory_path):
12 |         if not filename.endswith(".txt"):
13 |             continue
14 |         filepath = os.path.join(directory_path, filename)
15 |         try:
16 |             chunked_doc = sc.get_chunks(filepath)  # List[str]
17 |         except Exception as e:
18 |             print(f"[RAG] Skipping {filename}: {e}")
19 |             continue
20 | 
21 |         if not chunked_doc:
22 |             print(f"[RAG] Skipping {filename}: produced 0 chunks")
23 |             continue
24 | 
25 |         for i, chunk in enumerate(chunked_doc):
26 |             documents.append(
27 |                 Document(page_content=chunk, metadata={"source": filename, "chunk_number": i})
28 |             )
29 | 
30 |     if not documents:
31 |         raise ValueError(f"No usable .txt files found in {directory_path}")
32 | 
33 |     vectordb = Chroma.from_documents(
34 |         documents=documents,
35 |         embedding=embedding_model,
36 |         persist_directory=persist_directory
37 |     )
38 |     vectordb.persist()
39 |     return vectordb
40 | 
41 | 
42 | def get_vector_db(persist_directory, embedding_model):
43 |     """Loads an existing Chroma vector database."""
44 |     vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding_model)
45 |     return vectordb
46 | 
47 | # Use a good open-source embedding model
48 | embedding_model = HuggingFaceEmbeddings(
49 |     model_name="sentence-transformers/all-MiniLM-L6-v2"
50 | )


--------------------------------------------------------------------------------
/utils/semanticchunker.py:
--------------------------------------------------------------------------------
  1 | import nltk
  2 | import openai
  3 | import os
  4 | import re
  5 | from pathlib import Path
  6 | from dotenv import load_dotenv
  7 | from nltk.tokenize import sent_tokenize
  8 | from langchain.chat_models import init_chat_model
  9 | from langchain_core.prompts import ChatPromptTemplate
 10 | from pydantic import BaseModel, Field
 11 | 
 12 | nltk.download('punkt')
 13 | 
 14 | project_root = Path(__file__).resolve().parent.parent
 15 | dotenv_path = project_root / '.env'
 16 | load_dotenv(dotenv_path=dotenv_path)
 17 | 
 18 | apikey = os.environ.get("OPENAI_API_KEY")
 19 | # print(apikey)
 20 | 
 21 | # _file = "C:\\Users\\Teh Ze Shi\\OneDrive\\schoolwork\TT Techjam 2025\\lol\\kb\\youth_safety\\CA_SB967.txt"
 22 | _file = "C:\\Users\\Teh Ze Shi\\OneDrive\\schoolwork\TT Techjam 2025\\lol\\kb\\youth_safety\\FL_HB3.txt"
 23 | 
 24 | class Chunk(BaseModel):
 25 |     id: int = Field(description="Chunk index starting at 0")
 26 |     sentence_ids: list[int] = Field(
 27 |         description="Ordered sentence indices that belong to this chunk"
 28 |     )
 29 | 
 30 | class SemanticChunks(BaseModel):
 31 |     chunks: list[Chunk] = Field(
 32 |         description="List of chunks; each has an id and its sentence indices"
 33 |     )
 34 | 
 35 | def open_txt(txtfile):
 36 |     try:
 37 |         file = open(txtfile, encoding='utf-8')
 38 |         return file.read()
 39 |     except Exception as e:
 40 |         print(e)
 41 |         return None
 42 | 
 43 | # Initialize structured llm function
 44 | def init_llm():
 45 |     try:
 46 |         llm = init_chat_model("gpt-4o-mini", model_provider="openai")
 47 |         structured_llm = llm.with_structured_output(SemanticChunks)
 48 |         return structured_llm
 49 |     except openai.APIError as e:
 50 |         print(f"An API error occurred: {e}")
 51 | 
 52 | 
 53 | def split_and_index_doc(legi_doc_txt: str):
 54 |     legi_doc = open_txt(legi_doc_txt)
 55 |     if not legi_doc or not legi_doc.strip():
 56 |         # make cause obvious to caller
 57 |         raise ValueError(f"Empty or unreadable file: {legi_doc_txt}")
 58 | 
 59 |     # normalize newlines
 60 |     legi_doc = legi_doc.replace("\r\n", "\n").replace("\r", "\n")
 61 | 
 62 |     # primary sentence split
 63 |     legi_doc_split = sent_tokenize(legi_doc)
 64 | 
 65 |     # fallback if tokenizer yields nothing
 66 |     if not legi_doc_split:
 67 |         # split on punctuation or newlines as a last resort
 68 |         legi_doc_split = [s.strip() for s in re.split(r'(?<=[\.\?\!])\s+|\n+', legi_doc) if s.strip()]
 69 | 
 70 |     # still nothing? raise
 71 |     if not legi_doc_split:
 72 |         raise ValueError(f"No sentences tokenized for: {legi_doc_txt}")
 73 | 
 74 |     sentence_idx = {}
 75 |     legi_doc_split_idxed = []
 76 |     for i, sentence in enumerate(legi_doc_split):
 77 |         legi_doc_split_idxed.append(f"<{i}>{sentence}</{i}>")
 78 |         sentence_idx[i] = sentence
 79 | 
 80 |     out_str = " ".join(legi_doc_split_idxed)
 81 |     return out_str, sentence_idx
 82 | 
 83 | 
 84 | def get_chunks(doc, model=None):
 85 |     if not model:
 86 |         model = init_llm()
 87 | 
 88 |     processed_doc, reconstruction_index = split_and_index_doc(doc)
 89 | 
 90 |     # if somehow empty, bail out early (caller can skip file)
 91 |     if not reconstruction_index:
 92 |         return []
 93 | 
 94 |     chunking_prompt = ChatPromptTemplate.from_template(
 95 |         """You are an expert at splitting text into smaller chunks without breaking context.
 96 |         Each sentence in the input has a numeric index in <index>sentence</index> tags.
 97 |         Return ONLY the fields defined in the SemanticChunking schema.
 98 | 
 99 |         Rules:
100 |         - Keep sentences in original order within each chunk.
101 |         - Do not skip indices you include; no duplicates within a chunk.
102 |         - Prefer 1-2 sentences per chunk if sentences are short, but just 1 if sentences are long.
103 | 
104 |         Text to split:
105 |         {text}"""
106 |     )
107 | 
108 |     chunking_prompt_w_text = chunking_prompt.invoke({"text": processed_doc})
109 |     chunks = model.invoke(chunking_prompt_w_text)
110 | 
111 |     reconstructed_chunks = []
112 | 
113 |     # (optional) keep your prints if you like
114 |     # print(reconstruction_index.keys())
115 |     for chunk in chunks.chunks:
116 |         print(chunk)
117 |         chunk_sentences = []
118 |         for sentence_idx in chunk.sentence_ids:
119 |             # **GUARD**: only append if index exists
120 |             if sentence_idx in reconstruction_index:
121 |                 chunk_sentences.append(reconstruction_index[sentence_idx])
122 |             # else silently skip bad indices from the model
123 |         if chunk_sentences:
124 |             reconstructed_chunks.append(" ".join(chunk_sentences))
125 | 
126 |     # If the model returned only bad indices, make a single fallback chunk
127 |     if not reconstructed_chunks:
128 |         reconstructed_chunks = [" ".join(reconstruction_index[i] for i in sorted(reconstruction_index))]
129 | 
130 |     return reconstructed_chunks


--------------------------------------------------------------------------------
 Add to README

Other Tools
API

