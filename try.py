from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client(api_key="AIzaSyA1q7NWImiosKYQM0sFpD8TCOcvZ8tXXF4")

response = client.models.generate_images(
    model='imagen-3.0-generate-002',
    prompt='Robot holding a red skateboard',
    config=types.GenerateImagesConfig(
        number_of_images= 4,
    )
)
for generated_image in response.generated_images:
  generated_image.image.show()



{'changes': [{'file': 'generated_output/src/app/resume-preview.page.ts', 'reason': "The user wants to change the background color of the resume itself. The '.mock-resume' CSS class is responsible for styling the main content area of the resume, and its background is currently set to white.", 'current_code_excerpt': 'background-color: #fff;', 'instructions': "Modify the 'background-color' property within the '.mock-resume' style block from '#fff' to a suitable blue color. For example, change it to '#add8e6' for a light blue."}], 'notes': "The chosen blue color code is an example. The user can specify any desired shade of blue to replace '#fff'."}