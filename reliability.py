import torch
import torch.nn as nn


class ReliabilityEstimator(nn.Module):
    """
    Recursive reliability estimator.

    R_{t+1} = λ R_t + (1-λ) s_t

    where
        R_t : historical reliability
        s_t : continuous quality score in [0,1]
    """

    def __init__(self,
                 num_modalities=3,
                 forgetting_factor=0.90,
                 initial_reliability=0.50):

        super().__init__()

        self.lambda_factor = forgetting_factor

        self.register_buffer(
            "reliability",
            torch.ones(num_modalities) * initial_reliability
        )

    def reset(self):
        self.reliability.fill_(0.5)

    def update(self, quality_scores):

        """
        quality_scores : tensor(num_modalities)

        values must lie between 0 and 1
        """

        quality_scores = torch.clamp(
            quality_scores.detach(),
            0.0,
            1.0
        )

        self.reliability = (
            self.lambda_factor * self.reliability
            +
            (1.0 - self.lambda_factor) * quality_scores
        )

        return self.reliability

    def get(self):
        return self.reliability.clone()

    def forward(self, quality_scores):

        return self.update(quality_scores)
