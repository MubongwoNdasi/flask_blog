# here is my dictionary of words
def data_dictionary():
    data_dictionary = {
        'today': ['today', 'this day', 'this very day', 'before tomorrow', 'this morning',
                  'this afternoon', 'this evening', 'this moment', 'time being', 'now', 'recent', 'this week'],

        'yesterday': ['yesterday', 'last day', 'lang syne', 'recently', 'not long ago',
                      'the other day', 'foretime', 'previous day', 'yesterday morning',
                      'yesterday afternoon', 'yesterday evening', 'past day'],

        'last_week': ['last week', 'past week', 'previous week', 'for a week', 'for the past week', 'one week ago'],

        'last_month': ['last month', 'past one month', 'last one month', 'month ago', 'one month ago', 'previous month', 'month old', 'for a month', 'past month'],

        'last_year': ['last year', 'past year', 'this past year', 'previous year',
                      'year ago', 'senior year', 'one year ago', 'ayear', 'year earlier'],

        'next_month': ['next month', 'a month', 'in one month', 'following month', 'for the next month', 'within a month', 'coming month',
                       'for a month', 'upcoming month', 'about a month', 'month from now',
                       'one month later', 'by next month'],

        'tomorrow': ['tomorrow', 'by-and-by', 'the following day', 'future', 'futurity', 'hereafter', 'offing', 'morrow', 'time to come', 'time ahead', 'what lies ahead', 'coming times', 'subsequent time', 'aftertime', 'afterward', 'fullness of time', 'life to come', 'world to come'],

        'next_week': ['the coming week', 'the following week', 'the week coming'],

        'cost': ['cost', 'price', 'charge', 'fee', 'rate', 'amount', 'bill', 'figure', 'tariff', 'value', 'expenditure', 'expense', 'fare', 'quotation', 'spend', 'assessment', 'damage', 'dues' 'estimate', 'expenses', 'freight', 'levy', 'outlay', 'payment', 'retail', 'score', 'setback', 'sum', 'valuation', 'appraisal', 'appraisement', 'bounty', 'budget', 'demand', 'duty', 'ransom', 'rental', 'squeeze', 'monetary value', 'price tag', 'selling price', 'market price', 'payment required', 'face value', 'hire charge', 'arm and a leg'],

        'revenue': ['sales', 'revenues', 'sale', 'revenue', 'income', 'incomings', 'produce', 'enrichment', 'acquirement', 'annuity', 'fruits', 'fund', 'funds', 'current funds', 'handle', 'payoff', 'perquisite', 'salary', 'stock', 'strength', 'take', 'turnover', 'wages', 'bottom line'],

        'profit': ['profit', 'returns', 'return', 'reward', 'rewards', 'yield', 'yields', 'interest', 'gain', 'profits', 'earning', 'earnings', 'surplus', 'remuneration', 'boot', 'excess', 'gains', 'killing', 'lucre', 'payback', 'percentage', 'emolument', 'emoluments', 'gross', 'takings', 'winnings', 'accumulation', 'acquisition', 'harvest', 'output', 'outturn', 'production', 'turnout', 'net profit', 'operating profit', 'gross profit', 'financial gain', 'pay dirt'],

        'cash_flow': ['cash flow', 'cash-flow', 'cash_flow', 'capital', 'means', 'available means', 'available resources', 'pecuniary resources', 'stock in trade', 'capital goods', 'assets', 'available funds', 'black-ink items', 'capitalization', 'financial resources', 'liquid assets', 'means of production', 'pluses', 'producer goods', 'balance', 'estate and effects', 'net worth', 'resources', 'total assets', 'wherewithal', 'worth']
    }
    return data_dictionary


# list of pipe names
def pipes():
    pipes = ["today", "yesterday", "last_week", "last_month", "last_year",
             "tomorrow", "next_week", "next_month", "revenue", "cost", "profit", "cash_flow"]
    return pipes

# ('pipe_name', 'pipe_label')


def pipeline_dict():
    pipeline_dict = {
        'today': 'TODAY',
        'yesterday': 'YESTERDAY',
        'last_week': 'LAST_WEEK',
        'last_month': 'LAST_MONTH',
        'last_year': 'LAST_YEAR',
        'tomorrow': 'TOMORROW',
        'next_week': 'NEXT_WEEK',
        'next_month': 'NEXT_MONTH',
        'revenue': 'REVENUE',
        'cost': 'COST',
        'profit': 'PROFIT',
        'cash_flow': 'CASH_FLOW'
    }
    return pipeline_dict


def TABLE_NAMES():
    TABLE_NAMES = ['COST', 'REVENUE', 'PROFIT', 'CASH_FLOW']
    return TABLE_NAMES


def DATE_RANGES():
    DATE_RANGES = ['TODAY', 'YEATERDAY', 'LAST_WEEK', 'LAST_MONTH',
                   'LAST_YEAR', 'TOMORROW', 'NEXT_WEEK', 'NEXT_MONTH']
    return DATE_RANGES
