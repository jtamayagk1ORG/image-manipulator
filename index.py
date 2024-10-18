import os
from PIL import Image

def resize_image(image_path, output_sizes, output_dir="resized_images"):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the image file
    with Image.open(image_path) as img:
        # Get the base name of the file (e.g., "github-administration.png")
        image_filename = os.path.basename(image_path)
        
        # Iterate through the desired sizes
        for label, size in output_sizes.items():
            resized_img = img.resize(size, Image.LANCZOS)  # Resize the image
            # Create the output path
            output_path = os.path.join(output_dir, f"{label}_{image_filename}")
            resized_img.save(output_path)  # Save the resized image
            print(f"Saved: {output_path}")

# Path to the uploaded image
image_path = "images/github-administration.png"

# Define output sizes
output_sizes = {
    "small": (80, 80),
    "medium": (100, 100),
    "large": (120, 120)
}

# Resize the image and save
resize_image(image_path, output_sizes)

print("Images resized and saved.")
