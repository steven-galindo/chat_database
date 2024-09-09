# Project Description

The goal of this project is to develop an interactive web application that leverages natural language processing to query and analyze data from the [Bike Store Database](https://www.kaggle.com/datasets/dillonmyrick/bike-store-sample-database). The application allows users to request statistical information, generate and download DataFrames in CSV format, and create visualizations based on the stored data. With a focus on user-friendliness, this app enables users to quickly and easily gain valuable insights through simple prompts.A demo of the application deployed on AWS can be consulted at this [link](https://demo-challenge-aws.sgn-aidev.uk/).

![Flow Chart](flow%20chart.png)

The diagram describes the internal functioning of the application.

## Process Stages

1. **Prompt Input:**

   The process starts with a **user prompt**, which is a natural language request or question directed at the database.

2. **Processing by GPT-4o-mini:**

   The prompt is processed by the GPT-4o-mini language model. Using this model and the LangChain library, the table referenced by the question is inferred.

3. **Processing by PandasAI:**

   Once a candidate table is identified, it is loaded using PandasAI. With the help of the language model, the requested information is extracted.

4. **Processing by Streamlit:**

   Finally, using Streamlit for the user interface, the type of response from PandasAI is determined and then displayed or graphed accordingly.

---

# Instructions to Install and Run the Application using Docker

This section details the steps required to set up and run this application using Docker and Docker Compose.

## Prerequisites

Before starting, make sure you have the following programs installed on your system:

- [Docker](https://docs.docker.com/get-docker/) (version >=26.1.4)
- [Docker Compose](https://docs.docker.com/compose/install/) (version >=v2.27)

## Steps to Configure and Run the Application

1. **Clone the Repository**

   Clone the repository to your local machine using `git`:

   ```bash
   git clone https://github.com/steven-galindo/GenAI-Engineering-Challenge.git
   cd GenAI-Engineering-Challenge
   ```

2. **Create the '.env' File**

   Create an environment variables file to store the OpenAI API key:

   ```bash
   OPENAI_API_KEY=sk*******
   ```

3. **Build the Docker Image**

   To build the Docker image, navigate to the root directory of the project and run the following command:

   ```bash
   docker-compose build
   ```

4. **Run the Application**

   To run the container, use the command:

   ```bash
   docker-compose up -d
   ```

5. **Access the Application**

   Once the container is running, you can access the application from your browser at the following address:

   ```
   http://localhost:8501
   ```

---

