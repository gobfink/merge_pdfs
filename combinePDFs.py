from PyPDF2 import PdfFileMerger, PdfFileReader
import sys

if len(sys.argv) < 3:
    print(f"Usage:{sys.argv[0]} <pdf to output> <pdf in 1> <pdfin2> ... ")
    exit

mergedObject = PdfFileMerger()
output_pdf=sys.argv[1]
input_pdfs=sys.argv[2:]

print(f"creating {output_pdf} from {input_pdfs}")

# Loop through all of the incoming files
for pdf_in in input_pdfs:
    print(f"Working on - {pdf_in}")
    mergedObject.append(PdfFileReader(pdf_in,'rb'))
    
# Write all the files into a file which is named as shown below
mergedObject.write(output_pdf)
print(f"Finished writing {output_pdf}")
