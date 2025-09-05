from flask import Flask, render_template, request, jsonify
import pandas as pd
from model.recommender import get_recommendations

app = Flask(__name__)

# Load dataset (make sure the CSV has been processed with normalized columns)
courses_df = pd.read_csv("data/courses.csv")
# (Optional) Normalize column names if needed:
courses_df.columns = [col.strip().lower() for col in courses_df.columns]

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    if request.method == "POST":
        user_input = request.form["query"]
        recommendations = get_recommendations(user_input, courses_df)
    return render_template("index.html", recommendations=recommendations)

# Suggestion endpoint for autocomplete
@app.route("/suggest", methods=["GET"])
def suggest():
    query = request.args.get("q", "").strip().lower()
    suggestions = []
    if query:
        # Here we use a simple substring match on the course title.
        # You can refine this NLP technique if needed.
        matched = courses_df[courses_df['course_title'].str.lower().str.contains(query, na=False)]
        suggestions = matched['course_title'].drop_duplicates().head(5).tolist()
    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(debug=True)
