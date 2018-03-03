import re
import utils


print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))


@utils.timer
def is_valid_email(addr):
    re_email = re.compile(r'^([\w\.]+)@(\w+)\.(\w{3})$')
    if re_email.match(addr):
        return True
    else:
        return False


# test:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('pass')


@utils.timer
def name_of_email(addr):
    re_email = re.compile(r'<?([\w\s]*)>?\s*\w*@\w+\.\w{3}$')
    return re_email.match(addr).group(1)


# test:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('pass')
