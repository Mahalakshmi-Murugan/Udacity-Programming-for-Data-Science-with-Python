import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    print("Applied Filter >> {}".format(applied_filter))
    start_time = time.time()

    print('\n...Popular Station...')
    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    start_station_counts = df[df['Start Station'] == start_station].count()[0]
    print("Start Station:{}, Count:{}".format(start_station, start_station_counts))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    end_station_counts = df[df['End Station'] == end_station].count()[0]
    print("End Station:{}, Count:{}".format(end_station, end_station_counts))
    # print("Start Station:{}, Count:{} - End Station:{}, Count:{}, Filter:{}".format(start_station, start_station_counts, end_station, end_station_counts, applied_filter))

    print('\n...Popular Trip...')
    df['Trip combination'] = df['Start Station']+' - '+df['End Station']
    # print(df)
    # TO DO: display most frequent combination of start station and end station trip
    popular_trip_station = df['Trip combination'].mode()[0]
    popular_trip_station_counts = df[df['Trip combination'] == popular_trip_station].count()[0]
    print("Trip:({}, {}), Count:{}".format(popular_trip_station.split(" - ")[0], popular_trip_station.split(" - ")[1], popular_trip_station_counts))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    print("Applied Filter >> {}".format(applied_filter))
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_counts = df['Trip Duration'].count()
    avg_travel_time = df['Trip Duration'].mean()
    print("Total Duration:{}, Count:{}, Average Duration:{}".format(total_travel_time.round(2), total_travel_counts, avg_travel_time.round(2)))

    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    print("Applied Filter >> {}".format(applied_filter))
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n...User Types...')
    subscriber_counts = df[df['User Type'] == 'Subscriber'].count()[0]
    customer_counts = df[df['User Type'] == 'Customer'].count()[0]
    print("Subscribers:{}, Customers:{}".format(subscriber_counts, customer_counts))

    # TO DO: Display counts of gender
    try:
      print('\n...Gender...')
      male_counts = df[df['Gender'] == 'Male'].count()[0]
      female_counts = df[df['Gender'] == 'Female'].count()[0]
      print("Male:{}, Female:{}".format(male_counts, female_counts))
    except KeyError:
      print("!!! The city you've selected doesn't have Gender data !!!")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      print('\n...Birth Year...')
      earliest_birth_year = int(df['Birth Year'].min())
      recent_birth_year = int(df['Birth Year'].max())
      common_birth_year = int(df['Birth Year'].mode()[0])
      print("Earliest:{}, Most Recent:{}, Most Common:{}".format(earliest_birth_year, recent_birth_year, common_birth_year))
    except KeyError:
      print("!!! The city you've selected doesn't have Birth Year data !!!")
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
