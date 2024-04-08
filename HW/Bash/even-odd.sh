#!/bin/bash

month=$1
day=$2

declare -A months=( ["Jan"]=1 ["Feb"]=2 ["Mar"]=3 ["Apr"]=4 ["May"]=5 ["Jun"]=6 ["Jul"]=7 ["Aug"]=8 ["Sep"]=9 ["Oct"]=10 ["Nov"]=11 ["Dec"]=12 )

month_num=${months[$month]}

if (( $month_num % 2 == 0 )); then
    month_type="even"
else
    month_type="odd"
fi

if (( $day % 2 == 0 )); then
    day_type="even"
else
    day_type="odd"
fi

echo "Month $month is $month_type and day $day is $day_type."
