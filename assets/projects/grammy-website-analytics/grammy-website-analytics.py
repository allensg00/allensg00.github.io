"""
# Grammys Project
![](https://www.moviedebuts.com/wp-content/uploads/2021/05/ra_ga_logo.png)

Are you excited to dive into data work for an exciting project at The Recording Academy? You know, the non-profit organization behind the Grammy Awards!

In this project, you'll work on real data from both websites owned by The Recording Academy, the non-profit organization behind the famous Grammy Awards. As you just learned, Ray Starck, the VP of Digital Strategy, decided to split the websites into grammy.com and recordingacademy.com to better serve the Recording Academy's various audience needs.

Now, you are tasked with examining the impact of splitting up the two websites, and analyzing the data for a better understanding of trends and audience behavior on both sites.  

Are you ready?!?!

Let's do this!
"""

"""
![](https://media.giphy.com/media/ZSK6UPKTSLZCKd7orz/giphy.gif)
"""

"""
## Data Dictionary
To start, you will be working with two files, `grammys_live_web_analytics.csv` and `ra_live_web_analytics.csv`.

These files will contain the following information:

- **date** - The date the data was confirmed. It is in `yyyy-mm-dd` format.
- **visitors** - The number of users who went on the website on that day.
- **pageviews** - The number of pages that all users viewed on the website.
- **sessions** - The total number of sessions on the website. A session is a group of user interactions with your website that take place within a given time frame. For example a single session can contain multiple page views, events, social interactions.
- **bounced_sessions** - The total number of bounced sessions on the website. A bounced session is when a visitor comes to the website and does not interact with any pages / links and leaves.
- **avg_session_duration_secs** - The average length for all session durations for all users that came to the website that day.
- **awards_week** - A binary flag if the dates align with marketing campaigns before and after the Grammys award ceremony was held. This is the big marketing push to get as many eyeballs watching the event.
- **awards_night** - The actual night that Grammy Awards event was held.
"""

"""
# Part I - Exploratory Data Analysis

![](https://media.giphy.com/media/6y6fyAD9OIE6NvhJEu/giphy.gif)
"""

"""
## Task 1

Import the `pandas`,`numpy`, and `plotly.express` libraries.
"""

# Import libraries
import pandas as pd
import numpy as np
import plotly.express as px


# RUN THIS CELL - DO NOT MODIFY
# this formats numbers to two decimal places when shown in pandas
pd.set_option('display.float_format', lambda x: '%.2f' % x)


"""
## Task 2

Load in the first two files for your analysis. They are the `grammy_live_web_analytics.csv` and `ra_live_web_analytics.csv`.


**A.** For the `grammy_live_web_analytics.csv` file store that into a dataframe called `full_df`

**B.** For the `ra_live_web_analytics.csv` file store that into a dataframe called `rec_academy`

**C.** Preview the dataframes to familiarize yourself with the data.

All files needed can be found in the `datasets` folder.
"""

# Read in dataframes
full_df = pd.read_csv('grammy_live_web_analytics.csv')
rec_academy = pd.read_csv('ra_live_web_analytics.csv')

# Convert date columns to datetime for easier analysis
full_df['date'] = pd.to_datetime(full_df['date'])
rec_academy['date'] = pd.to_datetime(rec_academy['date'])


# preview full_df dataframe
full_df.head()


# preview rec_academy dataframe
rec_academy.head()


"""
## Task 3

We all know The Grammy Awards is *the* biggest music event in the music industry, but how many visitors does that bring to the website?

**A.** Create a line chart of the number of users on the site for every day in the `full_df`. See if you can spot the days the Grammys awards are hosted.
"""

# Plot a line chart of the visitors on the site.
fig = px.line(
    full_df,
    x='date',
    y='visitors',
    title='Daily Visitors on Grammy Website(s)',
    labels={'date': 'Date', 'visitors': 'Visitors'}
)
fig.show()


"""
<span style='background-color: rgba(138, 43, 226, 0.4); padding: 0.2em 0.4em; border-radius: 4px;'>**Remark:** The smaller spikes, typically around November/December of each year, are when the nominees are announced.</span>
"""

"""
**B.** What can you say about the visitors to the website by looking at the graph?
"""

"""
The line chart shows very large spikes on a small number of days, which line up with Grammy event periods. Those peaks likely represent the awards ceremony and related media attention, because traffic is much higher than a normal day.

Outside of those spikes, traffic is much lower and more stable. This tells me the Grammy brand creates major short-term demand during event windows, while regular daily traffic is much more modest.
"""

