# Development Environment Setup Guide

This guide provides detailed, step-by-step instructions for setting up a local development environment for the iSignify project.

### Prerequisite: Python 3.10+

Ensure you have Python 3.10 or a newer version installed on your system. On many Linux systems, you will need to use the `python3` command instead of `python`.


### Step 1: Create the Virtual Environment

From the root directory of the project (`iSignify/`), run the following command. This will create a `venv` folder in your project, which is safely ignored by Git.

```bash
python3 -m venv venv
```

### Step 2: Activate the Environment

You must "activate" the environment to use it. The command differs based on your operating system.

- On macOS or Linux:

```bash
source venv/bin/activate
```

- On Windows (Command Prompt or PowerShell):

```bash
.\venv\Scripts\activate
```
Your terminal prompt should now have a (venv) prefix, indicating the environment is active.

### Step 3: Install Dependencies

With the environment active, run the following command from the project root to install all required packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Step 4: Configure Your Code Editor (VS Code)

To ensure your editor recognizes the packages in your virtual environment:

- 1. Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P).

- 2. Type and select Python: Select Interpreter.

- 3. Choose the Python interpreter that includes (venv) in its path.

### Step 5: Deactivating the Environment

```bash
deactivate
```

### Step 6: Authenticate with Hugging Face (for AI Summaries)

To enable the AI summary feature, you need to authenticate with the Hugging Face Hub to download the Gemma model. This is a one-time setup for your machine.

1. Accept the Model Terms:
    - Make sure you have a free account on [Hugging Face](https://huggingface.co/)
    - Go to the Gemma model page: [https://huggingface.co/google/gemma-2b](https://huggingface.co/google/gemma-2b)
    - Click to read and accept the license terms.

2. Create an Access Token:
    - In your Hugging Face account settings, navigate to the **"Access Tokens"** section.
    - Create a **"New token"** with a **"read"** role.
    - Copy the generated token to your clipboard.

3. Create an Access Token:
    - Make sure your `(venv)` is active.
    - Run the login commadn in your terminal:
    ```bash
    huggingface-cli login
    ```
    - Paste your access token when prompted and press Enter.

Once you are logged in, the application will be able to download the Gemma model and generate AI summaries.    

---

### Linux-Specific: Fixing Docker Permission Errors

When running Docker on Linux for the first time, you may encounter a `permission denied` error when trying to connect to the Docker daemon socket. This means your user account doesn't have the rights to run Docker commands.

You have two options to fix this:

**Option 1: The Quick Fix (Prefix with `sudo`)**

You can run all docker commands with `sudo`. This is a quick workaround.

```bash
sudo docker build -t isignify-app .
sudo docker run -p 8000:8000 isignify-app
```

**Option 2: The Permanent Fix (Recommended)**

Add your user to the `docker` group to grant the necessary permissions. You only need to do this once.

1. Run the command to add your user to the group:

```bash
sudo usermod -aG docker $USER
```

2. **Log out of your system and log back in** for this change to take full effect.

After logging back in, you will be able to run all docker commands without sudo.
After you've updated the documentation, which fix would you like to use to solve the permission error on your machine? The quick `sudo` fix, or the permanent `usermod` fix?