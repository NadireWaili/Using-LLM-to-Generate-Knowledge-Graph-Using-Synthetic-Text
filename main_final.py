"""
COMPREHENSIVE KNOWLEDGE GRAPH BUILDER - FINAL VERSION
Includes enhanced visualization, legend, F1 trait evaluation, and all assessment criteria
"""

import os
import re
from collections import defaultdict

# =============================================================================
# DEPENDENCY CHECK
# =============================================================================
try:
    import networkx as nx
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    print("✅ All dependencies loaded successfully")
except ImportError as e:
    print(f"❌ Missing dependencies: {e}")
    print("📋 Please run: pip install networkx matplotlib")
    exit(1)

# =============================================================================
# SYNTHETIC DATA
# =============================================================================
CHARACTERS = [
    {"name": "Sarah Chen", "role": "Product Manager", "organization": "TechInnovate Inc",
     "location": "San Francisco", "base_traits": {"openness": "medium", "conscientiousness": "high",
     "extraversion": "medium", "agreeableness": "medium", "neuroticism": "low"},
     "relationships": {"manages": ["David Rodriguez", "Emily Watson"], "reports_to": "Maria Lopez",
                       "collaborates_with": ["Mark Thompson"]}},
    {"name": "David Rodriguez", "role": "UX Designer", "organization": "TechInnovate Inc",
     "location": "New York", "base_traits": {"openness": "high", "conscientiousness": "low",
     "extraversion": "low", "agreeableness": "high", "neuroticism": "high"},
     "relationships": {"reports_to": "Sarah Chen", "mentors": ["Junior Designers"],
                       "collaborates_with": ["Emily Watson", "Frontend Team"]}},
    {"name": "Maria Lopez", "role": "CEO", "organization": "TechInnovate Inc",
     "location": "San Francisco", "base_traits": {"openness": "medium", "conscientiousness": "high",
     "extraversion": "high", "agreeableness": "medium", "neuroticism": "low"},
     "relationships": {"leads": ["Sarah Chen", "Mark Thompson", "Executive Team"],
                       "boards": ["TechInnovate Inc", "Startup Advisory Board"]}},
    {"name": "Mark Thompson", "role": "Project Manager", "organization": "TechInnovate Inc",
     "location": "Austin", "base_traits": {"openness": "low", "conscientiousness": "high",
     "extraversion": "medium", "agreeableness": "low", "neuroticism": "medium"},
     "relationships": {"reports_to": "Maria Lopez", "manages": ["Development Team", "QA Team"],
                       "coordinates_with": ["Sarah Chen", "Vendor Partners"]}},
    {"name": "Emily Watson", "role": "Lead Software Developer", "organization": "TechInnovate Inc",
     "location": "Seattle", "base_traits": {"openness": "high", "conscientiousness": "medium",
     "extraversion": "low", "agreeableness": "high", "neuroticism": "low"},
     "relationships": {"reports_to": "Sarah Chen", "leads": ["Backend Team", "Infrastructure Team"],
                       "collaborates_with": ["David Rodriguez", "Mark Thompson"]}},
    {"name": "Alex Kim", "role": "Data Scientist", "organization": "TechInnovate Inc",
     "location": "Boston", "base_traits": {"openness": "high", "conscientiousness": "high",
     "extraversion": "low", "agreeableness": "medium", "neuroticism": "low"},
     "relationships": {"reports_to": "Emily Watson", "specializes_in": ["Machine Learning", "Data Analytics"]}}
]

