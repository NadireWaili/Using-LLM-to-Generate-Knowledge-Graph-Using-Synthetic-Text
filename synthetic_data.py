"""
Enhanced Synthetic Data for Comprehensive Knowledge Graph
Includes multiple entity types for rich knowledge representation
"""

# Character profiles (now with additional attributes)
CHARACTERS = [
    {
        "name": "Sarah Chen",
        "role": "Product Manager",
        "organization": "TechInnovate Inc",
        "location": "San Francisco",
        "base_traits": {
            "openness": "medium",
            "conscientiousness": "high", 
            "extraversion": "medium",
            "agreeableness": "medium",
            "neuroticism": "low"
        }
    },
    {
        "name": "David Rodriguez",
        "role": "UX Designer", 
        "organization": "TechInnovate Inc",
        "location": "New York",
        "base_traits": {
            "openness": "high",
            "conscientiousness": "low",
            "extraversion": "low",
            "agreeableness": "high",
            "neuroticism": "high"
        }
    },
    {
        "name": "Maria Lopez",
        "role": "CEO",
        "organization": "TechInnovate Inc",
        "location": "San Francisco",
        "base_traits": {
            "openness": "medium",
            "conscientiousness": "high",
            "extraversion": "high", 
            "agreeableness": "medium",
            "neuroticism": "low"
        }
    },
    {
        "name": "Mark Thompson",
        "role": "Project Manager",
        "organization": "TechInnovate Inc", 
        "location": "Austin",
        "base_traits": {
            "openness": "low",
            "conscientiousness": "high",
            "extraversion": "medium",
            "agreeableness": "low", 
            "neuroticism": "medium"
        }
    },
    {
        "name": "Emily Watson",
        "role": "Software Developer",
        "organization": "TechInnovate Inc",
        "location": "Seattle",
        "base_traits": {
            "openness": "high",
            "conscientiousness": "medium",
            "extraversion": "low",
            "agreeableness": "high",
            "neuroticism": "low"
        }
    }
]

# Enhanced paragraphs with multiple entity types and relationships
PARAGRAPHS = [
    # Text 1: Corporate structure and personality
    "Sarah Chen, the Product Manager at TechInnovate Inc headquarters in San Francisco, demonstrated her high conscientiousness during the quarterly planning meeting. She meticulously reviewed every user story while David Rodriguez, based in the New York office, proposed innovative research methods that challenged conventional approaches at the company.",
    
    # Text 2: Leadership and events
    "During the annual Tech Leadership Conference in Las Vegas, CEO Maria Lopez delivered a keynote about artificial intelligence adoption. Her presentation impressed stakeholders from Global Ventures Corporation and sparked discussions about future partnerships between the two companies.",
    
    # Text 3: Project management and locations
    "The Q3 product launch event was coordinated by Mark Thompson from the Austin development center. The team faced challenges with the Seattle deployment but Emily Watson's technical expertise helped resolve critical infrastructure issues at the AWS data centers.",
    
    # Text 4: Team dynamics and concepts
    "At the design sprint workshop in Chicago, David showed high openness by exploring unconventional user interface concepts. However, budget constraints identified by Finance Department required scaling back the initial project scope for the mobile application development.",
    
    # Text 5: Client relationships and business context
    "During client negotiations with MegaCorp International, Sarah's medium agreeableness helped maintain positive relationships while Mark's strict adherence to project timelines occasionally created tension. The meeting at the Boston convention center resulted in a revised delivery schedule.",
    
    # Text 6: Crisis management and personality under pressure
    "When the production outage occurred at the primary data center in Virginia, David's high neuroticism became apparent as he anxiously monitored system metrics. In contrast, Maria remained calm and coordinated the incident response team across multiple time zones.",
    
    # Text 7: Innovation and collaboration
    "Emily's proposal to integrate machine learning capabilities into the core platform was approved during the innovation review at Silicon Valley Labs. She collaborated with the Research and Development team to prototype the new features ahead of the Developer Conference.",
    
    # Text 8: Strategic planning and market context
    "The board meeting at TechInnovate Inc's San Francisco headquarters addressed market competition from rival company NextGen Solutions. Maria presented the new strategic roadmap while Sarah provided detailed analytics on customer adoption trends across different regions."
]

# Additional entities for richer knowledge graph
ORGANIZATIONS = [
    "TechInnovate Inc",
    "Global Ventures Corporation", 
    "MegaCorp International",
    "NextGen Solutions",
    "Silicon Valley Labs",
    "AWS",
    "Finance Department",
    "Research and Development"
]

LOCATIONS = [
    "San Francisco",
    "New York", 
    "Austin",
    "Seattle",
    "Las Vegas",
    "Chicago",
    "Boston",
    "Virginia",
    "Silicon Valley"
]

EVENTS = [
    "quarterly planning meeting",
    "Tech Leadership Conference",
    "Q3 product launch event", 
    "design sprint workshop",
    "client negotiations",
    "innovation review",
    "board meeting",
    "Developer Conference"
]

CONCEPTS = [
    "artificial intelligence",
    "budget constraints",
    "mobile application development",
    "production outage",
    "machine learning", 
    "market competition",
    "strategic roadmap",
    "customer adoption trends"
]

def get_all_texts():
    """Return all paragraphs for processing"""
    return PARAGRAPHS

def get_character_names():
    """Return list of all character names"""
    return [char["name"] for char in CHARACTERS]

def get_character_traits(character_name):
    """Get base traits for a specific character"""
    for char in CHARACTERS:
        if char["name"] == character_name:
            return char["base_traits"]
    return None

def get_organizations():
    """Return all organizations"""
    return ORGANIZATIONS

def get_locations():
    """Return all locations"""
    return LOCATIONS

def get_events():
    """Return all events"""
    return EVENTS

def get_concepts():
    """Return all concepts"""
    return CONCEPTS

if __name__ == "__main__":
    print(f"📊 Enhanced Synthetic Data Summary:")
    print(f"   Characters: {len(CHARACTERS)}")
    print(f"   Paragraphs: {len(PARAGRAPHS)}")
    print(f"   Organizations: {len(ORGANIZATIONS)}")
    print(f"   Locations: {len(LOCATIONS)}")
    print(f"   Events: {len(EVENTS)}")
    print(f"   Concepts: {len(CONCEPTS)}")