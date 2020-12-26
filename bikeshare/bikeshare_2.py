#import dataframes time, pandas, numpy
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#display the filtering questions and get user inputs
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington).  Using a while loop to handle invalid inputs
    while True:
        try:
            city = input("Would you like to see the data for chicago, new york city or washington?\n").lower().strip()
            if city in ['chicago','new york city','washington'] :
                break
            else:
                print("Sorry, your input should be: chicago new york city or washington")

        except ValueError:
            print("Sorry, your input is wrong")
            continue

    #get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Which Month (all, january, february, march, april, may, june)?\n").lower().strip()
            if month in ['january', 'february', 'march', 'april', 'may', 'june','all'] :
                break
            else:
                print("Sorry, Which month do you mean january, february, march, april, may, june or all")

        except ValueError:
            print("Sorry, your input is wrong")
            continue


    #get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Which day? (all, sunday, monday, tuesday, wedensday, thuesday, saturday)\n").lower().strip()
            if day in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'] :
                break
            else:
                print("Sorry, Which day do you mean sunday, monday, tuesday, wedensday, thuesday, saturday or all ")

        except ValueError:
            print("Sorry, your input is wrong")
            continue


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
    #load data file to the dataframe
    df = pd.read_csv(CITY_DATA[city])
    #convert the start time from str to time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #create new columnes for (month,day and hour)
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = month.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    popular_month = df['month'].mode()[0]
    print('What is the most popular month for traveling?\n', popular_month)

    # display the most common day of week
    popular_day_of_week = df['day'].mode()[0]
    print('What is the most popular day for traveling?\n', popular_day_of_week)

    # display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print('What is the most popular hour of the day to start your travels?\n', popular_start_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('What is the most popular start station?\n', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('What is the most popular end station?\n', popular_end_station)

    # display most frequent combination of start station and end station trip
    startend=df.groupby(['Start Station','End Station'])
    popular_startend_station = startend.size().sort_values(ascending=False).head(1)
    print('Below are the most popular start and end station respectively\n', popular_startend_station)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #  display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('What was the total traveling time done?\n', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('What is the average total travel time?\n', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    type_counts=df['User Type'].value_counts()
    print('What is the count of the users by the type?\n',type_counts)


    # Display counts of gender
    try:
     gender_counts=df['Gender'].value_counts()
     print('What is the count of the users by the gender?\n',gender_counts)

    # Display earliest, most recent, and most common year of birth
     most_common_year = df['Birth Year'].mode()[0]
     recent = df['Birth Year'].max()
     earliest = df['Birth Year'].min()
     print('What is the earliest, most recent, and most popular year of birth respectively?\n')
     print('The most recent:',recent,'\nThe earliest:', earliest,'\nThe most popular year of the birth:', most_common_year)

    except:
        pass

            # Display counts of genderhis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#display 5 lines of raw data
def raw_data(df):
    """ display upon request by the user if they want to see 5 lines of raw data, display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'."""

    start_loc=0
    preview = input('\nWould you like to view 5 rows of raw data? Enter yes or no.\n').lower().strip()
    while(preview == 'yes'):
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5
            to_continue=input('Would you like to view more?\n').lower().strip()
            if to_continue != 'yes':
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

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
