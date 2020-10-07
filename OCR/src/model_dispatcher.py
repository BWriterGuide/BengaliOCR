import models

MODEL_DISPATCHER = {
    'resnet34': models.ResNet34,
    'resnet152': models.ResNet152,
    'densenet161': models.DenseNet161
}