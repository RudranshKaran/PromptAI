# PromptAI

A web application that enhances prompts using the Mistral AI API.

## Prerequisites

1. Python 3.9 or higher
2. Mistral AI API key (get it from [Mistral AI Platform](https://mistral.ai))

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd PromptAI
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

4. Configure API key:
   - Create a `.env` file in the project root
   - Add your Mistral API key: `MISTRAL_API_KEY=your_api_key_here`

## Running the Application

1. Start the backend server:
```bash
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

2. In a new terminal, serve the frontend:
```bash
cd frontend
python -m http.server 80
```

3. Access the application:
   - Open your web browser and navigate to `http://localhost`
   - The backend API will be available at `http://localhost:8000`

## Usage

1. Enter your original prompt in the text area
2. Click the "Enhance Prompt" button
3. Wait for the enhanced version to appear

## Development

Run tests:
```bash
cd backend
pytest
```

## Troubleshooting

1. If you see API errors:
   - Verify your Mistral API key in `.env`
   - Check if the backend server is running
   - Look for error messages in the browser console

2. If the frontend doesn't load:
   - Ensure port 80 is available
   - Try using a different port (e.g., `python -m http.server 8080`)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License
