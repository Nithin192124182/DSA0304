class DateFSM:
    def __init__(self):
        self.states = {'start', 'day', 'separator1', 'month', 'separator2', 'year', 'accept'}
        self.transitions = {
            'start': {'0': 'day', '1-3': 'day'},
            'day': {'0-9': 'day', '/': 'separator1'},
            'separator1': {'/': 'month'},
            'month': {'0': 'month', '1': 'month', '2': 'month', '/': 'separator2'},
            'separator2': {'/': 'year'},
            'year': {'0-9': 'year', 'accept': 'accept'},
        }

    def recognize_date(self, date_str):
        current_state = 'start'
        for char in date_str:
            if char.isdigit():
                char_type = '0-9'
            else:
                char_type = char

            if char_type in self.transitions[current_state]:
                current_state = self.transitions[current_state][char_type]
            else:
                return False

        return current_state == 'accept'


# Example usage
date_fsm = DateFSM()
date1 = "31/12/2022"
date2 = "15/05/1985"
date3 = "02/29/2021"  # Invalid leap year date

print(f"{date1} is valid: {date_fsm.recognize_date(date1)}")
print(f"{date2} is valid: {date_fsm.recognize_date(date2)}")
print(f"{date3} is valid: {date_fsm.recognize_date(date3)}")