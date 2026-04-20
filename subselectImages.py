import sys
from PIL import Image
from transformers import pipeline
from tqdm import tqdm


def subselect_images(image_file_list, out_file_name):
    detector = pipeline("zero-shot-object-detection", model="google/owlvit-base-patch32", device=0)
    with open(image_file_list, 'r', encoding='utf-8-sig') as f:
        image_paths = [line.strip() for line in f]
    selected_files = []
    print(f"Scanning {len(image_paths)} images for squirrels and birdfeeders...")
    for img_path in tqdm(image_paths):
        try:
            image = Image.open(img_path).convert("RGB")
            results = detector(image, candidate_labels=["squirrel", "birdfeeder"])
            found_squirrel = any(res['label'] == 'squirrel' and res['score'] > 0.1 for res in results)
            found_feeder = any(res['label'] == 'birdfeeder' and res['score'] > 0.1 for res in results)

            if found_squirrel and found_feeder:
                selected_files.append(img_path)
        except Exception as e:
            pass

    with open(out_file_name, 'w') as f:
        for path in selected_files:
            f.write(f"{path}\n")

    print(f"\nDone! Found {len(selected_files)} matching images.")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        subselect_images(sys.argv[1], sys.argv[2])
    else:
        subselect_images("allImages.txt", "selectedImages.txt")