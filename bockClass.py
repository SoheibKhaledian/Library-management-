import pandas as pd


class Bock:
    file_path = 'book.xlsx'
    df = pd.read_excel(file_path)

    def __init__(self, id, name, author_name, topic, total, existing):
        self.id = id
        self.name = name
        self.author = author_name
        self.topic = topic
        self.total = total
        self.existing = existing

    @classmethod
    def search_id(cls, id_to_search):
        for _, row in cls.df.iterrows():
            if row['id'] == id_to_search:
                return Bock(row['id'], row['name'], row['author'], row['topic'], row['total'], row['existing'])
        return None

    @classmethod
    def get_id(cls):
        used_ids = set(cls.df.iloc[:, 0])

        new_id = 1
        while new_id in used_ids:
            new_id += 1

        return new_id

    @classmethod
    def add_bock(cls, name, author_name, topic, total):
        new_bock = Bock(cls.get_id(), name, author_name, topic, total, total)

        new_row = {
            'id': new_bock.id,
            'name': new_bock.name,
            'author': new_bock.author,
            'topic': new_bock.topic,
            'total': total,
            'existing': total
        }

        new_row_df = pd.DataFrame([new_row])
        cls.df = pd.concat([cls.df, new_row_df], ignore_index=True)

        cls.df.to_excel(cls.file_path, index=False)
        return "bock added successfully!"

    @classmethod
    def name_search(cls, name_to_search):
        for _, row in cls.df.iterrows():
            if row['name'] == name_to_search:
                return Bock(row['id'], row['name'], row['author'], row['topic'], row['total'], row['existing'])
        return None

    @classmethod
    def author_search(cls, author_to_search):
        bocks = []
        for _, row in cls.df.iterrows():
            if row['author'] == author_to_search:
                bocks.append(Bock(row['id'], row['name'], row['author'], row['topic'], row['total'], row['existing']))
        return bocks

    @classmethod
    def topic_search(cls, topic_to_search):
        bocks = []
        for _, row in cls.df.iterrows():
            if row['topic'] == topic_to_search:
                bocks.append(
                    Bock(row['id'], row['name'], row['author'], row['topic'], row['total'], row['existing']))
        return bocks

    @classmethod
    def give_bock(cls, bock):
        bock.existing -= 1

        cls.df.loc[cls.df['id'] == bock.id, 'existing'] = bock.existing
        cls.df.to_excel(cls.file_path, index=False)

    @classmethod
    def return_bock(cls, bock):
        bock.existing += 1

        cls.df.loc[cls.df['id'] == bock.id, 'existing'] = bock.existing
        cls.df.to_excel(cls.file_path, index=False)

    @classmethod
    def delete_bock(cls, bock_name):
        cls.df = cls.df[cls.df['name'] != bock_name]
        cls.df.to_excel(cls.file_path, index=False)
        return "the book got deleted"

    @classmethod
    def all_deposit_bock(cls):
        file_path = 'deposit.xlsx'
        df = pd.read_excel(file_path)

        bocks = []

        wdf = df[df['status'] == 1]
        for _, row in wdf.iterrows():
            bock = Bock.search_id(row['bock_id'])
            if bock:
                bocks.append([
                    bock.name,
                    row['give_data'],
                    row['expiration_data'],
                    row.get('return_data')
                ])

        return bocks

