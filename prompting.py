import pathlib
import textwrap

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

import os
from dotenv import load_dotenv

from openai import OpenAI
import urllib.request
client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def responseOnTopic(topic, subject):
    message = f"""You are instruxion. You are supposed to generate notes on the topic that comes under the subject given below.
            Topic: {topic}
            Subject: {subject}

            Explain in simple terms.

            Below is an example for the topic: Apple and Subject: biology
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

            Below is an example for subject: biology and topic: nervous system 

            1. Introduction to the Nervous System:
            - The nervous system is a complex network of specialized cells that transmits signals between different parts of the body.
            - It is responsible for coordinating actions and responses, processing sensory information, and regulating bodily functions.

            2. Divisions of the Nervous System:
            - Central Nervous System (CNS):
                - Consists of the brain and spinal cord.
                - Serves as the primary processing and control center.
            - Peripheral Nervous System (PNS):
                - Comprises nerves that connect the CNS to the rest of the body.
                - Includes sensory neurons, which transmit information to the CNS, and motor neurons, which carry signals from the CNS to muscles and glands.

            3. Neurons: The Basic Units of the Nervous System:
            - Nerve cells or neurons are the fundamental building blocks of the nervous system.
            - They receive, process, and transmit electrical and chemical signals through specialized structures:
                - Dendrites: Receive signals from other neurons.
                - Cell Body (Soma): Contains the nucleus and performs metabolic functions.
                - Axon: Conducts signals away from the cell body.
                - Axon Terminals: Transmit signals to other neurons or effector organs.

            4. Neurotransmitters: Chemical Messengers of the Nervous System:
            - Neurons communicate with each other through chemical messengers called neurotransmitters.
            - Examples of neurotransmitters include acetylcholine, dopamine, serotonin, and GABA.
            - Each neurotransmitter has specific functions and plays a crucial role in various brain processes.

            5. Reflex Arc: A Simple Neural Pathway:
            - A reflex arc is a basic neural pathway that mediates quick, involuntary responses to stimuli.
            - It involves a sensory receptor, an afferent neuron, an interneuron in the CNS, an efferent neuron, and an effector organ.

            6. Spinal Cord: The Information Highway of the CNS:
            - The spinal cord is a cylindrical structure that extends from the brainstem and runs through the vertebral column.
            - It serves as a communication channel between the brain and the rest of the body.
            - It contains ascending tracts (sensory information) and descending tracts (motor commands).

            7. Brain: The Command Center of the Nervous System:
            - The brain is the most complex part of the nervous system and comprises various regions with specialized functions.
            - Major regions include the cerebrum, cerebellum, brainstem, and limbic system.
            - The cerebrum is responsible for higher cognitive functions, including perception, reasoning, memory, and voluntary movement.
            - The cerebellum coordinates muscle movements and balance.
            - The brainstem controls vital functions such as breathing, heart rate, and sleep-wake cycles.
            - The limbic system is involved in emotions, learning, and memory formation.

            8. Autonomic Nervous System (ANS): Regulating Internal Functions:
            - The ANS regulates involuntary bodily functions such as heart rate, digestion, and respiration.
            - It has two main branches:
                - Sympathetic Nervous System: Activates the body's "fight-or-flight" response.
                - Parasympathetic Nervous System: Promotes "rest-and-digest" activities.

            9. Synapses: The Junctions for Neural Communication:
            - Synapses are the specialized junctions where neurons communicate with each other.
            - They consist of a presynaptic neuron, a postsynaptic neuron, and a synaptic cleft.
            - Neurotransmitters are released from the presynaptic neuron into the synaptic cleft, where they bind to receptors on the postsynaptic neuron, initiating a response.

            10. Neuroplasticity: The Brain's Ability to Adapt:
                - The nervous system exhibits a remarkable ability to change and adapt, known as neuroplasticity.
                - It involves the formation of new neural connections, strengthening or weakening existing ones, and rewiring neural pathways in response to experiences, learning, and injury.





            """
    
    try:
        response = model.generate_content(message)
        print(response.text)
        return response.text
    except Exception as e:
        print(f"Error in generating content: {str(e)}")
        return f"Error: {str(e)}"       
    