"""
## Task 4

Let's investigate what an "average" day looks like when the awards show is being hosted versus the other 364 days out of the year.

**A.** Use the pandas `.groupby()` to calculate the number of visitors on the site based on the values in the column `awards_night`.
"""

awards_night_visitors = full_df.groupby('awards_night')['visitors'].mean()
awards_night_visitors


"""
On average, the website gets about **32,388** visitors on a regular day and about **1,389,590** visitors on an awards night. That means the awards ceremony brings in roughly **1.36 million more visitors** than a normal day.

This difference is huge and shows that awards night is the main traffic driver for the site. It is the moment when audience attention is highest, so it is an important opportunity for content, promotions, and engagement.
"""

"""
<span style='background-color: rgba(138, 43, 226, 0.4); padding: 0.2em 0.4em; border-radius: 4px;'>**Remark:** This is The Recording Academy's biggest challenge! How do you transform a business that relies on the success of **one** event per year into one that continues to bring users back on the site year round?</span>
"""

"""
## Task 5

When The Recording Academy decided to split their website into two domains, grammy.com and recordingacademy.com, the data capture for grammy.com was not affected. So the `full_df` variable needs to be split separately into two dataframes. The day the domains were switched is on `2022-02-01`.

Create two new dataframes:

1. `combined_site` for all dates before `2022-02-01`
2. `grammys` for all dates after (and including) `2022-02-01`
"""

# Split the data to separate the full_df into two new dataframes.
# One for before the switch of the websites and one for after.
split_date = '2022-02-01'

combined_site = full_df[full_df['date'] < split_date]
grammys = full_df[full_df['date'] >= split_date]


# Run the following cell - DO NOT MODIFY
# .copy() prevents pandas from printing a scary-looking warning message
combined_site = combined_site.copy()
grammys = grammys.copy()


# print the shape of the combined_site dataframe
combined_site.shape


"""
<span style='background-color: rgba(138, 43, 226, 0.4); padding: 0.2em 0.4em; border-radius: 4px;'>If done correctly, the `combined_site` dataframe should have a total of `1857` rows and `8` columns</span>
"""

"""
# Part II - It's all about KPIs

![](https://media.giphy.com/media/zoKdmndB8QBR2c0gjy/giphy.gif)

There are certain key performance indicators (KPIs) of interest for The Recording Academy. Let's investigate those a little more.
"""

"""
## Task 6

**A.** Create a new list called `frames` that has the `combined_site`, `rec_academy`, and `grammys` dataframes as entries. e.g. If the 3 dataframes were `df1`, `df2`, and `df3`, then the code would look like:

```python
frames = [df1, df2, df3]
```
"""

# create the list of dataframes
frames = [combined_site, rec_academy, grammys]


"""
**B.** For each frame in the frames list, create a new column `pages_per_session`. This new column is the average number of pageviews per session on a given day. The higher this number the more "stickiness" your website has with your visitors.

<span style='background-color: rgba(138, 43, 226, 0.4); padding: 0.2em 0.4em; border-radius: 4px;'>**Hint:** Divide the `pageviews` by `sessions`</span>

This can be achieved by using the following template:

```python
for frame in frames:
    frame['new_col'] = frame['col_A'] / frame['col_B']
```
"""

# create the `pages_per_session` column for all 3 dataframes.
for frame in frames:
    frame['pages_per_session'] = frame['pageviews'] / frame['sessions']


"""
**C.** Visualize this new metric using a line chart for each site. (You will have 3 separate graphs)
"""

# Combined Site graph
fig = px.line(
    combined_site,
    x='date',
    y='pages_per_session',
    title='Combined Site Pages Per Session',
    labels={'date': 'Date', 'pages_per_session': 'Pages Per Session'}
)
fig.show()


# Grammys graph
fig = px.line(
    grammys,
    x='date',
    y='pages_per_session',
    title='Grammys Pages Per Session',
    labels={'date': 'Date', 'pages_per_session': 'Pages Per Session'}
)
fig.show()


# Recording Academy graph
fig = px.line(
    rec_academy,
    x='date',
    y='pages_per_session',
    title='Recording Academy Pages Per Session',
    labels={'date': 'Date', 'pages_per_session': 'Pages Per Session'}
)
fig.show()


