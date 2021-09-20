#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = CITY_DATA.keys()

months =['january','february','march','april','may','june','all']

days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city you want to analyze?\n1. Chicago \n2. New York City\n3. Washington')
        city = city.lower()
    
        if city in cities:
            print('\nSo you chose {}!\n'.format(city.title()))
            break
        else:
            print('\nInvalid input. Please check that you are writing one of the three cities.\n')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        
        month=input('Do you want to specify a month? Type one from the first six months, If not type "all".\n1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. All')
        month=month.lower()
        
        if month in months:
            print('\nSo you chose {}!\n'.format(month.title())) 
            break
        else:
             print('\nInvalid input. Please check that you are writing the right answer.\n')
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Do you want to specify a day? Type the day name, If not type "all"')
        day = day.lower()
        
        if day in days:
            print('\nSo you chose {}!'.format(day.title()))
            break
        else:
            print('\nInvalid input. Please check that you are writing the right answer.\n')


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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.day_name()
     
    if month != 'all':
        
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]
             

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe most common month is {}'.format(df['month'].mode()[0]))
               
    # TO DO: display the most common day of week
    print('\nThe most common day is {}'.format(df['day_of_week'].mode()[0]))
                  

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('\nThe most common start hour is {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\n The most commonly used start station is {}'.format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print('\n The most commonly end start station is {}'.format(df['End Station'].mode()[0]))              


    # TO DO: display most frequent combination of start station and end station trip
    df['comb. of start and end stations'] = df['Start Station'] + " to " + df['End Station']
    print('\n The most frequent combination of start station and end station trip is: {}'.format(df['comb. of start and end stations'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is {}\n'.format(np.sum(df['Trip Duration'])))              

    # TO DO: display mean travel time
    print('Mean travel time is {}\n'.format(np.mean(df['Trip Duration'])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

   
    # TO DO: Display counts of gender
    if city != 'washington':
        
        print(df['Gender'].value_counts())
        
    # TO DO: Display earliest, most recent, and most common year of birth
    
        print('\nThe earliest year of birth is {}\n'.format(df['Birth Year'].min()))
        print('\nThe most recent year of birth is {}\n'.format(df['Birth Year'].max()))              
        print('\nThe most common year of birth is {}\n'.format(df['Birth Year'].mode()[0]))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data.lower() =='yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
	
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
	display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

            
if __name__ == "__main__":
	main()          


# In[ ]:




