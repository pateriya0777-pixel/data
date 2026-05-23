import os
import shutil
import cv2
import imagehash
from PIL import Image
from tqdm import tqdm

def get_sharpness(image_path):
    """Calculates sharpness of the center of the image."""
    img = cv2.imread(image_path)
    if img is None: return 0
    h, w = img.shape[:2]
    # Crop to center 50% to ignore bokeh/blurred backgrounds
    crop = img[h//4:3*h//4, w//4:3*w//4]
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

def keep_sharpest_wedding_photos(source_folder):
    dup_dir = os.path.join(source_folder, 'duplicates_lower_quality')
    os.makedirs(dup_dir, exist_ok=True)

    # Dictionary to store {hash: (filename, sharpness_score)}
    best_images = {}
    files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    print(f"Analyzing {len(files)} images to find the sharpest versions...")

    for filename in tqdm(files, desc="Comparing Quality"):
        path = os.path.join(source_folder, filename)
        
        try:
            # 1. Get Perceptual Hash
            with Image.open(path) as img:
                h = str(imagehash.phash(img))
            
            # 2. Get Sharpness Score
            current_sharpness = get_sharpness(path)

            # 3. If we've seen this image before, compare quality
            if h in best_images:
                prev_filename, prev_sharpness = best_images[h]

                if current_sharpness > prev_sharpness:
                    # Current is better: Move the OLD one to duplicates
                    old_path = os.path.join(source_folder, prev_filename)
                    if os.path.exists(old_path):
                        shutil.move(old_path, os.path.join(dup_dir, prev_filename))
                    
                    # Update record to the new, sharper version
                    best_images[h] = (filename, current_sharpness)
                    tqdm.write(f"Found sharper version: {filename} replaced {prev_filename}")
                else:
                    # Current is worse: Move CURRENT one to duplicates
                    shutil.move(path, os.path.join(dup_dir, filename))
            else:
                # First time seeing this image
                best_images[h] = (filename, current_sharpness)

        except Exception as e:
            tqdm.write(f"Error with {filename}: {e}")

    print("\nProcess Complete. Only the sharpest versions remain in your main folder!")

# Run the script
my_path = r"F:\A_marriage\01_Haldi\01"
keep_sharpest_wedding_photos(my_path)