import PyPDF2
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Open the PDF file in read-binary mode
with open('files/86420-SARSFIELD_PRELIM_TITLE_COMMITMENT.PDF.pdf', 'rb') as f:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(f)

    # Get the text from the first page
    first_page_text = pdf_reader.pages[0].extract_text()

    # Tokenize the text into words
    words = word_tokenize(first_page_text)

    # Count the frequency of each word
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

    # Select the words that occur only once
    unique_words = [word for word in word_freq if word_freq[word] == 1]

    # Print the unique words
    print(unique_words)
