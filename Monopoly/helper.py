import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(games, scores1, scores2):
    
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    #plt.plot(score2)
    plt.plot(games)
    plt.plot(scores1)
    plt.plot(scores2)
    
    plt.ylim(ymin=0)
    plt.text(len(games)-1, games[-1], str(games[-1]))
    plt.text(len(scores1)-1, scores1[-1], str(scores1[-1]))
    plt.text(len(scores2)-1, scores2[-1], str(scores2[-1]))
    plt.show(block=False)
    plt.pause(.1)
