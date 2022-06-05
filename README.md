# QA Streaming ML Pipeline Challenge

The challenge consists of three fundamental steps:

1. Start the `api` service through the provided docker-compose.yml file
2. Develop a script to ingest data through the api's main endpoint.
 <br> The data from the API endpoint is paginated. You can find the API's documentation at http://0.0.0.0:5000/docs or http://0.0.0.0:5000/redoc

3. Now that you are able to ingest data from the API, implement an online regression model (you can use 
any library) which gets incrementally fitted on the data (See "ML Model" section).

**IMPORTANT** The ingestion script should ingest data in batches and feed it to the model in batches.
Do not just pre-load all the data in advance. This is the "streaming" part of the challenge.

## ML Model

Our API returns 4 columns:
* `id` (`int`): An incremental identifier for each row.
* `network_ability` (`float`): Represents the networking ability of an employee.
* `competence` (`float`): Represents actual work competence of an employee.
* `promoted` (`bool`): Indicates whether the employee got a promotion or not.

We are interested in two kind of models:

1. A simple classification algorithm which attempts to predict the variable `promoted` through the other variables. <br>
The focus of this model is pure prediction capability. This is the focus of our ML application.

2. A regression model in which the predicted/target variable is `network_ability`. <br>
The goal of this second kind of model is to understand the relationship between the other variables and `network_ability`. <br>
You are **not** required to include this model within the final application. <br>
**Hint**: Try to reason qualitatively about the dependencies of the variables before starting to crunch numbers, try to think like a scientist.

Save the model, the current page, the coefficients and any relevant statistical measure to the SQLite database (on a different table than `data`) while you are updating it.


## User Interaction

You can be creative about how an user should interact with your streaming ML pipeline.

How can the user visualize the convergence/updating of the model? How are you going to present the results?

Possible ways to represent the data are:

* A CLI application

* A web-based application

The only requirement is that the application needs to be interactive and that the models need to be updated incrementally while the application is running (i.e. no pre-training).


## Submission

Please send a Git repository (hosted on any git provider) to giulio@quickalgorithm.com containing all the necessary files and a text/markdown file explaining how you solved the various steps.
