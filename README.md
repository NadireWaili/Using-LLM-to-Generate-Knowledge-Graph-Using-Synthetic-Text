# Using-LLM-to-Generate-Knowledge-Graph-Using-Synthetic-Text

## Overview
This project extracts entities, relationships, and personality traits from text and builds a **knowledge graph**. It evaluates personality trait extraction against ground truth data using **F1 score metrics**.

Key features:  
- Extracts entities: people, organizations, locations, and personality traits.  
- Uses enhanced **OCEAN trait mapping** for personality analysis.  
- Builds a multi-entity knowledge graph with **NetworkX**.  
- Graph visualization with color-coded nodes and a comprehensive legend.  
- Calculates **precision, recall, and F1 score** for personality trait extraction.  

---


## Data
Data is synthesized data from LLM, specifically Deepseek for this project. Text includes both character and paragraph element, example would be: 
Character= ["name": "Sarah Chen", "role": "Product Manager", "organization": "TechInnovate Inc",
     "location": "San Francisco", "base_traits": {"openness": "medium", "conscientiousness": "high",
     "extraversion": "medium", "agreeableness": "medium", "neuroticism": "low"},
     "relationships": {"manages": ["David Rodriguez", "Emily Watson"], "reports_to": "Maria Lopez",
                       "collaborates_with": ["Mark Thompson"]}],
Paragraph=[ "Product Manager Sarah Chen displayed remarkable conscientiousness and organizational skills during the Q1 product planning session at San Francisco headquarters. She meticulously reviewed every user story while maintaining a balanced approach to team feedback, showing her medium agreeableness."]

## 🛠️ Features

- **Enhanced Trait Mapping** – maps adjectives and traits to OCEAN dimensions.  
- **F1 Evaluation** – calculates precision, recall, and F1 for each character's traits.  
- **Graph Visualization** – interactive layout showing connections between entities.  
- **Extensible** – easy to add new entities, relationships, or traits.

## Install Dependencies
pip install networkx matplotlib

## Example Output
✅ F1 Trait Metrics:
{'precision': 0.818, 'recall': 0.45, 'f1': 0.581, 'tp': 9, 'fp': 2, 'fn': 11}

  


