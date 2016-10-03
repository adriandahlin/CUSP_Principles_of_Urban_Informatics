# Citibike Review
## Jonathan Pichot (jp4772) reviewing Adrian Dahlin's (adk361) proposal

**(a)**
I'm not sure if simply asking if a variable 'effects' another variable is enough. I would reframe the Null Hypothesis to be a bit clearer about the relationship you expect to see between the variables. Something like:

Alternative hypothesis: The average duration of a bike trip becomes *shorter* the older a rider is.

Null hypothesis: The average duration of a bike trip *is the same or longer* the older a rider is.

The research will be done to a .05 confidence interval.

**(b)**
1. You'll want to uncomment the `unzip` code so that someone later on can download and immediately use the code you're sharing.
2. It appears you have some NaN values in the data. It looks to be coming from the birth year. My assumption is that sharing your birth year with Citibike is optional so they do not have the age of all riders. (It may also come from day riders, ie. non-members that buy a day pass directly from the kiosk.)
3. Removing the outliers should help the scatter plot look better. You can also zoom in a bit with something like: `pl.axis([0, 80, 0, 500000])`

**(c)**
A simple Correlation test should do the trick here since we're dealing with 2 continous variables. The result of this test will give us how strongly and in what direction the bike trip duration and age of rider are correlated. But there may be other factors to take into account. If you can identify some (like, say time of day, distance traveled, etc.), you could use a Multiple Regression test. This might clarify if there is indeed a correlation between the variables you're interested in since we'll be able to control for other factors that effect trip duration.
