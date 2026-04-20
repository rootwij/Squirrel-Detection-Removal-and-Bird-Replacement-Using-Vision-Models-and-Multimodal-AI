# Squirrel Detection, Removal, and Bird Replacement

This project compares two image manipulation approaches for wildlife scenes:

- **Method 1:** a modular computer vision pipeline using Hugging Face models for detection, segmentation, and inpainting
- **Method 2:** online multimodal AI tools for image editing and video generation

The main goal of Method 1 is to:
1. select images containing a **squirrel next to a birdfeeder**
2. generate a **mask** for the squirrel
3. create an image where the **squirrel is removed**
4. create an image where the **squirrel is replaced with a bird**

---

## Project Files

```text
├── originalImgs/
├── allImages.txt
├── selectedImages.txt
├── assignment5_utils.py
├── subselectImages.py
├── segmentSquirrels.py
├── removeSquirrels.py
├── replaceSquirrelsWithBirds.py
├── chatTranscriptLinks.txt
├── eraseChatTranscriptLinks.txt
├── generationChatTranscriptLinks.txt
├── videoPromptGenerationChat.txt
├── myVideo.mp4
├── myImageFiles.zip
└── README.md
What Each Script Does
subselectImages.py

Reads a text file of image paths and selects only the images that contain a squirrel near a birdfeeder.
Creates:

selectedImages.txt
segmentSquirrels.py

Reads selectedImages.txt, detects the squirrel, and creates a slightly enlarged squirrel mask.
Creates one mask per selected image:

imageName-sqMask.png
removeSquirrels.py

Uses the saved mask and an inpainting model to remove the squirrel from the image.
Creates:

imageName-squirrelRemoved.jpg
replaceSquirrelsWithBirds.py

Uses the saved mask and an inpainting model to replace the squirrel with a bird.
Creates:

imageName-birdReplaced.jpg
Requirements

Install Python packages before running the pipeline:

pip install torch torchvision pillow numpy transformers diffusers accelerate sentencepiece protobuf
Input Dataset

The source images are stored in the originalImgs/ folder.

Before running the code, create a text file named allImages.txt containing all image paths from that folder.

PowerShell command to generate allImages.txt
Get-ChildItem -Path .\originalImgs -Recurse -File -Include *.jpg,*.jpeg,*.png |
Select-Object -ExpandProperty FullName |
Set-Content .\allImages.txt
Check that it worked
Get-Content .\allImages.txt
Count how many images were found
(Get-Content .\allImages.txt).Count
How to Run the Code

Run the pipeline in this exact order.

Step 1: Select squirrel-at-birdfeeder images
python subselectImages.py allImages.txt selectedImages.txt
Output

Creates:

selectedImages.txt

This file contains only the paths of images selected by the object detection stage.

Step 2: Create squirrel masks
python segmentSquirrels.py selectedImages.txt
Output

For each selected image, creates a mask named:

imageName-sqMask.png

Example:

originalImgs/example-sqMask.png
Step 3: Remove squirrels from the selected images
python removeSquirrels.py selectedImages.txt
Output

For each selected image, creates:

imageName-squirrelRemoved.jpg

Example:

originalImgs/example-squirrelRemoved.jpg
Step 4: Replace squirrels with birds
python replaceSquirrelsWithBirds.py selectedImages.txt
Output

For each selected image, creates:

imageName-birdReplaced.jpg

Example:

originalImgs/example-birdReplaced.jpg
Full Run Example

After setting up the image list, run:

python subselectImages.py allImages.txt selectedImages.txt
python segmentSquirrels.py selectedImages.txt
python removeSquirrels.py selectedImages.txt
python replaceSquirrelsWithBirds.py selectedImages.txt
Expected Outputs

After the full pipeline runs, you should have:

selectedImages.txt
one -sqMask.png file per selected image
one -squirrelRemoved.jpg file per selected image
one -birdReplaced.jpg file per selected image

If an input image is:

originalImgs\squirrel_feeder_01.jpg

then the expected outputs are:

originalImgs\squirrel_feeder_01-sqMask.png
originalImgs\squirrel_feeder_01-squirrelRemoved.jpg
originalImgs\squirrel_feeder_01-birdReplaced.jpg
Recommended Workflow

For best results:

generate allImages.txt
run subselectImages.py
inspect selectedImages.txt
run segmentSquirrels.py
inspect the masks
run removeSquirrels.py
run replaceSquirrelsWithBirds.py
inspect realism and image quality

This matters because assignment quality depends on:

selecting the correct images
making complete squirrel masks
generating realistic edited outputs
Method 2 Deliverables

Using at least 3 images from selectedImages.txt, use an online multimodal assistant to create:

Squirrel replaced by bird

Save images as:

onlineModed1.jpg
onlineModed2.jpg
onlineModed3.jpg

Save transcript links in:

chatTranscriptLinks.txt
Squirrel erased

Save images as:

onlineErased1.jpg
onlineErased2.jpg
onlineErased3.jpg

Save transcript links in:

eraseChatTranscriptLinks.txt
Text-to-image generations

Save images as:

onlineGenerated1.jpg
onlineGenerated2.jpg
onlineGenerated3.jpg

Save transcript links in:

generationChatTranscriptLinks.txt
Video generation

Generate an 8-second instructional video and save:

myVideo.mp4

Save the chat or prompt development in:

videoPromptGenerationChat.txt
Packaging for Submission

Bundle the generated images and related outputs into:

myImageFiles.zip

Final submission should include:

subselectImages.py
segmentSquirrels.py
removeSquirrels.py
replaceSquirrelsWithBirds.py
myImageFiles.zip
chatTranscriptLinks.txt
eraseChatTranscriptLinks.txt
generationChatTranscriptLinks.txt
videoPromptGenerationChat.txt
Notes
The squirrel masks should be slightly larger than the squirrel, not extremely tight.
Inpainting quality may vary depending on the model and prompt.
Manual inspection is important for both mask quality and realism.
If outputs look strange, prompt tuning and mask adjustment can improve results.


Thanks !!!
