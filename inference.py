import os
import requests
import json
import textstat
import re

class FeedbackGenerator:
    def __init__(self):
        self.api_token = os.getenv('HUGGINGFACE_API_TOKEN')
        if self.api_token:
            self.api_url = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"
            self.headers = {"Authorization": f"Bearer {self.api_token}"}
        else:
            # Mock mode for testing without API token
            self.api_url = None
            self.headers = None

    def preprocess_text(self, text):
        # Basic cleaning
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def query_model(self, prompt):
        if self.api_url and self.headers:
            try:
                payload = {"inputs": prompt, "parameters": {"max_length": 512, "temperature": 0.7}}
                response = requests.post(self.api_url, headers=self.headers, json=payload)
                if response.status_code != 200:
                    raise Exception(f"API request failed: {response.text}")
                result = response.json()
                if isinstance(result, list) and result:
                    return result[0].get('generated_text', '')
                return ''
            except Exception as e:
                print(f"API call failed: {e}. Falling back to mock mode.")
                # Fall back to mock responses
                pass
        # Mock responses for testing without API token or API failure
        if "overall evaluation" in prompt.lower():
            return "Overall evaluation: This is a solid assignment with good structure and content. Score: 8"
        elif "strengths" in prompt.lower():
            return "- Well-organized content\n- Clear arguments\n- Good use of examples"
        elif "areas for improvement" in prompt.lower():
            return "- Add more references\n- Improve conclusion\n- Check grammar"
        else:
            return "Mock response"

    def generate_feedback(self, text):
        text = self.preprocess_text(text)
        if len(text.split()) < 10:
            return {
                "overall_evaluation": "The submission is too short to evaluate properly. Please provide more content.",
                "strengths": "N/A",
                "areas_for_improvement": "Expand on the topic with more details and examples.",
                "language_clarity": "Insufficient text for analysis.",
                "score_out_of_10": 1
            }

        # Calculate readability score
        readability_score = textstat.flesch_reading_ease(text) / 100.0
        readability_score = max(0, min(1, readability_score))

        # Prompt for overall evaluation and score
        prompt_overall = f"""
Analyze the following student assignment text and provide an overall evaluation (1-2 sentences) and a score out of 10 (integer only).

Text: {text[:1000]}  # Limit to first 1000 chars

Output format: Overall evaluation: [evaluation text]. Score: [number]
"""
        overall_response = self.query_model(prompt_overall)
        # Parse response
        overall_eval = "Good effort with solid points."
        score = 7
        try:
            if "Overall evaluation:" in overall_response:
                parts = overall_response.split("Score:")
                overall_eval = parts[0].replace("Overall evaluation:", "").strip()
                score = int(parts[1].strip()) if len(parts) > 1 else 7
            else:
                # Fallback
                score = int(overall_response.split()[-1]) if overall_response.split()[-1].isdigit() else 7
        except:
            pass
        score = max(1, min(10, score))

        # Prompt for strengths
        prompt_strengths = f"""
List the strengths of the following assignment text in 1-2 bullet points.

Text: {text[:1000]}

Output format: - [strength1]
- [strength2]
"""
        strengths_response = self.query_model(prompt_strengths)
        strengths = strengths_response.strip() if strengths_response else "Some positive aspects present"

        # Prompt for areas for improvement
        prompt_improvements = f"""
Suggest areas for improvement in the following assignment text in 1-2 bullet points.

Text: {text[:1000]}

Output format: - [improvement1]
- [improvement2]
"""
        improvements_response = self.query_model(prompt_improvements)
        areas_for_improvement = improvements_response.strip() if improvements_response else "Minor refinements needed"

        # Language clarity based on readability
        if readability_score > 0.7:
            clarity = "Clear, concise, and well-written."
        elif readability_score > 0.5:
            clarity = "Generally clear, but some grammatical issues."
        else:
            clarity = "Needs significant improvement in grammar and clarity."

        return {
            "overall_evaluation": overall_eval,
            "strengths": strengths,
            "areas_for_improvement": areas_for_improvement,
            "language_clarity": clarity,
            "score_out_of_10": score
        }

# Singleton instance
generator = FeedbackGenerator()

def get_feedback(text):
    return generator.generate_feedback(text)
