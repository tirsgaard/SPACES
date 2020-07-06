from .space.space import Space
from .space.space import Space_atari

__all__ = ['get_model']

def get_model(cfg):
    """
    Also handles loading checkpoints, data parallel and so on
    :param cfg:
    :return:
    """
    model = None
    if cfg.model == 'SPACE':
        model = Space()
        
    if cfg.model == 'SPACE_atari':
        model = Space_atari()
        
    return model
