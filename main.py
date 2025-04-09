from flask import Flask, render_template_string

app = Flask(__name__)


form_template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>URL Redirector</title>
</head>
<body>
    <h1>Открытие сайта через несколько секунд</h1>
    {% if redirect_url %}
        <p>Перенаправление на <a href="{{ redirect_url }}">{{ redirect_url }}</a>...</p>
        <meta http-equiv="refresh" content="3;url={{ redirect_url }}">
    {% else %}
        <p>No URL found.</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    try:
        with open('link.txt', 'r') as file:
            url = file.readline().strip() 
            if url:
                print('URL:', url)
                redirect_url = f"https://{url}" 
            else:
                print('No URL found')
                redirect_url = "https://google.com"

    except Exception as e:
        print("Error reading the file:", e)
        redirect_url = None 

    return render_template_string(form_template, redirect_url=redirect_url)

if __name__ == '__main__':
    app.run(debug=True)