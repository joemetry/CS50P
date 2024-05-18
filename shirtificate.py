from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')

    def shirt_image(self, name):
        self.image('shirtificate.png', x=10, y=60, w=190)
        self.set_text_color(255, 255, 255)
        self.set_font('Arial', 'B', 20)
        self.set_y(120)
        self.cell(0, 10, name, 0, 1, 'C')

def main():
    name = input("Enter your name for the shirtificate: ")
    pdf = Shirtificate('P', 'mm', 'A4')
    pdf.add_page()
    pdf.shirt_image(name)
    pdf.output('shirtificate.pdf')

if __name__ == "__main__":
    main()
