import boto3
import base64
import json
import os

# AMAZON API CLIENT
rekognition_client = boto3.client('rekognition', region_name='us-east-1')
# PHOTO DIRECTORY
photo_name = 'rock.jpg'
file = open(photo_name, 'rb').read()

# USING DETECT_FACE API
response = rekognition_client.detect_faces(
    Image={
        'Bytes': file
    },
    Attributes=['ALL', ]
)

# PRINTING HEADER
print('=========================')
print('Details of ' + photo_name)
print('=========================')

# PHASING DATA AND USING ON OWN STYLE
for detail in response['FaceDetails']:
    # FOR MOUTH_OPEN
    mouth_open = str(detail['MouthOpen']['Value'])

    def change():
        if mouth_open == 'True':
            a = print('No')
        else:
            print('Yes')


# FORMATING ON JSON
data = {}
data['MouthOpen'] = {
    'Mouth Open': change()
}

# PRINTING OUTPUT ON CONSOLE
print(json.dumps(data, indent=2))

# SAVING DATA IN JSON FILE
out_file = open("myfile.json", "w")
json.dump(data, out_file, indent=2)
out_file.close()