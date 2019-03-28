class PasswordValidator():
    '''
    Write a password validator, which checks whether proposed passwords pass certain rules:
    - The password contains at least one capital letter.
    - The password contains at least one number.
    - The password contains at least one of a provided list of symbols.
    '''

    def __init__(self,contains_capital,contains_number,symbol_list):
        self.mysymblst = symbol_list
        self.mycaps = contains_capital
        self.mynums = contains_number

    def validate(self,password_to_validate):
        bsym = not len(self.mysymblst)>0
        bcap = self.mycaps
        bnum = self.mynums
        for char in password_to_validate:
            if char in ''.join(self.mysymblst):
                bsym = True
        for char in password_to_validate:
            if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                bcap = True
        for char in password_to_validate:
            if char in '0123456789':
                bnum = True
        return bsym and bcap and bnum
