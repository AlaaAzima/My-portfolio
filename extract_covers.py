import os
import fitz
import re
import urllib.parse

books_dir = r"d:\New folder (7)\New folder (3)\assets\books"
covers_dir = r"d:\New folder (7)\New folder (3)\assets\images\books_covers"
html_file = r"d:\New folder (7)\New folder (3)\index.html"

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

for filename in os.listdir(books_dir):
    if filename.lower().endswith('.pdf'):
        pdf_path = os.path.join(books_dir, filename)
        cover_filename = filename[:-4] + ".png"
        cover_path = os.path.join(covers_dir, cover_filename)
        
        try:
            doc = fitz.open(pdf_path)
            page = doc.load_page(0)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            pix.save(cover_path)
            doc.close()
            pass
        except Exception as e:
            pass
            continue

        title = title_mapping.get(filename, filename)
        encoded_pdf = urllib.parse.quote(filename)
        encoded_img = urllib.parse.quote(cover_filename)

        html = f'''                <a href="assets/books/{encoded_pdf}" target="_blank" class="book-card" style="text-decoration: none; color: inherit;">
                    <div class="book-cover" style="padding: 0; border-bottom: none;">
                        <img src="assets/images/books_covers/{encoded_img}" alt="{title} Cover" style="width: 100%; height: 100%; object-fit: cover;">
                    </div>
                    <div class="book-info">
                        <h3>{title}</h3>
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

print(f"Added {len(html_pieces)} books to the grid with covers.")
