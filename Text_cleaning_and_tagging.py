import os
import spacy
from nltk.corpus import stopwords
import nltk

# Load the spaCy model for Russian
nlp = spacy.load('ru_core_news_sm')

# Set the maximum length of a document in spaCy to handle large texts
nlp.max_length = 2000000

# Function to split text into chunks of specified length
def split_text(text, max_length=1000000):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

# Function to preprocess text: remove stopwords and lemmatize tokens
def preprocess_text(text, stopwords_list, make_tags=False):
    parts = split_text(text)  # Split text into parts
    result_list = []
    
    for part in parts:
        doc = nlp(part)  # Process each part with spaCy
        for token in doc:
            if len(token) > 1 and token.is_alpha:  # Filter out non-alphabetic tokens and single characters
                lemma = token.lemma_  # Get the lemma of the token
                if lemma not in stopwords_list:  # Remove stopwords
                    if make_tags:
                        pos = token.pos_  # Get part-of-speech tag
                        result_list.append(f"{lemma}_{pos}" if pos else lemma)  # Append lemma with POS tag if needed
                    else:
                        result_list.append(lemma)  # Append only the lemma
    return " ".join(result_list)  # Join the lemmatized tokens back into a string

# Function to save processed text to a file
def save_file(file_path, text):
    # Check if the directory exists, if not create it
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Function to process all texts in a folder, saving them with and without tags
def process_texts_in_folder(input_folder, output_folder_with_tags, output_folder_no_tags, stopwords_list):
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()  # Read the text from the file

            # Process text without tags and save it with only the filename (no path)
            processed_text_no_tags = preprocess_text(text, stopwords_list, make_tags=False)
            output_file_path_no_tags = os.path.join(output_folder_no_tags, filename)  # Use only the filename
            save_file(output_file_path_no_tags, processed_text_no_tags)

            # Process text with tags and save it with only the filename (no path)
            processed_text_with_tags = preprocess_text(text, stopwords_list, make_tags=True)
            output_file_path_with_tags = os.path.join(output_folder_with_tags, filename)  # Use only the filename
            save_file(output_file_path_with_tags, processed_text_with_tags)

# Define input and output folder paths
input_folder = 'archive'
output_folder_with_tags = 'output_with_tags'
output_folder_no_tags = 'output_no_tags'

# Download the Russian stopwords list from NLTK
nltk.download('stopwords', quiet=True)
stopwords_list = set(stopwords.words('russian'))  # Set of stopwords in Russian

# Process the texts in the input folder and save the results with only filenames
process_texts_in_folder(input_folder, output_folder_with_tags, output_folder_no_tags, stopwords_list)
