import time
from AbbyyOnlineSdk import AbbyyOnlineSdk, ProcessingSettings

class OCR(AbbyyOnlineSdk):
    ApplicationId = "EZOrderOCR"
    Password = "dVfPhA5AXHFcAmzSDsWps+xh"

_ocr = None
def get_ocr():
    global _ocr
    if not _ocr:
        _ocr = OCR()
    return _ocr

class OCRSettings(ProcessingSettings):
    Profile = "documentConversion"
    OutputFormat = "txt" # rtf,xml

def ocr_image(path):
    processor = get_ocr()
    task = processor.ProcessImage(path, OCRSettings)
    assert task is not None
    while task.IsActive() == True :
        time.sleep(2)
        task = processor.GetTaskStatus(task)
    assert task.Status == "Completed"
    assert task.DownloadUrl != None
    f = processor.GetResultFile( task )
    return f.read()

if __name__ == '__main__':
    import sys
    _, path = sys.argv
    print ocr_image(open(path, 'rb'))
