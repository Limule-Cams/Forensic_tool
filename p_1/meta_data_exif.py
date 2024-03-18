#!/venv/bin/python3
#coding:utf8

from PyPDF2 import PdfReader,PdfWriter
import argparse
import re
import exifread

file = "c.pdf"

def info_Pdf(file_name):
    with open(file_name, 'rb') as fichier:
        fic = PyPDF2.PdfReader(fichier)
        info = fic.metadata
        for i, j in info.items():
            print(f"{i} : {j}\n")

def info_Pdf_all(file_name):
    with open(file_name, 'rb') as fic:
        al = fic.read()
    ret = re.compile('[\S\s]{4,}')
    for i in ret.finditer(al.decode("utf-8", "backslashreplace")):
        print(i.group())


def brute_force_pdf(pdf, file):
    reader = PdfReader(pdf)
    writer = PdfWriter()
    if reader.is_encrypted:
        with open(file, 'rb') as fic:
            for line in fic:
                line = line.strip()  
                reader.decrypt(line)
                if not reader.is_encrypted:
                    break

    for page in reader.pages:
        writer.add_page(page)

    with open(pdf, "wb") as f:
        writer.write(f)


def info_meta_img(img):
    with open(img, 'rb') as fic:
        meta = exifread.process_file(fic)
        for i, j in meta.items():
            if isinstance(j, bytes):
                #j = j.decode()
                break
            print(f"{i} : {j}")

   


parser = argparse.ArgumentParser(description="search tools")
parser.add_argument("-pdf", dest="pdf", help="chemin fichier", required=False)
parser.add_argument("-img", dest="src", help="image file", required=False)
args = parser.parse_args()

if args.pdf:
    info_Pdf_all(args.pdf)    
if args.src:
    info_meta_img(args.src)
