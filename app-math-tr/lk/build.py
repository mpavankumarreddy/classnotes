import os, sys
    
if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex lk.tex")
    os.system("evince lk.pdf")
    exit()
    
