# app.py
from flask import Flask, render_template, request, jsonify
import os, json, requests
from dotenv import load_dotenv

# Load .env
load_dotenv()
JD_CLIENT = os.getenv("JDOODLE_CLIENTID")
JD_SECRET = os.getenv("JDOODLE_CLIENTSECRET")
JD_URL = "https://api.jdoodle.com/v1/execute"

DB_FILE = "programs.json"
app = Flask(__name__, template_folder="templates", static_folder="static")


def load_programs():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def run_with_jdoodle(source, language="python3", version_index="3", stdin_text=""):
    """
    Execute code using JDoodle API. Returns dict with result or error message.
    """
    if not JD_CLIENT or not JD_SECRET:
        return {"ok": False, "error": "JDoodle credentials not set. Put them in .env (JDOODLE_CLIENTID/JDOODLE_CLIENTSECRET)."}

    payload = {
        "clientId": JD_CLIENT,
        "clientSecret": JD_SECRET,
        "script": source,
        "language": language,
        "versionIndex": version_index
    }
    if stdin_text:
        payload["stdin"] = stdin_text

    try:
        resp = requests.post(JD_URL, json=payload, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        # JDoodle returns 'output' or inside run; adapt depending on JDoodle response format
        output = data.get("output") or data.get("result") or data.get("data", {}).get("output") or data
        return {"ok": True, "result": output, "meta": data}
    except requests.exceptions.RequestException as e:
        return {"ok": False, "error": f"Request error: {e}"}
    except Exception as e:
        return {"ok": False, "error": f"Execution error: {e}"}


@app.route("/", methods=["GET"])
def index():
    programs = load_programs()
    return render_template("index.html", programs=programs)


@app.route("/all", methods=["GET"])
def all_programs():
    db = load_programs()
    # show all programs
    return render_template("all_programs.html", db=db)


@app.route("/run", methods=["POST"])
def run():
    """
    POST JSON:
    {
      "code": "...",
      "language": "python3",
      "versionIndex": "3",
      "stdin": "input lines separated by \\n"
    }
    """
    data = request.get_json(force=True)
    code = data.get("code", "")
    language = data.get("language", "python3")
    version_index = str(data.get("versionIndex", "3"))
    stdin_text = data.get("stdin", "")

    if not code:
        return jsonify({"ok": False, "error": "No code provided."}), 400

    res = run_with_jdoodle(code, language=language, version_index=version_index, stdin_text=stdin_text)
    return jsonify(res)


if __name__ == "__main__":
    # Debug mode for development only
    app.run(debug=True, port=5000)
