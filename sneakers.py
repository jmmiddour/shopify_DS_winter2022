"""
Program to provide analyst on the provided dataset of sneaker shops, and
    some of their order details.

Analysis was done in the `Joanne_Middour_Winter2022_Intern_Challenge.ipynb`
    notebook in this repository prior to creating this program to clean
    the data, remove extreme outliers, and provide an answer to the
    business question posed in the instructions of this challenge.
"""

# imports
import pandas as pd


# Load in the data from locally downloaded copy of the Google Sheet file from
#   url = https://docs.google.com/spreadsheets/d/16i38oonuX1y1g7C_UAmiK9GkY7cS-64DfiDMNiR41LM/edit?usp=sharing
orders = pd.read_csv(
    '2019_Winter_Data_Science_Intern_Challenge_Data_Set_Sheet1.csv'
)


"""
Based on my analysis done in the notebook in this repository:
    - Some of the values in the original dataset are obviously inaccurately inputted
    - Found that the average price for some of those outliers came to $25,725 per sneaker
"""


def clean_data(df, int_col, dt_col, col, max_val, min_val=0):
    """
    This function will change the given column(s) in the dataframe
        to the proper data type. Also, cleans outliers in the provided
        dataset about sneaker shops.

    :parameter
        **df**      : *dataframe* : data needing to be cleaned

        **int_col** : *str, list* : Column(s) needing to be typed as integers

        **dt_col**  : *str, list* : Column(s) needing to be typed as datetime

        **col**     : *str*       : name of column used to removed outliers

        **max_val** : *int*       : maximum value to remain in the DataFrame

        **min_val** : *int*       : (default=0) minimum value to remain

    :returns
        **df** : *dataframe* : cleaned data with major outliers removed
    """
    # Change all integer columns to int data types
    for i in int_col:
        df[i] = pd.to_numeric(df[i])

    # Change all datetime columns to datetime data types
    df[dt_col] = pd.to_datetime(df[dt_col])

    # Add a new column with the price per sneaker in the order
    for i in df:
        df['price_per_item'] = df['order_amount'] / df['total_items']

    # Remove extreme outliers
    df = df[df[col].between(min_val, max_val)]

    return df


# Create a list of the columns that need to be changed to integers
int_cols = ['order_id', 'shop_id', 'user_id', 'order_amount', 'total_items']

# Use my function to make sure all columns are typed properly
orders = clean_data(orders, int_cols, 'created_at', 'order_amount', 1000, 0)


def print_stats(df, title):
    """
    Function to print out statistical metrics of the given DataFrame to help
        better visualize the analysis of the data.

    Parameters
    ----------
        df    : Dataframe : dataframe with the data needing statistics from
        title : string    : title of the print out in a string format

    Returns
    -------
        Printed out report of statistics for the given DataFrame
    """
    return f"""
    {title}
    ------------------------------------------------------------
        Total Number of Observations:      {df.shape[0]}
    ------------------------------------------------------------      
        Statistics on Total Items Purchased:

            Total of Number of Items Sold:  {df.total_items.sum():,.0f}
            Total Number of Unique Values:  {df.total_items.nunique():,.0f}
            Maximum Number of Items Sold:   {df.total_items.max():,.0f}
            Minimum Number of Items Sold:   {df.total_items.min():,.0f}
            Average Number of Items Sold:   {df.total_items.mean():,.0f}
            Median Number of Items Sold:    {df.total_items.median():,.0f}
            Standard Deviation:             {df.total_items.std():,.0f}
            25th Percentile:                {df.total_items.quantile(.25):,.0f}
            75th Percentile:                {df.total_items.quantile(.75):,.0f}
    ------------------------------------------------------------
        Statistics on Price per Item:

            Total Number of Unique Values:   {df.price_per_item.nunique():,.0f}
            Maximum Price per Item:         ${df.price_per_item.max():,.2f}
            Minimum Price per Item:         ${df.price_per_item.min():,.2f}
            Average Price per Item:         ${df.price_per_item.mean():,.2f}
            Median Price per Item:          ${df.price_per_item.median():,.2f}
            Standard Deviation:             ${df.price_per_item.std():,.2f}
            25th Percentile:                ${df.price_per_item.quantile(.25):,.2f}
            75th Percentile:                ${df.price_per_item.quantile(.75):,.2f}
    ------------------------------------------------------------      
        Statistics on Order Amounts:

            Total Amount of all Orders:     ${df.order_amount.sum():,.2f}
            Total Number of Unique Values:   {df.order_amount.nunique():,.0f}
            Maximum Value of Order:         ${df.order_amount.max():,.2f}
            Minimum Value of Order:         ${df.order_amount.min():,.2f}
            Average Order Value (AOV):      ${df.order_amount.mean():,.2f}
            Median Order Value:             ${df.order_amount.median():,.2f}
            Standard Deviation:             ${df.order_amount.std():,.2f}
            25th Percentile:                ${df.order_amount.quantile(.25):,.2f}
            75th Percentile:                ${df.order_amount.quantile(.75):,.2f}
    """


# Use the function above to print a report on the statistics of the cleaned data
print(print_stats(orders, 'Report on the Data from Sneaker Shop Orders'))
