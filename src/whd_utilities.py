    
import copy
import numpy as np
import pandas as pd

def WHD_pack_violtn_grps(data, constant_cols, ref_map):
    """
    Function that packs columns of the dataframe per the reference map provided.
    constant_cols are columns to be preserved. Returns grouped dataframe.
    """
    
    dat = copy.copy(data[constant_cols])
    
    for groupCol, sourceCols in ref_map.items():
        dat[groupCol] = np.sum(data[sourceCols], axis=1)
        
    return dat
    
    
