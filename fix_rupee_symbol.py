with open("generate_proposal_text.py") as f:
    text = f.read()

# Replace ₹ with Rs. 
text = text.replace("₹", "Rs. ")

with open("generate_proposal_text.py", "w") as f:
    f.write(text)

with open("generate_pdf.py") as f:
    pdf_code = f.read()

# Replace ₹ in generate_pdf.py
pdf_code = pdf_code.replace("<b>₹40.00 Lakhs</b>", "<b>Rs. 40.00 Lakhs</b>")
pdf_code = pdf_code.replace("<b>₹20.00 Lakhs</b>", "<b>Rs. 20.00 Lakhs</b>")
pdf_code = pdf_code.replace("₹40.00 Lakhs", "Rs. 40.00 Lakhs")
pdf_code = pdf_code.replace("₹40 Lakhs", "Rs. 40 Lakhs")
pdf_code = pdf_code.replace("₹20.00 Lakhs", "Rs. 20.00 Lakhs")
pdf_code = pdf_code.replace("Allocation (₹)", "Allocation (Rs.)")
pdf_code = pdf_code.replace("₹6.0L", "Rs. 6.0L")
pdf_code = pdf_code.replace("₹5.0L", "Rs. 5.0L")
pdf_code = pdf_code.replace("₹3.0L", "Rs. 3.0L")
pdf_code = pdf_code.replace("<b>₹20,00,000</b>", "<b>Rs. 20,00,000</b>")
pdf_code = pdf_code.replace("₹6,50,000", "Rs. 6,50,000")
pdf_code = pdf_code.replace("₹5,00,000", "Rs. 5,00,000")
pdf_code = pdf_code.replace("₹4,50,000", "Rs. 4,50,000")
pdf_code = pdf_code.replace("₹4,00,000", "Rs. 4,00,000")
pdf_code = pdf_code.replace("<b>₹40,00,000</b>", "<b>Rs. 40,00,000</b>")
pdf_code = pdf_code.replace("₹", "Rs. ")

with open("generate_pdf.py", "w") as f:
    f.write(pdf_code)

print("generate_proposal_text.py and generate_pdf.py updated.")
