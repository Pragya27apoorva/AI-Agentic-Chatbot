 Large Language Models (LLMs) and multi agent 
AI systems have shown strong capabilities in reasoning, retrieval, 
and decision-making tasks. However, most such systems operate 
as black boxes, offering limited transparency into their internal 
processes. This paper proposes a traceable multi-agent AI system 
using Retrieval-Augmented Generation (RAG) and LangChain to 
improve explainability and accountability. The architecture 
consists of three specialized agents: a Classifier Agent for query 
intent analysis, a Retriever Agent for semantic retrieval using 
vector embeddings and cosine similarity, and a Decision Agent for 
validating retrieved information before response generation. The 
system is trained on six domain-specific research papers 
segmented into 536 text chunks stored in a vector database. For 
each query, the system generates fact-grounded responses along 
with traceability metrics such as processing time, accuracy level, 
and token usage. The proposed framework demonstrates 
improved transparency, auditability, and trustworthiness, 
contributing to the advancement of Explainable Artificial 
Intelligence (XAI). 
