# 🐿️ Squirrel Detection, Removal, and Bird Replacement

> **A dual-approach computer vision project comparing local Hugging Face pipelines with online multimodal AI tools for intelligent wildlife image manipulation.**

This project explores two distinct methodologies for automated image editing:
* **Method 1:** A modular, local computer vision pipeline utilizing Hugging Face models for zero-shot detection, segmentation, and inpainting.
* **Method 2:** Cloud-based multimodal AI tools for advanced image editing and video generation.

### 🎯 Pipeline Objectives (Method 1)
1. **Filter:** Select images featuring a squirrel next to a birdfeeder.
2. **Segment:** Generate an accurate, slightly enlarged mask isolating the squirrel.
3. **Erase:** Seamlessly remove the squirrel from the background.
4. **Replace:** Inpaint a bird into the squirrel's original location.

---

## 📁 Project Structure

```text
📦 project-root
├── 📂 originalImgs/                       # Source image dataset
├── 📄 allImages.txt                       # Generated list of all image paths
├── 📄 selectedImages.txt                  # Output list of filtered images
├── 🐍 assignment5_utils.py                # Helper functions and models
├── 🐍 subselectImages.py                  # Step 1: Detects and filters images
├── 🐍 segmentSquirrels.py                 # Step 2: Generates squirrel masks
├── 🐍 removeSquirrels.py                  # Step 3: Inpaints to remove squirrels
├── 🐍 replaceSquirrelsWithBirds.py        # Step 4: Inpaints to replace with birds
├── 📄 chatTranscriptLinks.txt             # Method 2: Replacement chat links
├── 📄 eraseChatTranscriptLinks.txt        # Method 2: Erasure chat links
├── 📄 generationChatTranscriptLinks.txt   # Method 2: T2I chat links
├── 📄 videoPromptGenerationChat.txt       # Method 2: Video prompt dev logs
├── 🎬 myVideo.mp4                         # Method 2: 8-second instructional video
├── 🤐 myImageFiles.zip                    # Final packaged outputs
└── 📖 README.md
```

---

## 🛠️ Requirements & Setup

Ensure you have the required Python packages installed before executing the pipeline:

```bash
pip install torch torchvision pillow numpy transformers diffusers accelerate sentencepiece protobuf
```

### Input Dataset Preparation
Place all your source images in the `originalImgs/` directory. Before running the Python scripts, generate a text file containing all the image paths.

**PowerShell Command to generate `allImages.txt`:**
```powershell
Get-ChildItem -Path .\originalImgs -Recurse -File -Include *.jpg,*.jpeg,*.png |
Select-Object -ExpandProperty FullName |
Set-Content .\allImages.txt
```

*Verification commands:*
```powershell
Get-Content .\allImages.txt               # View the generated list
(Get-Content .\allImages.txt).Count       # Count the total number of images found
```

---

## 🚀 Method 1: Local CV Pipeline Workflow

For the best results, execute the scripts sequentially.

### Step 1: Filter Images
Detects and selects only the images containing a squirrel near a birdfeeder.
```bash
python subselectImages.py allImages.txt selectedImages.txt
```
* **Outputs:** `selectedImages.txt`

### Step 2: Generate Masks
Reads the selected images, isolates the squirrel, and creates a mask.
```bash
python segmentSquirrels.py selectedImages.txt
```
* **Outputs:** `imageName-sqMask.png` (e.g., `originalImgs/example-sqMask.png`)

### Step 3: Remove Squirrels
Utilizes an inpainting model alongside the generated mask to erase the squirrel.
```bash
python removeSquirrels.py selectedImages.txt
```
* **Outputs:** `imageName-squirrelRemoved.jpg`

### Step 4: Replace with Birds
Utilizes the mask and inpainting to swap the squirrel with a bird.
```bash
python replaceSquirrelsWithBirds.py selectedImages.txt
```
* **Outputs:** `imageName-birdReplaced.jpg`

---

## 🌐 Method 2: Multimodal AI Deliverables

Using an online multimodal assistant, process at least **3 images** from your `selectedImages.txt` file to complete the following tasks:

| Task | Output Image Files | Transcript File |
| :--- | :--- | :--- |
| **Replace** (Squirrel to Bird) | `onlineModed1.jpg`, `onlineModed2.jpg`, `onlineModed3.jpg` | `chatTranscriptLinks.txt` |
| **Erase** (Remove Squirrel) | `onlineErased1.jpg`, `onlineErased2.jpg`, `onlineErased3.jpg` | `eraseChatTranscriptLinks.txt` |
| **Generate** (Text-to-Image) | `onlineGenerated1.jpg`, `onlineGenerated2.jpg`, `onlineGenerated3.jpg` | `generationChatTranscriptLinks.txt` |

---

## 💡 Notes & Best Practices

* **Mask Sizing:** Ensure squirrel masks are slightly larger than the subject (not tightly cropped) for better blending.
* **Prompt Tuning:** Inpainting quality is highly dependent on the model and prompts. Adjust your text descriptions if outputs look unnatural.
* **Manual Inspection:** Always manually review your masks and the realism of your generated outputs. The quality of this pipeline relies heavily on accurate initial filtering and complete masks.
