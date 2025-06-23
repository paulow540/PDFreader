from fpdf import FPDF

# Create PDF document
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 70, 130)
        self.cell(0, 10, 'SQL for Data Analysis Curriculum (2025 Edition - Microsoft Standard)', 0, 1, 'C')
        self.ln(2)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(1)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.set_text_color(0)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Content from the document (what is data analysis)
content = """
Data analysis is the process of inspecting, cleansing, transforming, and modeling data with the goal of 
discovering useful information, informing conclusions, and supporting decision-making. It involves systematically 
applying statistical and/or logical techniques to describe, illustrate, condense, recap, and evaluate data. 
Essentially, it's about taking raw data and turning it into actionable insights. 
What is Data Analysis? 
Here's a more detailed breakdown:
Inspection:
- Examining the data to identify potential issues, errors, or inconsistencies. 
Cleansing:
- Correcting or removing inaccurate, incomplete, irrelevant, or duplicated data. 
Transformation:
- Converting data into a suitable format for analysis, such as converting categorical data into numerical data. 
Modeling:
- Applying statistical or machine learning techniques to find patterns, relationships, and trends in the data. 
Interpretation:
- Drawing conclusions and making recommendations based on the findings of the analysis. 
Data analysis is crucial in various fields, including scientific research, business, and healthcare, where it 
helps in understanding past trends, predicting future outcomes, and improving efficiency. 
"""

# Add content to PDF
pdf.chapter_body(content)

# Save PDF
pdf_path = "what_is_dataanalysis.pdf"
pdf.output(pdf_path)
