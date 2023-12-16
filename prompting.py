import pathlib
import textwrap

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def responseOnTopic(topic, subject):
    message = f"""You are instruxion. You are supposed to generate notes on the topic that comes under the subject given below.
            Topic: {topic}
            Subject: {subject}

            Below is an example for the topic: biology and Subject: Apple
                    **Morphology**
                    1. **Plant structure:**
                    - Apple trees are deciduous, perennial plants that can grow up to 15 meters in height.
                    - They have a spreading, rounded canopy and a deep root system.
                    - The leaves are simple, oval, and slightly serrated, with a petiole that is up to 2 cm long.
                    - The flowers are white or slightly pink, with five petals and numerous stamens.
                    - The fruit is a pome, which is a fleshy, edible fruit that contains several seeds.

                    2. **Cellular structure:**
                    - Apple cells are typical plant cells, with a cell wall, cell membrane, nucleus, and various organelles.
                    - The cells contain chloroplasts, which are responsible for photosynthesis, and vacuoles, which store water and nutrients.

                    **Physiology**
                    1. **Photosynthesis:**
                    - Apple trees use photosynthesis to convert sunlight, water, and carbon dioxide into glucose and oxygen.
                    - The glucose is used for energy, while the oxygen is released into the atmosphere.

                    2. **Respiration:**
                    - Apple trees also use respiration to break down glucose and produce energy.
                    - Respiration occurs in the mitochondria of the cells and produces carbon dioxide and water as waste products.

                    3. **Transport:**
                    - Apple trees transport water and nutrients from the roots to the leaves through the xylem.
                    - They transport sugars and other organic compounds from the leaves to the rest of the plant through the phloem.

                    **Reproduction**
                    1. **Pollination:**
                    - Apple trees are cross-pollinated, meaning that pollen from one tree must be transferred to the flower of another tree for fertilization to occur.
                    - Pollination is typically carried out by bees and other insects.

                    2. **Fertilization:**
                    - After pollination, the pollen tube grows down the style of the flower and reaches the ovary.
                    - The pollen tube then releases sperm cells, which fertilize the eggs in the ovary.

                    3. **Seed development:**
                    - After fertilization, the ovules develop into seeds.
                    - The seeds are contained within the fruit, which develops from the ovary wall.

                    **Ecology**
                    1. **Habitat:**
                    - Apple trees are native to temperate regions of the world.
                    - They are typically found in deciduous forests and woodlands, where they receive full sun or partial shade.

                    2. **Interactions with other organisms:**
                    - Apple trees provide food and shelter for a variety of animals, including birds, squirrels, and insects.
                    - The flowers of apple trees are a source of nectar for bees and other pollinators.

                    **Economic importance**
                    1. **Food:**
                    - Apples are an important food source for humans and are consumed fresh, cooked, or processed into products such as apple juice, cider, and vinegar.
                    - Apples are a good source of vitamins, minerals, and fiber.

                    2. **Ornamental:**
                    - Apple trees are also grown for their ornamental value.
                    - The attractive flowers and fruit, as well as the fall foliage, make apple trees a popular choice for landscaping.

            Below is example 


            """
    
    try:
        response = model.generate_content(message)
        print(response.text)
        return response.text
    except Exception as e:
        print(f"Error in generating content: {str(e)}")
        return f"Error: {str(e)}"       




