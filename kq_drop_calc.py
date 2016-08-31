


print """\n********README FIRST*******
This module takes the drop rates of 3 drops and presents the probability of receiving
at least one of those drops after N kills.\nA drop rate of the form 1/x is assumed.
Simply enter a number for 'x'\n"""

item1 = raw_input('First Item Name: ')
rate_item1 = int(raw_input('Drop Rate of {}: '.format(item1)))

item2 = raw_input('Second Item Name: ')
rate_item2 = int(raw_input('Drop Rate of {}: '.format(item2)))

item3 = raw_input('Third Item Name: ')
rate_item3 = int(raw_input('Drop Rate of {}: '.format(item3)))

numKills = int(raw_input('Number of Kills: '))

probRecItem = lambda rate, numKills: float(1) - pow((float(1) - float(1)/float(rate)), numKills)

probItem1 = probRecItem(rate_item1, numKills)
probItem2 = probRecItem(rate_item2, numKills)
probItem3 = probRecItem(rate_item3, numKills)

# P(A U B U C) = P(A) + P(B) + P(C) - P(A ^ B) - P(B ^ C) - P(A ^ C) + P(A ^ B ^ C)
probAtLeastOne = probItem1 + probItem2 + probItem3 -\
                 (probItem1 * probItem2) - (probItem2 * probItem3) -\
                 (probItem1 * probItem3) + (probItem1 * probItem2 * probItem3)
print 'A={}\nB={}\nC={}\n'.format(item1, item2, item3)
print('Probability P(A u B u C)={}\n\n'.format(round(probAtLeastOne*100, 2)))
print """Thanks for using the script! Any feedback/suggestions for improvement
is/are greatly appreciated!\n\n"""