PARAGRAPHS = [
    "During the quarterly executive retreat in Lake Tahoe, CEO Maria Lopez demonstrated exceptional strategic vision and emotional stability while presenting the company's ambitious 5-year roadmap to the board of directors. Her high extraversion was evident as she energized the entire leadership team.",
    "Product Manager Sarah Chen displayed remarkable conscientiousness and organizational skills during the Q1 product planning session at San Francisco headquarters. She meticulously reviewed every user story while maintaining a balanced approach to team feedback, showing her medium agreeableness.",
    "UX Designer David Rodriguez, working from the New York creative hub, showcased his high openness and creativity by proposing a revolutionary interface design that challenged industry conventions. However, his high neuroticism surfaced during client presentations when he became visibly anxious about critical feedback.",
    "Lead Developer Emily Watson, based in Seattle, demonstrated both high openness and technical excellence when she architected the new microservices platform. Her low extraversion was apparent as she preferred deep technical discussions over large team meetings.",
    "Project Manager Mark Thompson, coordinating from the Austin development center, exhibited his high conscientiousness through meticulous timeline management during the critical Q3 launch. His low agreeableness occasionally created tension when he enforced strict deadlines with the development team.",
    "During the crisis management drill, Maria's low neuroticism and high conscientiousness helped her calmly coordinate the incident response team across multiple time zones, while David's high neuroticism made him particularly sensitive to the simulated pressure scenarios.",
    "The cross-functional workshop in Chicago revealed interesting team dynamics: Sarah's medium openness allowed her to bridge creative and technical perspectives, while Mark's low openness initially resisted unconventional approaches proposed by David's highly creative team.",
    "Data Scientist Alex Kim, joining from the Boston research lab, demonstrated high openness and conscientiousness when integrating machine learning capabilities into the core platform, collaborating effectively with Emily's backend team.",
    "During high-stakes negotiations with MegaCorp International in their Dallas headquarters, Sarah's medium agreeableness helped maintain positive client relationships, while Mark's methodical approach ensured all contractual details were properly addressed.",
    "The annual developer conference in Las Vegas showcased Maria's high extraversion as she delivered a keynote that inspired 500+ attendees, while Emily's technical.",
    "Executive coach Dr. Roberts noted that David's high neuroticism was being managed through mindfulness techniques, while his high openness made him exceptionally receptive to personal development strategies.",
    "Mark's leadership development plan focused on improving his low agreeableness through empathy training, while leveraging his high conscientiousness for strategic planning responsibilities.",
    "During the AI integration sprint, Alex's high openness and conscientiousness drove the successful implementation of predictive analytics features, while Emily's architectural oversight ensured scalability and maintainability.",
    "The design thinking workshop at Stanford University highlighted David's exceptional creativity and Sarah's balanced approach to user-centered design principles."
]

# =============================================================================
# DATA PROCESSING & NORMALIZATION
# =============================================================================
class DataProcessor:
    """Handles text normalization and enhanced trait mapping"""
    def __init__(self):
        self.enhanced_mapping = {
            # Openness
            'creative': 'openness', 'innovative': 'openness', 'curious': 'openness',
            'imaginative': 'openness', 'visionary': 'openness', 'artistic': 'openness',
            'aesthetic': 'openness', 'adventurous': 'openness', 'explorer': 'openness',
            'intellectual': 'openness', 'open-minded': 'openness', 'unconventional': 'openness',
            'progressive': 'openness', 'dreamer': 'openness',
            # Conscientiousness
            'organized': 'conscientiousness', 'meticulous': 'conscientiousness',
            'responsible': 'conscientiousness', 'reliable': 'conscientiousness',
            'competent': 'conscientiousness', 'effective': 'conscientiousness',
            'neat': 'conscientiousness', 'systematic': 'conscientiousness',
            'dutiful': 'conscientiousness', 'ambitious': 'conscientiousness',
            'driven': 'conscientiousness', 'goal-oriented': 'conscientiousness',
            'disciplined': 'conscientiousness', 'focused': 'conscientiousness',
            'persistent': 'conscientiousness', 'cautious': 'conscientiousness',
            'deliberate': 'conscientiousness', 'careful': 'conscientiousness',
            # Extraversion
            'outgoing': 'extraversion', 'sociable': 'extraversion', 'friendly': 'extraversion',
            'gregarious': 'extraversion', 'assertive': 'extraversion', 'confident': 'extraversion',
            'forceful': 'extraversion', 'energetic': 'extraversion', 'active': 'extraversion',
            'dynamic': 'extraversion', 'excitement-seeking': 'extraversion',
            'thrill-seeking': 'extraversion', 'cheerful': 'extraversion',
            'optimistic': 'extraversion', 'positive': 'extraversion',
            # Agreeableness
            'cooperative': 'agreeableness', 'collaborative': 'agreeableness',
            'empathetic': 'agreeableness', 'trusting': 'agreeableness',
            'believing': 'agreeableness', 'accepting': 'agreeableness',
            'moral': 'agreeableness', 'ethical': 'agreeableness',
            'principled': 'agreeableness', 'altruistic': 'agreeableness',
            'helpful': 'agreeableness', 'generous': 'agreeableness',
            'accommodating': 'agreeableness', 'flexible': 'agreeableness',
            'modest': 'agreeableness', 'humble': 'agreeableness',
            'unassuming': 'agreeableness', 'sympathetic': 'agreeableness',
            'compassionate': 'agreeableness', 'caring': 'agreeableness',
            # Neuroticism
            'anxious': 'neuroticism', 'worried': 'neuroticism', 'nervous': 'neuroticism',
            'angry': 'neuroticism', 'irritable': 'neuroticism', 'frustrated': 'neuroticism',
            'sad': 'neuroticism', 'depressed': 'neuroticism', 'unhappy': 'neuroticism',
            'self-conscious': 'neuroticism', 'insecure': 'neuroticism', 'shy': 'neuroticism',
            'impulsive': 'neuroticism', 'indulgent': 'neuroticism', 'immoderate': 'neuroticism',
            'vulnerable': 'neuroticism', 'sensitive': 'neuroticism', 'fragile': 'neuroticism',
            'calm': 'neuroticism', 'resilient': 'neuroticism', 'stable': 'neuroticism'
        }

    def preprocess_text(self, text):
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def normalize_trait(self, trait):
        return self.enhanced_mapping.get(trait.lower(), trait)

