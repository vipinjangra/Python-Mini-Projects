*********************************************************************
#You can use source codes as you want
#But You have to give our profile link in your code as comment
#Copy Below Codes and Paste in your codes Comment Section
*********************************************************************
#Github: https://github.com/vipinjangra
#Youtube: https://www.youtube.com/c/vipincoding/
#Blog: http://vipincoding.wordpress.com/
#Website: http://vipincoding.blogspot.com
#Facebook: https://www.facebook.com/vipincoding
#Instagram: https://www.instagram.com/vipincoding/
*********************************************************************

from PyPDF2 import PdfFileWriter, PdfFileReader


def secure_pdf(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)
    with open(f"encrypted_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"encrypted_{file} Your file has been secured")


if __name__ == "__main__":
    file = "your_pdf_file.pdf"
    password = "yourpassword"
    secure_pdf(file, password)
