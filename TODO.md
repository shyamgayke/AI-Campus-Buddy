# Campus Feedback App Setup and API Guide

## API Usage Explanation
The app uses Hugging Face Inference API with google/flan-t5-base model to generate structured feedback on assignment text. The model is prompted to return feedback with specific fields: overall_evaluation, strengths, areas_for_improvement, language_clarity, and score_out_of_10. This allows the model to work on real data via API calls, providing dynamic and up-to-date feedback.
