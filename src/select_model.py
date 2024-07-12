import argparse
from glob import glob
import pandas as pd
import json

def main(args):
    files = glob(f'{args.basedir}/*/{args.file}')
    items = []
    for f in files:
        with open(f, 'r') as f:
            items.append(json.loads(f.read()))
    df = pd.DataFrame.from_records(items)
    idx = df[args.col].argmax()
    with open(f'{args.basedir}/selected_{args.file}', 'w') as f:
        f.write(df.iloc[idx].to_json())

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--basedir', type=str, default='output')
    parser.add_argument('--file', type=str, default='lgbm_cv.json')
    parser.add_argument('--col', type=str, default='mean_auc')
    args = parser.parse_args()

    print(f'params: {args}')
    main(args)
