"""
The 'alibi.explainers' module includes feature importance, counterfactual and anchor-based explainers.
"""

from .ale import ALE, plot_ale
from .anchor_tabular import AnchorTabular, DistributedAnchorTabular
from .anchor_image import AnchorImage
from .cfrl_base import CounterfactualRL
from .cfrl_tabular import CounterfactualRLTabular

__all__ = ["ALE",
           "AnchorTabular",
           "DistributedAnchorTabular",
           "AnchorText",
           "AnchorImage",
           "CEM",
           "Counterfactual",
           "CounterfactualProto",
           "CounterfactualRL",
           "CounterfactualRLTabular",
           "plot_ale",
           "IntegratedGradients",
           ]

try:
    from .shap_wrappers import KernelShap, TreeShap

    __all__ += ["KernelShap", "TreeShap"]
except ImportError:
    pass
