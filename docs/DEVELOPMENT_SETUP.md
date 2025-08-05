# Development Environment Setup Guide

This guide provides detailed, step-by-step instructions for setting up a local development environment for the iSignify project.

### Step 1: Create the Virtual Environment

From the root directory of the project (`iSignify/`), run the following command. This will create a `venv` folder in your project, which is safely ignored by Git.

```bash
python -m venv venv
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


