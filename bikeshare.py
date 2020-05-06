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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('Would you like to see data from chicago, new york city or washington?    \n')
    while city not in ('chicago', 'new york city','washington'):
        print('Please enter a correct city name    \n')
        city = input('Would you like to see data from chicago, new york city or washington?    \n')
        
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('Which month would you like to see data from? Please choose january, february, march, april, may, june or all         \n')
    while month not in ( 'january','february','march','april','may','june','all'):
        print('Please enter a correct month    \n')
        month=input('Which month would you like to see data from? Please choose january, february, march, april, may, june or all         \n')
              
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Which day of the week would you like to see data from? Please write your response as an integer. Example.     Monday = 1, Tuesday = 2, Wednesday = 3...or all   \n' )
    while day not in ("1", '2', '3', '4', '5', '6', '7'):
        print('Pleae enter a correct day of week from 1 to 7, Monday to Sunday.\n')
        day= input('Which day of the week would you like to see data from? Please write your response as an integer.               Example: Monday = 1, Tuesday = 2, Wednesday = 3...and so on\n' )
      

    print('-'*40)
    print (city, month, day)
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
    print(df.head())
    print(df.columns)
     
    
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    print(df['month'].head())
    
    df['day_of_week'] = df['Start Time'].dt.day
    print(df['day_of_week'].head())
    
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
       
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    start_time = time.time()
    
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    print(df['month'].head())
    popular_month = df['month'].value_counts().idxmax()
    
    
    print('Most Common month:', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common day of week:', popular_day_of_week )

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    print("\nHour:")
   

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()
    print('The most common used start station is: ', most_common_start_station)
    
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()
    print('The most common used end station is: ', most_common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_finish = df.groupby(['Start Station''End Station']).size().idmax()
    print('The most frequent combination of start station and end station trip are: ', most_common_start_finish )
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print ('The total travel time is: ',total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean() 
    print ('The mean travel time is: ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].nunique()
    print('The count for different user types is: ', user_type)
    
    
    # TO DO: Display counts of gender
    if city == 'new york city' or 'chicago':
    
        counts_of_gender = df['Gender'].nunique()
        print('The count of gender is: ', counts_of_gender)
    
    
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'new york city' or 'chicago':
    
        df['Birth Year'] = pd.to_datetime(df['Birth Year'])
        least_recent_date = df['Birth Year'].min()
        recent_date = df['Birth Year'].max()
        most_common_date = df['Birth Year'].mode()
        print('The most recent date of Birth is: ',recent_date)
        print('The most common date of Birth is: ', most_common_date)

        
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
