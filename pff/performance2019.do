set more off
clear all
set matsize 11000
set maxvar 32000
set seed 0
global bootstraps 1000


// Set environmet variables
global projects: env projects
global storage: env storage

// General locations
global dataraw =  "$storage/Thorpe"
global output = "$projects/Thorpe/pff"


// Data (manually created from raw data in $storage/Thorpe)
use $output/season2019

// Recode implied values
gen impliedValueOpen = real(substr(differenceo,1,3)) if substr(differenceo,1,1) != "-"
replace impliedValueOpen = real(substr(differenceo,1,4)) if substr(differenceo,1,1) == "-"

gen impliedValueClose = real(substr(differencec,1,3)) if substr(differencec,1,1) != "-"
replace impliedValueClose = real(substr(differencec,1,4)) if substr(differencec,1,1) == "-"

sum impliedValueOpen
sum impliedValueClose

replace bettype = "MoneyLine" if bettype == "Money Line"
// Recode Outcome
gen outcomeOpen = 1 if betresulto == "W"
replace outcomeOpen = 0 if betresulto == "L"

gen outcomeClose = 1 if betresultc == "W"
replace outcomeClose = 0 if betresultc == "L"

// Save dataset
save $output/season2019Recoded.dta, replace
global data = "$output/season2019Recoded.dta"

local bets = "MoneyLine, Spread, Total"
foreach bet in `bets' {
    use $data, replace
    display "`bet'"
    drop if bettype != "`bet'"
    sum outcomeOpen
    sum outcomeClose
    sum outcomeOpen if impliedValueOpen > 0
    sum outcomeClose if impliedValueClose > 0
    sum outcomeOpen if impliedValueOpen > 1
    sum outcomeClose if impliedValueClose > 1
}

