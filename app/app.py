from flask import Flask, request, jsonify
import onnxruntime
import json
import numpy as np
import time

app = Flask(__name__)

class AddressVerifier:
    def __init__(self, model_path, word_index_path):
        """
        Initialize the AddressVerifier class.

        Parameters:
        - model_path (str): Path to the ONNX model file.
        - word_index_path (str): Path to the word index JSON file.
        """
        self.session = onnxruntime.InferenceSession(model_path)
        self.word_index = self.load_word_index(word_index_path)

    def load_word_index(self, word_index_path):
        """
        Load the word index from a JSON file.

        Parameters:
        - word_index_path (str): Path to the word index JSON file.

        Returns:
        - dict: Loaded word index.
        """
        with open(word_index_path, 'r') as f:
            word_index = json.load(f)
        return word_index

    def preprocess_text(self, text):
        """
        Preprocess the input text by tokenizing and padding it.

        Parameters:
        - text (str): Input text to be preprocessed.

        Returns:
        - list: Padded sequence of word indices.
        """
        tokenized_text = text.split()
        indexed_text = [self.word_index.get(token, 0) for token in tokenized_text]
        padded_sequence = self.pad_sequence(indexed_text, max_length)
        return padded_sequence

    def pad_sequence(self, sequence, max_length):
        """
        Pad the input sequence to a specified maximum length.

        Parameters:
        - sequence (list): Input sequence.
        - max_length (int): Maximum length for padding.

        Returns:
        - list: Padded sequence.
        """
        padded_sequence = sequence[:max_length] + [0] * max(0, max_length - len(sequence))
        return padded_sequence

    def predict_address(self, text):
        """
        Make a prediction on the input text using the loaded model.

        Parameters:
        - text (str): Input text for prediction.

        Returns:
        - np.array: Prediction result.
        """
        preprocessed_data = self.preprocess_text(text)
        input_name = self.session.get_inputs()[0].name
        output_name = self.session.get_outputs()[0].name
        prediction = self.session.run([output_name], {input_name: np.array([preprocessed_data], dtype=np.float32)})[0]
        return prediction

    def process_address(self, address_text):
        """
        Process the input address text, make a prediction, and return the result.

        Parameters:
        - address_text (str): Input address text.

        Returns:
        - dict: Result dictionary containing 'is_in_cairo' and 'confidence'.
        """
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
    """
    Endpoint to verify if an address is in Cairo.

    Expected JSON payload:
    {
        "address": "Input address text"
    }

    Returns:
    - JSON: Result dictionary containing 'is_in_cairo' and 'confidence'.
    """
    data = request.get_json()
    address_text = data.get('address', '')

    result = address_verifier.process_address(address_text)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
