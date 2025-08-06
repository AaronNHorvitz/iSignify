# Development Environment Setup Guide

This guide provides detailed, step-by-step instructions for setting up a local development environment for the iSignify project, and how to run and test the application.

---

## 1. Environment Setup

### Prerequisite: Python 3.10+

Ensure you have Python 3.10 or a newer version installed on your system. On many Linux systems, you will need to use the `python3` command instead of `python`.

### Step 1: Clone the Repository
```bash
git clone [https://github.com/AaronNHorvitz/iSignify.git](https://github.com/AaronNHorvitz/iSignify.git)
cd iSignify
```

### Step 2: Create the Virtual Environment

From the root directory of the project `(iSignify/)`, run the following command. This will create a `venv` folder, which is safely ignored by Git.

```bash
python3 -m venv venv
```

### Step 3: Create the Virtual Environment

The command differs based on your operating system.

- On macOS or Linux
```bash
source venv/bin/activate
```
- On Windows (Command Prompt or PowerShell):
```bash
.\venv\Scripts\activate
```

Your terminal prompt should now have a (venv) prefix.

### Step 4: Install Dependencies

With the environment active, run the following command from the project root to install all required packages.

```bash
pip install -r requirements.txt
```

### Step 5: Configure VS Code (Recommended)

To ensure your editor recognizes the packages in your virtual environment:

1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
2. Type and select `Python: Select Interpreter`.
3. Choose the Python interpreter that includes `(venv)` in its path.

### Step 6: Authenticate with Hugging Face (for AI Summaries)

This is a one-time setup for your machine to enable the AI summary feature.

1. Accept Model Terms: Go to the Gemma model page https://huggingface.co/google/gemma-2b and accept the license terms. You will need a free Hugging Face account.

2. Create an Access Token: In your Hugging Face account settings, navigate to the "Access Tokens" section and create a new token with a "read" role. Copy the token.

3. Log In from Terminal: Run huggingface-cli login in your terminal, and paste your access token when prompted.

---

# 2. Running the Application

### Step 1. Run the Backend Server
```bash
# Navigate into the backend folder
cd backend

# Run the server from within the backend directory
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`.

### Step 2: Open the Frontend

- Navigate to the `frontend/` directory and open `index.html` in your web browser.

---

# 3. Running Tests

### A. Locally (Recommended for Development)

1. Navigate to the backend/ directory:

    ```bash
    cd backend
    ```
2. Run pytest:

    ```bash
    pytest
    ```
### B. Using Docker (Ensures a Clean Environment)

1. From the project's root directory, build the Docker image:

    ```bash
    docker build -t isignify-app .
    ```
2. Run the tests inside a temporary container:

    ```bash
    pdocker run --rm isignify-app pytest
    ```
---

# 4. Troubleshooting

### Linux-Specific: Fixing Docker Permission Errors

If you see a permission denied error when running Docker, you have two options:

If you see a permission denied error when running Docker, you have two options:

- **Option 1 (Quick Fix):** Prefix all docker commands with sudo.

- **Option 2 (Permanent Fix):** Add your user to the docker group with sudo usermod -aG docker $USER, then log out and log back in.