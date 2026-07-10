# confidence.py

import torch
import torch.nn as nn


class ConfidenceEstimator(nn.Module):
    """
    Standard confidence estimator.

    Computes confidence scores for each modality from
    normalized quality indicators.

    Output:
        confidence ∈ [0,1]
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def normalize(x):
        return torch.sigmoid(x)

    def face_confidence(
        self,
        image_quality,
        liveness_score
    ):
        """
        image_quality : normalized IQA score
        liveness_score : PAD score
        """

        c = 0.5 * image_quality + 0.5 * liveness_score
        return torch.clamp(c, 0.0, 1.0)

    def voice_confidence(
        self,
        snr_score,
        speaker_score
    ):
        """
        snr_score : normalized SNR
        speaker_score : ASV confidence
        """

        c = 0.5 * snr_score + 0.5 * speaker_score
        return torch.clamp(c, 0.0, 1.0)

    def gait_confidence(
        self,
        motion_score,
        tracking_score
    ):
        """
        motion_score : motion stability
        tracking_score : tracking consistency
        """

        c = 0.5 * motion_score + 0.5 * tracking_score
        return torch.clamp(c, 0.0, 1.0)

    def forward(
        self,
        face_quality,
        face_liveness,
        voice_snr,
        voice_asv,
        gait_motion,
        gait_tracking
    ):

        face = self.face_confidence(
            face_quality,
            face_liveness
        )

        voice = self.voice_confidence(
            voice_snr,
            voice_asv
        )

        gait = self.gait_confidence(
            gait_motion,
            gait_tracking
        )

        confidence = torch.stack(
            [
                face,
                voice,
                gait
            ],
            dim=0
        )

        return confidence
