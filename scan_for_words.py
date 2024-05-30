import os
import csv
import re
import PyPDF2

# Define the folder path where your PDF files are located
pdf_folder = '/path/to/your/pdf/folder'

# Define the specific words you want to search for
target_words = ['word1', 'word2', 'word3']

# Initialize an empty list to store results
results = []

# Iterate through each PDF file in the folder
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, filename)
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            body_text = ''
            for page in pdf_reader.pages:
                text = page.extract_text()
                body_text += text.lower()  # Convert to lowercase for case-insensitive search

            # Count occurrences of target words
            word_counts = {word: len(re.findall(r'\b{}\b'.format(word), body_text, re.IGNORECASE)) for word in target_words}

            # Determine 'yes' or 'no' based on word count
            word_count_threshold = 2
            word_presence = 'yes' if any(count > word_count_threshold for count in word_counts.values()) else 'no'

            # Append results for this file
            results.append((filename, word_counts, word_presence))

# Write results to a CSV file
output_csv = '/path/to/output/results.csv'
with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File Name', 'Word Counts', 'Word Presence'])
    writer.writerows(results)

print(f"Results saved to {output_csv}")


#Replace `/path/to/your/pdf/folder` with the actual path to your folder containing the PDF files. Adjust the #`target_words` list as needed. The script will create a CSV file named `results.csv` with the specified columns. 