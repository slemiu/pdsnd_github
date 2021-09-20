#!/usr/bin/env python
# coding: utf-8

# In[21]:


do not import time
import pandas as pd
import numpy as np

CITY_DATA=CITY_DATA={'Chicago': 'chicago.csv', 'New York City':'new_york_city.csv','Washington':'washington.csv'}
city_list=list(CITY_DATA.keys())
month_list=['January','February','March', 'April', 'May', 'June']
day_list=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello there! For this session, I would like to show you what I did with US bikeshare data. Let's go!")

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('\nPlease type one of these cities, Chicago, New York City or Washington ').title()
    while city not in city_list:
        print('Please check your city spelling and try again!')
        city = input('Please type one of these cities, Chicago, New York or Washington ').title()
    print('You have selected', city)

    # get user input for month

    month = input('\nPlease type a month from January to June or type "All Months" for all the months ').title()
    if month=='All Months' and month not in month_list:
        print('You wish to have data for "All Months"' )
    elif month != 'All Months' and month not in month_list:
        print('Please check your month spelling and try again!')
        month = input('Please type a month from January to June or type "All Months" for all the months ').title()
    else:
        print('You wish to have data for', month)

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('\nPlease type a day from Monday to Sunday or type "All Days" for all the days in the week ').title()
    if day=='All Days' and day not in day_list:
        print('You wish to have data for "All Days"' )
    elif day != 'All Days' and day not in day_list:
        print('Please check your day spelling and try again!')
        day = input('Please type a day from Monday to Sunday or type "All Days" for all the days in the week ').title()
    else:
        print('You wish to have data for', day)

    print('\nYou have selected ', city.title() +','+' ' + month.title() +' ' + 'and' +' '+ day.title() +' '+ 'in your filter. Fantastic!')
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'All Months':
        month = month_list.index(month) + 1
        df=df[df['month']==month]
    if day != 'All Days':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nLet's get some data on most common times people travel \n")
    start_time = time.time()

     # display the most common month

    print('\nWhat month was most frequently used for bike travelling?')
    pop_month = df['month'].mode()[0]
    freq_month=month_list[(pop_month-1)].title()
    print('The month with the highest number of bike travellers is: ', freq_month)

    # display the most common day of week

    print('\nOn what day of the week do we have the most bike travellers?')
    freq_day=df['day_of_week'].mode()[0]
    print('The day of the week with the highest number of bike travellers is: ', freq_day)

    # display the most common start hour

    print('\nFinally, at what hour of the day do we have the most bike travellers?')
    df['hour'] = df['Start Time'].dt.hour
    freq_hour = df['hour'].mode()[0]
    print('The hour of the day with the highest number of bike travellers is: ', str(freq_hour) +':'+'00'+' '+'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nLet's get some data  on the most Popular stations and Trip")

    start_time = time.time()

    # display most commonly used start station

    freq_start = df['Start Station'].mode()[0]
    print('\nThe most commonly used Start Station by travellers is: ', freq_start)

    # display most commonly used end station

    freq_end = df['End Station'].mode()[0]
    print('The most commonly used End Station by travellers is: ', freq_end)

    # display most frequent combination of start station and end station trip

    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    freq_combination = df['combination'].mode()[0]
    print('Travellers most commonly used a combination of these stations: ', freq_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nLet's get some data on trip duration. ")
    start_time = time.time()

    # display total travel time
    sum_travel = df['Trip Duration'].sum()
    sum_travel_hours=sum_travel//3600
    print('\nFor the period selected, total duration of travel using bikeshare in seconds is:', sum_travel)
    print('In hours, this is just over: ', str(sum_travel_hours)+' '+'hours')

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    mean_time=mean_time//1
    mean_time_min=mean_time//60
    print('For the period selected, average duration of a bikeshare trip in seconds is approximately:', mean_time)
    print('In minutes, this is approximately: ',str(mean_time_min)+' '+'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("Let's get some statistics on persons who use bikeshare ")
    start_time = time.time()

    # Display counts of user types

    print('\nHow many customers and subscribers used bikeshare during the period selected?')
    users = df['User Type'].value_counts()
    print('\nThe data reveals the following number of subscribers and customers:\n',users)

    # Display counts of gender

    print('\nWhat is the male:female distribution of subscribers for the period selected?')
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('\nThe male:female distribution is:\n',gender)
    else:
        print('\nThere is no gender information in this city.')

    # Display earliest, most recent, and most common year of birth

    print('\nLets see some statistics on the birth year of subscribers')
    if 'Birth_Year' in df:
        earliest_year = df['Birth_Year'].min()
        print('The oldest subscriber was born in: ', earliest_yeat)
        most_recent_year = df['Birth_Year'].max()
        print(most_recent_year)
        common_birth_year = df['Birth Year'].mode()
        print('The most common year of birth is:',common_birth_year)
    else:
        print('\nThere is no birth year information in this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data (df):
    """Displays raw data and prints r rows."""
    raw_data=input('\nIf you would like to see the data behind the figures please type yes if not type no ').title()
    if raw_data!='Yes':
        print('\nYou have opted not to see additional data')
    elif raw_data=='Yes':
        print('\nYou chose "Yes". Fantastic! Let us print the first 5 rows. Here we go!\n')
        row=0
        while raw_data == 'Yes':
            print(df.head(row+5))
            row+=5
            new_row=input('\nWould you like to see 5 more rows? Please type yes if you do or no if you do not. \n ').title()
            if new_row != 'Yes':
                print('\nYou have opted not to see additional data')
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nThat is all for this session. Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('\nYou have ended this session. Good bye!')
            break
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:
