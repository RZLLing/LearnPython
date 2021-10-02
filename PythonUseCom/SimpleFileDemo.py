import win32api, win32file, win32con
import os

def SimpleFileDemo():
    testName = os.path.join(win32api.GetTempPath(),"win32file_demo_test_file")
    if os.path.exists(testName): os.unlink(testName)
    handle = win32file.CreateFile(testName,win32file.GENERIC_WRITE,0,None,win32con.CREATE_NEW,0,None)
    test_Data = "Hello\0there".encode("ascii")
    win32file.WriteFile(handle,test_Data)
    handle.close()

    handle = win32file.CreateFile(testName,win32file.GENERIC_READ,0,None,win32con.OPEN_EXISTING,0,None)
    rc, data = win32file.ReadFile(handle,1024)
    handle.close()
    if data == test_Data:
        print( "successfully wrote and read a file" )
    else:
        raise Exception("Got different data back??")

    os.unlink(testName)


if __name__ == '__main__':
    SimpleFileDemo();