# Finance

## CFA Level 1

### Volume 1 - Quantitative Methods

**Future Value Formula**

$$FV_N = PV(1 + r)^N$$

The future value after N time periods ($FV_N$) is equal to the present value ($PV$) multiplied by one plus the interest rate ($r$) raised to the $N_{th}$ power.

* Note that both the interest rate $r$ and the time period $N$ must be in the same units (i.e. if $N$ is stated in months, then $r$ should be the monthly interest rate, unannualized).

* Another way of saying this is that the future value after $N$ periods ($FV_N$) is the present value ($PV$) scaled by a factor of $(1 + r)^N$.

#### Compounding

The future value formula (above) is used when interest is compounded annually. When interest is compounded more frequently, one uses:

$$FV_N = PV \left( 1 + \frac{r_s}{m} \right)^{mN}$$

This can be used for any discrete division of a time interval. When interest is compounded *continuously*, the formula becomes:

$$FV_N = PVe^{r_sN}$$

* $r_s$ = **stated annual interest rate/Quoted interest rate** (when interest is compounded more frequently than annually, financial institutions often state the annual interest rate as opposed to breaking it down into more precise units).

* $m$ = Number of compounding periods per year (i.e. 12 if compounded monthly).

* $N$ = Years ($N$ can always be interpreted as years in the above equation).

* $FV_N$ = Future value after $N$ years.

* $PV$ = Present value.

**Annual Percentage Yield (APY)**

As one can see from the above formulas, the **effective annual rate** (synonymous to annual percentage yield) is often slightly different than the stated annual interest rate, which can make a large difference over time.

This leads to the need for a "standardized" rate, a rate that allows interest rates that are compounded at different frequencies to be compared. **Enter APY**. The annual percentage yield gives one the ability to aptly compare stated annual interest rates with different compounding periods.

If compounding is discrete (most often the case):

$$APY (EAR) = \left( 1 + \frac{r_s}{m} \right)^m - 1$$

If compounding is continuous:

$$APY (EAR) = e^{r_s} - 1$$
