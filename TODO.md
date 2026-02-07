# Campus Feedback App Setup and API Guide

## Current Progress
- App structure is complete with Flask backend, Hugging Face Inference API integration, and frontend.
- API token is set in .env file using environment variables for security.
- Updated requirements.txt with necessary dependencies.
- Modified inference.py to use Hugging Face API for real-time feedback generation.

## Steps to Complete
- [x] Update app.py to load environment variables.
- [x] Create .env file template for Hugging Face API token.
- [x] Update requirements.txt with Hugging Face hub and other dependencies.
- [x] Modify inference.py to use Hugging Face Inference API instead of local models.
- [x] Install Python dependencies.
- [ ] Set your Hugging Face API token in .env file (replace 'your_api_token_here' with your actual token).
- [ ] Run the Flask app locally.
- [ ] Test the feedback API with sample input.
- [x] Guide on obtaining Hugging Face API token if needed.

## API Usage Explanation
The app uses Hugging Face Inference API with google/flan-t5-base model to generate structured feedback on assignment text. The model is prompted to return feedback with specific fields: overall_evaluation, strengths, areas_for_improvement, language_clarity, and score_out_of_10. This allows the model to work on real data via API calls, providing dynamic and up-to-date feedback.
