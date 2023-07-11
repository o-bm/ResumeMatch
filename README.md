# ResumeMatch

This project matches job descriptions with a given resume based on TF-IDF similarity. It helps identify the job position that best suits the provided resume.

## What is TF-IDF? and Why?
TF-IDF (Term Frequency-Inverse Document Frequency) is a way to measure the importance of words in a document or a collection of documents. It combines two factors:
Term Frequency (TF): How often a word appears in a document. If a word appears multiple times, it is likely to be more important.
Inverse Document Frequency (IDF): How rare a word is across all documents. If a word is rare, it is likely to be more significant.

TF-IDF helps identify important words that are specific to a document while filtering out common words. It has several benefits:

1. **Highlighting Important Words:** TF-IDF emphasizes words that are important and relevant to a document.
2. **Extracting Features:** It is useful for extracting meaningful features from text for tasks like classification, clustering, and retrieval.
3. **Reducing Dimensionality:** TF-IDF can reduce the complexity of text data while retaining crucial information.
4. **Filtering Noise:** TF-IDF helps filter out common words (stopwords) and focuses on distinctive and meaningful words.

One might think that longer documents have a greater chance to be more similar due to content length, however, TF-IDF does not prioritize longer documents. It looks at the significance of words within a document, considering both local and global measures. The IDF component ensures that important words are not overshadowed by document length. So, whether a document is short or long, TF-IDF allows us to effectively analyze and retrieve relevant information.

## Requirements

- Python 3.7x and above
- NLTK library
- scikit-learn library

## Installation

Clone the repository:

```bash
git clone https://github.com/o-bm/ResumeMatch.git
```

Download the necessary NLTK resources:
```python
import nltk

nltk.download('punkt')
nltk.download('stopwords')
```

Provide job description files in the "jobs" directory. Each job description should be a text file with a ".txt" extension.
Put the resumes in the "resumes" directory. Each resume should also be a text file with a ".txt" extension.

Run the program:

```bash
python runner.py
```
Enter the full file name with the .txt extention

The program will calculate the similarity between the resume and each job description using TF-IDF. It will then display the most suited job position and a table of the top and bottom five matches.

Example Output


The position most suited to your resume is for a Software Engineer with a similarity of 0.85

Top Five Matches:

Job              | Similarity
------------------|------------
Software Engineer| 0.85
Data Analyst     | 0.80
UX Designer      | 0.76
Project Manager  | 0.73
Sales Executive  | 0.68

Bottom Five Matches:

Job              | Similarity
------------------|------------
Marketing Intern | 0.25
Administrative Assistant | 0.28
Customer Support | 0.32
Graphic Designer | 0.35
Accountant       | 0.40

