from .dense_baseline import DenseBaseline
from .dssm import DSSM
from .cdssm import CDSSM

def list_available() -> list:
    from matchzoo.engine.base_model import BaseModel
    from matchzoo.utils import list_recursive_concrete_subclasses
    return list_recursive_concrete_subclasses(BaseModel)
