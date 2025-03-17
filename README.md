# Text_cleaning_and_tagging
## Description
This Python script performs text preprocessing on Russian-language texts by removing stopwords, lemmatizing tokens, and optionally tagging each word with its part of speech (POS). The script processes the text and provides two outputs: one with the part-of-speech tags and one without. It utilizes the spaCy library for natural language processing and NLTK for stopword removal.

## Functional Description
The program performs the following steps:
1. Loads the Russian language model from spaCy (`ru_core_news_sm`).
2. Tokenizes the input text and removes stopwords.
3. Lemmatizes the remaining tokens.
4. Optionally tags tokens with their part of speech.
5. Splits long texts into smaller chunks for processing.
6. Saves the processed text into output files, both with and without POS tags.

## How It Works
1. The script loads a Russian-language spaCy model (`ru_core_news_sm`) to perform tokenization and lemmatization.
2. It processes the input text, removing stopwords and applying lemmatization to the tokens.
3. The script can generate outputs with part-of-speech tags attached to each word or without tags, depending on the user's preference.
4. The processed text is saved into two separate files: one with tags and one without.

## Input Structure
To run the program, the following parameters need to be provided:
1. **Input Folder**: The folder containing the text files to be processed.
2. **Stopword List**: A set of Russian stopwords (downloaded from NLTK).
3. **Output Folders**:
   - One for texts with part-of-speech tags (`output_with_tags`).
   - One for texts without part-of-speech tags (`output_no_tags`).

## Technical Requirements
To run the program, the following are required:
1. Python 3.x
2. Installed libraries: spaCy, NLTK
3. spaCy Russian language model: `ru_core_news_sm`
4. NLTK stopwords for Russian.

## Usage
1. Set the paths for your input and output folders.
2. Run the script to process the text files in the input folder:
    - The script will create two versions of the output: one with POS tags and one without.
    - Each file will be saved in the corresponding output folder.

## Example Output
### Input text (example):
"Сегодня хорошая погода для прогулок."

### Output with tags:
"сегодня_ADV хороший_ADJ погода_NOUN для_PREP прогулка_NOUN"

### Output without tags:
"сегодня хороший погода для прогулок"

## Conclusion
This script helps in preprocessing Russian text by cleaning, lemmatizing, and optionally tagging words with their parts of speech. It allows users to generate both tagged and untagged versions of the text, useful for various natural language processing tasks.
