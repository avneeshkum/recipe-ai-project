from fpdf import FPDF
from datetime import datetime
import re
import os  # Added for folder creation

class RecipePDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(0, 102, 204)
        self.cell(0, 10, "AI-Powered Recipe Generator", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()} | Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}", align="C")

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(0)
        self.cell(0, 10, f"\n{title}", ln=True)

    def section_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

# 🧹 Emoji Cleaner
def remove_emojis(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

# 📁 Define output directory
OUTPUT_DIR = "sample_recipes"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_to_text(filename, content):
    if not filename.endswith(".txt"):
        filename += ".txt"
    full_path = os.path.join(OUTPUT_DIR, filename)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Recipe saved to {full_path}")

def save_to_pdf(filename, content):
    if not filename.endswith(".pdf"):
        filename += ".pdf"
    full_path = os.path.join(OUTPUT_DIR, filename)

    content = remove_emojis(content)  # 🧹 Clean content before saving

    pdf = RecipePDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Format each section
    sections = content.strip().split("\n\n")
    for section in sections:
        lines = section.strip().split("\n")
        if len(lines) > 1:
            pdf.section_title(lines[0])
            pdf.section_body("\n".join(lines[1:]))
        else:
            pdf.section_body(section)

    pdf.output(full_path)
    print(f"✅ Recipe saved as PDF: {full_path}")
