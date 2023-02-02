Objective 3 
(Sandra with Kim assisting)

Keep these US holiday dates in mind.
August 18 School starts, Dec 23-Jan 3 Christmas Break, Mar 13-17 Spring Break, Summer Break May 24-Aug 16

Explore the relationship between video publishing and length of days trending:
    day of the week (i.e. Mon, Tues etc), 
    month, 
    time of the day (i.e. 1am, 4pm) 
    length of video (i.e. 1:30, 10:10)


There are 6347 unique videos in the US You tube csv file.
129 Unique videos trended for 20-30 days.
6218 trended for less than 20 days (1077 10-19 days, 4434 1-9 days, 707 1 day).


        For the Hour of publish, needed to convert datetime from column titled "publish_time_formatted".
        Added columns to dataFrame for hour and minutes of publishing time.


        For the length (duration) of videos used a YouTube API
        See File Youtube.ipynb
        Also involved converting PT10M20S into an integer (seconds).
        -Videos that trended the longest (Top 19 - removed outlier from Top 20) Mode = 231 seconds long 
            (Fig14BoxplotDurationTop20.png)
            (Fig15LineGraphDurationTop20.png)
            (Fig16DurationTop20.csv)
            (Fig17DurationTop19.csv)
            (Fig18BoxplotDurationTop19.png)
            (Fig19LineGraphDurationTop19.png)
        -For all unique videos (only 5798) Mode = 283 seconds long 
            (Fig20UniqueVideosDuration.csv)



Figures 1-4 and charts are an analysis of publishing day/month/time for all unique videos 6347.

Figure 1 Publish Hour (Fig1PublishTimeSummaryStatistics.csv)
Plots the 6347 unique videos and the hour that they were published. 
Most videos were published between 1-11pm (13-23).
The highest number of videos published at 4pm (16).
Time of Day: 83.03% 1pm-12am (13-23), 32.87% 12am-1pm (0-13)

Figure 2 Publish Day (Fig2PublishDaySummaryStatistics.csv)
Plots the 6347 unique videos and the day of the week that they were published.
Videos were most frequently published on a Wednesday, Tuesday, Thursday, Friday and Monday. 
Fewer videos published on a Sunday and Saturday.
Day: 83.03% Mon-Fri, 17.43% Sat/Sun

Figure 3 Publish Month (Fig3PublishMonthSummaryStatistics.csv)
Plots the 6347 unique videos and the month that they were published.
Videos were mostly published between Nov-Feb, followed by March-May, then June.
Few videos published between July-Oct.
Month: 69.33% Nov-Feb, 27.77% March-May, 2.32% June, 0.58% July-Oct
Dec/Jan 38.34% - coinciding with Thanksgiving/Fall Break at the end of November.  
As well as Christmas and New Year, and University winter break (mid December to late Jan)

Figure 4 Video Category (Fig4PublishVideoCategorySummaryStatistics)
Plots the 6347 unique videos and the category name.
Entertainment videos were double in number, when comparted with the 2nd most published video category, music. 
Both were the most frquently published category type, with 15 types in total.



Figures 8-10 and charts are an analysis of publishing day/month/time for 129 Videos that trended for 20 days or longer.

Figure 8 (linked to Figure 1) Publish Hour (Fig8PublishHourSummaryStatistics.csv)
Plots the Top 129 Videos and the Hour of the day published.
Most videos were published between 12-12pm (12-23).
The highest number of videos published at 12noon (12) and 4pm (16).

Figure 9 (linked to Figure 2) Publish Day (Fig9PublishDaySummaryStatistics.csv)
Videos were most frequently published on a Thursday, Friday, Tuesday and Wednesday. 
Followed by Sunday and Monday.
Least videos published on a Saturday.

No Figure (linked to Figure 3)
No plot as 97.67% videos published in May.
2.33% published in April.

Figure 10 (linked to Figure 4) (Fig10CategorySummaryStatistics.csv)
Plots the Top 129 Videos and the category.
Music (1) and Entertainment (2) were the top 2 categories published. 
Followed by Howto & Style (3), Gaming (4), Comedy (5), Film & Animation (6). 
Listed in brackets is where categories were ranked in the 129 published and trending for longer then 20 days.



Figure 11 (Linked to Figures 1 and 8) (Fig11PublishHour.png)
Plots hour of publish comparing all unique videos (6347) to 129 videos that trended for 20 days or longer.



The following 2 plots were comparing the views, followed likes over the duration of days that the seconds highest trending (in days). Just to get a feel for the data.
Figure 12 (Fig12SecondLongestTrendingVideoViews.png)
Figure 13 (Fig13SecondLongestTrendingVideoLikes.png)




Figures 5-9 and charts are an analysis of publishing day/month/time for 20 videos that had the longest days trending. This was what data I used originally to compare to the total data base, then decided to determine how many videos published for X amount of days, as described at the top of the page and thought I'd present findings based on the 129 that trended for 20 days or longer.

Figure 5 (linked to Figure 1) Publish Hour (Fig5PublishHourSummaryStatistics.csv)
Plots the Top 20 Videos and the Hour of the day published.
80% Published after 1pm (13), with 20% before 1pm.

Figure 6 (linked to Figure 2) Publish Day (Fig6Top20DaySummaryStatistics.csv)
Plots the Top 20 Videos and the day of the week that they were published.
Thursday was the day most Top 20 videos were published. Interestingly publishing on a Sunday for the Top 20 was not as low compared with the total number of videos.

No Figure (linked to Figure 3)
No plot as the top 20 were all released in May.

Figure 7 (linked to Figure 4) (Fig7Top20CategorySummaryStatistics.csv)
Plots the Top 20 Videos and the category.
Entertainment (1) and Music (2)  were the top 2 categories published in the Top 20 videos. 
With only 4 other categories published. Film & Animation (9), Science & Technology (8), Howto & Style (3) and Education(10). 
Listed in brackets is where these were ranked in the number published for all unique videos.


