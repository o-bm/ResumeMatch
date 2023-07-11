import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

stop_words = set(stopwords.words('english'))

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

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    preprocessed_text = " ".join(tokens)
    return preprocessed_text

# barista resume
file1_path = "C:/Users/iiobm/OneDrive/Desktop/sample_jobs/barista.txt"

# pilot resume
#file1_path = "C:/Users/iiobm/OneDrive/Desktop/sample_jobs/pilot.txt.txt"  
directory_path = "C:/Users/iiobm/OneDrive/Desktop/Work/matching/resumes-sample/resume"  

max_similarity = 0.0
most_similar_file = None

all_files = {}

# Loop through the files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
        file2_path = os.path.join(directory_path, filename)
        
        similarity = calculate_tfidf_similarity(file1_path, file2_path)
        
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_file = filename
        
        all_files[filename] = similarity

print("\n###################################################################\n")
print(f"The file with the highest TF-IDF similarity to file 1 is: {most_similar_file} with a similarity of {max_similarity}")


all_files_sorted = sorted(all_files.items(), key=lambda x: x[1], reverse=True)


print("\n###################################################################\n")
print("TOP FIVE")


for file_name, similarity in all_files_sorted[:5]:
    print(f"File: {file_name}, Similarity: {similarity}")

print("\n\n###################################################################\n\n")
print("BOTTOM FIVE")


for file_name, similarity in all_files_sorted[-5:][::-1]:
    print(f"File: {file_name}, Similarity: {similarity}")

    