# Hall of Fame Predictor

Accurately predicting the probability of active players making it into the hall of fame.

## Premise

Building a mathematical model based on current hall of fame players to predict future ones. 

### Web scraping

The database was built using scrape.py which scrapes basketballreference.com to build a database of hall of fame players career statistics as well as current players. 

### Logistic Regression

Regressed over all the features and used backward selection to output this final model. This model is logist_regress file, which outlines the selected features used as well as their coefficients. 

Below is an output of the top fifteen players as predicted by this model, the full predictions can be found in Predictions_current.xlsx

| Player        | HOF Probability |
| ------------- |:-------------:| 
|LeBron James|1.000|
|Dwyane Wade|1.000|
|Dirk Nowitzki|1.000|
|Kevin Durant|1.000|
|Chris Paul|1.000|
|Russell Westbrook|1.000|
|Carmelo Anthony|1.000|
|Stephen Curry|1.000|
|Tony Parker|1.000|
|James Harden|1.000|
|Dwight Howard|0.999|
|Vince Carter|0.997|
|Anthony Davis|0.996|
|John Wall|0.996|

These outputs have been verified using a human model that collected input from average fans and compiled into a list almost identical to the one above

