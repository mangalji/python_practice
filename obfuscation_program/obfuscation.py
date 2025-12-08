import secrets
import string

trans = "file_a.txt"
emails_ = "file_b.txt"
final_file = "file_c.txt"


with open(trans, 'r') as file:
    lines = file.readlines()

with open(emails_, 'r') as file:
    emails =[]
    for email in file.readlines():
        emails.append(email.strip())
    
def generate_random_hex_hash(length=10):
    hex_chars = string.hexdigits.lower()
    return ''.join(secrets.choice(hex_chars) for _ in range(length))

def obfuscation_of_emails():
    with open(final_file, 'w') as file:  # open in write mode to overwrite

        for line in lines:
            original_line = line  

            
            start_sender_email = line.find(' at ') + len(' at ')
            end_sender_email = line.find(' ', start_sender_email)
            sender_email = line[start_sender_email:end_sender_email]

            
            start_auditor_email = line.rfind(' at ') + len(' at ')
            end_auditor_email = line.find(' ', start_auditor_email)
            auditor_mail = line[start_auditor_email:end_auditor_email]

            if sender_email in emails:
                secret_code = generate_random_hex_hash()
                line = line.replace(sender_email, secret_code)

            if auditor_mail in emails:
                secret_code = generate_random_hex_hash()
                line = line.replace(auditor_mail, secret_code)

            if line != original_line:
                file.write(line)

obfuscation_of_emails()

def deobfuscation_of_emails():
    pass
   