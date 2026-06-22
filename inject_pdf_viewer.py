import re
import os

html_file = r"d:\New folder (7)\New folder (3)\index.html"

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <a href="assets/books/..." target="_blank" class="book-card">
# with <div class="book-card" onclick="openPdfViewer('assets/books/...')">

def replacer(match):
    pdf_url = match.group(1)
    # Return a div instead of a tag, keeping the inner HTML
    return f'<div class="book-card" onclick="openPdfViewer(\'{pdf_url}\')" style="cursor: pointer;">'

pattern = re.compile(r'<a href="(assets/books/[^"]+\.pdf)" target="_blank" class="book-card"[^>]*>')
content = pattern.sub(replacer, content)

# Change closing </a> to </div> for the book cards
# Since we only want to change </a> inside books-grid, we can just replace all </a> in the books-grid block
grid_pattern = re.compile(r'(<div class="books-grid">.*?)(</section>)', re.DOTALL)
def grid_replacer(match):
    grid_content = match.group(1)
    grid_content = grid_content.replace('</a>', '</div>')
    return grid_content + match.group(2)

content = grid_pattern.sub(grid_replacer, content)

# Inject PDF Modal HTML right after the Lightbox
modal_html = '''
    <!-- PDF Viewer Modal -->
    <div id="pdf-modal" class="hidden">
        <div class="pdf-modal-content">
            <div class="pdf-header">
                <div class="pdf-controls">
                    <button id="pdf-prev" class="btn btn-outline"><i class="ph-fill ph-caret-left"></i> Prev</button>
                    <span>Page: <span id="pdf-page-num"></span> / <span id="pdf-page-count"></span></span>
                    <button id="pdf-next" class="btn btn-outline">Next <i class="ph-fill ph-caret-right"></i></button>
                </div>
                <span class="close-pdf" onclick="closePdfModal()">&times;</span>
            </div>
            <div class="pdf-canvas-container">
                <canvas id="pdf-canvas"></canvas>
            </div>
        </div>
    </div>
'''

if 'id="pdf-modal"' not in content:
    content = content.replace('<!-- Lightbox -->', modal_html + '\n    <!-- Lightbox -->')

# Add PDF.js script to head
pdfjs_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>'
if 'pdf.min.js' not in content:
    content = content.replace('</head>', f'    {pdfjs_script}\n</head>')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated HTML for PDF Viewer.")
