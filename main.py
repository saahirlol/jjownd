from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__, static_folder='src')

html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>Moodboard</title>
    <style>
        body {
            background-color: black;
        }
        div {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Adjust the height as needed */
        }
    </style>
</head>
<body>

    <div id="image-container">
        {% for image in images %}
        <center>
        <img src="{{ url_for('send_image', filename=image) }}" alt="Image" width="300">
        {% endfor %}
        </center>
    </div>

</body>
</html>
'''

@app.route('/')
def index():
    image_files = [f for f in os.listdir('src') if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template_string(html_content, images=image_files)

@app.route('/src/<filename>')
def send_image(filename):
    return send_from_directory('src', filename)

if __name__ == '__main__':
    app.run(debug=True)
