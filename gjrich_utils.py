''' 
Module: Wheyland Pythoni - Building Better Modules

This module provides a simple, reusable foundation for analytics projects. 
Code should be reusable.
A good byline could be used in every Python analytics project that is done.

Process:

Code is not written from top to bottom; instead, it is written from the outside, in.
Here's what a first draft of utils_case.py might look like:

1. This docstring is included at the beginning to clarify the purpose of the Python file and organize it.
   
2. A global variable is declared for the byline string and it is set it to some simple text.

3. The main() function is defined for the module. When the script is run, main() can be used to test the byline.

4. Boilerplate conditional execution code is added so the main() function only runs when 
   this script is executed directly (but not when imported into another file).

Testing was completed in an online interpreter (https://www.online-python.com/)

For the sake of fun, added variables were kooky. 
This also could be used as a marketing scheme to convince potential clients to engage our services,
since in the modern era quirkyness equates to intelligence & competence.
'''


''' 5th and Final iteration: 
   - added variables missed in iteration 3 (success_status, flight count, former clients, best numbers)
   - Updated byline to include output from them
'''


####################################################
# Modules Import - included at the top of the script
####################################################

# Modules provide additional tools and functions not included in the basic installation.
# The following modules will be imported:
#  'statistics' - provides tools to calculate pieces like averages
# You can use ctrl+F to find where it is used
# Look for examples like statistics.mean() and statistics.stdev()

import statistics


####################################################
# Declare global variables (keep byline at end)
# This information will be used fo ra smarter byline
####################################################


# Boolean to indicate whether the company has international clients
has_international_clients: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 144

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Harmonic Balancing", "Modular Consulting", "Equilibrium Evaluation"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.5, 4.4, 4.7, 4.2, 4.9, 5.0, 4.4, 4.4, 3.9, 4.7, 4.8]

# Bool Custom Example - success status
success_status: bool = True

# Number of flights taken to meet clients
flight_count: int = 410

# List of strings representing companies we've worked with
# Had some fun making up tangential tech company names
former_clients: list = ["Pear", "Soothsayer", "Nile", "Masktome", "Webtoons"]

# List of ints indicating the best numbers - no surprise that they are mostly primes
best_numbers: list = [3, 7, 17, 37, 49, 51]


####################################################
# Calculate Basic Statistics
# Completed BEFORE we declare the byline
# Ensures values have been calculated & are ready for byline
####################################################


# Basic Stats using built-in functions min(), max() and statistics module functions mean() and stdev()

# calculated for both Client Satisfaction Scores and Best Numbers
min_scores: float = min(client_satisfaction_scores)
max_scores: float = max(client_satisfaction_scores)
mean_scores: float = statistics.mean(client_satisfaction_scores)
stdev_scores: float = statistics.stdev(client_satisfaction_scores)



min_best_numbers: float = min(best_numbers)
max_best_numbers: float = max(best_numbers)
mean_best_numbers: float = statistics.mean(best_numbers)
stdev_best_numbers: float = statistics.stdev(best_numbers)


####################################################
# Declare a global variable named byline
# Make it an f-string to show our information
####################################################

byline: str = f"""
----------------------------------------------------
Wheyland Pythoni: Building Better Modules

A new and unique company that can serve 
your specific needs - whatever they are.

We can provide whatever tools your company thinks you need
in exchange for money. Let's work together!
----------------------------------------------------
Has International Clients:      {has_international_clients}
Years in Operation:             {years_in_operation}
Flights Taken to Clients:       {flight_count}
Skills Offered:                 {skills_offered}
Are we successful?              {success_status}
Former Clients:                 {former_clients}

Best Numbers:                   {best_numbers}
Minimum Best Number:            {min_best_numbers}
Maximum Best Number:            {max_best_numbers}
Mean Best Number:               {mean_best_numbers:.3f}
Best Number Standard Deviation: {stdev_best_numbers:.3f}

Client Satisfaction Scores:     {client_satisfaction_scores}
Minimum Score:                  {min_scores}
Maximum Score:                  {max_scores}
Mean Score:                     {mean_scores:.3f}
Score Standard Deviation:       {stdev_scores:.3f}


Please hire us! Or else!

"""


####################################################
# Define the get_byline function
####################################################

def get_byline() -> str:
   # return a byline for Wheyland Pythoni
   return byline

####################################################
# Define a main() function for this module.
####################################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

####################################################
# Conditional Execution - Only call main() when executing this module as a script.
####################################################

if __name__ == '__main__':
    main()