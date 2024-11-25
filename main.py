from openai import OpenAI
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import time

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


@app.route('/generate-image', methods=['POST'])
def generate_image():
    try:
        data = request.json

        if not data or 'prompt' not in data:
            return jsonify({
                'error': 'No prompt provided',
                'status': 'failed'
            }), 400

        prompt = data['prompt']

        # Send prompt to OpenAI API
        res = generate_image_helper(prompt)
        return res

    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'failed'
        }), 500


def generate_image_helper(prompt):
    try:
        res = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = res.data[0].url

        return jsonify({
            'image_url': image_url,
            'status': 'success'
        })

    except Exception as openai_error:
        return jsonify({
            'error': str(openai_error),
            'status': 'failed'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, port=5004)
