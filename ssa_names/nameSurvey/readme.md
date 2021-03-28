Names data sourced from US SSA
https://www.ssa.gov/OACT/babynames/limits.html

txt files stored in data/names folder. Currently only works for the names by year txt in 'names'
Files within 'names' are yobYYYY.txt format "name,sex,number"

Use command line argument parsing, eg:
python nameview.py --rank 8 22 --space 1 --years 1926 1969 --sex M

defaults set to top 11 spaced 1 apart every year since 1972 for both sexes if you call without args,

python nameview.py

or comment out the argparse bit at bottom and define these five params


Program is set up to display rank name ranges for male, female, or both across a span of years.
Goal to add trending, grouping, or recommendation expanding pandas work. But for now using to browse through large name set because name websites are not great.

todo: add larger year intervals to extend span of name sets readable.
return only names beginning with one letter or set of letters.
