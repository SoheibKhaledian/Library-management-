import pandas as pd
import openpyxl
import random


books = [
    "1984", "To Kill a Mockingbird", "Pride and Prejudice", "The Great Gatsby",
    "Moby Dick", "War and Peace", "The Catcher in the Rye", "Jane Eyre",
    "The Hobbit", "Crime and Punishment", "Wuthering Heights", "The Odyssey",
    "Brave New World", "Fahrenheit 451", "The Lord of the Rings",
    "The Alchemist", "Harry Potter and the Sorcerer's Stone", "The Kite Runner",
    "Anna Karenina", "The Grapes of Wrath", "The Road", "Slaughterhouse-Five",
    "The Old Man and the Sea", "The Picture of Dorian Gray", "A Tale of Two Cities",
    "Les Misérables", "The Shining", "Dracula", "The Da Vinci Code",
    "One Hundred Years of Solitude", "The Book Thief", "The Giver", "The Bell Jar",
    "The Stranger", "Frankenstein", "The Handmaid's Tale", "A Game of Thrones",
    "The Hunger Games", "Dune", "Gone with the Wind", "The Secret Garden",
    "Of Mice and Men", "Life of Pi", "The Fault in Our Stars", "Catch-22",
    "Percy Jackson & The Lightning Thief", "Twilight", "Eragon", "Shogun",
    "Memoirs of a Geisha", "The Help", "Water for Elephants", "The Time Traveler's Wife",
    "The Goldfinch", "The Night Circus", "Big Little Lies", "Eleanor Oliphant Is Completely Fine",
    "The Midnight Library", "Circe", "Where the Crawdads Sing", "The Light We Lost",
    "Before We Were Strangers", "Malibu Rising", "Daisy Jones & The Six",
    "The House in the Cerulean Sea", "Mexican Gothic", "The Paris Library",
    "Project Hail Mary", "The Seven Husbands of Evelyn Hugo", "The Silent Patient",
    "Verity", "It Ends with Us", "Ugly Love", "Reminders of Him", "November 9",
    "Confess", "The Inheritance Games", "A Court of Thorns and Roses", "Legendborn",
    "Crescent City", "Throne of Glass", "Red Queen"
]

authors = [
    "George Orwell", "Harper Lee", "Jane Austen", "F. Scott Fitzgerald",
    "Herman Melville", "Leo Tolstoy", "J.D. Salinger", "Charlotte Brontë",
    "J.R.R. Tolkien", "Fyodor Dostoevsky", "Emily Brontë", "Homer",
    "Aldous Huxley", "Ray Bradbury", "J.R.R. Tolkien",
    "Paulo Coelho", "J.K. Rowling", "Khaled Hosseini",
    "Leo Tolstoy", "John Steinbeck", "Cormac McCarthy", "Kurt Vonnegut",
    "Ernest Hemingway", "Oscar Wilde", "Charles Dickens",
    "Victor Hugo", "Stephen King", "Bram Stoker", "Dan Brown",
    "Gabriel García Márquez", "Markus Zusak", "Lois Lowry", "Sylvia Plath",
    "Albert Camus", "Mary Shelley", "Margaret Atwood", "George R.R. Martin",
    "Suzanne Collins", "Frank Herbert", "Margaret Mitchell", "Frances Hodgson Burnett",
    "John Steinbeck", "Yann Martel", "John Green", "Joseph Heller",
    "Rick Riordan", "Stephenie Meyer", "Christopher Paolini", "James Clavell",
    "Arthur Golden", "Kathryn Stockett", "Sara Gruen", "Audrey Niffenegger",
    "Donna Tartt", "Erin Morgenstern", "Liane Moriarty", "Gail Honeyman",
    "Matt Haig", "Madeline Miller", "Delia Owens", "Jill Santopolo",
    "Renée Carlino", "Taylor Jenkins Reid", "Taylor Jenkins Reid",
    "T.J. Klune", "Silvia Moreno-Garcia", "Janet Skeslien Charles",
    "Andy Weir", "Taylor Jenkins Reid", "Alex Michaelides",
    "Colleen Hoover", "Colleen Hoover", "Colleen Hoover", "Colleen Hoover",
    "Colleen Hoover", "Jennifer Lynn Barnes", "Sarah J. Maas", "Tracy Deonn",
    "Sarah J. Maas", "Sarah J. Maas", "Victoria Aveyard", "Leigh Bardugo"
]

topics = [
    "Dystopia", "Social Justice", "Romance", "American Dream",
    "Adventure", "Historical Fiction", "Coming of Age", "Gothic",
    "Fantasy", "Philosophy", "Tragedy", "Epic Poetry",
    "Science Fiction", "Censorship", "Epic Fantasy",
    "Spiritual Journey", "Fantasy", "Redemption",
    "Russian Society", "Great Depression", "Post-apocalyptic", "War Satire",
    "Survival", "Moral Corruption", "Revolution",
    "Social Justice", "Horror", "Horror", "Mystery",
    "Magical Realism", "Holocaust", "Utopian Society", "Mental Health",
    "Existentialism", "Science Fiction", "Feminism", "Epic Fantasy",
    "Dystopian", "Epic Fantasy", "Romance", "Gardening",
    "Friendship", "Adventure", "Young Love", "War Satire",
    "Mythology", "Vampires", "Dragons", "Historical Fiction",
    "Japanese Culture", "Civil Rights", "Circus Life", "Time Travel",
    "Art", "Magic", "Domestic Fiction", "Self Discovery",
    "Mental Health", "Greek Mythology", "Southern Fiction", "Romance",
    "Romance", "Music Industry", "Drama",
    "Found Family", "Horror", "Historical Fiction",
    "Science Fiction", "Hollywood", "Psychological Thriller",
    "Romance", "Romance", "Romance", "Romance",
    "Romance", "Thriller", "Fantasy", "Young Adult",
    "Fantasy", "Fantasy", "Dystopian", "Dark Fantasy"
]

names = [
    "James", "Olivia", "Liam", "Emma", "Noah", "Sophia", "Ethan", "Isabella",
    "Mason", "Mia", "Jacob", "Amelia", "William", "Harper", "Michael", "Ella",
    "Alexander", "Grace", "Benjamin", "Avery", "Elijah", "Scarlett", "Daniel",
    "Chloe", "Henry", "Victoria", "Jackson", "Lily", "Sebastian", "Zoe",
    "Samuel", "Maya", "Matthew", "Aria", "Joseph", "Luna", "David", "Ella",
    "Jack", "Charlotte", "Luke", "Nora", "Andrew", "Evelyn"
]

print(f'{len(books)}, {len(topics)}, {len(authors)}')
print(len(names))

total = [random.randint(1, 9) for i in range(82)]

book_data = {
    'id': [i for i in range(82)],
    'name': [book.lower() for book in books],
    'author': [author.lower() for author in authors],
    'topic': [topic.lower() for topic in topics],
    'total': total,
    'existing': total
}

# user_data = {
#     'id': [i for i in range(44)],
#     'name': names,
#     'access': [0 for i in range(44)],
#     'pass': [i for i in range(44)]
# }

book_df = pd.DataFrame(book_data)
book_df.to_excel('book.xlsx', index=False)
#
# user_df = pd.DataFrame(user_data)
# user_df.to_excel('user.xlsx', index=False)


