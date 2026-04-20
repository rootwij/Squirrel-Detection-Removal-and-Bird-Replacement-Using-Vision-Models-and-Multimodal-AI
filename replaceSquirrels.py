import sys
import os
import torch
from PIL import Image, ImageFilter
from diffusers import AutoPipelineForInpainting
from tqdm import tqdm


def replace_with_birds(image_file_list):
    print("Loading Stable Diffusion Inpainting Model...")
    pipeline = AutoPipelineForInpainting.from_pretrained(
        "runwayml/stable-diffusion-inpainting",
        torch_dtype=torch.float16,
        variant="fp16"
    ).to("cuda")
    with open(image_file_list, 'r', encoding='utf-8-sig') as f:
        image_paths = [line.strip() for line in f if line.strip()]
    print(f"Replacing squirrels with birds in {len(image_paths)} images...")
    for img_path in tqdm(image_paths):
        try:
            base_name = os.path.splitext(os.path.basename(img_path))[0]
            mask_path = os.path.join(os.path.dirname(img_path), f"{base_name}-sqMask.png")
            init_image = Image.open(img_path).convert("RGB")
            mask_image = Image.open(mask_path).convert("RGB")
            mask_image = mask_image.filter(ImageFilter.MaxFilter(9))
            prompt = "A highly detailed, beautiful, colorful small songbird perched, sharp focus, photorealistic, national geographic photography, natural lighting"
            negative_prompt = "squirrel, fur, ugly, deformed, cartoon, illustration, floating, bad anatomy, missing beak"

            image = pipeline(
                prompt=prompt,
                negative_prompt=negative_prompt,
                image=init_image,
                mask_image=mask_image,
                num_inference_steps=50,
                guidance_scale=7.5
            ).images[0]
            save_path = os.path.join(os.path.dirname(img_path), f"{base_name}_bird.jpg")
            image.save(save_path)
        except Exception as e:
            print(f"Error processing {img_path}: {e}")
    print("\nReplacement complete! Check your folder for the '_bird' images.")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        replace_with_birds(sys.argv[1])
    else:
        replace_with_birds("selectedImages.txt")