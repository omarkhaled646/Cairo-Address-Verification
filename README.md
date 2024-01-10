# Cairo Address Verification

## Overview

Cairo Address Verification is an HTTP API that takes an address name and checks if it exists in Cairo or not using an LSTM Deep Learning Model.

## Building the Docker Image

- Open Docker Desktop on your computer
- Open your CMD then navigate to the location of the project
- Use the following Docker command:

<pre>
docker build -t (your-image-name) .
</pre>

- Or use the following command:
  
<pre>
docker-compose build
</pre>

- Then, use the following command to run it:
  
<pre>
docker-compose up
</pre>

## Dataset

- The Dataset is collected from the combination Cairo.txt that contains districts that are in Cairo and data from <a href="https://eg.dowwr.com/regions/">dowwer.com </a> using web scraping.
- You can find both the Cairo.txt file and the generated dataset in the datasets directory
- It consists of two columns the district name and the label (1 if in Cairo else 0) and contains 413 districts from all Egypt governorates
- You can open it in proper format in Excel by the following steps: 

   1- Open Excel and from the top bar navigate to data

  ![annotely_image](https://github.com/omarkhaled646/Cairo-Address-Verfication/assets/63152184/0eb11040-7119-4442-bf34-8529879c02d1)

  2- Click on From Text/CSV

  ![annotely_image (1)](https://github.com/omarkhaled646/Cairo-Address-Verfication/assets/63152184/c69bd28d-4fc5-41f9-adc4-e279fe6af40d)

  3- Choose the dataset with the name district_data.csv in the datasets directory from its location on your computer and click Import

  4- Click on Load

  ![annotely_image (2)](https://github.com/omarkhaled646/Cairo-Address-Verfication/assets/63152184/d5f8f103-4ae8-49a7-9dfb-534bc2a39d4b)

- Here is a sample of the dataset that should appear to you

  ![Book1 - Excel 1_10_2024 2_23_20 PM](https://github.com/omarkhaled646/Cairo-Address-Verfication/assets/63152184/f89570a1-af6e-41c7-bdb8-6b17bbce8b91)

## Test Script

- After running the command: <pre>docker-compose up</pre>
- You can use the test_script.py file which is in the scripts directory
- Open the project folder using any IDE
- Then, navigate to the file I referred to earlier in scripts/test_script.py
- Type your address to test here (Remember to write it in Arabic):

   ![annotely_image (3)](https://github.com/omarkhaled646/Cairo-Address-Verfication/assets/63152184/1ffd2ad7-b320-48ff-963c-18868a053fbd)

- Open the terminal in your IDE and Run it using the following command: <pre>python scripts/test_script.py</pre>

## Project Structure
<code>app:</code><br>
&emsp;&emsp;<code>app.py:</code> code for HTTP API<br>
&emsp;&emsp;<code>requirements.txt:</code> contains all libraries needed to run app.py<br>
<code>core model architecture:</code><br>
&emsp;&emsp;<code>nlp_task.ipynb:</code> notebook contain all the model generation stages<br>
&emsp;&emsp;<code>onnx_model_creation.py:</code> convert the saved model to ONNX model<br>
<code>datasets:</code><br>
&emsp;&emsp;<code>Cairo.txt:</code> contains district names in Cairo<br>
&emsp;&emsp;<code>dataset_sources.txt:</code> contains link of the dataset and the word embedding model<br>
&emsp;&emsp;<code>district_data.csv:</code> contains district names and labels<br>
&emsp;&emsp;<code>word_embeddings.csv:</code> contains each word embedding vector<br>
&emsp;&emsp;<code>word_embeddings_for_ordinary_classifiers.csv:</code> contains each word embedding vector and label<br>
<code>extra models:</code><br>
&emsp;&emsp;<code>birnn_model.h5:</code> bidirectional RNN model<br>
&emsp;&emsp;<code>gru_model.h5:</code> GRU model<br>
<code>model:</code><br>
&emsp;&emsp;<code>lstm_model.h5:</code> LSTM model<br>
&emsp;&emsp;<code>model.onnx:</code> ONNX model that is generated from the LSTM model and used for prediction in API<br>
&emsp;&emsp;<code>word_index.json:</code> JSON file that maps each word to it's corresponding indx<br>
<code>scripts:</code><br>
&emsp;&emsp;<code>test_scriot.py:</code> script used to test the HTTP API<br>
<code>Dockerfile:</code> used to build the Docker Image<br>
<code>docker-compose.yml:</code> used to run our Docker Image<br>


## Results

### metrics: 

| Model           | Training Precision | Training Recall | Testing Precision | Testing Recall | ROC Score |
|-----------------|--------------------|------------------|---------------------|----------------|-----------|
| LSTM            | 0.72               | 0.9              | 0.53                | 0.62           | 0.91      |
| GRU             | 0.71               | 0.87             | 0.5                 | 0.69           | 0.90      |
| biRNN           | 0.85               | 0.87             | 0.5                 | 0.62           | 0.92      |

- Note that the represented numbers are approximated to 2 decimal points

### Graph of ROC and Precision vs Recall Comparison 

![image](https://github.com/omarkhaled646/Cairo-Address-Verfication/assets/63152184/d7f5701c-301f-43cc-96ec-b3d722afa57e)

### Testing with Postman using docker-compose.yml

| ![Image 1](https://github.com/omarkhaled646/Cairo-Address-Verfication/assets/63152184/0e5d4e89-28e6-41dc-8d15-61b37c8b2c83) | ![Image 2](https://github.com/omarkhaled646/Cairo-Address-Verfication/assets/63152184/064ebd27-1c15-434f-b661-b103f82461a7) |
| --- | --- |
| ![Image 3](https://github.com/omarkhaled646/Cairo-Address-Verfication/assets/63152184/ebfaaf6a-ed8e-4667-8267-202e98fa0e70) | ![Image 4](https://github.com/omarkhaled646/Cairo-Address-Verfication/assets/63152184/683494e2-879c-4e42-a7e4-b0558f4e13d9) |

### Testing using the test script file

| ![test_script_res_2](https://raw.githubusercontent.com/omarkhaled646/Cairo-Address-Verfication/main/assets/63152184/c63e8162-7536-4c75-957e-222c89fc8ce4) |








## Verifying Results

Explain how to verify the claimed results. This could involve specific steps or commands to check the output or compare against expected results.

### Notes

Include any additional notes or considerations that users should be aware of. This could cover troubleshooting tips, known issues, or other relevant information to enhance the user experience.
