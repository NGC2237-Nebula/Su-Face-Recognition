# -*- coding: utf-8 -*-
import numpy


def encoding_FaceStr(image_face_encoding):
    # 将numpy array类型转化为列表
    encoding__array_list = image_face_encoding.tolist()
    # 将列表里的元素转化为字符串
    encoding_str_list = [str(i) for i in encoding__array_list]
    # 拼接列表里的字符串
    encoding_str = ','.join(encoding_str_list)
    return encoding_str


def decoding_FaceStr(encoding_str):
    # 将字符串转为numpy ndarray类型，即矩阵
    # 转换成一个list
    decoding_list = encoding_str.strip(' ').split(',')
    # 将list中str转换为float
    decoding_float = list(map(float, decoding_list))
    face_encoding = numpy.array(decoding_float)
    return face_encoding
