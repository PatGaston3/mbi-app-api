MBI API Application
==============================

MBI: Medicare Beneficiary Identifier (MBI)

What Is It?
-------------

This is a simple Python/Flask API. This API is a backend for a frontend Angular project (https://github.com/PatGaston3/mbi-app-ui) with a few simple endpoints. One endpoint to generate an MBI and another to verify if a string is a valid MBI based on the current MBI format.


How To Use This
---------------

1. cd into root directory `cd mbi-app-ui`
2. cd into /api directory `cd api`
3. run the command `python3 api.py`
4. The app is live is at http://127.0.0.1:5000! You can hit either endpoint: http://127.0.0.1:5000/generate -GET or http://127.0.0.1:5000/verify?mbi{param} -POST


Testing
-------

1. cd into root directory `cd mbi-app-ui`
2. run the command `python3 -m unittest`

results will look something like:
```.............
----------------------------------------------------------------------
Ran 13 tests in 0.000s

OK
```

Acess via Heroku
----------------

#### Accessing the API directly ####

You can reach both endpoints at: https://mbi-app-api.herokuapp.com

Example: 
https://mbi-app-api.herokuapp.com/generate


#### Accessing the Application through the UI ####

Simply go to: https://mbi-app-ui.herokuapp.com/


Example EndPoints
-------

* Local (http://127.0.0.1:5000)
  * /generate - GET that returns a randomly generated MBI 
  * /verify?mbi={param} - POST to create a booking - returns the ID in the response
  * Example response
```
   {  
     "mbi": "8VW7YJ3UD63"
   }
```  
* Heroku (https://mbi-app-api.herokuapp.com)
  * /generate - GET that returns a randomly generated MBI 
  * /verify?mbi={param} - POST to create a booking - returns the ID in the response
  * Example response
```
   {
      "isValid": false
   }
```


