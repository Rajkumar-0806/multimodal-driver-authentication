# preprocessing.py

import os
import cv2
import numpy as np
import pandas as pd
import librosa


# =====================================================
# Face Preprocessing
# =====================================================

class FacePreprocessor:

    def __init__(self,
                 image_size=(160,160)):

        self.image_size = image_size

    def preprocess(self, image_path):

        image = cv2.imread(image_path)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = cv2.resize(image, self.image_size)

        image = image.astype(np.float32) / 255.0

        image = (image - 0.5) / 0.5

        image = np.transpose(image, (2,0,1))

        return image


# =====================================================
# Voice Preprocessing
# =====================================================

class VoicePreprocessor:

    def __init__(self,
                 sample_rate=16000,
                 duration=3,
                 n_mfcc=40):

        self.sample_rate = sample_rate
        self.duration = duration
        self.n_mfcc = n_mfcc

    def preprocess(self, audio_path):

        signal, sr = librosa.load(
            audio_path,
            sr=self.sample_rate
        )

        expected_length = self.sample_rate * self.duration

        if len(signal) < expected_length:

            signal = np.pad(
                signal,
                (0, expected_length-len(signal))
            )

        else:

            signal = signal[:expected_length]

        signal = librosa.util.normalize(signal)

        mfcc = librosa.feature.mfcc(
            y=signal,
            sr=self.sample_rate,
            n_mfcc=self.n_mfcc
        )

        mfcc = mfcc.T

        return mfcc.astype(np.float32)


# =====================================================
# Gait Preprocessing
# =====================================================

class GaitPreprocessor:

    def __init__(self,
                 sequence_length=150):

        self.sequence_length = sequence_length

    def preprocess(self, csv_file):

        df = pd.read_csv(csv_file)

        features = df.iloc[:,1:].values.astype(np.float32)

        mean = np.mean(features, axis=0)

        std = np.std(features, axis=0) + 1e-8

        features = (features-mean)/std

        if len(features) < self.sequence_length:

            pad = np.zeros(

                (

                    self.sequence_length-len(features),

                    features.shape[1]

                ),

                dtype=np.float32

            )

            features = np.vstack([features,pad])

        else:

            features = features[:self.sequence_length]

        return features


# =====================================================
# Complete Multimodal Preprocessor
# =====================================================

class MultimodalPreprocessor:

    def __init__(self):

        self.face = FacePreprocessor()

        self.voice = VoicePreprocessor()

        self.gait = GaitPreprocessor()

    def preprocess(self,

                   face_path,

                   voice_path,

                   gait_path):

        face = self.face.preprocess(face_path)

        voice = self.voice.preprocess(voice_path)

        gait = self.gait.preprocess(gait_path)

        return {

            "face":face,

            "voice":voice,

            "gait":gait

        }


# =====================================================
# Example
# =====================================================

if __name__=="__main__":

    processor = MultimodalPreprocessor()

    sample = processor.preprocess(

        "face.jpg",

        "voice.wav",

        "gait.csv"

    )

    print(sample["face"].shape)

    print(sample["voice"].shape)

    print(sample["gait"].shape)
