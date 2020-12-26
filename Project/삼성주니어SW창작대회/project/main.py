from utils.config import parse_args
from utils.data_loader import get_data_loader
from models.nk_model import nkModel
import pandas as pd
import getpass

user = getpass.getuser()


def main(args):
    train_loader, test_loader = get_data_loader(args)
    model = nkModel(args, train_loader, test_loader)

    if args.is_train:
        model.train()
    else:
        temp_list = model.test()
        my_df = pd.DataFrame(temp_list)
        my_df.to_csv('/home/{}/PycharmProjects/project/file/sample.csv'.format(user), index=False, header=False)


if __name__ == '__main__':
    config = parse_args()
    main(config)