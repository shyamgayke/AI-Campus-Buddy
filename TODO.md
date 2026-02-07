# Campus Feedback App Setup and API Guide

## Current Progress
- App structure is complete with Flask backend, Google Gemini integration, and frontend.
- API key is set in app.py using environment variables for security.
- Added python-dotenv to requirements for env var usage.

## Steps to Complete
- [x] Update app.py to use environment variable for API key (security best practice).
- [x] Create .env file template for API key.
- [x] Install Python dependencies.
- [x] Run the Flask app locally.
- [x] Test the feedback API with sample input.
- [x] Guide on obtaining Google Gemini API key if needed.

## API Usage Explanation
The app uses Google's Gemini API (gemini-1.5-flash) to generate structured feedback on assignment text. The prompt instructs the AI to return JSON with specific fields: overall_evaluation, strengths, areas_for_improvement, language_clarity, and score_out_of_10.
