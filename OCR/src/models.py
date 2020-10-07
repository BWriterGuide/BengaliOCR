import pretrainedmodels
import torch.nn as nn
from torch.nn import functional as F

class ResNet34(nn.Module):
    def __init__(self, pretrained):
        super(ResNet34, self).__init__()
        if pretrained is True:
            self.model = pretrainedmodels.__dict__["resnet34"](pretrained="imagenet")
        else:
            self.model = pretrainedmodels.__dict__["resnet34"](pretrained=None)

        dimension_features = self.model.last_linear.in_features
        # print(dimension_features)
        self.l0 = nn.Linear(dimension_features,168)
        self.l1 = nn.Linear(dimension_features,11)
        self.l2 = nn.Linear(dimension_features,7)

    def forward(self, x):
        bs, _, _, _  = x.shape
        x = self.model.features(x)
        x = F.adaptive_avg_pool2d(x,1).reshape(bs, -1)
        l0 = self.l0(x)
        l1 = self.l1(x)
        l2 = self.l2(x)
        return l0,l1,l2

class ResNet152(nn.Module):
    def __init__(self, pretrained):
        super(ResNet152, self).__init__()
        if pretrained is True:
            self.model = pretrainedmodels.__dict__["resnet152"](pretrained="imagenet")
        else:
            self.model = pretrainedmodels.__dict__["resnet152"](pretrained=None)

        dimension_features = self.model.last_linear.in_features
        self.l0 = nn.Linear(dimension_features,168)
        self.l1 = nn.Linear(dimension_features,11)
        self.l2 = nn.Linear(dimension_features,7)

    def forward(self, x):
        bs, _, _, _  = x.shape
        x = self.model.features(x)
        x = F.adaptive_avg_pool2d(x,1).reshape(bs, -1)
        l0 = self.l0(x)
        l1 = self.l1(x)
        l2 = self.l2(x)
        return l0,l1,l2

class DenseNet161(nn.Module):
    def __init__(self, pretrained):
        super(DenseNet161, self).__init__()
        if pretrained is True:
            self.model = pretrainedmodels.__dict__["densenet161"](pretrained="imagenet")
        else:
            self.model = pretrainedmodels.__dict__["densenet161"](pretrained=None)

        dimension_features = self.model.last_linear.in_features
        self.l0 = nn.Linear(dimension_features,168)
        self.l1 = nn.Linear(dimension_features,11)
        self.l2 = nn.Linear(dimension_features,7)

    def forward(self, x):
        bs, _, _, _  = x.shape
        x = self.model.features(x)
        x = F.adaptive_avg_pool2d(x,1).reshape(bs, -1)
        l0 = self.l0(x)
        l1 = self.l1(x)
        l2 = self.l2(x)
        return l0,l1,l2
