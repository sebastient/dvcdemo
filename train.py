from dvclive import Live
from yaml import safe_load as load_yaml
import random
import string


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


with open('params.yaml', 'r') as f:
    params = load_yaml(f)

with Live('out', report='md', save_dvc_exp=True) as live:
    for idx in range(params['iters']):
        print('step %d' % idx)
        live.log_metric('index', idx)
        live.next_step()
    live.end()

with open('out/model.1', 'w') as f:
    f.write(randomword(32))
