import os
import re
import urllib.parse

html_file = r"d:\New folder (7)\New folder (3)\index.html"

# Mapping filenames to professional titles
title_mapping = {
    "Animals.pdf": "Animal Kingdom Discovery Cards",
    "BodyParts.pdf": "Human Anatomy for Kids",
    "Rectangle 1.pdf": "Shapes & Geometry Basics",
    "english salma 3.pdf": "Early English Learning: Vol 3",
    "final Arabic m salma (1).pdf": "Arabic Foundations for Beginners",
    "fruits.pdf": "Fruit Explorer: Vocabulary Cards",
    "math 1 2 3.pdf": "First Steps in Mathematics",
    "math m salma.pdf": "Interactive Math Workbook",
    "phonics.pdf": "Phonics & Sound Mastery",
    "pre kg  123.pdf": "Pre-K Numbers & Counting",
    "pre kg (letters) final.pdf": "Pre-K Alphabet Adventure",
    "vegetables.pdf": "Vegetable Garden Vocabulary",
    "الحساب 1.pdf": "Mathematics Essentials (Arabic)",
    "الحيوانات.pdf": "Wonders of Animals (Arabic)",
    "تجميعة الكوت.pdf": "Learning Cards Collection",
    "فاكهه وخضار.pdf": "Fruits & Veggies Vocabulary (Arabic)",
    "كروت الالوان مس سلمى.pdf": "Color Spectrum Learning Cards",
    "كروت الفواكه م سلمى.pdf": "Fruit Discovery Cards Collection",
    "مهارات 2.pdf": "Cognitive Skills Development: Level 2",
    "مهام م سلمى.pdf": "Daily Tasks & Activities Workbook"
}

html_pieces = []
for filename, professional_title in title_mapping.items():
    encoded_file = urllib.parse.quote(filename)
    # Using 'a' tag to open the PDF directly
    html = f'''                <a href="assets/books/{encoded_file}" target="_blank" class="book-card" style="text-decoration: none; color: inherit;">
                    <div class="book-cover">
                        <i class="ph-fill ph-file-pdf"></i>
                        <p>View PDF</p>
                    </div>
                    <div class="book-info">
                        <h3>{professional_title}</h3>
                        <p>Educational Material</p>
                    </div>
                </a>'''
    html_pieces.append(html)

new_grid_inner = "\n".join(html_pieces)

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(<div class="books-grid">).*?(</section>)', re.DOTALL)
replacement = r'\1\n' + new_grid_inner + r'\n            </div>\n        \2'

new_content = pattern.sub(replacement, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Added {len(title_mapping)} books to the grid.")
