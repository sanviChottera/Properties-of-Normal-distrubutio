import pandas as pandas
import seaborn as sb




#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation
second_std_deviation_start, second_std_deviation_end = mean- (2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean(3*std_deviation), mean+(3*std_deviation)
#Platform the chart and lines for mean 1 standard deviation and 2 standard deviation


thin_1_std_deviation = [result for result in data if results > first_std_deviation_start and result < first_std_deviation_end ]
thin_2_std_deviation = [result for result in data if results > second_std_deviation_start and result < second_std_deviation_end ]
thin_3_std_deviation = [result for result in data if results > third_std_deviation_start and result < third_std_deviation_end ]