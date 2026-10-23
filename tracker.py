trades = [{"coin" : "SOL", "buy" : 100, "sell" : 150},
          {"coin": "BTC", "buy" : 200, "sell" : 175},
          {"coin": "ETH" , "buy" : 300, "sell" : 400}]
x=0
def percent_change(buy,sell) :
      return (sell-buy)/buy*100
for trade in trades :
  outcome=(trade['sell']-trade['buy'])
  x=x+outcome
  if outcome>0:
    print(f"you made a profit of {abs(outcome)} and a percent change of {round(percent_change(trade['buy'], trade['sell']))}%")
  else :
    print(f"you made a loss of {abs(outcome)} and a percent change of {round(percent_change(trade['buy'], trade['sell']))}%")

if x<0 :
  print(f"you lost a total of {abs(x)}")
else :
  print(f"you made a total of {x}")
