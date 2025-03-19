# Text_cleaning_and_tagging

## Description

This script processes a set of text files stored in a folder by splitting large texts into smaller chunks, removing stopwords, and lemmatizing the text using the `spaCy` library for Russian language processing. It generates two versions of each processed text:
1. A version with lemmatized tokens and part-of-speech (POS) tags.
2. A version with only lemmatized tokens (without POS tags).

The script works on all `.txt` files in a specified input folder and saves the processed texts into two output folders.

## Functional Description

### Steps Involved:
1. **Text Splitting**: If a text file is too large, it is split into smaller chunks to ensure it fits within spaCy's processing limits.
2. **Text Preprocessing**: The text is cleaned by removing stopwords and lemmatizing each token. Optionally, the script can include POS tags with the lemmatized tokens.
3. **File Saving**: After processing, the script saves the lemmatized text into output folders with and without POS tags.
4. **Processing Multiple Files**: The script processes all `.txt` files in a specified input folder.

### Key Functions

1. **`split_text(text, max_length=1000000)`**:
   - Splits large texts into smaller chunks to fit within spaCy's processing limits.

2. **`preprocess_text(text, stopwords_list, make_tags=False)`**:
   - Processes the input text by:
     - Tokenizing and lemmatizing each word.
     - Removing stopwords (based on the `stopwords_list`).
     - Optionally including POS tags for each lemmatized token.

3. **`save_file(file_path, text)`**:
   - Saves the processed text into a specified file path, ensuring the necessary directories exist.

4. **`process_texts_in_folder(input_folder, output_folder_with_tags, output_folder_no_tags, stopwords_list)`**:
   - Loops through all `.txt` files in the input folder.
   - Processes each file and saves two versions: one with tags and one without tags.

### Input Structure

1. **Input Folder**: Contains `.txt` files to be processed.
2. **Output Folders**:
   - `output_with_tags`: Stores processed texts with lemmatized tokens and POS tags.
   - `output_no_tags`: Stores processed texts with only lemmatized tokens (no tags).

### Example Workflow

1. The script starts by reading all `.txt` files from the input folder.
2. Each file is processed:
   - **Text Splitting**: If needed, large texts are split into smaller parts.
   - **Text Preprocessing**: The text is tokenized, lemmatized, and stopwords are removed.
   - **With Tags**: The text is saved with lemmatized tokens and their POS tags.
   - **Without Tags**: The text is saved with just the lemmatized tokens.
3. The processed texts are saved in two separate output folders.

### Example Output

1. **Text File in `output_with_tags`**: 
