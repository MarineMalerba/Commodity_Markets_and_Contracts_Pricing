# Commodity_Markets_and_Contracts_Pricing
This project provides tools for pricing both past and future commodity markets using linear regression, as well as estimating the price of commodity contracts based on various parameters.

## Commodity Market Pricing ##
* Purpose: Analyzes historical data (__ Nat_Gas.csv __) to predict commodity prices for both past and future dates, using linear regression.
* Input: A specific date.
* Output: Estimated commodity price for the given date.

## Commodity Contract Pricing ##
* Purpose: Calculates the price of a commodity contract based on specified conditions.
* Input:
  * Injection date(s)
  * Withdrawal date(s)
  * Injection/withdrawal rate
  * Cost rate
  * Storage cost rate
  * Maximum storage capacity
  * Commodity price estimates on injection and withdrawal dates
* Output: Estimated contract price.
