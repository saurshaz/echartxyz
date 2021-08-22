
## Backend start with
`. ./venv/bin/activate` && `python app.py`

## Chart 1  
http://localhost:5000/?sm=CVS&sdd=1&smm=1&syr=2021&edd=1&emm=6&eyr=2021 `tenchanJS`

## Chart 2
http://localhost:5000/echart?sm=CVS&sdd=1&smm=1&syr=2020&edd=1&emm=6&eyr=2021 `echartJS`



### Examples 
https://echartxyz.vercel.app/echart?sm=^NSEI&sdd=1&smm=11&syr=2020&edd=26&emm=8&eyr=2021 (Nifty)
https://echartxyz.vercel.app/echart?sm=^NSEBANK&sdd=1&smm=11&syr=2020&edd=26&emm=8&eyr=2021 (Banknifty)
https://echartxyz.vercel.app/echart?sm=INFY.NS&sdd=1&smm=11&syr=2020&edd=26&emm=8&eyr=2021 (INFY)
https://echartxyz.vercel.app/echart?sm=MRF.NS&sdd=1&smm=11&syr=2020&edd=26&emm=8&eyr=2021%20 (MRF)


Any NSE entity's symbol in URL would be `{symbol.NS}`  ... i.e. - INFY.NS, RELIANCE.NS etc
Any NASDAQ entity's symbol in URL would be `{symbol}` ... i.e. - TSLA, AAPL etc


#### KNOWN ISSUES
- backend is based on `pandas_datareader` which shall be replaced with something else for min by min data. right now data is day basis
- This could be used for investors, maybe not by traders till the time real streaming comes in
- IS a hobby project, collaboration welcome