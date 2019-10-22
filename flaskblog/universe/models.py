import sqlalchemy as db
import pandas as pd
from flaskblog.universe.utils import DateRangeManager
from flaskblog.universe import nlp, get_query_params

# mapping table names


class QueryMapper:
    def __init__(self):
        self.date_range = DateRangeManager()
        self.today = self.date_range.today_string
        self.engine = db.create_engine(
            'postgresql://rash:<ronalto>;@localhost:5432/universe')
        self.connection = self.engine.connect()
        self.df_daily = pd.read_sql_table(
            'daily_sales', con=self.engine, index_col="Date", parse_dates={'Date': "DD-MM-YY"})
        self.table_name = ''

    def get_results(self, input_string):
        input_string = str(input_string.lower())
        doc = nlp(input_string)

        query_params = get_query_params(doc)

        if query_params['table_name'] != 'Error':
            self.table_name = self.get_table_name(query_params['table_name'])
            return self.get_date_range(query_params['date_range'])
        elif query_params['table_name'] == 'Error':
            return query_params['result']

    def get_table_name(self, table_name):
        return {
            'COST': 'Net Purchase',
            'REVENUE': 'Gross Sales',
            'PROFIT': 'Margin',
            'CASH_FLOW': 'cash_flow'
        }.get(table_name, None)

    def query_today(self):
        date = self.today

        return self.df_daily[str(date)][['Day_Name', self.table_name]]

    def query_yesterday(self):
        date = self.date_range.previous_day

        return self.df_daily[str(date)][['Day_Name', self.table_name]]

    def query_last_week(self):
        start, end = self.date_range.last_week()

        return self.df_daily[str(start):str(end)][['Day_Name', self.table_name]]

    def query_last_month(self):
        year, month = self.date_range.last_month()

        return self.df_daily[f"{str(year)}-{str(month)}"][['Day_Name', self.table_name]]

    def query_last_year(self):
        year = self.date_range.last_year()

        return self.df_daily[str(year)][['Day_Name', self.table_name]]

    def get_date_range(self, period):

        return {
            'TODAY': self.query_today(),
            'YESTERDAY': self.query_yesterday(),
            'LAST_WEEK': self.query_last_week(),
            'LAST_MONTH': self.query_last_month(),
            'LAST_YEAR': self.query_last_year(),
            'TOMORROW': ('tomorrow'),
            'NEXT_WEEK': ('next_year'),
            'NEXT_MONTH': ('next_month'),
            '': self.query_today()
        }.get(period, None)
