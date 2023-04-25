"""
This principle mainly says that a given derived class must be substitutable
for its base classes.
https://www.pythontutorial.net/python-oop/python-liskov-substitution-principle/

It says the base class must not change the behaviour or the base class.

You should always be able to substitute a base type for a subtype.
"""

from abc import ABCMeta, abstractmethod


# class Notification(metaclass=ABCMeta):
#     @abstractmethod
#     def notify(self, message: str, email: str):
#         pass
#
#
# class Email(Notification):
#     def notify(self, message: str, email: str):
#         print(f'Send {message} to {email}')
#
#
# class SMS(Notification):
#     """
#     This class breaks the Liskov substitution principle. It changes (or uses) the email variable
#     as a phone number.
#     """
#     def notify(self, message: str, phone: str):
#         print(f"Send {message} to {phone}")

# ####################################### LSP #############################


class Notification(metaclass=ABCMeta):
    @abstractmethod
    def notify(self, message: str):
        pass


class Email(Notification):
    def __init__(self, email: str):
        self.email = email

    def notify(self, message: str):
        print(f"Send {message} to {self.email}")


class SMS(Notification):
    def __init__(self, phone: str):
        self.phone = phone

    def notify(self, message: str):
        print(f"Send {message} to {self.phone}")


class Contact:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self, message: str):
        self.notification.notify(message)


if __name__ == "__main__":
    contact = Contact("Karim Moradi", "kmoradi.ai@gmail.com", "+3165432899")
    sms_notification = SMS(phone=contact.phone)
    email_notification = Email(email=contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send("Hello Karim!")

    notification_manager.notification = email_notification
    notification_manager.send("Hi Karim!")
