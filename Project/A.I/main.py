from utils.config import parse_args
from utils.data_loader import get_data_loader
from utils.models import nkModel
import pandas as pd


def main(args):
    train_loader, val_loader, test_loader = get_data_loader(args)
    model = nkModel(args, train_loader, val_loader, test_loader)

    if args.is_train:
        model.train()
    else:
        temp_list = model.test()
        print(temp_list)
        my_df = pd.DataFrame(temp_list)
        my_df.to_csv("my_csv.csv", index=False, header=False)


if __name__ == '__main__':
    config = parse_args()
    main(config)
