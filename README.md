# unique_words_finder_pdf
This code will allow user to get a list of unique words that are only present in first pages of a pdf file

# CURRENTLY PDF-TO-IMAGE.PY FILE IS WORKING.
It uses PdfReader to convert the pdf file to images and pytesseract to convert that image to raw text
## always delete the .gitkeep files before running the script

Upon fetching the text, it take the unique words present in the first page and look whether the same keyword is present in other pages

For generating keywords for multiple file we can create a "files" directory then run the files
