import pandas as pd
import time

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city='new york city'
month = 'all'
day_of_week = 'all'

def load_data(city,month,day_of_week):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #read in city data based on user input
    df = pd.read_csv(CITY_DATA[city])

    #extract month and day from Start time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour

    # Filter on month and day inputs
    if month != 'all' and day_of_week != 'all':
        df = df[(df['month'] == month) & (df['day'] == day_of_week)]
    elif month == 'all' and day_of_week != 'all':
        df = df[(df['day'] == day_of_week)]
    elif month != 'all' and day_of_week == 'all':
        df = df[(df['month'] == month)]
    else:
        df

    return df

df=load_data(city,month,day_of_week)

def time_stats(df_input):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month, common dow & common start hour
    popular_month = df['month'].mode()[0]
    popular_dow = df['day'].mode()[0]
    popular_start_hour = df['start_hour'].mode()[0]

    print('Most Popular Month:', popular_month)
    print('Most Popular Day of Week:', popular_dow)
    print('Most Popular start hour:', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

time_stats(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start_station=df.groupby('Start Station').size().reset_index(name='trip_counts').sort_values('trip_counts',ascending=False)['Start Station'].iloc[0]
    print('The most commonly used start station: {}'.format(pop_start_station))

    # display most commonly used end station
    pop_end_station=df.groupby('End Station').size().reset_index(name='trip_counts').sort_values('trip_counts',ascending=False)['End Station'].iloc[0]
    print('The most commonly used end station: {}'.format(pop_end_station))

    # display most frequent combination of start station and end station trip
    df['station_combo']=df['Start Station'] +" & " + df['End Station']
    pop_station_combo=df.groupby('station_combo').size().reset_index(name='trip_counts').sort_values('trip_counts',ascending=False)['station_combo'].iloc[0]
    print('The most common station combination: {}'.format(pop_station_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

station_stats(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time_sum = round(df['Trip Duration'].sum()/3600,2)
    print('The total time travelled was {} hours'.format(travel_time_sum))

    # display mean travel time
    travel_time_mean = round(df['Trip Duration'].mean()/3600,2)
    print('The average trip duration was {} hours'.format(travel_time_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
trip_duration_stats(df)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df.groupby('User Type').size().reset_index(name='trip_counts').sort_values('trip_counts',ascending=False)
    print('\nNumber of trips by each User Type:\n')
    print(user_type_counts)

    # Display counts of gender & Birth year for cities where data available
    if city in ['new york city','chicago']:
        gender_counts = df.groupby('Gender').size().reset_index(name='trip_counts').sort_values('trip_counts',ascending=False)
        print('\nNumber of trips by each Gender:\n')
        print(gender_counts)
        #calculate yob data
        latest_yob = int(df['Birth Year'].sort_values(ascending = False).iloc[0])
        earliest_yob = int(df['Birth Year'].sort_values(ascending = True).iloc[0])
        common_yob = int(df.groupby('Birth Year').size().reset_index(name='yob_counts').sort_values('yob_counts',ascending=False)['Birth Year'].iloc[0])

        print('\nThe most recent birth year: {}'.format(latest_yob))
        print('The earliest birth year: {}'.format(earliest_yob))
        print('The most common birth year: {}'.format(common_yob))

    else:
        print('\nNo gender or birth year data available for {}'.format(city.title()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

user_stats(df,city)
