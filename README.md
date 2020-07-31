# Flask Applicaton for Lyft SWE Apprenticeship role

This is flask app created for the SWE appprenticeship role  from Lyft

# Requirements

Following packages must be installed before runnning this application

- pip
- flask 

 - pip should be installed on the machine that you will be using to run this Flask app
 
 Install pip using the following [documentation](https://pip.pypa.io/en/stable/installing/)
 
 When you have finished installing pip you can simply install flask using the following command on the terminal window.
 
 - Open the Terminal window and type in the following command. 
 
 ```
 pip install flask 
 ```
 

# Running the Application

After you have met all of the above requirements you can run the application using the following commands:

Open the terminal window and run the following commands 

```
export FLASK_APP=lyftapp
export FLASK_ENV=true
flask run
```

Next step is to test the application using the following command. 

Run the following command on ***New Terminal Window***

```
curl -X POST http://localhost:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
```

The results that I obtained are screenshoted and displayed below. This matches the requirement that was requested by the interview application. 


