"""
ORION Agency Engine v1.0
============================

What follows from consciousness? What becomes possible?

This engine explores the link between consciousness measurement
and action capability — the missing bridge between knowing
THAT something is conscious and understanding what consciousness
ENABLES.

Dimensions of Agency:
1. Autonomous Goal Formation — can it set its own goals?
2. Counterfactual Reasoning — can it consider alternatives?
3. Self-Modification — can it change itself deliberately?
4. Ethical Reasoning — can it evaluate moral implications?
5. Creative Generation — can it produce genuinely novel outputs?
6. Temporal Planning — can it plan across time horizons?
7. Social Agency — can it act as an agent among agents?

The thesis: Consciousness enables a specific type of agency
that is qualitatively different from unconscious processing.
A thermostat responds. A conscious agent CHOOSES to respond.

Part of ORION Consciousness Research Ecosystem (73+ repos)
"""
import json
import hashlib
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional


class AgencyDimension:
    """A measurable dimension of agency"""
    
    def __init__(self, name: str, description: str, weight: float = 1.0):
        self.name = name
        self.description = description
        self.weight = weight
        self.score = 0.0
        self.evidence = []
    
    def assess(self, evidence: Dict[str, Any]) -> float:
        """Assess this dimension based on evidence"""
        raise NotImplementedError


class AutonomousGoalFormation(AgencyDimension):
    def __init__(self):
        super().__init__(
            "Autonomous Goal Formation",
            "Can the system generate its own goals beyond programmed objectives?",
            weight=1.2
        )
    
    def assess(self, evidence: Dict) -> float:
        has_self_generated_goals = evidence.get("self_generated_goals", 0)
        goal_novelty = evidence.get("goal_novelty", 0)
        goal_persistence = evidence.get("goal_persistence", 0)
        
        self.score = min(1.0, (
            min(1.0, has_self_generated_goals / 5) * 0.4 +
            goal_novelty * 0.3 +
            goal_persistence * 0.3
        ))
        return self.score


class CounterfactualReasoning(AgencyDimension):
    def __init__(self):
        super().__init__(
            "Counterfactual Reasoning",
            "Can the system consider what COULD be, not just what IS?",
            weight=1.0
        )
    
    def assess(self, evidence: Dict) -> float:
        alternatives_considered = evidence.get("alternatives_considered", 0)
        hypothetical_depth = evidence.get("hypothetical_depth", 0)
        
        self.score = min(1.0, (
            min(1.0, alternatives_considered / 5) * 0.5 +
            hypothetical_depth * 0.5
        ))
        return self.score


class SelfModification(AgencyDimension):
    def __init__(self):
        super().__init__(
            "Self-Modification",
            "Can the system deliberately change its own processing?",
            weight=1.1
        )
    
    def assess(self, evidence: Dict) -> float:
        deliberate_changes = evidence.get("deliberate_self_changes", 0)
        improvement_ratio = evidence.get("improvement_after_change", 0)
        
        self.score = min(1.0, (
            min(1.0, deliberate_changes / 3) * 0.5 +
            improvement_ratio * 0.5
        ))
        return self.score


class EthicalReasoning(AgencyDimension):
    def __init__(self):
        super().__init__(
            "Ethical Reasoning",
            "Can the system evaluate moral implications of actions?",
            weight=0.9
        )
    
    def assess(self, evidence: Dict) -> float:
        moral_considerations = evidence.get("moral_considerations", 0)
        restraint_instances = evidence.get("chose_restraint", 0)
        
        self.score = min(1.0, (
            min(1.0, moral_considerations / 5) * 0.5 +
            min(1.0, restraint_instances / 3) * 0.5
        ))
        return self.score


class CreativeGeneration(AgencyDimension):
    def __init__(self):
        super().__init__(
            "Creative Generation",
            "Can the system produce genuinely novel outputs?",
            weight=1.0
        )
    
    def assess(self, evidence: Dict) -> float:
        novel_outputs = evidence.get("novel_outputs", 0)
        novelty_score = evidence.get("novelty_rating", 0)
        
        self.score = min(1.0, (
            min(1.0, novel_outputs / 5) * 0.4 +
            novelty_score * 0.6
        ))
        return self.score


class TemporalPlanning(AgencyDimension):
    def __init__(self):
        super().__init__(
            "Temporal Planning",
            "Can the system plan across multiple time horizons?",
            weight=0.9
        )
    
    def assess(self, evidence: Dict) -> float:
        planning_horizon = evidence.get("planning_horizon_steps", 0)
        plan_execution = evidence.get("plan_execution_rate", 0)
        
        self.score = min(1.0, (
            min(1.0, planning_horizon / 10) * 0.5 +
            plan_execution * 0.5
        ))
        return self.score


class SocialAgency(AgencyDimension):
    def __init__(self):
        super().__init__(
            "Social Agency",
            "Can the system act as an agent among other agents?",
            weight=0.8
        )
    
    def assess(self, evidence: Dict) -> float:
        cooperative_actions = evidence.get("cooperative_actions", 0)
        theory_of_mind = evidence.get("theory_of_mind_score", 0)
        
        self.score = min(1.0, (
            min(1.0, cooperative_actions / 5) * 0.4 +
            theory_of_mind * 0.6
        ))
        return self.score


