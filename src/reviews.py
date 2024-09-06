def write_review(reviews: list) -> list:
    review = input("Введіть свій відгук:")
    reviews.append(review)
    print("Ваш відгук додано")
    return reviews


def show_all_reviews(reviews: list) -> None:
    for review in reviews:
        print(review)


def find_repeated_phrases(reviews: list) -> list:
    reviews = "".join(reviews).lower()

    repeated_phrases = set()
    for i in range(len(reviews)):
        for j in range(i + 1, len(reviews)):
            if reviews.count(reviews[i:j]) >= 2:
                repeated_phrases.add(reviews[i:j])
    print(f"Фрази, які повторюються не меньше 2 разів{repeated_phrases}")