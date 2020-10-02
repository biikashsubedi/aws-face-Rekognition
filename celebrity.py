import boto3
import json

# Change photo to the path and filename of your image.
photo = 'rock.jpg'
client = boto3.client('rekognition')
with open(photo, 'rb') as image:
    response = client.recognize_celebrities(Image={'Bytes': image.read()})

# print(response)
print('Detected faces for ' + photo)

for celebrity in response['CelebrityFaces']:
    print('Name: ' + celebrity['Name'])
    print('Id: ' + celebrity['Id'])
    print('Position:')
    print('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
    print('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
    print('Info')

    for url in celebrity['Urls']:
        print('   ' + url)
