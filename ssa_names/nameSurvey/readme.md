Names data sourced from US SSA
https://www.ssa.gov/OACT/babynames/limits.html

nameView.py program will display rank name ranges for male, female, or both across a span of years.
Intent to browse through large name set as an alternate to name websites. Goal to add trending, grouping, or recommendation expanding pandas work.


Use command line argument parsing, eg:
% python nameview.py --rank 8 22 --space 1 --years 1926 1969 --skip 2 --sex M
returns rank 8 thru 22 complete from 1926 to 1969 every other year for males

nameview.py
defaults set to top 12 spaced 1 apart every year since 1972 for both sexes if you call without args,

years processed in descending order so if skip >1 then final year will be included but initial year may not depending on indexing increments.

txt files stored in data/names folder. Currently only works for the names by year txt in 'names'
Files within 'data/names' are yobYYYY.txt format "name,sex,number".