"""
The combined website generally has the lowest pages per session, while the separate websites perform better after the split. In particular, the **Recording Academy** site tends to have the strongest pages-per-session values, and the **Grammys** site is also above the old combined-site baseline most of the time.

This suggests the split likely improved how well each website serves its specific audience. When users land on a more focused website, they seem more likely to continue browsing instead of stopping after only one page.
"""

"""
*(Double-click this cell to write your answer)*
"""

"""
## Task 7

Bounce rate is another important metric for The Recording Academy. Bounce Rate is a measure of the percentage of visitors who come to the site and *never  interact with the website and leave*. In this task, you will define a function that takes in a dataframe as input and outputs the bounce rate.

**A.** Create a function called `bounce_rate` that:

1. Takes in a `dataframe` as input
2. adds up all of the values in the `bounced_sessions` column and stores in a variable called `sum_bounced`
3. adds up all of the values in the `sessions` column and stores it in a variable called `sum_sessions`
4. returns `100 * sum_bounced / sum_sessions`


<span style='background-color: rgba(138, 43, 226, 0.4); padding: 0.2em 0.4em; border-radius: 4px;'>**Hint:** You will need use the `.sum()` function both in the `sum_bounced` and `sum_sessions` calculations. Don't forget to multiply by `100` so that the answer appears as a percentage instead of a decimal.</span>
"""

def bounce_rate(dataframe):
    '''
    Calculates the bounce rate for visitors on the website.
    input: dataframe with bounced_sessions and sessions columns
    output: bounce rate as a percentage
    '''
    sum_bounced = dataframe['bounced_sessions'].sum()
    sum_sessions = dataframe['sessions'].sum()
    return 100 * sum_bounced / sum_sessions


"""
**B.** Use the `frames` variable from Task 6 to loop over each website (represented by a dataframe) to calculate the bounce rate. Print the bounce rate for each site.

A template for getting the function to work will look like code below. Remember that this is NOT the print statement, you will still need to add that part.

<span style='background-color: rgba(138, 43, 226, 0.4); padding: 0.2em 0.4em; border-radius: 4px;'>**Hint:** To get the bounce rate use `bounce_rate(frame)` </span>

```python
for frame in frames:
    my_value = my_function(frame)
```

<span style='background-color: rgba(138, 43, 226, 0.4); padding: 0.2em 0.4em; border-radius: 4px;'>**Tip:** If you want to reduce the number of decimals shown in an f-string, you can add `:0.2f` just before the end of the curly brackets but after your variable. Example: `print(f'my value is: {my_value:0.2f}')`</span>
"""

# Calculate the Bounce Rate for each site. Use the frames list you created in Task 6.
site_names = ['Combined Site', 'Recording Academy', 'Grammys']

for site_name, frame in zip(site_names, frames):
    rate = bounce_rate(frame)
    print(f'{site_name} bounce rate: {rate:0.2f}%')


"""
<span style='background-color: rgba(138, 43, 226, 0.4); padding: 0.2em 0.4em; border-radius: 4px;'>If done correctly, the `combined_site` and `grammys` site will each have bounce rates in the low 40s. The `rec_academy` will have a bounce rate in the low 30s</span>
"""

"""
**C.** Another useful metric is how long on average visitors are staying on the website.

Calculate the `mean` of the `avg_session_duration_secs` for each of the sites.
Print each one using an f-string.
"""

# Calculate the average of the avg_session_duration_secs. Use the frames list you created in Task 6.
for site_name, frame in zip(site_names, frames):
    avg_duration = frame['avg_session_duration_secs'].mean()
    print(f'{site_name} average session duration: {avg_duration:0.2f} seconds')


"""
**D.** What can you say about these two metrics as it relates to each of the websites?

*(Double-click this cell to write your answer)*
"""

"""
# Part III - Demographics

![](https://media.giphy.com/media/GrUhLU9q3nyRG/giphy.gif)

Age demographics are a way to see which audience(s) your content is resonating with the most. This can inform marketing campaigns, ads, and much more.

Let's investigate the demographics for the two websites. This will require reading in two new files and joining them in python.
"""

"""
## Task 8

The `grammys_age_demographics.csv` and `tra_age_demographics.csv` each contain the following information:

- **age_group** - The age group range. e.g. `18-24` are all visitors between the ages of 18 to 24 who come to the site.
- **pct_visitors** - The percentage of all of the websites visitors that come from that specific age group.
"""

"""
**A.** Read in the `grammys_age_demographics.csv` and `tra_age_demographics.csv` files and store them into dataframes named `age_grammys` and `age_tra`, respectively.
"""

