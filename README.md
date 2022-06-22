# Election Analysis with Python

## Overview of election audit
A Colorado Board of Election employee has given the follwing tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes and percentage of vote each candidate received.
4. Calculate the total number of votes and percentage of votes in each county.
5. Determine county with largest voter turnout.
6. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.13, Visual Studio Code 1.68.1

## Election audit results
The analysis of the election show that:
- There were 369,711 total voetes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The county voter turnout results were:
    - Jefferson county voter turnout was 38,855 with 10.5% of total votes.
    - Denver county voter turnout was 306,055 with 82.8% of total votes.
    - Arapahoe county voter turnout was 24,801 with 6.7% of total votes.
- The county with largest with voter turnout was:
    - Denver county.
- The candidate results were:
    - Chalres Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes. <br>

<figure>
    <figcaption>Election Results in Terminal</figcaption>
    <img src="/Resources/election_results_in_terminal.png" width="1337" height="681"
         alt="election_results_in_terminal">
</figure> <br>

The link to the text file.<br>
[Election Results in Text File](/analysis/election_analysis.txt)<br>

The link to the script.<br>
[Python Code](/PyPoll_Challenge.py)<br>

## Election audit summary
The script is for local congressional election that summarizes total votes, county votes and candidate votes. The script can be used for any election with some modifications. Example, script can be used for national election with summary of state votes instead of county vote. In that case county related variables need to be changed to state related variables.  A Colorado Board of Election employee has given the follwing tasks to complete the election audit of a recent local congressional election. Another example in such national election where state level data is avialable along with county level data then third "if" loop can be written within "for" loop to get summary of both county votes and state votes.