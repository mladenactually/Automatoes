class TicketState:
    def mark_as_read(self):
        pass

    def mark_repair(self, accepted):
        pass


class SentState(TicketState):
    pass


class ReceivedState(TicketState):
    def mark_as_read(self):
        pass


class AcceptedState(TicketState):
    def mark_repair(self, accepted):
        pass


class RejectedState(TicketState):
    def mark_repair(self, accepted):
        pass


class Ticket:
    def __init__(self, sender, recipient, device, message, read=False):
        self.read = read
        # TODO: можда self.read треба да буде атрибут класе TicketState
        self.sender = sender
        self.recipient = recipient
        self.device = device
        self.message = message
        self.state = SentState()

    def notify_received(self):
        pass

    def notify_accepted(self):
        pass

    def notify_rejected(self):
        pass

    def lock_device(self):
        pass

    def unlock_device(self):
        pass