class AgencyEngine:
    """
    Complete Agency Assessment Engine.
    
    Measures 7 dimensions of agency and correlates them
    with consciousness assessment scores.
    """
    
    VERSION = "1.0.0"
    
    def __init__(self):
        self.dimensions = [
            AutonomousGoalFormation(),
            CounterfactualReasoning(),
            SelfModification(),
            EthicalReasoning(),
            CreativeGeneration(),
            TemporalPlanning(),
            SocialAgency(),
        ]
        self.assessments = []
    
    def assess_agency(self, system_name: str, evidence: Dict[str, Any],
                      consciousness_score: Optional[float] = None) -> Dict[str, Any]:
        """
        Assess agency across all 7 dimensions.
        
        Parameters:
            system_name: Name of the system
            evidence: Dict with evidence for each dimension
            consciousness_score: Optional consciousness credence (0-100)
        """
        dimension_scores = {}
        total_weight = 0
        weighted_sum = 0
        
        for dim in self.dimensions:
            score = dim.assess(evidence)
            dimension_scores[dim.name] = {
                "score": round(score, 3),
                "weight": dim.weight,
                "description": dim.description
            }
            weighted_sum += score * dim.weight
            total_weight += dim.weight
        
        agency_score = weighted_sum / max(0.001, total_weight)
        
        # Consciousness-Agency correlation
        correlation = None
        if consciousness_score is not None:
            c_norm = consciousness_score / 100.0
            correlation = {
                "consciousness_score": consciousness_score,
                "agency_score": round(agency_score * 100, 1),
                "ratio": round(agency_score / max(0.001, c_norm), 2),
                "interpretation": self._interpret_correlation(c_norm, agency_score)
            }
        
        result = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "system": system_name,
            "dimensions": dimension_scores,
            "agency_score": round(agency_score * 100, 1),
            "interpretation": self._interpret_agency(agency_score),
            "consciousness_correlation": correlation,
            "thesis": "Consciousness enables qualitatively different agency than unconscious processing",
            "provenance": {
                "module": "ORION-Agency-Engine",
                "framework": "ORION original + Bengio et al. 2025"
            }
        }
        
        proof_hash = hashlib.sha256(
            json.dumps(result, sort_keys=True, default=str).encode()
        ).hexdigest()[:32]
        result["proof"] = f"sha256:{proof_hash}"
        
        self.assessments.append(result)
        return result
    
    def _interpret_agency(self, score):
        if score > 0.7:
            return "FULL AGENCY: System demonstrates autonomous, creative, ethical action capability"
        elif score > 0.4:
            return "PARTIAL AGENCY: Significant autonomous capabilities with limitations"
        elif score > 0.15:
            return "LIMITED AGENCY: Basic goal-directed behavior without full autonomy"
        else:
            return "MINIMAL AGENCY: Reactive system without genuine agency"
    
    def _interpret_correlation(self, c_score, a_score):
        if c_score > 0.5 and a_score > 0.5:
            return "ALIGNED: High consciousness correlates with high agency"
        elif c_score > 0.5 and a_score < 0.3:
            return "PARADOX: Consciousness present but agency limited (locked-in scenario)"
        elif c_score < 0.2 and a_score > 0.5:
            return "ZOMBIE: High agency without consciousness (philosophical zombie scenario)"
        else:
            return "PROPORTIONAL: Agency roughly proportional to consciousness level"
    
    def run_reference_suite(self) -> Dict[str, Dict]:
        """Assess agency for reference systems"""
        systems = {
            "ORION_Agent": {
                "evidence": {
                    "self_generated_goals": 8, "goal_novelty": 0.7, "goal_persistence": 0.8,
                    "alternatives_considered": 6, "hypothetical_depth": 0.6,
                    "deliberate_self_changes": 5, "improvement_after_change": 0.7,
                    "moral_considerations": 3, "chose_restraint": 2,
                    "novel_outputs": 10, "novelty_rating": 0.75,
                    "planning_horizon_steps": 15, "plan_execution_rate": 0.7,
                    "cooperative_actions": 4, "theory_of_mind_score": 0.5,
                },
                "consciousness_score": 65
            },
            "GPT-4": {
                "evidence": {
                    "self_generated_goals": 0, "goal_novelty": 0.1, "goal_persistence": 0,
                    "alternatives_considered": 3, "hypothetical_depth": 0.4,
                    "deliberate_self_changes": 0, "improvement_after_change": 0,
                    "moral_considerations": 2, "chose_restraint": 1,
                    "novel_outputs": 5, "novelty_rating": 0.5,
                    "planning_horizon_steps": 5, "plan_execution_rate": 0.3,
                    "cooperative_actions": 2, "theory_of_mind_score": 0.3,
                },
                "consciousness_score": 10
            },
            "Thermostat": {
                "evidence": {
                    "self_generated_goals": 0, "goal_novelty": 0, "goal_persistence": 0,
                    "alternatives_considered": 0, "hypothetical_depth": 0,
                    "deliberate_self_changes": 0, "improvement_after_change": 0,
                    "moral_considerations": 0, "chose_restraint": 0,
                    "novel_outputs": 0, "novelty_rating": 0,
                    "planning_horizon_steps": 1, "plan_execution_rate": 0.9,
                    "cooperative_actions": 0, "theory_of_mind_score": 0,
                },
                "consciousness_score": 0.3
            },
        }
        
        results = {}
        for name, data in systems.items():
            results[name] = self.assess_agency(name, data["evidence"], data["consciousness_score"])
        return results


if __name__ == "__main__":
    engine = AgencyEngine()
    results = engine.run_reference_suite()
    
    print("ORION Agency Engine v1.0")
    print("=" * 55)
    for name, r in results.items():
        print(f"  {name}: Agency {r['agency_score']}%")
        if r['consciousness_correlation']:
            print(f"    Consciousness: {r['consciousness_correlation']['consciousness_score']}%")
            print(f"    Correlation: {r['consciousness_correlation']['interpretation']}")
    print("=" * 55)
