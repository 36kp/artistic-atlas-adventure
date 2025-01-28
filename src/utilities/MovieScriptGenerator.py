import io
import os
import asyncio

from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image


class MovieScriptGenerator:
    """
    A class to generate movie scripts based on image input using the Gemini AI model.

    This class interacts with Google's Gemini AI to analyze an image and produce 
    a movie synopsis. The script includes a director, three actors, and an estimated 
    IMDb rating based on similar movies.
    """

    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        self.modelName = "gemini-1.5-flash"


    def generate_script(self, image_path):
        """
        Generates a movie script based on the given image.

        This asynchronous function takes an image file path, processes the image

        Args:
            image_path (str): The file path of the input image.

        Returns:
            str: The generated movie script as a string.

        Raises:
            FileNotFoundError: If the provided image path does not exist.
            ValueError: If the image format is unsupported.
        """
        
        # Configure the API key
        genai.configure(api_key=self.GEMINI_API_KEY)

        # try to open the image file
        try:
            with open(image_path, "rb") as image_file:
                image_data = image_file.read()
            image = Image.open(io.BytesIO(image_data))

            # Create the model
            model = genai.GenerativeModel(self.modelName)

            # Set the prompt
            prompt = self.prompt()

            # Generate text from the prompt and image
            response = model.generate_content([prompt, image]) 
            return response.text
        
        except Exception as e:
            return str(e)
        

    def prompt(self):
        return """
        You are a movie producer.  
        Analyize the picutre and write an movie synopsis for a movie that is based on the picture. 
        Choose a director and 3 actors for the movie that have appeared in simular movies.
        A well as an IMDB rating based on simular movies on IMBD.
        """  
