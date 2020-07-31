# Flask Applicaton for Lyft SWE Apprenticeship role

This is flask app created for the SWE appprenticeship role  from Lyft

# Requirements

 - pip should be installed on the machine that you will be using to run this Flask app
 

# Running the Application

After you have met all of the above requirements you can run the application using the following commands:

Open the terminal window and run the following commands 

```
export FLASK_APP=lyftapp
export FLASK_ENV=true
flask run
```

Next step is to test the application using the following command. 

Run the following command on ***A new Terminal window***

```
curl -X POST http://localhost:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
```
