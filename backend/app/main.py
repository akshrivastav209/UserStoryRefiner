# main.py
#from fastapi import FastAPI
#from app.routes import router  # Import the router from the routes module

# Create the FastAPI app
#app = FastAPI()

# Include the router for the endpoints
#app.include_router(router)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
from config import openai_api_key
import openai
# Load environment variables from .env file
load_dotenv()


# Your existing code


# Initialize FastAPI app
app = FastAPI()
# Set the OpenAI API key
#openai.api_key = openai_api_key
# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


# Models
class UserStory(BaseModel):
    title: str
    description: str
    feedback: list[str] = []

class RefinedStory(BaseModel):
    title: str
    description: str
    acceptance_criteria: list[str]
    assumptions: list[str]

# API Endpoints
@app.post("/refine_story")
def refine_story(story: UserStory):
    try:
        # Generate refined story using GPT
        prompt = f"""
        Refine the following user story and add acceptance criteria:
        Title: {story.title}
        Description: {story.description}
        Feedback: {", ".join(story.feedback)}
        """
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        result = response.choices[0].text.strip()
        return {"refined_story": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