# read in the files
age_grammys = pd.read_csv('grammys_age_demographics.csv')
age_tra = pd.read_csv('tra_age_demographics.csv')


# preview the age_grammys file. the age_tra will look very similar.
age_grammys.head()


"""
**B.** For each dataframe, create a new column called `website` whose value is the name of the website.
e.g. the `age_grammys` values for `website` should all be `Grammys` and for the `age_tra` they should be `Recording Academy`.
"""

# create the website column
age_grammys['website'] = 'Grammys'
age_tra['website'] = 'Recording Academy'


"""
**C.** use the `pd.concat()` method to join these two datasets together. Store the result into a new variable called `age_df`

<span style='background-color: rgba(138, 43, 226, 0.4); padding: 0.2em 0.4em; border-radius: 4px;'>**Hint:** Remember that you need to put your dataframe variables inside of a **list** first then pass that as your input of `pd.concat()`</span>
"""

# use pd.concat to join the two datasets
age_df = pd.concat([age_grammys, age_tra], ignore_index=True)
age_df


"""
<span style='background-color: rgba(138, 43, 226, 0.4); padding: 0.2em 0.4em; border-radius: 4px;'>If done correctly your new dataframe will have `12` rows and `3` columns.</span>
"""

"""
**D.** Create a bar chart of the `age_group` and `pct_visitors`. This chart should have, for each age group, one color for the Recording Academy and a different color for the Grammys.

<span style='background-color: rgba(138, 43, 226, 0.4); padding: 0.2em 0.4em; border-radius: 4px;'>**Hint:** You will need to use the `barmode='group'` option in `px.bar()`. See the code snippet below to guide you.</span>

```python
# template for visualization
px.bar(dataframe, x='variable1', y='variable2', color='variable3', barmode='group')
```
"""

# Create bar chart
fig = px.bar(
    age_df,
    x='age_group',
    y='pct_visitors',
    color='website',
    barmode='group',
    title='Age Demographics by Website',
    labels={'age_group': 'Age Group', 'pct_visitors': 'Percent of Visitors'}
)
fig.show()


"""
**E.** Looking at the chart above, what can you say about how the age demographics differ between the two websites?
"""

"""
Both websites attract a relatively young audience, with the largest shares coming from the **18–24** and **25–34** age groups. That means the strongest audience for both brands is concentrated under age 35.

The Grammys site appears to skew slightly younger, while the Recording Academy site has a slightly stronger share in some of the older age brackets and in the 25–34 group. Overall, the audiences are similar, but the split still makes sense because the Grammys audience looks a bit more event- and entertainment-focused.
"""

"""
# Part IV - Recommendation
![](https://media.giphy.com/media/0Av9l0VIc01y1isrDw/giphy.gif)
"""

"""
Based on this analysis, I would recommend that the two websites **stay separate**. After the split, the websites appear to perform better on engagement-related metrics than the old combined site. Both the Grammys and Recording Academy sites show stronger pages per session than the combined site, which suggests that users are finding more relevant content and moving through the site more effectively. This is a good sign that the separate domains create a clearer experience for different visitor needs.

The KPI results also support this recommendation. The **Recording Academy** site has the strongest engagement overall, with the **highest pages per session**, the **lowest bounce rate**, and the **longest average session duration**. The **Grammys** site does not perform as strongly on every KPI, but it still benefits from being focused on the Grammy brand and event-driven traffic. The very large traffic spikes on awards night show that the Grammys audience behaves differently from the broader Recording Academy audience, so keeping the sites separate allows each one to serve its own purpose.

From a business and user experience perspective, separate websites make the most sense. The Grammys site can stay centered on entertainment, event coverage, and fans, while the Recording Academy site can focus more on industry information, advocacy, and organization-related content. Even though their age demographics are somewhat similar, their traffic patterns and engagement behavior show enough difference to justify maintaining two distinct web experiences.
"""

"""
# LevelUp
![](https://media.giphy.com/media/6fUIhrlrHCzEHvY8oF/giphy.gif)
"""

"""
Ray and Harvey are both interested to see how the Grammys.com website compares to that of their main music award competitor, The American Music Awards (AMA). The dashboard below is aggregated information about the performace of The AMA website for the months of April, May, and June of 2023.

Your task is to determine how the Grammys website is performing relative to The AMA website. In particular, you will be looking at the device distribution and total visits over the same time span and leveraging information about Visit Duration, Bounce Rate, and Pages / Visit from your work in the core of this project.
"""

