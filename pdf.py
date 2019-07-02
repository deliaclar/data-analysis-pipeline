from fpdf import FPDF

def creoPDF():
    pdf=FPDF()
    pdf.add_page()
    pdf.set_margins(10,10)
    pdf.set_font('Arial', 'B', 20) 
    pdf.cell(100, 10, 'Gráficas Pokemon',align='center')
    y=50

    for i in range(3):
        pdf.cell(90, 10, " ", 0, 2, 'C')   
        pdf.image('figura{}.png'.format(i), x=50, y=y, w=100, h=100, type = '', link = '')
        y+=100
        pdf.add_page()

    pdf.output("Proyecto.pdf","F")


