# ResumeMatch

This project matches job descriptions with a given resume based on TF-IDF similarity. It helps identify the job position that best suits the provided resume.

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

