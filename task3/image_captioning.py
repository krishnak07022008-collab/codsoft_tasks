from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the pretrained BLIP model
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Load image
image = Image.open("sample.jpg").convert("RGB")

# Process image
inputs = processor(images=image, return_tensors="pt")

# Generate caption
output = model.generate(**inputs)

# Decode caption
caption = processor.decode(output[0], skip_special_tokens=True)

print("\nGenerated Caption:")
print(caption)
