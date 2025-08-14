from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1>Welcome to NITTE!</h1><p>This is simple Flask app.</p>"



















































































from flask import Flask, request, render_template_string

app = Flask(__name__)

# Function to generate Fibonacci series
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series

# HTML template as a string
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Fibonacci Series</title>
</head>
<body>
    <h1>Fibonacci Series Generator</h1>
    <form method="get" action="/fibonacci">
        <label for="n">Enter number of terms:</label>
        <input type="number" id="n" name="n" value="{{ n or '' }}" required>
        <button type="submit">Generate</button>
    </form>

    {% if result is not none %}
        <h2>Fibonacci Series ({{ n }} terms):</h2>
        <p>{{ result }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    n = request.args.get('n', default=None, type=int)
    result = None

    if n is not None:
        if n < 0:
            result = "Please enter a non-negative integer."
        else:
            result = fibonacci_series(n)

    return render_template_string(HTML_TEMPLATE, result=result, n=n)

if __name__ == '__main__':
    app.run(debug=True)
