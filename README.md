# CounterAttack
Destroy account scammers with this one neat trick!

Recently, a loved one had their facebook account stolen. The scammer used a common phishing technique to set up a fake login page and coerce the target into inputting their login information. The attacker then manually logged in to the targetted account and in turn attempted to use the same attack on me. In response, I wrote this script.

Counterattack procedurally generates usernames and passwords based on data contained in names.json and passwords.json respectively. In doing so, it attempts to create formats that are as indistinguishable as possible from actual logins. 

# Functions

**randomizeCase(string)**:
Randomizes the case of a string input. Used to prevent automated filtering of counterattack information.
Example: input password12 will convert to any of the following examples: pAssword12, PASsword12, PasSSWORD12, passwoRD12, etc.

Notes:
- Input type: string
- Return type: string
	
Dependencies: 
- Libraries: random, string

**unameGenerator(lim)**:
Generates usernames for ints in range [0, limit]. Each element in the output username array is of the following form

[uname_base][int extension][generic provider]

Ex: aaron23@gmail.com, connor56@yahoo.com, etc.

Notes: 
 - Input type: int
 - Return type: array 
		  
Dependencies: 
 - Data: names.json
 - Library: random
      
**passGenerator(lim)**:

Generates passwords for ints in range [0,limit]. Each element in the output password array is of the following form:

[pwd_base][pwd_extension]

Ex: carbon14, oxygen8, etc.

Each password is also passed through the randomized capitalization function, so inputs are sometimes convoluted to 

Ex: CarbON14, OXYGen8, etc.

Notes:
- Input type: int
- Return type: array
    
Dependencies: 
- data: passwords.json
- libaray: random

**sessionGenerator(lim)**:

Generates usernames and passwords for ints in range(0, limit) using previously defined functions.

Ex: (uname = aalebel33, pwd = carbon14)

Notes:
  -Input type: int
  -Return type: Array of tuples

Dependencies: 
  -function: passGenerator
  -function: unameGenerator

**submitData(payload = ("username","password"), url = "")**:

Completes a single form submission requiring username and password input. Does not allow redirects to increase speed of form submission.

Input types: 
  - payload = tuple
  - url = string
   
Return types:
  - None
  
Dependencies:
  - Library: Requests

**counterAttack(url = "", limit = 0)**:

  Attack script. Generates a list of uname and pwd tuples and passes them through the submit data function.
  Currently limited by the size of the data input for usernames, which is 2283. 
  However, this function can be run multiple times and yield consistently uniqueresults. P(duplicate entry) < 2e-10)
  
  Notes:
   Input types:
     - url: string 
     - limit: int
   No output
    
  This function must be reconfigured for each use--variable names and urls must be consistent with defending site protocols.
    
  Dependencies: 
    -Functions: submitData

