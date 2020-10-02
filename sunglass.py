import boto3
import base64
import json
import os

rekognition_client = boto3.client('rekognition', region_name='us-east-1')
file = open('rock.jpg', 'rb').read()

response = rekognition_client.detect_faces(
    Image={
        'Bytes': file
    },
    Attributes=['ALL']
)
for face in response['FaceDetails']:
    print('The Detection face is between ' + str(face['AgeRange']['Low']) + ' and' + str(
        face['AgeRange']['High'] + ' year old')

    # print('The detection face is of ' + str(face['Gender']['Value']))
    #
    # sunglass = str(face['Sunglasses']['Value'])
    #
    # if sunglass == True:
    #    print('The detection face wears a Sunglass')
    # else:
    #     print('The detection face is not wears a Sunglass')


# FACEDETAIL REAL


# import boto3
# import base64
# import json
# import os
#
# rekognition_client = boto3.client('rekognition', region_name='us-east-1')
# photo_name = 'rock.jpg'
# file = open(photo_name, 'rb').read()
#
# response = rekognition_client.detect_faces(
#     Image={
#         'Bytes': file
#     },
#     Attributes=['ALL', ]
# )
#
# print(response)
# print('============')
#
# for detail in response['FaceDetails']:
#     print('Age Between: ' + str(detail['AgeRange']['Low'])+ ' to '+ str(detail['AgeRange']['High']))
#     print('============')
#     print('Gender: ' + str(detail['Gender']['Value']))
#     print('============')
#
#     for emot in detail['Emotions']:
#         print(str(emot['Type']) + ': ' + str(emot['Confidence']))
#
#     print('============')
#     print('Sunglass: ' + str(detail['Sunglasses']['Value']))
#     print('============')
#     print('Mustache: ' + str(detail['Mustache']['Value']))
