from abc import ABC, abstractmethod


class Message:
    def __init__(self, subject, body, sender):
        self.subject = subject
        self.body = body
        self.sender = sender
    #     self.flow = [sender]

    # @property
    # def current(self):
    #     return self.flow[-1]

    def send(self, to_user):
        if to_user.__class__ not in self.sender.allowed:
            print(to_user.__class__, self.sender.allowed)
            print(
                f"{self.sender.__class__} is not allowed to send email to {to_user.__class__}")
        else:
            # self.flow.append(to_user)
            print(to_user.__class__, self.sender.allowed)
            print(f"message send to {to_user.__class__}")


class AbsractUser(ABC):
    @property
    @abstractmethod
    def allowed(self):
        pass


class ManagingDirector(AbsractUser):
    allowed = []


class InternalManager(AbsractUser):
    allowed = [ManagingDirector]


class Supervisor(AbsractUser):
    allowed = [InternalManager]


class Operator(AbsractUser):
    allowed = [Supervisor]


class Client(AbsractUser):
    allowed = [Operator, InternalManager]


if __name__ == "__main__":
    opt = Operator()
    spr = Supervisor()
    inm = InternalManager()
    mnd = ManagingDirector()

    client = Client()
    message = Message("Issue #1234", "Issue description", client)

    message.send(opt)
    # message.send(spr)
    # message.send(inm)
    # message.send(mnd)