# =============================================================================
# F1 SCORE CALCULATION
# =============================================================================
class F1KnowledgeGraphEvaluator:
    """Compute F1 metrics for personality traits (can run in detailed or lightweight aggregated mode)"""
    def __init__(self, ground_truth_characters):
        self.ground_truth = ground_truth_characters

    def calculate_trait_f1(self, kg_builder, detailed=True):
        metrics = {}
        G = getattr(kg_builder, "graph", None)
        if G is None:
            return metrics

        per_person_results = {}
        for char in self.ground_truth:
            person_name = char["name"]
            gt_traits = {f"trait_{t}" for t, lvl in char["base_traits"].items() if lvl in ['high', 'medium']}

            if G.has_node(person_name):
                try:
                    neighbors = list(G.neighbors(person_name))
                except Exception:
                    neighbors = []
                pred_traits = {n for n in neighbors if G.nodes[n].get('type') == 'personality_trait'}
            else:
                pred_traits = set()

            tp = len(gt_traits & pred_traits)
            fp = len(pred_traits - gt_traits)
            fn = len(gt_traits - pred_traits)
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

            per_person_results[person_name] = {
                'precision': round(precision, 3),
                'recall': round(recall, 3),
                'f1': round(f1, 3),
                'tp': tp, 'fp': fp, 'fn': fn,
                'ground_truth': sorted(list(gt_traits)), 'predicted': sorted(list(pred_traits))
            }

        if detailed:
            metrics.update(per_person_results)
            if per_person_results:
                avg_p = sum(m['precision'] for m in per_person_results.values()) / len(per_person_results)
                avg_r = sum(m['recall'] for m in per_person_results.values()) / len(per_person_results)
                avg_f1 = sum(m['f1'] for m in per_person_results.values()) / len(per_person_results)
                metrics['macro_avg'] = {'precision': round(avg_p, 3), 'recall': round(avg_r, 3), 'f1': round(avg_f1, 3)}
            return metrics
        else:
            total_tp = sum(m['tp'] for m in per_person_results.values())
            total_fp = sum(m['fp'] for m in per_person_results.values())
            total_fn = sum(m['fn'] for m in per_person_results.values())
            precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
            recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
            metrics['aggregated'] = {
                'precision': round(precision, 3),
                'recall': round(recall, 3),
                'f1': round(f1, 3),
                'tp': total_tp, 'fp': total_fp, 'fn': total_fn
            }
            return metrics

