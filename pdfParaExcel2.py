import PyPDF2
import csv
from tkinter import *
from tkinter import filedialog
import os

def converterParaCSV():
    # Open the PDF file in read-binary mode
    with open(arquivo, 'rb') as file:
    # Create a PDF file reader object
        pdf_reader = PyPDF2.PdfReader(file)
        nome_arquivo_csv()
        populaCSV(pdf_reader)

# Loop through each page in the PDF file
def populaCSV(arquivoPDF):
    fields = ['VALOR ORIGINAL', 'VALOR ATUALIZADO', 'DEPREC. NO MES', 'DEPREC. NO EXERC', 'DEPREC. ACUMULADA', 'CORR.MON. MES', 'CORR. MON.EXERC', 'CORR. MONET. ACUM.', 'CORR.DEPR. MES', 'CORR.DEPR.EXERC.', 'CORR. DEPR. ACUM' ]
    dicionario = []
    # Create a CSV file writer object
    csv_writer = csv.writer(open(arquivo_CSV+'.csv', 'w', newline=''))
    for page_num in range(1, len(arquivoPDF.pages)):
        # Get the page object
        page = arquivoPDF.pages[page_num]
        # Extract the text from the page
        text = page.extract_text()
        # Split the text into lines
        #  if(len(cabecalho) == 0):
        #     valoresCabecalho = ['VALOR ORIGINAL', 'VALOR ATUALIZADO',  'DEPREC', 'NO MES DEPREC', 'NO EXERC',   'DEPREC', 'ACUMULADA',   'CORR.MON', 'MES CORR', 'MON.EXERC'  'CORR',  'MONET', 'ACUM', 'CORR.DEPR', 'MES',  'CORR.DEPR.EXERC', 'CORR', 'DEPR',  'ACUM']
        #    array = text.strip()
            
            #   cabecalho = [elemento for elemento in valoresCabecalho if elemento in array]

        lines = text.strip().split('\n')
        valores2 = []
        for line in range(len(lines)):
            #print(lines[1])
            #print('\n Nova Linha \n')
            #valores1 = lines[line]
            valores2.append(lines[line].split('--------------------------------------------------- --------------------------------------------------- --------------------------------------------------- --------------------------------------------------- ---------------- '))
            #print(valores1)
            
            print(valores2[line])
        
        # Write each line as a row in the CSV file
        csv_writer.writerow([dicionario])
        for line in lines:
            valores = line.strip().split('-')
            csv_writer.writerow([valores[1:]+['D']+[valores[:1]]])
    print("Inicio Cabeçalho")
    print(dicionario)
 
    print("Fim Cabeçalho")

def abrir_arquivo():
    global arquivo
    caminho = filedialog.askopenfilename(initialdir=os.getcwd(), title="identifique o arquivo de contatos",  filetypes=(("text files", "*.PDF"), ("all files", "*.*")))
    caminhoParaLista = caminho.split('/')
    arquivo = caminhoParaLista[-1]

def nome_arquivo_csv():
    global arquivo_CSV
    arquivo_CSV_temp = arquivo_saida.get('1.0', END)
    arquivo_CSV = arquivo_CSV_temp.strip()
    



janela = Tk()
janela.title("Disparo de mensagens - Whatsapp Busness")
janela.geometry("500x180")
janela.configure(background="#dde")
# ----------------------------------------------------
Button(janela, text="Sair", command=janela.quit).place(x=400, y=10)
Button(janela, text="Selecioar arquivo PDF ", command=abrir_arquivo).place(x=50, y=10)

Label(janela, text="Nome do arquivo de saída").place(x=50, y=50)
arquivo_saida = Text(janela, height=1, width=50, autoseparators=True)
arquivo_saida.place(x=50, y=80, )

#Label(janela, text="Link para postagem").place(x=50, y=210)
#link = Entry(janela)
#link.place(x=50, y=230, width=400)

#------------------------------------------------------
btnEnviar = Button(janela, text="Converter Arquivo", command=converterParaCSV)
btnEnviar.place(x=180, y=120)

janela.mainloop()