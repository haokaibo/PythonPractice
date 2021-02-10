# name = 'Kaibo'
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()                   # Display the plot
import calendar
from datetime import datetime
class Common:
    @staticmethod
    def add_months(source_date: datetime, months):
        month = source_date.month - 1 + months
        year = source_date.year + month // 12
        month = month % 12 + 1
        day = min(source_date.day, calendar.monthrange(year, month)[1])
        return datetime(year, month, day)

    @staticmethod
    def get_sql_from_file(filename, params={}):
        # Open and read the file as a single buffer
        with open(filename, 'r') as reader:
            # Further file processing goes here
            sql_command = reader.read()

        return sql_command

month_interval = -2
end_datetime = datetime.now()
begin_datetime =datetime.strptime(Common.add_months(end_datetime, month_interval).strftime('%Y-%m-01'),'%Y-%m-%d') 
print(begin_datetime)

# %##