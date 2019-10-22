from datetime import timedelta, date, datetime
from dateutil.relativedelta import relativedelta
from datetimerange import DateTimeRange


# DateRangeManager
class DateRangeManager:
    def __init__(self):
        self.today = datetime.today()
        self.previous_day_date = self.today - timedelta(days=1)
        self.today_string = self.today.strftime(
            "%Y-%m-%d").replace('2019', '2018')
        self.previous_day = self.previous_day_date.strftime(
            "%Y-%m-%d").replace('2019', '2018')
        self.days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Function to covert string to datetime
    def string_to_date(self, date_time):
        format = '%Y-%m-%d'
        datetime_str = datetime.strptime(date_time, format)
        return datetime_str

    # last week
    def last_week(self):
        # refactoring to be done due to the year
        current_date = self.string_to_date(self.today_string)
        today_index = self.days.index(current_date.strftime("%a"))
        start_date = (current_date - (timedelta(8 + today_index))
                      ).strftime('%Y-%m-%d')
        end_date = (current_date - (timedelta(7 + today_index - 5))
                    ).strftime('%Y-%m-%d')

        return start_date, end_date

    # last month
    def last_month(self):
        # refactoring to be done due to the year
        current_date = self.string_to_date(self.today_string)
        month_int = (current_date - relativedelta(months=1)).strftime("%m")
        year_int = (current_date - relativedelta(months=1)).strftime("%Y")
        return year_int, month_int

    # last year
    def last_year(self):
        # refactoring to be done due to the year
        current_date = self.string_to_date(self.today_string)
        year_int = int((current_date - relativedelta(years=1)).strftime('%Y'))
        return year_int
