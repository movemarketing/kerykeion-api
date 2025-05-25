from flask import Flask, request, jsonify
from kerykeion.charts import KerykeionChart as Chart

app = Flask(__name__)

@app.route('/horoscope', methods=['POST'])
def generate_chart():
    data = request.json

    try:
        chart = Chart(
            name=data['name'],
            year=data['year'],
            month=data['month'],
            day=data['day'],
            hour=data['hour'],
            minute=data['minute'],
            city=data['city'],
            country=data['country']
        )

        image_path = f"/tmp/{data['name']}_chart.png"
        chart.plot(save_as=image_path)

        with open(image_path, "rb") as img_file:
            encoded = img_file.read()

        return encoded, 200, {'Content-Type': 'image/png'}

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/')
def home():
    return 'Kerykeion API kører! 🚀'
