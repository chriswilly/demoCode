# nameView.py

Names data sourced from US SSA
https://www.ssa.gov/OACT/babynames/limits.html

nameView.py program will display rank name ranges for male, female, or both across a span of years.
Browse through name set as an alternative to name websites. Goal to add trending, grouping, or recommendation using pandas query in nameFind.py or other module.


Use command line argument parsing, eg:

    % python nameview.py --rank 8 22 --space 1 --years 1926 1969 --skip 2 --sex M
returns rank 8 thru 22 complete from 1926 to 1969 every other year for males

nameView.py
defaults set to top 12 spaced 1 apart every year since 1972 for both sexes if you call without args, all --args are optional.

    % python nameview.py --rank 3 11 --years 1926 1969
is valid.

years processed in descending order so if skip >1 then final year will be included but initial year may not depending on indexing increments.

txt files stored in data/names folder. Currently only works for the names by year txt in 'names'
Files within 'data/names' are yobYYYY.txt format "name,sex,number".



# terminal commands
    usage: nameview.py [-h] [--rank lower bound upper bound] [--space [rank spacing]] [--years year start year end]
    
                   [--skip [year spacing]] [--sex [M/F/B]]


    Set name serach criteria


    optional arguments:

      -h, --help            show this help message and exit

      --rank lower bound upper bound
 
                           popularity starting and ending position, lower is more popular
 
     --space [rank spacing]

                            rank spacing: 0,1,2..., 0,2,4...
 
     --years year start year end

                            date range years
 
     --skip [year spacing]

                            year spacing: 1999, 2000, 2001,... 1998, 2000, 2002,...

      --sex [M/F/B]         F = Female, M = Male, None = Both




# example
    % python nameview.py --sex M --rank 5 30 --year 1902 2004 --space 4 --skip 7
        /Users/.../nameSurvey/data/names
      Top 5 to 30 male names in 2004
      ...
      Top 5 to 30 male names in 1983
             name  number
      5     James   36353
      9    Robert   32750
      13    Brian   26057
      17     Adam   23494
      21  Anthony   19831
      25  Timothy   16366
      29   Jeremy   14259
      ...
      Top 5 to 30 male names in 1903
             name  number
      5    Joseph    3121
      9    Thomas    1962
      13   Willie    1454
      17     Fred    1204
      21      Roy     975
      25  Richard     863
      29   Ernest     764
