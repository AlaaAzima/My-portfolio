import os
import re
import urllib.parse

design_dir = r"d:\New folder (7)\New folder (3)\My portfolio\assets\images\design"
html_file = r"d:\New folder (7)\New folder (3)\My portfolio\index.html"

images = []
for f in os.listdir(design_dir):
    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        images.append(f)

html_pieces = []
for img in images:
    label = "Design Work"
    if "روق" in img or "Rawaq" in img or "rawaq" in img.lower():
        label = "Rawaq (Brand Owner)"
    elif "FCAI" in img.upper() or "GAME DEV" in img.upper():
        label = "FCAI-Cu Game Dev"
    
    encoded_img = urllib.parse.quote(img)
    html = f'''                <div class="gallery-item" onclick="openLightbox(this)">
                    <img src="assets/images/design/{encoded_img}" alt="{label}">
                    <div class="item-overlay">
                        <span>{label}</span>
                    </div>
                </div>'''
    html_pieces.append(html)

new_gallery_inner = "\n".join(html_pieces)

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(<div class="masonry-gallery">).*?(</section>)', re.DOTALL)
replacement = r'\1\n' + new_gallery_inner + r'\n            </div>\n        \2'

new_content = pattern.sub(replacement, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("HTML updated with URL-encoded image paths.")
