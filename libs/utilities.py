# Utilities for various data handling

### Libs
import os
import pandas as pd
from keras.models import load_model
from keras import backend as K

import numpy as np
from numpy import linalg as LA

import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.io.wavfile import read
import librosa
import librosa.display
import librosa.feature as ftr
import librosa.onset as onst
import sys
import glob

def load_dataset(dataset_path):
    # TODO implement actual data handling
    # (requires figuring out data format)
    print('[u] Loading all wav files from {}'.format(dataset_path))
    filelist = glob.glob(os.path.join(dataset_path, '*.wav'))
    print('[u] Loaded {} files'.format(len(filelist)))
    return filelist


def create_autoencoder_model(model_args, **kwargs):
    print('[u] Creating autoencoder model')
    from models.model_example import AEModelFactory
    # enforce input shape convention
    K.set_image_data_format('channels_last')
    # generate model
    obj = AEModelFactory(**model_args)
    model = obj.get_model()
    # return model and loss
    return model, AEModelFactory.get_lossfunc(**kwargs)


def load_autoencoder_model(model_path, custom_objects=None):
    print('[u] Loading autoencoder model from {}'.format(model_path))
    model = load_model(model_path, custom_objects=custom_objects)
    # extract encoder from main model
    encoder = model.get_layer('encoder')
    decoder = model.get_layer('decoder')
    return encoder, decoder, model


def load_autoencoder_lossfunc(time_slice):
    print('[u] Loading loss function for model')
    from models.model_example import AEModelFactory
    # return loss function
    return AEModelFactory.get_lossfunc(time_slice)
