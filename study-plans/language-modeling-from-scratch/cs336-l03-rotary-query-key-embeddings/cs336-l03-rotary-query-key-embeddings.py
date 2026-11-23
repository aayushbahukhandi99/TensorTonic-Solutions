import torch

def rotary_embed(
    q: torch.Tensor, k: torch.Tensor,
    positions: torch.Tensor, inv_freq: torch.Tensor,
) -> dict:
    """
    Returns q_rotated and k_rotated tensors in a dictionary.
    """
    angles = positions.unsqueeze(-1) * inv_freq

    if positions.ndim == 1:
        angles = angles.unsqueeze(0).unsqueeze(0)  #(1, 1, S, D/2)
    else:
        angles = angles.unsqueeze(1)  # (B, 1 ,S , D/2)

    cos = angles.cos()
    sin = angles.sin()

    def rotate(x):
        x_pairs = x.reshape(*x.shape[:-1], -1, 2)

        x0 = x_pairs[..., 0]
        x1 = x_pairs[..., 1]

        c = cos.to(device = x.device, dtype = x.dtype)
        s = sin.to(device = x.device, dtype = x.dtype)

        rotated_0 = x0 * c - x1 * s
        rotated_1 = x0 * s + x1 * c

        rotated = torch.stack((rotated_0, rotated_1), dim =-1)

        return rotated.flatten(-2)

    return {
        "q_rotated": rotate(q),
        "k_rotated": rotate(k),
    }
