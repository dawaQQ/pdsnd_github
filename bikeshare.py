import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington).
    city_list = ['chicago', 'new york city', 'washington']
    month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']              
    
    while True:
        city = input('\nWould you like to see data for Chicago, New York City or Washington: ').lower()
        if city in city_list:
            break
        else:
            print('\nPlease enter a valid city!')
                     
        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nPlease enter a specific month (January, February, ... , June). Otherwise tye "all" for all months: ').lower()
        if month in month_list:
            break
        else:
            print('\nPlease enter a valid month or type "all" for all months!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nPlease enter a specific day (Monday, Tuesday, ... Sunday). Type "all" for all days: ').lower()
        if day in day_list:
            break
        else: 
            print('\nPlease enter a valid day or type "all" for all days!')
   
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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day of week and start hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    # new column start station to end station
    df['startend'] = df['Start Station'] + ' to ' + df['End Station']

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print('The most common month is: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print('The most common day of week is: ', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['start_hour'].value_counts().idxmax()
    print('The most common start hour is: ', most_common_hour)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frq_combination = df['startend'].value_counts().idxmax()
    print('The most frequent combination of start station and end station is: ', most_frq_combination)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ', total_travel_time)

    # TO DO: display mean travel time
    total_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: ', total_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: \n', user_types)
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].dropna()
        gender = df['Gender'].value_counts()
        print('Counts of gender: \n', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        df['Birth Year'] = df['Birth Year'].dropna()
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].value_counts().idxmax()
        print('Year of birth: The earliest year of birth is {}, the most recent year of birth is {} and the most common year of birth is {}'.format(earliest, most_recent, most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df):
    """Displays resulting raw data."""
    
    answer = input('\nWould you like to see 5 lines of raw data? Enter yes or no: ').lower()
    line = 0
    while True:
        if answer == 'yes':
            print(df.iloc[line:line + 5])
            morelines = input('\nWould you like to see 5 more lines of raw data? Enter yes or no: ').lower()
            line += 5
            if morelines != 'yes':
                break
        else:
            break
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
