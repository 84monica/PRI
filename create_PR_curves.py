import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay


recall_values = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

precision_values_Q8 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.75, 0.75]

precision_values_Q7_enhanced_synonyms = [1.0, 0.9, 0.9, 0.75, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666]

precision_values_Q7_base = [1.0, 0.9, 0.9, 0.75, 0.6792452830188679, 0.6792452830188679, 0.6792452830188679, 0.6792452830188679, 0.6792452830188679, 0.6792452830188679, 0.6779661016949152]

precision_values_Q6_base_enhanced = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

precision_values_Q6_synonyms = [1.0, 1.0, 0.75, 0.5454545454545454, 0.5454545454545454, 0.5333333333333333, 0.5, 0.4666666666666667, 0.4666666666666667, 0.4666666666666667, 0.4666666666666667]

precision_values_Q3 = [1.0, 0.9411764705882353, 0.8787878787878788, 0.8787878787878788, 0.8787878787878788, 0.8787878787878788, 0.8787878787878788, 0.8787878787878788, 0.8787878787878788, 0.8787878787878788, 0.8787878787878788]

precision_values_Q5 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.9166666666666666, 0.9166666666666666, 0.9166666666666666]


fig, ax = plt.subplots()
disp = PrecisionRecallDisplay(precision_values_Q8, recall_values)
disp.plot(ax=ax, name="All models")
fig.savefig('images/PR_Curve_Q8.png')

fig, ax = plt.subplots()
disp = PrecisionRecallDisplay(precision_values_Q7_base, recall_values)
disp.plot(ax=ax, name="Base Model")
disp2 = PrecisionRecallDisplay(precision_values_Q7_enhanced_synonyms, recall_values)
disp2.plot(ax=ax, name="Enhanced and Synonyms Models")
ax.legend()
fig.savefig('images/PR_Curve_Q7.png')

fig, ax = plt.subplots()
disp = PrecisionRecallDisplay(precision_values_Q6_base_enhanced, recall_values)
disp.plot(ax=ax, name="Base and Enhanced Models")
disp2 = PrecisionRecallDisplay(precision_values_Q6_synonyms, recall_values)
disp2.plot(ax=ax, name="Synonyms Models")
fig.savefig('images/PR_Curve_Q6.png')

fig, ax = plt.subplots()
disp = PrecisionRecallDisplay(precision_values_Q3, recall_values)
disp.plot(ax=ax, name="Query 3")
disp2 = PrecisionRecallDisplay(precision_values_Q5, recall_values)
disp2.plot(ax=ax, name="Query 5")
fig.savefig('images/PR_Curve_Old_Queries.png')
