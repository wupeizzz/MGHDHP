import datetime
import string
import hdhp
import notebook_helpers
import seaborn as sns

vocabulary = ['word' + str(i) for i in range(100)]  # the `words` of our documents
doc_min_length = 5
doc_length = 10
words_per_pattern = 50

alpha_0 = (2.5, 0.75)
mu_0 = (2, 0.5)
omega = 3.5

num_patterns = 10

process = hdhp.HDHProcess(num_patterns=num_patterns, alpha_0=alpha_0,
                          mu_0=mu_0, vocabulary=vocabulary,
                          omega=omega, words_per_pattern=words_per_pattern,
                          random_state=12)

overlap = notebook_helpers.compute_pattern_overlap(process)
sns.distplot(overlap, kde=True, norm_hist=True, axlabel='Content overlap')

process.reset()  # removes any previously generated data
for i in range(10):
    _= process.sample_user_events(min_num_events=100,
                                  max_num_events=5000,
                                  t_max=365)
print ('Total #events', len(process.events))

print (process.user_patterns_set(user=0))
print (process.user_pattern_history_str(user=0, patterns=[0, 1],show_time=True))
print (process.pattern_content_str(patterns=[0, 1],
                                  show_words=10))

start_date = datetime.datetime(2015, 9, 15)
fig = process.plot(start_date=start_date, user_limit=5,
                   num_samples=5000, time_unit='days',
                   label_every=1, seed=5)
process.show()


