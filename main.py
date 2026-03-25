from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Dashboard Interface
HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background: #000; color: #0f0; font-family: monospace; padding: 20px; }
        .card { border: 1px solid #0f0; padding: 15px; border-radius: 8px; }
        input { width: 94%; padding: 10px; margin: 10px 0; background: #111; border: 1px solid #333; color: #fff; }
        button { width: 100%; padding: 15px; background: #0f0; color: #000; border: none; font-weight: bold; cursor: pointer; }
        pre { background: #111; padding: 10px; font-size: 12px; color: #aaa; overflow-x: auto; white-space: pre-wrap; }
    </style>
</head>
<body>
    <div class="card">
        <h2>🛰️ RAILWAY MASTER</h2>
        <form method="POST">
            <label>Session ID:</label><br>
            <input type="text" name="sid" placeholder="dlkjanyoskd1..." required><br>
            <label>Market ID:</label><br>
            <input type="text" name="mid" placeholder="35405977" required><br>
            <label>Selection ID (Team):</label><br>
            <input type="text" name="selid" placeholder="123456" required><br>
            <label>API URL:</label><br>
            <input type="text" name="api" value="https://darkexch9.com/api/v1/listMarketBook"><br>
            <button type="submit">RUN INJECTION</button>
        </form>
        <hr>
        <h4>Response Log:</h4>
        <pre>{{ log }}</pre>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    log = "Ready... Waiting for Command"
    if request.method == "POST":
        sid = request.form.get("sid")
        mid = request.form.get("mid")
        api = request.form.get("api")
        
        headers = {
            "Cookie": f"ASP.NET_SessionId={sid}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
        payload = {"marketIds": [mid], "isAllData": True}
        
        try:
            r = requests.post(api, json=payload, headers=headers, timeout=10)
            log = f"Status: {r.status_code}\\nData: {r.text[:300]}"
        except Exception as e:
            log = f"Error: {str(e)}"
            
    return render_template_string(HTML, log=log)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
