from botcity.document_processing import *
import pathlib
import pandas as pd

dados = []

def lerPDF(arquivo):
    reader = PDFReader()
    parser = reader.read_file(arquivo)

    
    _date = parser.get_first_entry("Date:")
    date = parser.read(_date, 1.425, -1.75, 3.225, 3.5)
    print( 'Date: ' + date )
    
    _bill_to = parser.get_first_entry("Bill to:")
    bill_to = parser.read(_bill_to, 1.111111, -1.75, 6.240741, 3.25)
    print( 'Bill to: ' + bill_to )

    _contact = parser.get_first_entry("Contact:")
    contact = parser.read(_contact, 1.184211, -1.25, 4.842105, 2.5)
    print( 'Contact: ' + contact )

    _balance_due = parser.get_first_entry("Balance due:")
    balance = parser.read(_balance_due, 1.146667, -1.714286, 1.446667, 3.571429)
    print( 'Balance due: ' + balance )

    dados.append([date, bill_to, contact, balance])

arquivos = pathlib.Path('C:\\Users\\jhona\\OneDrive\Área de Trabalho\\botcity\curso-rpa-bot\\docs').glob('*.pdf')
for arquivo in arquivos:
    #print(arquivo)
    lerPDF(arquivo)

#lerPDF()

df = pd.DataFrame(dados, columns=['DATE', 'BILL TO', 'CONTACT', 'BALANCE'])
df.to_csv('dados_PDF.csv', sep= ',', index=False)
    




