import sys
import os
import torch
from PIL import Image, ImageFilter
from transformers import CLIPSegProcessor, CLIPSegForImageSegmentation
from tqdm import tqdm
import numpy as np


def segment_squirrels(image_file_list):
    print("Downloading/Loading the CLIPSeg segmentation model...")
    processor = CLIPSegProcessor.from_pretrained("CIDAS/clipseg-rd64-refined")
    model = CLIPSegForImageSegmentation.from_pretrained("CIDAS/clipseg-rd64-refined")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    with open(image_file_list, 'r', encoding='utf-8-sig') as f:
        image_paths = [line.strip() for line in f if line.strip()]

    print(f"Generating binary masks for {len(image_paths)} images...")

    for img_path in tqdm(image_paths):
        try:
            image = Image.open(img_path).convert("RGB")
            prompt = ["squirrel"]
            inputs = processor(text=prompt, images=[image], padding="max_length", return_tensors="pt").to(device)

            with torch.no_grad():
                outputs = model(**inputs)

            preds = outputs.logits.unsqueeze(1)
            mask = torch.sigmoid(preds[0][0]).cpu().numpy()

            # Create the binary mask
            binary_mask = (mask > 0.4) * 255
            mask_image = Image.fromarray(binary_mask.astype(np.uint8)).resize(image.size)

            # THE FIX: Dilate (enlarge) the mask so it captures the bushy hair!
            mask_image = mask_image.filter(ImageFilter.MaxFilter(15))

            # Save exactly as the professor requested
            base_name = os.path.splitext(os.path.basename(img_path))[0]
            save_path = os.path.join(os.path.dirname(img_path), f"{base_name}-sqMask.png")
            mask_image.save(save_path)

        except Exception as e:
            print(f"\nError processing {img_path}: {e}")

    print("\nDone! Check your folder for the new '-sqMask.png' files.")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        segment_squirrels(sys.argv[1])
    else:
        segment_squirrels("selectedImages.txt")