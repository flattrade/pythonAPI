
# 🚀 Flattrade Python API Setup Guide

This guide will walk you through setting up and using the Flattrade Python API step-by-step.

---

## 📦  Prerequisites

Ensure the following are installed:

- ✅ **Python 3** (Add to system PATH)
- ✅ **any Code editer** (Recommended **`Visual Studio code`**)

---

## ⬇️ Download the Source Code

Get the full source code from GitHub:

### 🔗 GitHub Repository  
**URL:** [https://github.com/flattrade/pythonAPI](https://github.com/flattrade/pythonAPI)

> 💡 You can **clone using Git** or **download it as a ZIP**.

---

### ✅ Option 1: Clone via Git

Open your terminal and run:

```bash
# Clone the repository
git clone https://github.com/flattrade/pythonAPI.git

# Navigate to the project folder using VS Code
code pythonAPI
```

#### 📽️ *GIF Preview:*  

![Clone via Git](https://flattrade.s3.ap-south-1.amazonaws.com/pidoc/Clone_repo.gif)

---

### ✅ Option 2: Download as ZIP

1. Visit [flattrade/pythonAPI](https://github.com/flattrade/pythonAPI)
2. Click the green **“Code”** button
3. Choose **“Download ZIP”**
4. Extract the contents to your desired location
5. Open in **`code editer`**
#### 📽️ *GIF Preview:*  

![Download ZIP](https://flattrade.s3.ap-south-1.amazonaws.com/pidoc/code_download.gif)

---

## 🔐 API Login & Token Generation

### 🔑 Step 1: Login to Flattrade

1. Go to: [https://wall.flattrade.in/login](https://wall.flattrade.in/login)  
2. Click the **Pi Menu**  
3. Create a **New API Key**

---

### 📝 Step 2: Enter API Key Details

When creating your API key, provide the following:

- **App Name** – Your app's full name  
- **App Short Name** – A short identifier  
- **Redirect URL** – Make use of `http://localhost:8080` or your redirect webpage.
- **Description** – A short explanation of your app

#### 📽️ *GIF Preview:*  

![API Key Creation](https://flattrade.s3.ap-south-1.amazonaws.com/pidoc/wall_token_create.gif)

---

### 📋 Step 3: Copy API Credentials

From the dashboard, save:

- ✅ **Port** (e.g., `8080`)
- ✅ **API Key**
- ✅ **Secret Key**

Edit the following file with your credentials:

```python
# token_generator/gettoken.py

# Configuration variables
EndPoint = "/"
GPort = 8080
api_key = "YOUR_API_KEY"
api_secret = "YOUR_SECRET_KEY"
```

#### 📽️ *GIF Preview:*  

![Set Secrets](https://flattrade.s3.ap-south-1.amazonaws.com/pidoc/set_secret.gif)

---

## ⚙️ Environment Setup

### 🐍 Step 4: Create a Virtual Environment

```bash
python -m venv myvenv
```

---

### 🚀 Step 5: Activate the Virtual Environment

**Linux/macOS:**
```bash
source myvenv/bin/activate
```

**Windows CMD:**
```cmd
myvenv\Scripts\activate
```

**Windows PowerShell:**
```powershell
myvenv\Scripts\Activate.ps1
```

#### 📽️ *GIF Preview:*  

![Setup Virtual Env](https://flattrade.s3.ap-south-1.amazonaws.com/pidoc/setup_env.gif)

#### ⚠️ Important Note

>set the environment one time do this one time only this command creates a virtual environment for project dependencies
---

### 📦 Step 6: Install Required Packages

```bash
pip install -r requirements.txt
pip install -r ./token_generator/requirements.txt
```

#### 📽️ *GIF Preview:*  

![Install Libraries](https://flattrade.s3.ap-south-1.amazonaws.com/pidoc/install_lib.gif)

---

## 🔐 Token Generation

### ▶️ Step 7: Run the Token Generator

```bash
python ./token_generator/gettoken.py
```

After running the `gettoken.py`, you’ll get a link like:

```
https://auth.flattrade.in/?app_key=YOUR_APP_KEY
```

#### 📽️ *GIF Preview:*  

![Run Token Script](https://flattrade.s3.ap-south-1.amazonaws.com/pidoc/run_token_code.gif)

---

### 🌐 Step 8: Complete Authentication

Open the link in your browser, log in, and approve access.

#### 📽️ *GIF Preview:*  

![Token Create](https://flattrade.s3.ap-south-1.amazonaws.com/pidoc/token_create.gif)

---

### 🧪 Step 9 (Optional): Test Your Token

Use **Postman** or another API testing tool to:

- Verify your token is valid  
- Try out the Flattrade APIs

#### 📽️ *GIF Preview:*  

![Test in Postman](https://flattrade.s3.ap-south-1.amazonaws.com/pidoc/postman_test.gif)



> now you can quickly check the API call with the sample file test_api.py provided in this folder.
> Before you run test_api.py, please set the `usersession` and `userid` variable in the file test_api.py
---

## ⚠️ Important Note

> 🕒 **Token Expiration Time:**  
> All tokens **expire daily at 5:00 AM (IST)**.  
> You must **generate a new token each day after 5 AM** to continue using the API without interruption.

💡 *Tip: Set a reminder if you're building a daily-use application.*

--- 