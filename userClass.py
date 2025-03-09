import pandas as pd
from bockClass import Bock
from datetime import datetime, timedelta


class User:
    file_path = 'user.xlsx'
    df = pd.read_excel(file_path)

    def __init__(self, id, name, access, pas):
        self.id = id
        self.name = name
        self.access = access
        self.pas = pas

    @classmethod
    def search_id(cls, id_to_search):
        for _, row in cls.df.iterrows():
            if row['id'] == id_to_search:
                return User(row['id'], row['name'], row['access'], row['pass'])
        return None

    @classmethod
    def get_id(cls):
        used_ids = set(cls.df.iloc[:, 0])

        new_id = 1
        while new_id in used_ids:
            new_id += 1

        return new_id

    @classmethod
    def add_user(cls, name, pas):
        new_user = User(cls.get_id(), name, 0, pas)

        new_row = {
            'id': new_user.id,
            'name': new_user.name,
            'access': new_user.access,
            'pass': new_user.pas
        }

        new_row_df = pd.DataFrame([new_row])
        cls.df = pd.concat([cls.df, new_row_df], ignore_index=True)

        cls.df.to_excel(cls.file_path, index=False)
        return new_user, f"User added successfully! \n you're id is: {new_user.id}"

    @classmethod
    def user_identification(cls, id, pas):
        user = cls.search_id(id)

        if user is None:
            return None

        if str(user.pas) == str(pas):
            return user
        else:
            return None

    @classmethod
    def change_name(cls, user, new_name):
        if not new_name:
            return "The name can't be empty or None"

        user.name = new_name

        cls.df.loc[cls.df['id'] == user.id, 'name'] = new_name

        cls.df.to_excel(cls.file_path, index=False)

        return f"The name was set to: {new_name}"

    @classmethod
    def change_pas(cls, user, new_pas):
        if not new_pas:
            return "The password can't be empty or None"

        user.pas = new_pas

        cls.df.loc[cls.df['id'] == user.id, 'pass'] = new_pas

        cls.df.to_excel(cls.file_path, index=False)

        return f"The password was set to: {new_pas}"

    @classmethod
    def favorite(cls, id):
        file_path = 'deposit.xlsx'
        df = pd.read_excel(file_path)

        wdf = df[df['user_id'] == id]

        if wdf.empty or wdf['bock_id'].empty:
            return "this user has no bock"

        favorite = wdf['bock_id'].value_counts().idxmax()

        if favorite is None:
            return "this user has no bock"

        return f"the favorite bock is {Bock.search_id(favorite).name}"

    def make_deposit(self, bock):
        file_path = 'deposit.xlsx'
        today = datetime.now()
        df = pd.read_excel(file_path)

        if bock.existing > 0:
            new_row = {
                'user_id': self.id,
                'bock_id': bock.id,
                'give_data': today,
                'expiration_data': today + timedelta(days=14),
                'status': 0,
                'return_data': None
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

            df.to_excel(file_path, index=False)
            Bock.give_bock(bock)
            return f"The book is yours \n return data: {today + timedelta(days=14)}"

        else:
            return "The book you want does not exist"

    def make_return(self, bock):
        file_path = 'deposit.xlsx'
        df = pd.read_excel(file_path)

        bocks_name = [b[0].name for b in self.find_user_bock()]

        if bock.name not in bocks_name:
            return "you don't have this bock"

        df.loc[(df['user_id'] == self.id) & (df['bock_id'] == bock.id), 'status'] = 1
        df.loc[(df['user_id'] == self.id) & (df['bock_id'] == bock.id), 'return_data'] = datetime.now()
        df.to_excel(file_path, index=False)

        Bock.return_bock(bock)

        return 'the bock has been return'

    def find_user_bock(self):
        file_path = 'deposit.xlsx'
        df = pd.read_excel(file_path)

        wdf = df[df['status'] == 0]

        bocks = []
        for _, row in wdf.iterrows():
            if int(row['user_id']) == int(self.id):
                bock = Bock.search_id(row['bock_id'])
                bocks.append([bock, row['give_data'], row['expiration_data']])

        return bocks

    def expiration(self):
        user_bock = self.find_user_bock()
        if len(user_bock) == 0:
            return user_bock

        today = datetime.now()
        expire_bocks = []

        for i in user_bock:
            if i[2] < today:
                expire_bocks.append([i[0].name, (today - i[2]).days])

        return expire_bocks
