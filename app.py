"""
app.py  —  Flask backend for Tech YouTube RAG
=============================================
Exposes the endpoints that tech_yt_rag.html expects:

  GET  /api/health   → { "status": "ok", "records": <int> }
  POST /api/summary  → { "summary": "<text>" }
                       body: { "product": str, "topic": str, "format": "bullet"|"paragraph" }
  POST /api/overall  → { "summary": "<text>" }
                       body: { "product": str, "format": "bullet"|"paragraph" }

Run with:
    python app.py

The server starts on http://localhost:5000
Make sure config.py, config_rag.py and rag_core.py are in the same directory before running.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS

# All RAG logic and models live in rag_core.py
from rag_core import (
    final_collection,
    query_product_topic_summary,
    query_product_overall_summary,    # ← ADD THIS LINE
)

# ── Flask app ─────────────────────────────────────────────────────────────────
app = Flask(__name__)
CORS(app)   # Allow the HTML file to call the API from any origin

@app.route("/api/overall", methods=["POST"])
def overall():
    """
    Overall user experience endpoint.

    Request body (JSON):
        { "product": str, "format": "bullet" | "paragraph" }

    Response (JSON):
        { "summary": str }
    """
    data = request.get_json(force=True, silent=True) or {}

    product     = (data.get("product") or "").strip()
    format_type = (data.get("format")  or "bullet").strip()

    if not product:
        return jsonify({"error": "'product' is required."}), 400

    try:
        result = query_product_overall_summary(product, format_type)
        return jsonify({"summary": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/health", methods=["GET"])
def health():
    """Health check — returns record count from the final collection."""
    try:
        count = final_collection.count_documents({})
        return jsonify({"status": "ok", "records": count})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500
    

@app.route("/api/products", methods=["GET"])
def products():
    """
    Returns the list of unique product names stored in MongoDB.
    Used by the frontend for autocomplete suggestions.
    """
    try:
        names = final_collection.distinct("product_name")
        names = sorted([n for n in names if n])   # remove blanks, sort A-Z
        return jsonify({"products": names})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/summary", methods=["POST"])
def summary():
    """
    RAG summary endpoint.

    Request body (JSON):
        { "product": str, "topic": str, "format": "bullet" | "paragraph" }

    Response (JSON):
        { "summary": str }
    """
    data = request.get_json(force=True, silent=True) or {}

    product     = (data.get("product") or "").strip()
    topic       = (data.get("topic")   or "").strip()
    format_type = (data.get("format")  or "bullet").strip()

    if not product or not topic:
        return jsonify({"error": "Both 'product' and 'topic' are required."}), 400

    if format_type not in ("bullet", "paragraph"):
        format_type = "bullet"

    try:
        result = query_product_topic_summary(product, topic, format_type)
        return jsonify({"summary": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

"""    
@app.route("/api/topics", methods=["GET"])
def topics():

    #Returns unique topic labels from MongoDB, optionally filtered by product.
    #Used by the frontend for topic autocomplete suggestions.
    #Query param: ?product=Samsung (optional)

    try:
        product = request.args.get("product", "").strip()
        query = {}
        if product:
            query["product_name"] = {"$regex": product, "$options": "i"}

        raw_topics = final_collection.distinct("topic_label", query)
        # Filter out blanks and "Uncategorized"
        cleaned = sorted([
            t for t in raw_topics
            if t and t.strip() and t.strip().lower() != "uncategorized"
        ])
        return jsonify({"topics": cleaned})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
"""

# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  Tech YouTube RAG — Flask Backend")
    print("  Open tech_yt_rag.html in your browser")
    print("  API running at http://localhost:5000")
    print("=" * 60 + "\n")
    app.run(host="0.0.0.0", port=5000, debug=False)
