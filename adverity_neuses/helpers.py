from _datetime import datetime
import sys


def getTimestampString():
    """

    :return: A Timestamp as String in a specified format
    """
    return str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ": "

def xprint(*args, **kwargs):
    """
    :param args: the text that is going to be printed
    :param kwargs:
    :return: the printed line with current timestamp prepended
    """
    print( getTimestampString() +" ".join(map(str,args)), **kwargs)



def CalculateSMA(n, timestamps, values):
    """

    :param n: moving average across n timestamps
    :param timestamps: the x- values
    :param values: the y vales
    :return: returns a two dimensional list which represents the moving average. the format is designed to fit the visualization library
        I am aware that this function is not optimized but it gets the job done. You could also rely on df.rolling(window=n).mean() for more performance.
    """
    data = []
    if len(timestamps) <= n+1:
        return []
    for ts in timestamps[-(len(timestamps) - 1 - n):]:
        base_index = timestamps.index(ts)
        value = 0
        sum = 0
        for k in range(n):
            sum = sum + values[base_index - 1 - k]
            value = sum / n
        data.append([ts, value])
    return data

