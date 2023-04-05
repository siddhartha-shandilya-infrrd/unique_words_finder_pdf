import PyPDF2
import re, os

for file in os.listdir("files"):

    # Open the PDF file
    with open(f"files/{file}", 'rb') as f:
        # Read the PDF file
        pdf_reader = PyPDF2.PdfReader(f)
        # Get the first page
        first_page = pdf_reader.pages[0]
        
        # Get the text content of the first page
        text = first_page.extract_text()

        print(f"\n\n first page \n\t{text}\n\n\t +++++")

        # Split the text into words and convert to lowercase
        words = re.findall(r'\b([a-zA-Z]+)\b', text.lower())
        
        # Find unique words in the first page only
        unique_words = set(words)
        for i in range(1, len(pdf_reader.pages)):
            page = pdf_reader.pages[i]
            page_text = page.extract_text()
            page_words = re.findall(r'\b\w+\b', page_text.lower())
            page_unique_words = set(page_words)
            unique_words = unique_words - page_unique_words

        # Create a text file with the same name as the input PDF file
        output_file = f'{file}.txt'
        with open(output_file, 'w') as f:
            # Write the unique words to the text file
            for word in unique_words:
                f.write(word + '\n')

        print(f'Successfully saved unique words to {output_file}')
