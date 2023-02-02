# project_1_mission_youtube 

Team members:
Shweta Jain
Mohsen Farrokhrouz
Kim Coleman
Ufuoma Atakere
Sandra Botica

Our purpose is to inform Content Creators how to optimise their videos based on those that are trending.

YouTube Trending Videos US 2017-2018 Dataset from Kaggle

Data exploration and Cleanup involved:
        US_cleaning.ipynb


Analysis involved exploring these 5 questions.

1. Which categories trend most often?                                                       
        See US_youtube_categories.ipynb
        Using the cleaned_us_data.csv generated an array of the unique category IDs.
        Used the {}US_category_id.json to identify the name of each category ID.
        Added a column to cleaned_us_data.csv with the category name associated with each ID.
        unique_us_cleaning_data.ipynb

2. What types of videos are trending multiple times?
        US_cleaning_categories_.ipynb
        
3. Does the month, day, time a video is published impact how long it trends?
        See US_youtube_release_time_day.ipynb
        See Objective 3 copy 2.md for a description of findings.
        See <ImagesObj3> folder for summary statistic tables and visualisations.
        See Youtube.ipynb for use of APi for duration of videos
 
4. Are trending videos a certain duration?
        See video_duration_data.ipynb for code and graphs
        See <ImagesObj4> folder for visualisations.
          
5. Is there any relationship between trending videos and likes/dislikes, views, comments, and tags?
        us_data_like.ipynb


The implications of our findings for each of the 5 questions include:

Question 1.     Publish videos in the entertainment or music categories.
                These categories have a the greatest number of trending videos.

Question 2.     April and May have the greatest number of trending videos.
                Ensure your video is published in time to take advantage of this.
                Also, don’t expect your video to trend in March, as it has the lowest number of trending videos.

Question 3.     Consider when your publish your video (time, day month).
                Publishing between 12pm to 11pm (more at 12pm  & 4pm) on a weekday, 
                during May or the months of November to February will increase the length of days a video trends.

Question 4.     Keep the video duration to under 9 minutes.
                Most trending videos are under 9 minutes, and half are less than 5 minutes.
                To trend for a longer period keep the video under 4 minutes.

Question 5.     Likes and views are related.
                Highly viewed categories have a higher number of likes and the relationship is strong.

                Be cautious if publishing videos in controversial areas.
                Content in controversial areas such as non-profits & activism and News & Politics are prone to dislikes.
                
                Tagification reduces dislikes.
                If you want to reduce the number of dislikes use a greater number of tags on your video.

  The full presentation can be viewed via this link https://docs.google.com/presentation/d/1g8Zez1SduSsBhCCOhyDryzRS-7NHFHT0/edit?usp=sharing&ouid=117521230680892718245&rtpof=true&sd=true
