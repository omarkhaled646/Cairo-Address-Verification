import tensorflow as tf
import tf2onnx
import onnx

tf_model = tf.keras.models.load_model('./models/lstm_model.h5')

# Convert the TensorFlow model to ONNX format
onnx_model, _ = tf2onnx.convert.from_keras(tf_model)

# Save the ONNX model to a file
onnx_model_path = './models/model.onnx'
onnx_model, _ = tf2onnx.convert.from_keras(tf_model, opset=13)
onnx.save(onnx_model, onnx_model_path)