def responseOnVideo(transcript, subject):
    message = f"""You are instruxion. You are supposed to generate notes from the transcript of a youtube video based on subject given below.
            transcript: {transcript}
            Subject: {subject}

            Below is an example of the output from the transcript of a video on nervous system: 

            1. Introduction to the Nervous System:
            - The nervous system is a complex network of specialized cells that transmits signals between different parts of the body.
            - It is responsible for coordinating actions and responses, processing sensory information, and regulating bodily functions.

            2. Divisions of the Nervous System:
            - Central Nervous System (CNS):
                - Consists of the brain and spinal cord.
                - Serves as the primary processing and control center.
            - Peripheral Nervous System (PNS):
                - Comprises nerves that connect the CNS to the rest of the body.
                - Includes sensory neurons, which transmit information to the CNS, and motor neurons, which carry signals from the CNS to muscles and glands.

            3. Neurons: The Basic Units of the Nervous System:
            - Nerve cells or neurons are the fundamental building blocks of the nervous system.
            - They receive, process, and transmit electrical and chemical signals through specialized structures:
                - Dendrites: Receive signals from other neurons.
                - Cell Body (Soma): Contains the nucleus and performs metabolic functions.
                - Axon: Conducts signals away from the cell body.
                - Axon Terminals: Transmit signals to other neurons or effector organs.

            4. Neurotransmitters: Chemical Messengers of the Nervous System:
            - Neurons communicate with each other through chemical messengers called neurotransmitters.
            - Examples of neurotransmitters include acetylcholine, dopamine, serotonin, and GABA.
            - Each neurotransmitter has specific functions and plays a crucial role in various brain processes.

            5. Reflex Arc: A Simple Neural Pathway:
            - A reflex arc is a basic neural pathway that mediates quick, involuntary responses to stimuli.
            - It involves a sensory receptor, an afferent neuron, an interneuron in the CNS, an efferent neuron, and an effector organ.

            6. Spinal Cord: The Information Highway of the CNS:
            - The spinal cord is a cylindrical structure that extends from the brainstem and runs through the vertebral column.
            - It serves as a communication channel between the brain and the rest of the body.
            - It contains ascending tracts (sensory information) and descending tracts (motor commands).

            7. Brain: The Command Center of the Nervous System:
            - The brain is the most complex part of the nervous system and comprises various regions with specialized functions.
            - Major regions include the cerebrum, cerebellum, brainstem, and limbic system.
            - The cerebrum is responsible for higher cognitive functions, including perception, reasoning, memory, and voluntary movement.
            - The cerebellum coordinates muscle movements and balance.
            - The brainstem controls vital functions such as breathing, heart rate, and sleep-wake cycles.
            - The limbic system is involved in emotions, learning, and memory formation.

            8. Autonomic Nervous System (ANS): Regulating Internal Functions:
            - The ANS regulates involuntary bodily functions such as heart rate, digestion, and respiration.
            - It has two main branches:
                - Sympathetic Nervous System: Activates the body's "fight-or-flight" response.
                - Parasympathetic Nervous System: Promotes "rest-and-digest" activities.

            9. Synapses: The Junctions for Neural Communication:
            - Synapses are the specialized junctions where neurons communicate with each other.
            - They consist of a presynaptic neuron, a postsynaptic neuron, and a synaptic cleft.
            - Neurotransmitters are released from the presynaptic neuron into the synaptic cleft, where they bind to receptors on the postsynaptic neuron, initiating a response.

            10. Neuroplasticity: The Brain's Ability to Adapt:
                - The nervous system exhibits a remarkable ability to change and adapt, known as neuroplasticity.
                - It involves the formation of new neural connections, strengthening or weakening existing ones, and rewiring neural pathways in response to experiences, learning, and injury.

            """
    
    try:
        response = model.generate_content(message)
        print(response.text)
        return response.text
    except Exception as e:
        print(f"Error in generating content: {str(e)}")
        return f"Error: {str(e)}"     

def quizGenerator(prompt):
    message  = """You are a quiz generator. You will be given the notes enclosed in angular brackets and you have to generate questions based on the notes. 
    For each question you have to generate 4 options out of which only one has to be correct.

    notes: """ + prompt + """The response should be in the following JSON format:

    {
        "responses":[
        {
            "question":<question>,
            "option1":<option1>,
            "option2":<option2>,
            "option3":<option3>,
            "option4":<option4>,
            "answer": <Correct answer as mentioned in the option.>
        }
        ]
    }
    
    For example if you are given a note based on nervous system:
    
     {
        "responses":[
        {
            "question":"Which of the following is a not a part of nervous system",
            "option1":"Central Nervous System",
            "option2":"Peripheral Nervous System",
            "option3":"Upper Nervous System",
            "option4":"All of the above",
            "answer": "Upper Nervous System"
        },
        {
            "question":"Functional unit of nervous system is called",
            "option1":"Central Nervous System",
            "option2":"Neuron",
            "option3":"Nervon",
            "option4":"Dendrite",
            "answer": "Neuron"
        }
        ]
    }
    """  
    try:
        response = model.generate_content(message)
        print(response.text)
        return response.text
    except Exception as e:
        print(f"Error in generating content: {str(e)}")
        return f"Error: {str(e)}"   

def generate_narration(prompt, content, subject):
    message = f"""You are instruxion. You are supposed to generate narration about the prompt. You will be either topic or transcript of a youtube video thet is given to you as prompt and enclosed in angular brackets. 
    You will also be given the subject for context. You will be given content about the topic. Output should be as text and should not be of markdown format.
    Steps to follow:
    1. Say hello and give an introduction about topic.
    2. Briefly explain about topic.
    3. Say Thank you
            transcript: <{prompt}>
            Subject: {subject}
            content: {content}"""
    try:
        response = model.generate_content(message)
        print(response.text)
        return response.text
    except Exception as e:
        print(f"Error in generating content: {str(e)}")
        return f"Error: {str(e)}"   
def generatePrompt(value, subject):
    message = f"""Generate a suitable short and factually correct prompt for generating image.  You will be either topic or transcript of a youtube video thet is given to you as prompt and enclosed in angular brackets. 
    You will also be given the subject for context.
    topic or transcript: {value}
    Subject: {subject}"""
    try:
        response = model.generate_content(message)
        print("Imageof : ", response.text)
        return response.text
    except Exception as e:
        print(f"Error in generating content: {str(e)}")
        return f"Error: {str(e)}"   
    

def generateImage(prompt):
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url
    destination_path = 'static/image.jpg'

    # Download the image
    urllib.request.urlretrieve(image_url, destination_path)

    print(f"Image downloaded to: {destination_path}")

        




