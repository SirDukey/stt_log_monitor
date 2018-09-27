import subprocess as sp
from datetime import datetime, timedelta

def getLogTime():
    log = sp.Popen(['grep', 'Elapsed', '/var/log/stt/attempt_recognition.log'], stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = log.communicate()
    output = output.decode('utf-8')
    error = error.decode('utf-8')

    if output:
        listA = output.split('\n')
        itemA = listA[-2]
        listB = itemA.split(' ')
        itemB = listB[0]
        itemB = itemB.strip('[')
        itemB = itemB.strip(']')
        return itemB[10:]        

    elif error:
        return error


if __name__ == '__main__':
    
    wall_time = datetime.now()
    delta = timedelta(hours=1)
    time_diff = wall_time - delta
    one_hour_ago = time_diff.strftime('%Y-%m-%d_%H_%M_%S')
    log_time = getLogTime()
    if log_time >= one_hour_ago:
        print(1)
    else:
        print(0)