# =============================================================================
# KNOWLEDGE GRAPH BUILDER
# =============================================================================
class ComprehensiveKnowledgeGraph:
    def __init__(self):
        self.graph = nx.Graph()
        self.dp = DataProcessor()
        print("✅ Knowledge Graph Builder initialized")

    def extract_entities(self, text):
        entities = {'people':[], 'organizations':[], 'locations':[], 'traits':[], 'relationships':[]}
        for c in CHARACTERS:
            if c['name'].lower() in text.lower():
                entities['people'].append(c['name'])
        if 'TechInnovate Inc' in text:
            entities['organizations'].append('TechInnovate Inc')
        locations = ['San Francisco','New York','Las Vegas','Austin','Seattle','Boston','Office','Conference']
        for loc in locations:
            if loc in text:
                entities['locations'].append(loc)
        trait_keywords = {'conscientiousness':['conscientiousness','organized','meticulous','detailed'],
                          'openness':['openness','creative','innovative','curious'],
                          'extraversion':['extraversion','leadership','sociable','outgoing'],
                          'agreeableness':['agreeableness','cooperative','collaborative','empathetic'],
                          'neuroticism':['neuroticism','anxious','calm','stressed']}
        for trait, kw in trait_keywords.items():
            for k in kw:
                if k in text.lower():
                    entities['traits'].append({'trait': self.dp.normalize_trait(trait),
                                               'sentence': text,
                                               'related_people': entities['people'],
                                               'confidence': 'high' if entities['people'] else 'medium'})
                    break
        return entities

    def build_knowledge_graph(self, texts):
        for t in texts:
            e = self.extract_entities(t)
            self._add_to_graph(e)
        return self.graph

    def _add_to_graph(self, entities):
        for p in entities['people']:
            self.graph.add_node(p, type='person', label=p)
        for o in entities['organizations']:
            self.graph.add_node(o, type='organization', label=o)
        for l in entities['locations']:
            self.graph.add_node(l, type='location', label=l)
        for trait in entities['traits']:
            t_name = f"trait_{trait['trait']}"
            self.graph.add_node(t_name, type='personality_trait', label=t_name)
            for person in trait['related_people']:
                self.graph.add_edge(person, t_name, confidence=trait['confidence'])
        for p in entities['people']:
            for o in entities['organizations']:
                self.graph.add_edge(p,o)
            for l in entities['locations']:
                self.graph.add_edge(p,l)

    def visualize_graph(self):
        plt.figure(figsize=(15,12))
        pos = nx.spring_layout(self.graph, k=0.8, iterations=50)
        node_colors = {'person':'skyblue','organization':'lightgreen','location':'orange','personality_trait':'pink'}
        nx.draw(self.graph, pos,
                with_labels=True,
                node_size=1500,
                node_color=[node_colors.get(self.graph.nodes[n]['type'],'grey') for n in self.graph.nodes],
                font_size=10,
                font_weight='bold')
        # Custom legend
        legend_elements = [Patch(facecolor=c, label=k) for k,c in node_colors.items()]
        plt.legend(handles=legend_elements)
        plt.title("Comprehensive Knowledge Graph", fontsize=16)
        plt.axis('off')
        plt.show()

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__=="__main__":
    kg_builder = ComprehensiveKnowledgeGraph()
    kg = kg_builder.build_knowledge_graph(PARAGRAPHS)
    # optional: comment out visualization if it's heavy / causing UI issues
    #kg_builder.visualize_graph()

    f1_eval = F1KnowledgeGraphEvaluator(CHARACTERS)
    # Use detailed=False to compute a single aggregated (lighter) F1 result
    trait_f1_metrics = f1_eval.calculate_trait_f1(kg_builder, detailed=False)
    print("✅ F1 Trait Metrics:")
    # print only the aggregated summary in lightweight mode
    if 'aggregated' in trait_f1_metrics:
        print(trait_f1_metrics['aggregated'])
    else:
        for k, v in trait_f1_metrics.items():
            print(f"{k}: {v}")

