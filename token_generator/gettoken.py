from flask import Flask, request, jsonify,render_template_string
import hashlib
import requests

# Configuration variables
#============================
# Endpoint for the API
EndPoint = "/"
# Port number for the Flask application
GPort = 8080
# API key for authentication
api_key = "4cfe6XXXXXXXXXXXXXXXXX0c3c"  #  YOUR_API_KEY
# API secret for generating hash
api_secret = "2025.f09ffXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX43777f2e3" #YOUR_SECRET_KEY
#==============================
# Display login URL
print(f"{'*-'*50}\n Click the link below to authenticate:\n{'*-'*50}\n\nhttps://auth.flattrade.in/?app_key={api_key}\n\n{'*-'*50}")

app = Flask(__name__)

# Generate API hash
def generate_hash(api_key, request_token, api_secret):
    return hashlib.sha256(f"{api_key}{request_token}{api_secret}".encode()).hexdigest()

# API request function
def get_api_token(payload):
    try:
        response = requests.post("https://authapi.flattrade.in/trade/apitoken", json=payload)
        return response.json() if response.status_code == 200 else {"error": f"HTTP {response.status_code}", "details": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": "RequestException", "details": str(e)}

# HTML template with escaped `{}` for CSS
html_template = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Flattrade Client Token</title>
  <script src="https://cdn.tailwindcss.com"></script></head>
<body class="bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center min-h-screen p-4 font-sans">
  <div class="bg-white rounded-xl shadow-lg p-6 w-full max-w-md space-y-4">
    <div class="flex items-center gap-3">
      <div class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-bold w-10 h-10 rounded-lg flex items-center justify-center">FT</div>
      <div><h1 class="text-xl font-bold text-gray-800">Client Data</h1><div class="text-xs text-blue-600">Authentication Details</div></div>
    </div><div class="space-y-3"><div class="flex justify-between items-center bg-gray-50 p-3 rounded-lg">
        <span class="text-sm font-medium">Client ID</span><div class="flex items-center gap-2">
          <span id="client-id" class="text-sm font-mono">{{ api_key }}</span><button data-copy="client-id" class="text-blue-500 hover:text-blue-700">📋</button>
        </div></div><div class="flex justify-between items-center bg-gray-50 p-3 rounded-lg"><span class="text-sm font-medium">Status</span>
        <span class="px-2 py-1 bg-green-100 text-green-800 text-xs font-bold rounded-full">{{ status }}</span>
      </div><div class="bg-gray-50 p-3 rounded-lg"><div class="flex justify-between items-center mb-2"><span class="text-sm font-medium">Token</span>
          <button data-copy="token" class="text-blue-500 hover:text-blue-700">📋</button>
        </div><div id="token" class="font-mono text-xs bg-white p-2 rounded border border-gray-200 break-all">{{ token }}</div>
      </div></div><div class="text-sm text-center text-gray-500 italic">{{ message }}</div></div><script>
    document.querySelectorAll("[data-copy]").forEach(btn => {btn.onclick = () => {navigator.clipboard.writeText(document.getElementById(btn.dataset.copy).textContent);
        btn.textContent = "✅";setTimeout(() => btn.textContent = "📋", 1500);};});</script></body></html>"""

# API Endpoint
@app.route(EndPoint, methods=['GET'])
def generate_secret():
    print("***********************************************************************1")
    request_token = request.args.get('code')
    if not request_token:
        return jsonify({"error": "Missing code in query parameters"}), 400

    hashed_secret = generate_hash(api_key, request_token, api_secret)
    output = {"api_key": api_key, "request_code": request_token, "api_secret": hashed_secret}
    print("output",output)
    response_data = get_api_token(output)

    # If you want to return HTML response
    if response_data.get("error") is None:
        print("response_data",response_data)
        response_html = render_template_string(
            html_template,api_key=response_data.get("client", "N/A"),status=response_data.get("stat", "Unknown"),message=response_data.get("emsg", ""),
            token=response_data.get("token", "No Token")
        )
        return response_html

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=False, port=GPort)
