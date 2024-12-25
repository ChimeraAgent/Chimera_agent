from typing import Dict, Any, List
from datetime import datetime

class LearningModule:
    def __init__(self):
        self.user_memories: Dict[str, List[Dict[str, Any]]] = {}
        self.knowledge_base: Dict[str, Any] = {}

    def record_interaction(self, user_id: str, user_input: str, agent_response: str, actions_taken: List[Dict[str, Any]] = None, user_feedback: str = None):
        interaction_data = {
            'timestamp': datetime.now().isoformat(),
            'user_input': user_input,
            'agent_response': agent_response,
            'actions_taken': actions_taken if actions_taken is not None else [],
            'user_feedback': user_feedback
        }
        self.user_memories.setdefault(user_id, []).append(interaction_data)

    def learn_from_interaction(self, user_id: str, user_input: str, agent_response: str, actions_taken: List[Dict[str, Any]] = None, user_feedback: str = None):
        if user_feedback:
            self._process_feedback(user_id, user_input, agent_response, user_feedback)

        if "I prefer" in user_input.lower():
            preference = user_input.split("I prefer", 1)[1].strip()
            self.knowledge_base.setdefault(user_id, {}).setdefault('preferences', []).append(preference)

        if actions_taken:
            for action in actions_taken:
                if action.get('success', True):
                    action_type = action.get('type')
                    if action_type:
                        self.knowledge_base[f"successful_action_type_{action_type}"] = self.knowledge_base.get(f"successful_action_type_{action_type}", 0) + 1

    def get_user_memory(self, user_id: str) -> List[Dict[str, Any]]:
        return self.user_memories.get(user_id, [])

    def get_learned_knowledge(self) -> Dict[str, Any]:
        return self.knowledge_base

    def _process_feedback(self, user_id: str, user_input: str, agent_response: str, feedback: str):
        if "good" in feedback.lower() or "helpful" in feedback.lower():
            print(f"Learned positive feedback for: '{agent_response}' to '{user_input}' from '{user_id}'.")
        elif "bad" in feedback.lower() or "wrong" in feedback.lower():
            print(f"Learned negative feedback for: '{agent_response}' to '{user_input}' from '{user_id}'.")
        self.knowledge_base.setdefault(user_id, {}).setdefault('feedback_history', []).append({
            'user_input': user_input,
            'agent_response': agent_response,
            'feedback': feedback,
            'timestamp': datetime.now().isoformat()
        })

if __name__ == "__main__":
    learning_module = LearningModule()
    user_id = "test_user"
    learning_module.record_interaction(user_id, "Hello", "Hi")
    learning_module.learn_from_interaction(user_id, "I prefer short replies", "ok")
    learning_module.learn_from_interaction(user_id, "ok", "great", user_feedback="good")
    print(learning_module.get_user_memory(user_id))
    print(learning_module.get_learned_knowledge())