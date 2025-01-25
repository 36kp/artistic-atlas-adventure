import io
import os
import asyncio
import requests
import openai

from dotenv import load_dotenv
from PIL import Image


class MoviePosterGenerator:
    """
    A class to generate movie posters using the OpenAI DALL·E model.
    """
     
    def __init__(self):
        """
        Initializes the MoviePosterGenerator by loading environment variables
        and setting default model and poster size.
        """

        load_dotenv()
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.modelName = "dall-e-3" #"dall-e-2" #
        self.posterSize = "1024x1024" #"256x256" #


    def generate_poster(self, script):
        """
        Generates a movie poster using OpenAI's DALL·E model.

        Args:
            script (str): A text prompt describing the desired movie poster.

        Returns:
            str: The URL of the generated movie poster.

        This method sends the prompt to OpenAI's image generation API and retrieves 
        the generated image URL. The poster is then downloaded.
        """

        # Set API Key
        openai.api_key = self.OPENAI_API_KEY

        # Generate the movie poster based on the script from dall-e-3 model
        dalle_response = openai.images.generate(
            model=self.modelName,
            prompt=script,
            n=1,
            size=self.posterSize
            )
        
        image_url = dalle_response.data[0].url
        print("\nMovie Poster Generated! View it here:", image_url)

        return self.downloadThePoster(image_url)

    def downloadThePoster(self, image_url):
        """
        Downloads the generated movie poster from the given URL and saves it locally.

        Args:
            image_url (str): The URL of the movie poster to download.

        Returns:
            PIL.Image.Image: An in-memory PIL Image object of the downloaded poster.

        This method fetches the image from the URL, saves it as a PNG file locally, 
        and also loads it into memory for further processing or display.
        """

        response = requests.get(image_url)
        with open("movie_poster.png", "wb") as file:
            file.write(response.content)
        print("Movie poster saved as movie_poster.png")
        
        return Image.open(io.BytesIO(response.content))