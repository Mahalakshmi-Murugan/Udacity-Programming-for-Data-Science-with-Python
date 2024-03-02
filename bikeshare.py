import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
applied_filter = None

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    city_list = ['chicago', 'new york city', 'washington']
    while city not in city_list:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        global applied_filter
        applied_filter = "City:" + city.title() + "   "

        if city not in city_list:
          print("Invalid option!!! Please enter the valid option.\n")

    filter_option = None
    filter_list = ['month', 'day', 'both', 'none', 'not at all']
    while filter_option not in filter_list:
        filter_option = input("Would you like to filter the data by month, day, both or not at all? Type “none” for no time filter.\n").lower()
        if city not in city_list:
          print("Invalid option!!! Please enter the valid option.\n")
    month_filter_flag = False
    day_filter_flag = False
    if filter_option == 'both':
      month_filter_flag = True
      day_filter_flag = True
    elif filter_option == 'month':
      month_filter_flag = True
    elif filter_option == 'day':
      day_filter_flag = True

    # TO DO: get user input for month (all, january, february, ... , june)
    month = None
    if (month_filter_flag):
      month_list = ['all','january', 'february', 'march', 'april', 'may', 'june']
      while month not in month_list:
        month = input("Which month? All, January, February, March, April, May or June\n").lower()
        applied_filter += ("Month:" + month.title() + "   ")
        if month not in month_list:
          print("Invalid option!!! Please enter the valid option.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    if (day_filter_flag):
      day_list = ['all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
      while day not in day_list:
        day = input("Which day? All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday\n").lower()
        applied_filter += ("Day:" + day.title())
        if day not in day_list:
          print("Invalid option!!! Please enter the valid option.\n")

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
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of week'] = df['Start Time'].dt.day_name()
    df['Start hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all' and month != None:
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = (months.index(month) + 1)

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all' and day != None:
        # filter by day of week to create the new dataframe
        df = df[df['Day of week'] == day.title()]
    # print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    print("Applied Filter >> {}".format(applied_filter))
    start_time = time.time()

    print('\n...Popular Trip Timings...')
    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_trip_month = df['Month'].mode()[0]
    common_trip_month_count = df[df['Month']==common_trip_month].count()[0]
    print("Most Common Month:{}, Count:{}".format(months[common_trip_month-1].title(), common_trip_month_count))

    # TO DO: display the most common day of week
    common_trip_day = df['Day of week'].mode()[0]
    common_trip_day_count = df[df['Day of week']==common_trip_day].count()[0]
    print("Most Common Day:{}, Count:{}".format(common_trip_day, common_trip_day_count))

    # TO DO: display the most common start hour
    common_trip_hour = df['Start hour'].mode()[0]
    common_trip_hour_count = df[df['Start hour']==common_trip_hour].count()[0]
    print("Most Common Hour:{}, Count:{}".format(common_trip_hour, common_trip_hour_count))

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


def individual_trip_data(df):
    total_records_count = df.count()[0]
    record_count = 0
    next_page_flag = True
    while next_page_flag != False and record_count < total_records_count:
      individual_record = input('\nWould you like to view individual trip data? Type ‘yes’ or ‘no’.\n')
      if individual_record.lower() == 'yes':
        print(df[record_count:(record_count+5)])
        record_count +=5
      else:
        next_page_flag = False


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        individual_trip_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
