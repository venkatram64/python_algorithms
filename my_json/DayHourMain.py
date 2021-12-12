from datetime import date, datetime, timedelta

def processDayAndTime():
    '''
    In this method source and target were built
    :return: combined source and target path
    '''
    baseDate="2021-09-01"
    dtObject = datetime.strptime(baseDate, "%Y-%m-%d")
    print("Start Date: ", dtObject)
    sourceAndTargetLoationArr = []
    for x in range(1, 5):
        startDate = (dtObject - timedelta(x)).strftime('%Y/%m/%d')
        print("Day is ", startDate)
        for h in range(0, 5):
            try:
                splittedDate = startDate.split("/")
                year = splittedDate[0]
                month = splittedDate[1]
                day = splittedDate[2]

                if h < 10:
                    prefix = '/0'
                else:
                    prefix = '/'
                print("Hour is ", str(h))

                sourceFilePath = 'dbfs:/mnt/xxxx/1.0/' + startDate + prefix + str(h)
                targetFilePath = 's3://someDir/mystore/myFile/1.0/' + startDate + prefix + str(h)
                sourceAndTargetLocation = sourceFilePath +'::'+ targetFilePath
                sourceAndTargetLoationArr.append(sourceAndTargetLocation)
            except Exception as ex:
                print('Error: ', ex)

    return sourceAndTargetLoationArr


def mainProcess():
    '''
    This is the main method to start the process
    :return:
    '''
    totalPaths = processDayAndTime()
    for i in range(len(totalPaths)):
        completePath = totalPaths[i]
        cpath = completePath.split('::')
        sourcePath = cpath[0]
        targetPath = cpath[1]
        print('Source Path: ', sourcePath)
        print('Target Path: ',targetPath)
        '''
        real process starts from here
        '''



'''
This main method to test on my pycharm, this is not needed in your code
'''
if __name__ == '__main__':
    mainProcess()