from flask import Flask, request, jsonify
import onnxruntime
import json
import numpy as np
import time

app = Flask(__name__)

class AddressVerifier:
    def __init__(self, model_path, word_index_path):
        self.session = onnxruntime.InferenceSession(model_path)
        self.word_index = self.load_word_index(word_index_path)

    def load_word_index(self, word_index_path):
        with open(word_index_path, 'r') as f:
            word_index = json.load(f)
        return word_index

    def preprocess_text(self, text):
        tokenized_text = text.split()
        indexed_text = [self.word_index.get(token, 0) for token in tokenized_text]
        padded_sequence = self.pad_sequence(indexed_text, max_length)
        return padded_sequence

    def pad_sequence(self, sequence, max_length):
        padded_sequence = sequence[:max_length] + [0] * max(0, max_length - len(sequence))
        return padded_sequence

    def predict_address(self, text):
        preprocessed_data = self.preprocess_text(text)
        input_name = self.session.get_inputs()[0].name
        output_name = self.session.get_outputs()[0].name
        prediction = self.session.run([output_name], {input_name: np.array([preprocessed_data], dtype=np.float32)})[0]
        return prediction
    
    def process_address(self, address_text):
        start_time = time.time()
        prediction = self.predict_address(address_text)

        confidence = prediction[0][0]
        threshold = 0.5
        is_in_cairo = confidence >= threshold
        confidence_prob = np.round(confidence, 2)
        if not is_in_cairo:
            confidence_prob = np.round(1 - confidence, 2)

        result = {'is_in_cairo': str(is_in_cairo), 'confidence': str(confidence_prob)}
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {np.round(execution_time, 3)} seconds")

        return result


model_path = '/model/model.onnx'
word_index_path = '/model/word_index.json'
max_length = 3  

address_verifier = AddressVerifier(model_path, word_index_path)

@app.route('/verify_cairo_address', methods=['POST'])
def verify_address():
    data = request.get_json()
    address_text = data.get('address', '')

    result = address_verifier.process_address(address_text)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
