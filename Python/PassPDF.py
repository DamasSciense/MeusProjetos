import fitz
import os

pdf = fitz.open('MeusProjetos/Python/FaturaC62022.pdf')

if pdf.is_encrypted:
    print('SIM')
    pdf.authenticate('675871')