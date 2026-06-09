import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Step 0: Download required NLTK data ---
nltk.download('punkt')
nltk.download('punkt_tab')  # Needed for newer NLTK versions

# --- Step 1: Sample FAQ Data ---
faqs = [
    {"question": "What is Python?", "answer": "Python is a high-level, versatile programming language."},
    {"question": "How do I install Python?", "answer": "You can download and install Python from the official website python.org."},
    {"question": "What are Python's key features?", "answer": "Python offers simplicity, readability, extensive libraries, and supports multiple programming paradigms."},
    {"question": "How can I run a Python script?", "answer": "Use the command 'python filename.py' in your terminal or command prompt."}
]

# --- Step 2: Preprocessing Utilities ---
def clean_text(text):
    """Tokenize, lowercase, and remove punctuation."""
    tokens = nltk.word_tokenize(text)
    tokens = [t.lower() for t in tokens if t.isalpha()]  # Keep only alphabetic tokens
    return " ".join(tokens)

# Clean FAQ questions
faq_questions = [clean_text(faq["question"]) for faq in faqs]

# --- Step 3: FAQ Matching via Cosine Similarity ---
vectorizer = TfidfVectorizer()
faq_matrix = vectorizer.fit_transform(faq_questions)

def find_best_match(user_query):
    user_query_clean = clean_text(user_query)
    user_vector = vectorizer.transform([user_query_clean])
    similarities = cosine_similarity(user_vector, faq_matrix).flatten()
    idx = similarities.argmax()
    return faqs[idx]["answer"], similarities[idx]

# --- Step 4: Simple Chat UI ---
print("Welcome to the Python FAQ Chatbot! Type your question (type 'exit' to quit).")
while True:
    user_input = input("You: ")
    if user_input.strip().lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    answer, score = find_best_match(user_input)
    print(f"Chatbot: {answer} (Similarity: {score:.2f})")