"""
![](figs/TheAMAs.png)
"""

"""
Let's review some of the content from above.

The **Total Visits** column is the total number of visitors on the website during the timespan given.
The **Device Distribution** is the percentage share of visitors coming from Desktop users (PCs, Macs, etc.) and Mobile Users (iPhone, Android, etc.).

Visitors on the AMA website are spending on average, 5 mins and 53 seconds on the site and viewing 2.74 pages per visit (aka session). They have a bounce rate of 54.31%
"""

"""
**A.** Load in the two files. The `desktop_users.csv` and `mobile_users.csv` files contain the users coming from desktop users and mobile users respectively.

Store them in variables named `desktop_users` and `mobile_users`
"""

# Load in the data
desktop_users = pd.read_csv('desktop_users.csv')
mobile_users = pd.read_csv('mobile_users.csv')

desktop_users['date'] = pd.to_datetime(desktop_users['date'])
mobile_users['date'] = pd.to_datetime(mobile_users['date'])


# preview the desktop_users file
desktop_users.head()


# preview mobile_users file
mobile_users.head()


"""
As you can imagine, you will be joining the two datasets together! But before you do that, you will modify the column names so that it's easier to use.

**B.** For each dataframe, change the name of the `visitors` column so that it says which category they come from. For example, the `desktop_users` dataframe should have a column named `desktop_visitors` instead of `visitors`.

Additionally, drop the `segment` column since it is no longer needed.
"""

# change name of the visitors column to indicate which category it comes from
desktop_users = desktop_users.rename(columns={'visitors': 'desktop_visitors'})
mobile_users = mobile_users.rename(columns={'visitors': 'mobile_visitors'})


# drop the segment column from each dataframe
desktop_users = desktop_users.drop(columns='segment')
mobile_users = mobile_users.drop(columns='segment')


"""
**C.** Join the two dataframes together in a new variable called `segment_df`.
"""

# join the two dataframes and preview the dataframe
segment_df = pd.merge(desktop_users, mobile_users, on='date')
segment_df.head()


"""
**D.** In the next few steps, you will calculate the percentage share of users coming from desktop and mobile on the Grammys website.

Calculate a new column, `total_visitors` that is the addition of `desktop_visitors` and `mobile_visitors`.
"""

# create total_visitors column
segment_df['total_visitors'] = segment_df['desktop_visitors'] + segment_df['mobile_visitors']
segment_df.head()


"""
To calculate the percentage share you will first need to filter the data to dates after (and including) `2023-04-01`. Then calculate the `sum` of desktop visitors and total visitors and divide those values. The percentage share of mobile visitors will be the value needed to get to 100%.
"""

# filter and calculate the percentage share
filtered_segment_df = segment_df[segment_df['date'] >= '2023-04-01']

desktop_total = filtered_segment_df['desktop_visitors'].sum()
mobile_total = filtered_segment_df['mobile_visitors'].sum()
total_visitors = filtered_segment_df['total_visitors'].sum()

desktop_share = 100 * desktop_total / total_visitors
mobile_share = 100 * mobile_total / total_visitors

print(f'Desktop share: {desktop_share:0.2f}%')
print(f'Mobile share: {mobile_share:0.2f}%')
print(f'Total visitors: {total_visitors:,}')


"""
From April 2023 through May 2023, the Grammys website traffic was about **31.84% desktop** and **68.16% mobile**. During that same period, the site had a total of **1,428,482 visitors**.

This shows that mobile is the dominant traffic source for the Grammys website. Any future improvements to the user experience should heavily prioritize mobile design, mobile page speed, and mobile engagement.
"""

"""
Compared with the AMA benchmark, the Grammys website is doing well in a few areas but still has room to improve. A clear strength is that the site has strong total traffic during major event periods and a mobile-heavy audience, which is a good sign for broad consumer reach. The site also appears capable of generating major bursts of attention around the awards show, which is something many brands would want.

At the same time, the Grammys site underperforms the AMA benchmark on several engagement KPIs. The AMA dashboard reports **5 minutes 53 seconds** average visit duration, **2.74 pages per visit**, and a **54.31% bounce rate**. For the Grammys site, average session duration is only about **83 seconds** and pages per session is around **2.14**, which suggests users are not going as deep into the site. Its bounce rate is lower than AMA's, which is positive, but the session depth and time on site still need improvement. The main opportunity for the Grammys is to keep users engaged longer once they arrive, especially on mobile devices.
"""
