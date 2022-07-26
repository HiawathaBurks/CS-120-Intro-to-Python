import matplotlib.pyplot as plt

def drawLineChart():
    file = open('1994_Weekly_Gas_Averages.txt')
    dataInput = file.read()
    gasValue = dataInput.split()
    file.close()
    for x in range(0,len(gasValue)):
        gasValue[x] = float(gasValue[x].strip())
    xCoords = list(range(1,53))
    plt.plot(xCoords,gasValue)
    plt.xlim([1,52])
    plt.title('1994 Weekly Gas Prices')
    plt.xlabel('Week')
    plt.ylabel('Price')
    plt.show()

drawLineChart()
