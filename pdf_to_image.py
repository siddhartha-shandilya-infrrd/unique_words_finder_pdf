from pdf2image import convert_from_path
import os
import pytesseract
from PIL import Image
import io, re
import PyPDF2


#cleaning some folder
os.remove("first_pages_append.txt")
os.remove("last_pages_append.txt")


UNIQUE_KEYWORDS = set()
INTERSECTION_SET = set()

def first_page_unique_words(text) -> set:
    print(f"\n\n first page \n\t{text}\n\n\t +++++")

        # Split the text into words and convert to lowercase
    words = re.findall(r'\b([a-zA-Z]+)\b', text.lower())
    
    # Find unique words in the first page only
    unique_words = set(words)
    return unique_words
    


for file in os.listdir("files"):
    pdfs = f"files/{file}"
    pages = convert_from_path(pdfs, 350)

    i = 1
    text_append = ''
    for page in pages:
        image_name =  str(file)+"_Page_" + str(i) + ".jpg" 
        
        os.makedirs(f"pdf_images/{file}", exist_ok=True)
        page.save(f"pdf_images/{file}/{image_name}", "JPEG")
        text = pytesseract.image_to_string(f"pdf_images/{file}/{image_name}")
        # Print the extracted text
        if i == 1:
            unique_words = first_page_unique_words(text)
            with open("first_pages_append.txt", 'a') as f:
                # Write the unique words to the text file
                f.write(text + '\n\n\n'+'+'*200+'\n\n')
            
        else:
            page_words = re.findall(r'\b\w+\b', text.lower())
            page_unique_words = set(page_words)
            unique_words = unique_words - page_unique_words
            with open("last_pages_append.txt", 'a') as f:
                # Write the unique words to the text file
                f.write(text + '\n\n\n'+'+'*200+'\n\n')
        
        text_append += text
        os.makedirs("pdf_text", exist_ok=True)
        i = i+1

    with open(f"pdf_text/{file}.txt", 'w') as f:
        # Write the unique words to the text file
        f.write(text_append + '\n')
    
    output_file = f'unique_keyword/{file}.txt'
    os.makedirs(f"unique_keyword", exist_ok=True)
    UNIQUE_KEYWORDS.update(unique_words)
    INTERSECTION_SET.intersection(unique_words)
    with open(output_file, 'w') as f:
        # Write the unique words to the text file
        for word in unique_words:
            f.write(word + '\n')


# output_file = f'unique_keyword/{file}/{file}.txt'
# os.makedirs(f"unique_keyword/{file}", exist_ok=True)
with open("total_keyworda.txt", 'w') as f:
    # Write the unique words to the text file
    for word in UNIQUE_KEYWORDS:
        f.write(word + '\n')

with open("total_Common_keywords.txt", 'w') as f:
    # Write the unique words to the text file
    for word in INTERSECTION_SET:
        f.write(word + '\n')

# Open the PDF file

# path_to_tesseract = r'/usr/bin/tesseract' #give the path of tesseract.exe here
# pytesseract.tesseract_cmd = path_to_tesseract

# with open('files/86420-SARSFIELD_PRELIM_TITLE_COMMITMENT.PDF.pdf', 'rb') as f:
#     # Read the PDF file
#     pdf_reader = PyPDF2.PdfReader(f)
    
#     # Get the first page
#     first_page = pdf_reader.pages[0]
    
#     # Convert the PDF page to an image (PNG)
#     image = pages = convert_from_path(pdfs, 350)
    
#     # Extract text from the image using pytesseract
#     text = pytesseract.image_to_string(image)
    
#     # Print the extracted text
#     print(text)
