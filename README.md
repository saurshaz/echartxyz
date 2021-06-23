
## Backend start with
`./start.sh`

## Chart 1  
http://localhost:8080/?sm=CVS&sdd=1&smm=1&syr=2021&edd=1&emm=6&eyr=2021 `tenchanJS`

## Chart 2
http://localhost:8080/echart.html?sm=CVS&sdd=1&smm=1&syr=2020&edd=1&emm=6&eyr=2021 `echartJS`

## TODOs

- [X] tenchanJS charts with indicators
- [X] echarts charts with indicators
- [X] connect to yahoo URLs instead of CSV files (via qs params)
- [ ] mobile first
- [ ] personalised charts (for past and present transactions)
- [ ] charts with alerts (IFTTT)
        - overlay displayable and clickable on charts
        
- [ ] scanners (with external API connected)
- [ ] strategy (with pinescript syntax ideally)
- [ ] backtesting
- [ ] automating trading with strategy and monitoring performances
- [ ] listing of strategies on marketplace(proof of income needed, profitsharing basis)
- [ ] charts to indicate all key indicators and initiate trading
- [ ] deploy to brokers (IFTTT)


### Trader IFTTT (If this Then that)

# "IF" conditions 
##### (inputs - sl, tp, price = cmp, spot = itm, proximity, strategy_name, tv_url, live=false)

    - SL_PNL, TP_PNL :: can be on the basis of PnL made like notify for this leg only when profit is Rs. 2000/-
    - SL_SPOT, TP_SPOT :: can be on the basis of spot price nearness (in case of options/future, like for a strike price 700 CE, when the spot nears 695 or for strike price 700 PE when spot nears 750, can be customized)
    - SL, TP :: can be on the basis of price of bought instrument (in case of equity stocks this is same as SL and TP)

    - any of the "strategies.json" strategy passes, (as per "strategies.json")
    - pre-configured "tv strategies" giving any action signal (TV url + action data needed) "tv_strategies.json"


# "THAT" actions
    - "notify" :: notify "call to action notification" on phone, email, system options (as per 'notify.json')
    - "autotrade" :: auto trade "passed trade" using my broker details (as per 'autotrade.json')

## a loop to check the circuit of indexes just opened and notifiy, so that as soon as the circuit is open index PE CE in watchlist can be purchased

# "notifty" action
## conditional notifiers ( system level alert, SMS, EMAIL to be added later)
   - SL_PNL, TP_PNL :: can be on the basis of PnL made like notify for this leg only when profit is Rs. 2000/-
   - SL_SPOT, TP_SPOT :: can be on the basis of spot price nearness (in case of options/future, like for a strike price 700 CE, when the spot nears 695 or for strike price 700 PE when spot nears 750, can be customized)
   - SL, TP :: can be on the basis of price of bought instrument (in case of equity stocks this is same as SL and TP)

## Overall logic simplified
- step 1 :: Trader passes configuration files ("exchange.json", "ifttt.json", "positions.json", "autotrade.json", "notify.json")
- step 2 :: Trader starts the python program (cli based, TODO: make installable)
- step 3 :: Timely iterations start on the basis of rules supplied 
- step 4 :: System level notifications are shown along with a sound, if criterias are matched, else nothing
- after a sleep of some seconds step 1 again

##### Thoughts :: 

- edelweiss app (simpler more navigable .. entire trading)
- backtesting strategies(streak, options alpha), 
- screener (screener, tv etc)
- show company details, (ET, moneycontrol)
- trading charts, live price (tradeclue, ET, moneycontrol) 
- ifttt, recommendations actions (social trading, streak)


https://nextlevelbot.com/

optionables.in

chartink.com





- JS side changes to achieve following workflow

- user sets up the chart with correct strategy with entry and close conditions (pine editor)
- user sets up the alerts in TV, and opens up logs sidebar (do using seleniumbase after setting up charts)

- `document.querySelectorAll('.widgetbar-page.active .widgetbar-widget-alerts_log')` is the log area selector on right


- `document.querySelectorAll('.widgetbar-page.active .widgetbar-widget-alerts_log div div div div:nth-child(2)')` is one log div selected

- `document.querySelectorAll('.widgetbar-page.active .widgetbar-widget-alerts_log div div div div:nth-child(2)  div:nth-child(2)')[0]` is the message like

```
UT Bot (3, 10): order sell @ 2 filled on TSLA. New strategy position is -476
```
iterate over all messages in alert log bar (can be for different securities)
- `document.querySelectorAll('.widgetbar-page.active .widgetbar-widget-alerts_log div div div div:nth-child(2)  div span:nth-child(1)')[0]` is the time 
- `document.querySelectorAll('.widgetbar-page.active .widgetbar-widget-alerts_log div div div div:nth-child(2)  div span:nth-child(2)')[0]` is the ticker 
- process ordering long/short as per this message
- now clear this log message `document.querySelectorAll('.widgetbar-page.active .widgetbar-widget-alerts_log div div div div:nth-child(2)  div')[0]` right click on this and click on `clear log`
`document.querySelectorAll('td[data-icon-cell="true"] span:nth-child(1)')[1].click()`

- alert log is empty now 