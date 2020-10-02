import boto3
import base64
import json
import os

# AMAZON API CLIENT
rekognition_client = boto3.client('rekognition', region_name='us-east-1')
# PHOTO DIRECTORY
photo_name = 'girl_smile.jpeg'
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
    # FOR AGE
    age = str(detail['AgeRange']['Low']) + ' to ' + str(detail['AgeRange']['High'])
    # FOR GENDER
    gender = str(detail['Gender']['Value'])
    # FOR EMOTION
    emotion_0 = str(detail['Emotions'][0]['Type'])
    emotion_0_con = str(int((detail['Emotions'][0]['Confidence'] * 100) + 0.5) / 100.0) + '%'
    emotion_1 = str(detail['Emotions'][1]['Type'])
    emotion_1_con = str(int((detail['Emotions'][1]['Confidence'] * 100) + 0.5) / 100.0) + '%'
    emotion_2 = str(detail['Emotions'][2]['Type'])
    emotion_2_con = str(int((detail['Emotions'][2]['Confidence'] * 100) + 0.5) / 100.0) + '%'
    emotion_3 = str(detail['Emotions'][3]['Type'])
    emotion_3_con = str(int((detail['Emotions'][3]['Confidence'] * 100) + 0.5) / 100.0) + '%'
    emotion_4 = str(detail['Emotions'][4]['Type'])
    emotion_4_con = str(int((detail['Emotions'][4]['Confidence'] * 100) + 0.5) / 100.0) + '%'
    emotion_5 = str(detail['Emotions'][5]['Type'])
    emotion_5_con = str(int((detail['Emotions'][5]['Confidence'] * 100) + 0.5) / 100.0) + '%'
    emotion_6 = str(detail['Emotions'][6]['Type'])
    emotion_6_con = str(int((detail['Emotions'][6]['Confidence'] * 100) + 0.5) / 100.0) + '%'
    emotion_7 = str(detail['Emotions'][7]['Type'])
    emotion_7_con = str(int((detail['Emotions'][7]['Confidence'] * 100) + 0.5) / 100.0) + '%'
    # FOR SUNGLASS
    sunglass = str(detail['Sunglasses']['Value'])
    # FOR MUSTACHE
    mustache = str(detail['Mustache']['Value'])
    # FOR SMILE
    smile = str(detail['Smile']['Value'])
    # FOR BEARD
    beard = str(detail['Beard']['Value'])
    # FOR MOUTH_OPEN
    mouth_open = str(detail['MouthOpen']['Value'])


    # FORMATING ON JSON
    data = {}
    data['AgeRange'] = {
        'Age Between': age,
    }
    data['Gender'] = {
        'Gender': gender
    }
    data['Emotions'] = {
        emotion_0: emotion_0_con,
        emotion_1: emotion_1_con,
        emotion_2: emotion_2_con,
        emotion_3: emotion_3_con,
        emotion_4: emotion_4_con,
        emotion_5: emotion_5_con,
        emotion_6: emotion_6_con,
        emotion_7: emotion_7_con
    }
    data['Sunglasses'] = {
        'Sunglass': sunglass
    }
    data['Mustache'] = {
        'Mustache': mustache
    }
    data['Smile'] = {
        'Smile': smile
    }
    data['Beard'] = {
        'Beard': beard
    }
    data['MouthOpen'] = {
        'Mouth Open': mouth_open
    }

    # PRINTING OUTPUT ON CONSOLE
    print(json.dumps(data, indent=2))

    # SAVING DATA IN JSON FILE
    out_file = open("myfile.json", "w")
    json.dump(data, out_file, indent=2)
    out_file.close()