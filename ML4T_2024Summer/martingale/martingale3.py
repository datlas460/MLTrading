""""""  		  	   		 	   			  		 			 	 	 		 		 	
"""Assess a betting strategy.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Template code for CS 4646/7646  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
and other users of this template code are advised not to share it with others  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   			  		 			 	 	 		 		 	
GT honor code violation.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
-----do not edit anything above this line---  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Student Name: Srihari Datla  		  	   		 	   			  		 			 	 	 		 		 	
GT User ID: sdatla8  		  	   		 	   			  		 			 	 	 		 		 	
GT ID: 903647808  		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def author():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    :return: The GT username of the student  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: str  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    return "sdatla8"  # replace tb34 with your Georgia Tech username.
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def gtid():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    :return: The GT ID of the student  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: int  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    return 903647808  # replace with your GT ID number
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def get_spin_result(win_prob):  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    :param win_prob: The probability of winning  		  	   		 	   			  		 			 	 	 		 		 	
    :type win_prob: float  		  	   		 	   			  		 			 	 	 		 		 	
    :return: The result of the spin.  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: bool  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    result = False  		  	   		 	   			  		 			 	 	 		 		 	
    if np.random.random() <= win_prob:  		  	   		 	   			  		 			 	 	 		 		 	
        result = True  		  	   		 	   			  		 			 	 	 		 		 	
    return result  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
def test_code():  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    Method to test your code  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    win_prob = 0.47  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once  		  	   		 	   			  		 			 	 	 		 		 	
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		 	   			  		 			 	 	 		 		 	
    # add your code here to implement the experiments

    fig1(win_prob)
    fig2(win_prob)
    fig3(win_prob)
    fig4(win_prob)
    fig5(win_prob)


def episode(win_prob):
    episode_winnings = 0
    count = 1
    winnings = pd.DataFrame(index = range(1), columns=range(1000))
    #print(winnings)
    winnings.loc[0, 0] = 0
    #winnings.rename(index={0:'1'}, inplace=True)
    while episode_winnings < 80:
        won = False
        bet_amount = 1
        while not won:
            won = get_spin_result(win_prob)
            if won == True:
                episode_winnings += bet_amount
            else:
                episode_winnings -= bet_amount
                bet_amount = bet_amount*2
            winnings.loc[0, count] = episode_winnings
            count += 1
    while count < 1000:
        winnings.loc[0, count] = episode_winnings
        count += 1
    #rint(winnings)
    return winnings

def episode2(win_prob):
    episode_winnings = 0
    count = 1
    winnings = pd.DataFrame(index = range(1), columns=range(1000))
    #print(winnings)
    winnings.loc[0, 0] = 0
    #winnings.rename(index={0:'1'}, inplace=True)
    while episode_winnings < 80 and episode_winnings > -256:
        won = False
        bet_amount = 1
        while not won:
            won = get_spin_result(win_prob)
            if won == True:
                episode_winnings += bet_amount
            else:
                episode_winnings -= bet_amount
                bet_amount = bet_amount*2
                if -256 >  episode_winnings-bet_amount:
                    bet_amount= -256-episode_winnings

            winnings.loc[0, count] = episode_winnings
            count += 1
    while count < 1000:
        winnings.loc[0, count] = episode_winnings
        count += 1
    #rint(winnings)
    return winnings

def fig1(win_prob):
    a = episode(win_prob)
    #print('FIRST CALC')
    #a = a.transpose()
    #a.plot()
    count= 1
    #plotting = a.plot(title='Martingale', label = 'Attempt 1')
    for i in range(9):
        b = episode(win_prob)
        #print(f'CALC NUMBER {count}')
        count+=1
        #b = b.transpose()
        #b.plot(label= f'Attempt {i+1}', plotting=plotting)
        #a = pd.concat([a,b[0]], axis = 1, ignore_index=True)
        a = pd.concat([a,b] , ignore_index=True)


    meanA = pd.Series(a.mean(axis=0))
    #a = pd.concat([a,meanA] , ignore_index=True)
    # plotting.set_xlabel('Tries')
    # plotting.set_ylabel('Winnings')
    # plotting.legend(loc='upper left')

    #print(a)
    a = a.transpose()
    #a['Mean'] = meanA
    #print('added')
    #print(a)
    #meanA = meanA.transpose()
    #print(meanA)
    ax = a.plot()
    ax.set_xlabel('Tries')
    ax.set_ylabel('Winnings')
    ax.legend(loc='lower left')
    ax.set_title('Figure 1')
    plt.xlim(0, 300)
    plt.ylim(-256,100)
    plt.savefig('images/figure1.png')

    #meanA.plot(label='Mean', ax=ax)
    #plt.show()

def fig2(win_prob):
    a = episode(win_prob)
    #print('FIRST CALC')
    #a = a.transpose()
    #a.plot()
    count= 1
    #plotting = a.plot(title='Martingale', label = 'Attempt 1')
    for i in range(999):
        b = episode(win_prob)
        #print(f'CALC NUMBER {count}')
        count+=1
        #b = b.transpose()
        #b.plot(label= f'Attempt {i+1}', plotting=plotting)
        #a = pd.concat([a,b[0]], axis = 1, ignore_index=True)
        a = pd.concat([a,b] , ignore_index=True)


    meanA = pd.Series(a.mean(axis=0))
    stdA = pd.Series(a.std(axis=0))
    upper = meanA + stdA
    lower = meanA - stdA
    #a = pd.concat([a,meanA] , ignore_index=True)
    # plotting.set_xlabel('Tries')
    # plotting.set_ylabel('Winnings')
    # plotting.legend(loc='upper left')

    #print(a)
    a = a.transpose()
    a['Mean'] = meanA
    a['Upper']= upper
    a['Lower'] = lower
    #print('added')
    #print(a)
    #meanA = meanA.transpose()
    #print(meanA)
    # ax = a['Mean'].plot()
    #
    # ax.set_xlabel('Tries')
    # ax.set_ylabel('Winnings')
    # ax.legend(loc='lower left')
    # ax.set_title('MonteCarlo Figure 2')
    plt.plot(a['Mean'])
    plt.plot(a['Upper'])
    plt.plot(a['Lower'])
    plt.xlim(0, 300)
    plt.ylim(-256,100)
    plt.title('Figure 2- Mean and Std Deviation')
    plt.savefig('images/figure2.png')

    #meanA.plot(label='Mean', ax=ax)
    #plt.show()

def fig3(win_prob):
    a = episode(win_prob)
    #print('FIRST CALC')
    #a = a.transpose()
    #a.plot()
    count= 1
    #plotting = a.plot(title='Martingale', label = 'Attempt 1')
    for i in range(999):
        b = episode(win_prob)
        #print(f'CALC NUMBER {count}')
        count+=1
        #b = b.transpose()
        #b.plot(label= f'Attempt {i+1}', plotting=plotting)
        #a = pd.concat([a,b[0]], axis = 1, ignore_index=True)
        a = pd.concat([a,b] , ignore_index=True)


    medA = pd.Series(a.median(axis=0))
    stdA = pd.Series(a.std(axis=0))
    upper = medA + stdA
    lower = medA - stdA
    #a = pd.concat([a,meanA] , ignore_index=True)
    # plotting.set_xlabel('Tries')
    # plotting.set_ylabel('Winnings')
    # plotting.legend(loc='upper left')

    #print(a)
    a = a.transpose()
    a['Median'] = medA
    a['Upper']= upper
    a['Lower'] = lower
    #print('added')
    #print(a)
    #meanA = meanA.transpose()
    #print(meanA)
    # ax = a['Mean'].plot()
    #
    # ax.set_xlabel('Tries')
    # ax.set_ylabel('Winnings')
    # ax.legend(loc='lower left')
    # ax.set_title('MonteCarlo Figure 2')
    plt.plot(a['Median'])
    plt.plot(a['Upper'])
    plt.plot(a['Lower'])
    plt.title('Figure 3- Median and Std Deviation')
    plt.xlim(0, 300)
    plt.ylim(-256,100)
    plt.savefig('images/figure3.png')

    #meanA.plot(label='Mean', ax=ax)
    #plt.show()

def fig4(win_prob):
    a = episode2(win_prob)
    #print('FIRST CALC')
    #a = a.transpose()
    #a.plot()
    count= 1
    #plotting = a.plot(title='Martingale', label = 'Attempt 1')
    for i in range(999):
        b = episode2(win_prob)
        #print(f'CALC NUMBER {count}')
        count+=1
        #b = b.transpose()
        #b.plot(label= f'Attempt {i+1}', plotting=plotting)
        #a = pd.concat([a,b[0]], axis = 1, ignore_index=True)
        a = pd.concat([a,b] , ignore_index=True)


    meanA = pd.Series(a.mean(axis=0))
    stdA = pd.Series(a.std(axis=0))
    upper = meanA + stdA
    lower = meanA - stdA
    #a = pd.concat([a,meanA] , ignore_index=True)
    # plotting.set_xlabel('Tries')
    # plotting.set_ylabel('Winnings')
    # plotting.legend(loc='upper left')

    #print(a)
    a = a.transpose()
    a['Mean'] = meanA
    a['Upper']= upper
    a['Lower'] = lower
    #print('added')
    #print(a)
    #meanA = meanA.transpose()
    #print(meanA)
    # ax = a['Mean'].plot()
    #
    # ax.set_xlabel('Tries')
    # ax.set_ylabel('Winnings')
    # ax.legend(loc='lower left')
    # ax.set_title('MonteCarlo Figure 2')
    plt.plot(a['Mean'])
    plt.plot(a['Upper'])
    plt.plot(a['Lower'])
    plt.title('Figure 4- Mean and Std Deviation')
    plt.xlim(0, 300)
    plt.ylim(-256,100)
    plt.savefig('images/figure4.png')

    #meanA.plot(label='Mean', ax=ax)
    #plt.show()

def fig5(win_prob):
    a = episode2(win_prob)
    #print('FIRST CALC')
    #a = a.transpose()
    #a.plot()
    count= 1
    #plotting = a.plot(title='Martingale', label = 'Attempt 1')
    for i in range(999):
        b = episode2(win_prob)
        #print(f'CALC NUMBER {count}')
        count+=1
        #b = b.transpose()
        #b.plot(label= f'Attempt {i+1}', plotting=plotting)
        #a = pd.concat([a,b[0]], axis = 1, ignore_index=True)
        a = pd.concat([a,b] , ignore_index=True)


    medA = pd.Series(a.median(axis=0))
    stdA = pd.Series(a.std(axis=0))
    upper = medA + stdA
    lower = medA - stdA
    #a = pd.concat([a,meanA] , ignore_index=True)
    # plotting.set_xlabel('Tries')
    # plotting.set_ylabel('Winnings')
    # plotting.legend(loc='upper left')

    #print(a)
    a = a.transpose()
    a['Median'] = medA
    a['Upper']= upper
    a['Lower'] = lower
    #print('added')
    #print(a)
    #meanA = meanA.transpose()
    #print(meanA)
    # ax = a['Mean'].plot()
    #
    # ax.set_xlabel('Tries')
    # ax.set_ylabel('Winnings')
    # ax.legend(loc='lower left')
    # ax.set_title('MonteCarlo Figure 2')
    plt.plot(a['Median'])
    plt.plot(a['Upper'])
    plt.plot(a['Lower'])
    plt.title('Figure 5- Mean and Std Deviation')
    plt.xlim(0, 300)
    plt.ylim(-256,100)
    plt.savefig('images/figure5.png')

    #meanA.plot(label='Mean', ax=ax)
    #plt.show()


  		  	   		 	   			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		 	   			  		 			 	 	 		 		 	
    test_code()  		  	   		 	   			  		 			 	 	 		 		 	
