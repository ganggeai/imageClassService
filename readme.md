# simple imageClassService demo by flask with keras VesNet50 based on tensorflow

## API document:

### API Name:status

#### Fuction:test connection to  the service and get the service version with timeStamp
#### url:http://domainName:5000/status 
#### Method:only GET 
#### Arguments:None
#### Return:Formate:json, Exmaple:{"timeStamp":"2020-04-01 12:00:00","version":"1.0"}

### API Name:predict

#### Fuction:post the image to let the service to predict the name of something
#### url:http://domainName:5000/predict
#### Method:only POST 
#### Arguments:an image File
#### Return:Format:json
####        Exmaple:{"result":"[(u'n02504013', u'Indian_elephant', 0.82658225), (u'n01871265', u'tusker', 0.1122357), (u'n02504458', u'African_elephant', 0.061040461)]"}