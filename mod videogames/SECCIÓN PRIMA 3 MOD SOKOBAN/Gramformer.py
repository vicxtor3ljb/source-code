# https://www.listendata.com/2024/01/4-ways-to-correct-grammar-with-python.html
# error python -m spacy download en
"""
Libraries to install:
pip install -U git+https://github.com/PrithivirajDamodaran/Gramformer.git
pip install torch
pip install spacy
python -m spacy download en
"""
 
from gramformer import Gramformer
import torch

def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

set_seed(1212)
gf = Gramformer(models = 1, use_gpu=False)
mytext = """I is testng grammar tool using python. It does not costt anythng."""
gf.correct(mytext, max_candidates=1)

print(gf.correct(mytext, max_candidates=1))
