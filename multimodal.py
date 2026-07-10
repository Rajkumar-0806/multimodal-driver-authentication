import torch
import torch.nn as nn


# ---------------------------------------------------------
# Face Encoder (CNN)
# ---------------------------------------------------------
class FaceEncoder(nn.Module):

    def __init__(self, embedding_dim=128):
        super().__init__()

        self.encoder = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, 3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),

            nn.AdaptiveAvgPool2d(1)
        )

        self.fc = nn.Linear(128, embedding_dim)

    def forward(self, x):

        x = self.encoder(x)

        x = x.view(x.size(0), -1)

        return self.fc(x)


# ---------------------------------------------------------
# Voice Encoder (LSTM)
# ---------------------------------------------------------
class VoiceEncoder(nn.Module):

    def __init__(self,
                 input_dim=40,
                 hidden_dim=128,
                 embedding_dim=128):

        super().__init__()

        self.lstm = nn.LSTM(
            input_dim,
            hidden_dim,
            num_layers=2,
            batch_first=True
        )

        self.fc = nn.Linear(hidden_dim, embedding_dim)

    def forward(self, x):

        _, (hidden, _) = self.lstm(x)

        return self.fc(hidden[-1])


# ---------------------------------------------------------
# Gait Encoder (LSTM)
# ---------------------------------------------------------
class GaitEncoder(nn.Module):

    def __init__(self,
                 input_dim=6,
                 hidden_dim=128,
                 embedding_dim=128):

        super().__init__()

        self.lstm = nn.LSTM(
            input_dim,
            hidden_dim,
            num_layers=2,
            batch_first=True
        )

        self.fc = nn.Linear(hidden_dim, embedding_dim)

    def forward(self, x):

        _, (hidden, _) = self.lstm(x)

        return self.fc(hidden[-1])


# ---------------------------------------------------------
# Standard Multimodal Fusion
# ---------------------------------------------------------
class MultimodalFusion(nn.Module):

    def __init__(self,
                 embedding_dim=128,
                 num_classes=100):

        super().__init__()

        fusion_dim = embedding_dim * 3

        self.classifier = nn.Sequential(

            nn.Linear(fusion_dim, 512),

            nn.ReLU(),

            nn.Dropout(0.4),

            nn.Linear(512, 256),

            nn.ReLU(),

            nn.Dropout(0.3),

            nn.Linear(256, num_classes)
        )

    def forward(self,
                face_embedding,
                voice_embedding,
                gait_embedding):

        fused = torch.cat(

            [

                face_embedding,

                voice_embedding,

                gait_embedding

            ],

            dim=1

        )

        return self.classifier(fused)


# ---------------------------------------------------------
# Complete Multimodal Network
# ---------------------------------------------------------
class MultimodalAuthenticationModel(nn.Module):

    def __init__(self,
                 embedding_dim=128,
                 num_classes=100):

        super().__init__()

        self.face_encoder = FaceEncoder(embedding_dim)

        self.voice_encoder = VoiceEncoder(
            embedding_dim=embedding_dim
        )

        self.gait_encoder = GaitEncoder(
            embedding_dim=embedding_dim
        )

        self.fusion = MultimodalFusion(
            embedding_dim=embedding_dim,
            num_classes=num_classes
        )

    def forward(

        self,

        face,

        voice,

        gait

    ):

        face_feature = self.face_encoder(face)

        voice_feature = self.voice_encoder(voice)

        gait_feature = self.gait_encoder(gait)

        logits = self.fusion(

            face_feature,

            voice_feature,

            gait_feature

        )

        return logits


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    model = MultimodalAuthenticationModel(
        embedding_dim=128,
        num_classes=20
    )

    face = torch.randn(8, 3, 160, 160)

    voice = torch.randn(8, 120, 40)

    gait = torch.randn(8, 150, 6)

    output = model(face, voice, gait)

    print(output.shape)
