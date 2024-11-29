#!/bin/sh
echo "Running Custom-Ring-App code"
#!/bin/sh
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found. Creating one..."
    uv venv .venv
    echo "Virtual environment created successfully."
else
    echo "Virtual environment already exists."
fi
# this will create venv from python version defined in .python-version
uv venv

# install requirements for the project
uv pip install -r requirements.txt

# run app using python from venv
uv run main.py