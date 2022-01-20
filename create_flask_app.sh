#****************************************************
#* Creates a basic framework for a flask website in *
#* current working directory.                       *
#****************************************************

#settings
create_virtualenv=1
create_repo=1

echo "Creating framework for a basic flask website."
#-> initialize empty git repo
if [[ "$create_repo" -eq 1 ]]; then
    git init
    touch .gitignore
    cat <<EOT >> .gitignore
__pycache__/
venv/
EOT
else
    echo "Skipping git init"
fi
#-> create virtual environment
if [[ "$create_virtualenv" -eq 1 ]]; then
    # specify version with: python3 -m virtualenv -p=<your_python_executable> venv
    pip install virtualenv
    python3 -m virtualenv venv
    source venv/bin/activate
    pip install flask
else
    echo "Skipping virtual environment"
fi
#-> create basic folder structure
mkdir tests
mkdir templates
mkdir static
mkdir static/images
mkdir static/scripts
mkdir static/styles
#-> create empty files
touch app.py
touch templates/base.html
touch templates/index.html
touch static/styles/styles.css
touch static/styles/init_script.js
#-> boilerplate code
cat <<EOT >> app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def form_view():
    return render_template('index.html')
EOT

cat <<EOT >> templates/base.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href = "{{ url_for('static', filename='styles/styles.css') }}">
    <!-- Bootstrap 5 import -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <div class = "content container">
        {% block content %}
        {% endblock %}
    </div>
    <!-- local script import -->
    <script src="{{ url_for('static', filename='scripts/init_script.js') }}"></script>
</body>
</html>
EOT