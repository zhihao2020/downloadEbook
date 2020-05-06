import sys
import os
import comtypes.client
os.chdir("E:/demo")
wdFormatPDF = 17
file = os.listdir("E:/demo")
for i in file:
    in_file = os.getcwd()+'\\' +i
    print("In:%s"%in_file)
    out_file = "E:/demo/PDF/%s.pdf"%i.strip(".docx")
    print("out:%s"%out_file)
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()