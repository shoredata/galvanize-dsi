#   Fundamental skills

Today's sprint focuses on several fundamental skills you need to succeed as a data scientist:

* Unix (Linux)
* Regex
* Workflow (CRISP-DM) and correctness in science
* Exploratory Data Analysis (EDA)

In addition, you will set up your AWS account so that Amazon can finish processing your account in time for the AWS sprint.


##  Objectives

*   Master basic Unix surival skills:
    -   Configure your environment (`export`, `echo`, dotfiles)
    -   Understand Unix permissions
    -   Navigate filesystem (`cd`, `rm`, `mkdir`, `rmdir`, `touch`, `find`, `chmod`, `chown`)
    -   Examine and characterize files (`less`, `head`, `tail`, `cat`, `wc`, `od`, `grep`, `md5sum`)
    -   Operate on text files (`sort`, `uniq`, `cut`, `paste`, `sed`, `awk`)
    -   Use filter + pipes model to create complex commands
    -   Write a basic shell script
    -   Access a remote machine (`ssh`, `scp`, `sftp`)
    -   Survive `vi`, `emacs`, `nano`, or `pico`
*   REGEX
    -   Define a regex
    -   Read & write basic regex for search and replace
*   Workflow
    -   Define steps
    -   Define steps in VV&UQ
*   Perform basic EDA
    -   Summary statistics: min, max, mean, sd, quartiles, median
    -   Plots: scatter, box, bar, histogram, matrix scatter plots
    -   Simple tests
    -   Handling missing data


##  Agenda

Today's agenda:

| Time      | Topic             |
| :-------- | :---------------- |
| 8:30-8:45 | Survey            |
| 8:45-9:15     | Sign up for AWS -- follow instructions in [setup_aws.md](setup_aws.md)
| 9:15-10:15    | Unix & REGEX lecture  |
| 10:15-12:00   | Individual exercise   |
| 1:15-2:30     | Workflow & EDA        |
| 2:30-5:30     | Pair exercise         |


##  A little background on today's topics

Unix -- and by extension OS/X from the terminal -- provides the best platform for doing science because it is robust and has many simple simple commands which can easily be combined to solve whatever problems you encounter.  Furthermore, scientific clusters and cloud computing such as [Amazon Web Services](https://aws.amazon.com) (AWS) almost always runs some flavor of Linux.  Learning Unix will considerably boost your productivity because it will help you wrangle data and quickly answer questions about files, data, and more.

[Regular expressions](https://en.wikipedia.org/wiki/Regular_expression) (a.k.a.,  REGEX or RE) are a language to describe arbitrarily complex patterns.  Learning regex will improve your abilities to search and replace text in your code and other files.  [RegExr](http://www.regexr.com) is a great resource to learn, test, and develop regular expressions.  You can use REGEX with both Unix command-line tools such as `grep`, editors, and  programming languages, including Python, Perl, and others.

Using a consistent and standard workflow will also make your more productive because following a standard process ensures that you don't omit steps in your analysis and that you avoid common errors.  [CRISP-DM](https://en.wikipedia.org/wiki/Cross_Industry_Standard_Process_for_Data_Mining) is currently one of the best and most popular approaches.  However, it doesn't put enough emphasis on testing and ensuring correctness.  [Verification, validation, and uncertainty quantification](https://en.wikipedia.org/wiki/Verification_and_validation) provides an epistemological framework for thinking about correctness in science.  [Oberkampf & Roy](http://www.amazon.com/Verification-Validation-Scientific-Computing-Oberkampf/dp/0521113601/ref=sr_1_1?ie=UTF8&qid=1444933963&sr=8-1&keywords=oberkampf+and+roy) is a better, but non-free, reference on VV&UQ.

Finally, EDA is also a crucial skill: EDA is how to approach a new data, to learn its properties, and to formulate hypotheses about its strengths and weaknesses as well as what kind of model to build.  EDA is a crucial step in the (CRISP-DM) workflow:  do not skip EDA, because you will not clean or model your data correctly if you don't understand it.

##  Exercises

Today's exercises are:

1.  [Setup AWS](setup_aws.md)
2.  [Individual Exercise](individual.md)
3.  [Pair Exercise](pair.md)

##  References

For Unix, one of Sobell's Linux books is a great references, such as [A Practical Guide to Linux Commands, Editors, and Shell Programming](http://www.amazon.com/Practical-Guide-Commands-Editors-Programming-ebook/dp/B009AVGJLO/ref=la_B000APJW04_1_4?s=books&ie=UTF8&qid=1444934667&sr=1-4&refinements=p_82%3AB000APJW04) because it covers all the basics as well as shell programming and editors

For VV & UQ, see [Verification and Validation in Scientific Computing](http://www.amazon.com/Verification-Validation-Scientific-Computing-Oberkampf/dp/0521113601/ref=sr_1_1?ie=UTF8&qid=1444933963&sr=8-1&keywords=oberkampf+and+roy) by Oberkampf and Roy.

[Fundamentals of Machine Learning for Predictive Data Analytics](https://mitpress.mit.edu/books/fundamentals-machine-learning-predictive-data-analytics) provides a great discussion of how to use CRISP-DM to solve data science problems as well as a good introduction to common ML models and several case studies.  In addition, their is a nice appendix which explains how to do EDA.

Wikipedia has a nice [summary of plots](https://en.wikipedia.org/wiki/Exploratory_data_analysis) which are useful during EDA.  Also, look at Anscombe's [quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet) to see the importance of plotting data and not just looking at summary statistics.

[Vim Adventures](http://vim-adventures.com) is a fun game which will teach you how to use `vim`.

A nice [tutorial](http://www.tutorialspoint.com/python/python_reg_expressions.htm) on regular expressions is available on [tutorialpoint](http://www.tutorialspoint.com/python/python_reg_expressions.htm).  Use [RegExr](http://www.regexr.com) to test your REs.
