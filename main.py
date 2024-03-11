# Read a PDF file , Extract the text, Write a Text to a Go Program Watcher folder in append mode.

import os
import PyPDF2


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    print("Text extraction from PDF completed!")
    return text


def write_to_file(output_path, text):
    with open(output_path, "a", encoding="utf-8") as output_file:
        output_file.write(text)
    print("Extracted Text sent to text file in watcher folder!")

def main():
    # Replace these paths with your specific folder and file paths
    pdf_folder = "/Users/AVisw5/GolandProjects/go_folderWatch/watchFolder/"
    output_folder = "/Users/AVisw5/GolandProjects/go_folderWatch/watchFolder/"

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each PDF file in the folder
    for pdf_filename in os.listdir(pdf_folder):
        if pdf_filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, pdf_filename)
            output_path = os.path.join(output_folder, "output.txt")

            text = extract_text_from_pdf(pdf_path)
            write_to_file(output_path, text)


if __name__ == "__main__":
    main()