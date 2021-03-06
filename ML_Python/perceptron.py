#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""感知机分类方法，用于对线性可分的数据集分类
这里采用感知机的对偶问题来求解，以减少计算次数"""
import numpy as np


class Perceptron(object):

    def __init__(self,sample,label):
        """sample是二维数组，每一行为一个样本点，每一列为一个特征。
        label是标签，对于感知机只有+1和-1两种取值"""
        self.sample=sample
        self.label=label
        self.Gram=np.zeros((self.sample.shape[0],self.sample.shape[0]))
        for i in range(self.sample.shape[0]):
            for j in range(i,self.sample.shape[0]):
                self.Gram[i,j]=np.dot(self.sample[i,:],self.sample[j,:].T)
                self.Gram[j,i]=self.Gram[i,j]

    def fit(self,eta):
        """eta,学习效率"""
        x=self.sample
        y=self.label
        G=self.Gram
        isChange=True
        alpha=np.zeros(x.shape[0])
        b=0
        while isChange:
            isChange=False
            for i in range(self.sample.shape[0]):
                if (np.sum(G[i,:]*y*alpha)+b)*y[i]<=0:
                    alpha[i]+=eta
                    b+=eta*y[i]
                    isChange=True
        self.w=np.zeros(x.shape[1])
        for i in range(x.shape[0]):
            self.w+=alpha[i]*x[i,:]*y[i]
        self.b=b

    def predict(self,x):
        ans=np.sum(x*self.w)+self.b
        if ans>0:
            return 1
        else:
            return -1

if __name__=='__main__':
    x=np.array([[3,3],[4,3],[1,1]])
    y=np.array([1,1,-1])
    per=Perceptron(x,y)
    per.fit(1)
    print(per.w)
    print(per.b)