import sys
import os
import torch
from PIL import Image, ImageFilter
from diffusers import AutoPipelineForInpainting
from tqdm import tqdm


def remove_squirrels(image_file_list):
    print("Loading Stable Diffusion Inpainting Model (this may take a minute)...")
    pipeline = AutoPipelineForInpainting.from_pretrained(
        "runwayml/stable-diffusion-inpainting",
        torch_dtype=torch.float16,
        variant="fp16"
    ).to("cuda")
    with open(image_file_list, 'r', encoding='utf-8-sig') as f:
        image_paths = [line.strip() for line in f if line.strip()]
    print(f"Erasing squirrels from {len(image_paths)} images...")

    for img_path in tqdm(image_paths):
        try:
            base_name = os.path.splitext(os.path.basename(img_path))[0]
            mask_path = os.path.join(os.path.dirname(img_path), f"{base_name}-sqMask.png")
            init_image = Image.open(img_path).convert("RGB")
            mask_image = Image.open(mask_path).convert("RGB")
            mask_image = mask_image.filter(ImageFilter.MaxFilter(11))
            prompt = "empty background, wooden texture, nature, seamless, continuous scenery, out of focus"
            negative_prompt = "squirrel, animal, artifacts, dark spot, blurry smudge, unnatural, ugly"
            image = pipeline(
                prompt=prompt,
                negative_prompt=negative_prompt,
                image=init_image,
                mask_image=mask_image,
                num_inference_steps=50,
                guidance_scale=7.5
            ).images[0]
            save_path = os.path.join(os.path.dirname(img_path), f"{base_name}-squirrelRemoved.jpg")
            image.save(save_path)

        except Exception as e:
            print(f"Error processing {img_path}: {e}")

    print("\nRemoval complete! Check your folder for the '-squirrelRemoved.jpg' images.")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        remove_squirrels(sys.argv[1])
    else:
        remove_squirrels("selectedImages.txt")