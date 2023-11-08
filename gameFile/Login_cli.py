import inquirer
from game import *
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship, backref, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key = True)
    userName = Column(String())
    swagScale = Column(Integer())
    scores = relationship("Score", backref = backref("users"), cascade = "all, delete-orphan")

    def __repr__ (self):
        return f"UserName: {self.userName}"
    
class Score(Base):
    __tablename__ = "score"

    id = Column(Integer(), primary_key = True)
    user = Column(Integer(), ForeignKey("users.id"))
    score = Column("score", Integer())

    def __repr__ (self):
        return f"Score: {self.score}"
    
if __name__ == "__main__":
    engine = create_engine("sqlite:///database.db")
    Base.metadata.create_all(engine)
    session = Session(engine)

    def starter_menu():
        print("""
        ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
        ▐.___  ___.   ______   .__   __.  __  ___  ___________    ____▌
        ▐|   \/   |  /  __  \  |  \ |  | |  |/  / |   ____\   \  /   /▌
        ▐|  \  /  | |  |  |  | |   \|  | |  '  /  |  |__   \   \/   / ▌
        ▐|  |\/|  | |  |  |  | |  . `  | |    <   |   __|   \_    _/  ▌
        ▐|  |  |  | |  `--'  | |  |\   | |  .  \  |  |____    |  |    ▌
        ▐|__|  |__|  \______/  |__| \__| |__|\__\ |_______|   |__|    ▌
        ▐                                                             ▌
        ▐  _______      ___      .___  ___.  _______                  ▌
        ▐ /  _____|    /   \     |   \/   | |   ____|                 ▌
        ▐|  |  __     /  ^  \    |  \  /  | |  |__                    ▌
        ▐|  | |_ |   /  /_\  \   |  |\/|  | |   __|                   ▌
        ▐|  |__| |  /  _____  \  |  |  |  | |  |____                  ▌
        ▐ \______| /__/     \__\ |__|  |__| |_______|                 ▌
        ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
        """)
        start_menu = [
        inquirer.List("options",
                        message = "Select one",
                        choices = ["Play", "View High Scores", "View Users", "Update Users", "Delete a User", "Quit"],
                        ),
        ]

        start_menu_responses = inquirer.prompt(start_menu)
        start_menu_responses_key = start_menu_responses["options"]

        if start_menu_responses_key == "Play":
            user_menu()
        elif start_menu_responses_key == "View High Scores":
            high_score()
        elif start_menu_responses_key == "View Users":
            view_users()
        elif start_menu_responses_key == "Update Users":
            update_users()
        elif start_menu_responses_key == "Delete a User":
            delete_user()
        elif start_menu_responses_key == "Quit":
            exit

    def return_to_start ():
        return_start = [
            inquirer.List("return",
                          message = "Would you like to return to the Start menu?",
                          choices = ["Yes", "No"],
                          ),
        ]
        return_start_answers = inquirer.prompt(return_start)
        if return_start_answers["return"] == "Yes":
            starter_menu()
        elif return_start_answers["return"] == "No":
            print("Thanks for Playing! Good-bye!")
            exit

    def user_menu():
        users = session.query(User).all()
        user_menu_options = [
            inquirer.List("new",
                            message = "Are you a New or Exsisting User?",
                            choices = ["New", "Exsisting"],
                            ),
        ]

        user_menu_responses = inquirer.prompt(user_menu_options)
        user_menu_responses_key = user_menu_responses["new"]

        if user_menu_responses_key == "New":
            create_new_user()
        if user_menu_responses_key == "Exsisting":
            if not users:
                print("There are no exsisting users with that name")
                user_menu()
            else:
                returning_user()

    def create_new_user():
        user_name = session.query(User.userName).all()
        question = [
            inquirer.Text("userName", message = "Enter a Username"),
            inquirer.Text("SwagScale", message = "Enter how much swag you have (must be a number)"),
        ]
        answers = inquirer.prompt(question)
        new_user = User(
            userName = answers['userName'],
            swagScale = answers['SwagScale'],
        )
        if new_user.userName in [user[0] for user in user_name]:
            print("There is already a user with that name")
            create_new_user()
        else:
            session.add(new_user)
            session.commit()
            user1 = session.query(User).filter_by(userName = new_user.userName).first()
            final_score = game()
            new_score = Score(
                user= user1.id,
                score= final_score
            )
            game_over_banner()
            session.add(new_score)
            session.commit()
            return_to_start()

    def high_score():
        users = session.query(User).all()
        all_scores = session.query(Score).all()
        all_scores1 = [(score.score, score.users.userName) for score in all_scores]
        sorted_list = sorted(all_scores1, key = lambda k: k[0], reverse = True)
        if not users:
            print("There are no exsisting users")
        else:
            print(f"""
            ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
            ▐ /$$   /$$ /$$           /$$                      ▌
            ▐| $$  | $$|__/          | $$                      ▌
            ▐| $$  | $$ /$$  /$$$$$$ | $$$$$$$                 ▌
            ▐| $$$$$$$$| $$ /$$__  $$| $$__  $$                ▌
            ▐| $$__  $$| $$| $$  \ $$| $$  \ $$                ▌
            ▐| $$  | $$| $$| $$  | $$| $$  | $$                ▌
            ▐| $$  | $$| $$|  $$$$$$$| $$  | $$                ▌
            ▐|__/  |__/|__/ \____  $$|__/  |__/                ▌
            ▐               /$$  \ $$                          ▌
            ▐              |  $$$$$$/                          ▌
            ▐               \______/                           ▌
            ▐  /$$$$$$                                         ▌
            ▐ /$$__  $$                                        ▌
            ▐| $$  \__/  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$ ▌
            ▐|  $$$$$$  /$$_____/ /$$__  $$ /$$__  $$ /$$__  $$▌
            ▐ \____  $$| $$      | $$  \ $$| $$  \__/| $$$$$$$$▌
            ▐ /$$  \ $$| $$      | $$  | $$| $$      | $$_____/▌
            ▐|  $$$$$$/|  $$$$$$$|  $$$$$$/| $$      |  $$$$$$$▌
            ▐ \______/  \_______/ \______/ |__/       \_______/▌
            ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
            Highest Score: {sorted_list[0][0]}  User: {sorted_list[0][1]}
            Second Highest: {sorted_list[1][0]}  User: {sorted_list[1][1]}
            Third Highest: {sorted_list[2][0]}  User: {sorted_list[2][1]}
            """)
        return_to_start()

    def view_users():
        users = session.query(User).all()
        all_scores = session.query(Score).all()
        if not users:
            print("No Exsiting Users")
            starter_menu()
        else:
            question = [
                inquirer.List("update",
                              message = "Select a User to View",
                              choices = [user for user in users],
                              ),
            ]
            answer = inquirer.prompt(question)
            times_played = [score.score for score in all_scores if answer["update"].id == score.user]
            swag = answer["update"].swagScale
            print(f"""
            {answer['update']}
            User Swag: {swag}
            Highest Score: {max(times_played)}
            """)
            return_to_start()

    def update_users():
        pass

    def delete_user():
        users = session.query(User).all()
        question = [
            inquirer.List("delete",
                          message = "Pick a User to delete.",
                          choices = [user for user in users]
                          ),
            inquirer.List("confirmation",
                          message = "Are you sure you want to delete this user?",
                          choices = ["Yes", "No"]
                          )
        ]
        answer = inquirer.prompt(question)

        if answer["confirmation"] == "No":
            print(f"You have saved {answer['delete'].userName} from deletion!")
        if answer["confirmation"] == "Yes":
            print("User has been deleted")
            session.delete(answer['delete'])
            session.commit()
        return_to_start()

    def returning_user():
        pass

    def game_over_banner():
        print("""
        ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
        ▐  _______      ___      .___  ___.  _______   ▌
        ▐ /  _____|    /   \     |   \/   | |   ____|  ▌
        ▐|  |  __     /  ^  \    |  \  /  | |  |__     ▌
        ▐|  | |_ |   /  /_\  \   |  |\/|  | |   __|    ▌
        ▐|  |__| |  /  _____  \  |  |  |  | |  |____   ▌
        ▐ \______| /__/     \__\ |__|  |__| |_______|  ▌
        ▐                                              ▌
        ▐  ______   ____    ____  _______ .______      ▌
        ▐ /  __  \  \   \  /   / |   ____||   _  \     ▌
        ▐|  |  |  |  \   \/   /  |  |__   |  |_)  |    ▌
        ▐|  |  |  |   \      /   |   __|  |      /     ▌
        ▐|  `--'  |    \    /    |  |____ |  |\  \----.▌
        ▐ \______/      \__/     |_______|| _| `._____|▌
        ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
        """)
    
    starter_menu()


