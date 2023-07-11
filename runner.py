import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# From NLTK, provides common stopwords like 'An, The, Who ..'
stop_words = set(stopwords.words('english'))

# We provide the directory of the job descriptions here
directory_path = "jobs"  

max_similarity = 0.0
most_similar_file = None

all_files = {}

resume_filename = input("Enter the full filename of the resume (example.txt): ")

# Get the resume file path based on the user input and the resumes directory
resume_directory = "resumes"
file1_path = os.path.join(resume_directory, resume_filename)


if not os.path.isfile(file1_path):
    print("Resume file not found.")
    exit()

# This is for calculating the similarity of the job description & resume
def calculate_tfidf_similarity(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        file1_contents = file1.read()
        file2_contents = file2.read()
        

        file1_preprocessed = preprocess_text(file1_contents)
        file2_preprocessed = preprocess_text(file2_contents)
        
        # TF-IDF vectors
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([file1_preprocessed, file2_preprocessed])
        
        # Get the TF-IDF vectors for file1 and file2
        file1_tfidf = tfidf_matrix[0]
        file2_tfidf = tfidf_matrix[1]
        
        # Calculate cosine similarity
        similarity = (file1_tfidf * file2_tfidf.T).toarray()[0, 0]
        
        return similarity

# Filter out non-alphabetic tokens and stopwords
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    preprocessed_text = " ".join(tokens)
    return preprocessed_text

# Loop through the files in the jobs directory
for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
        file2_path = os.path.join(directory_path, filename)
        
        similarity = calculate_tfidf_similarity(file1_path, file2_path)
        filename_without_extension = os.path.splitext(filename)[0]
        # Getting the most similar file
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_file = filename_without_extension
        
        all_files[filename_without_extension] = similarity

print(f"\nThe position most suited to your resume is for a {most_similar_file} with a similarity of {max_similarity}\n")


all_files_sorted = sorted(all_files.items(), key=lambda x: x[1], reverse=True)

data_top = [
    ["Job", "Similarity"],
]
data_bottom = [
    ["Job", "Similarity"],
]

for file_name, similarity in all_files_sorted[:5]:
    data_top.append([file_name, similarity])

for file_name, similarity in all_files_sorted[-5:][::-1]:
    data_bottom.append([file_name, similarity])

column_widths = [max(len(str(item)) for item in column) for column in zip(*data_top)]
column_widths2 = [max(len(str(item)) for item in column) for column in zip(*data_bottom)]


# Print the table
print("\n Top Five: \n")
for row in data_top:
    row_formatted = [str(item).ljust(width) for item, width in zip(row, column_widths)]
    print(' | '.join(row_formatted))

print("\n Bottom Five: \n")
for row in data_bottom:
    row_formatted = [str(item).ljust(width) for item, width in zip(row, column_widths)]
    print(' | '.join(row_formatted))

print("\n")

