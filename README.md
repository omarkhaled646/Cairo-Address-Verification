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



Provide an overview of the datasets and include source links:

- Overview of the datasets used
- Instructions on how to upload datasets in Excel format
- Notes on the datasets, if any
- Project structure related to datasets

### Testing Your Solution

Provide instructions on how to test the solution. Include details on using the test script, which interacts with the external server, sends HTTP requests, and returns results, including execution time.

### Verifying Results

Explain how to verify the claimed results. This could involve specific steps or commands to check the output or compare against expected results.

## Project Structure

### Test Script

Provide details on the test script that interacts with the external server:

- How to use the script
- What kind of requests it sends
- How to interpret the results, including execution time

### Results

Provide a section detailing the results of the project. Include any metrics, insights, or significant findings.

### Text File of Embeddings and Data Sources

Explain the contents of the text file containing embeddings and data sources. Include any specific information on how to use this file in the project.

### Notes

Include any additional notes or considerations that users should be aware of. This could cover troubleshooting tips, known issues, or other relevant information to enhance the user experience.
