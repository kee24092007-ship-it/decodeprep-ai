from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=10)

with open("decode_knowledge_base.txt", "r", encoding="utf-8") as f:
    for line in f:
        pdf.cell(200, 5, txt=line.strip(), ln=True)

pdf.output("Decode_Labs_Knowledge_Base.pdf")

print("PDF created successfully!")