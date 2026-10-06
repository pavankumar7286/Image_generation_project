from openai import OpenAI
from PIL import Image
from io import BytesIO
import os
import base64
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

def generate_img_txt(prompt, image_size="1024x1024"):
    try :
        print(f"Generating image for prompt: {prompt}")
        response = client.images.generate(
            model ="gpt-image-1",
            prompt=prompt,
            size=image_size
        )

        image_data = base64.b64decode(response.data[0].b64_json)

        image = Image.open(BytesIO(image_data))

        image.save("generated_image.png")
        print("Image saved")

        image.show()

        return "Image generated succesfully"
    except Exception as e:
        return f"Error :{str(e)}"

prompt_text = input("describe the image you want to generate: ")
result = generate_img_txt(prompt_text)
print(result)