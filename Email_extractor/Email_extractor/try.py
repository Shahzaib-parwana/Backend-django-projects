djtext = '''n today's digital age, communication via 
email has become an integral part of our lives. Whether it's for 
work-related correspondence, staying in touch with friends and family, or receiving updates 
from your favorite online stores, email is ubiquitous. For example, john.doe@example.com 
recently received an exciting offer from a renowned e-commerce website, while
emily.smith@example.net is eagerly awaiting a response to her job application sent to a
potential employer. Meanwhile, sarah.jones@example.org is organizing a charity event and
has been reaching out to volunteers via email. Additionally, businesses rely heavily on email 
marketing to promote their products and services. For instance, marketing@example.com has been
sending out newsletters to subscribers, offering exclusive discounts and promotions. With the 
sheer volume of emails being sent and received daily, it's essential to have efficient tools to
manage and organize our inbox. That's where email finding projects come into play, helping to sift
through text and extract 
all valid email addresses for various purposes.'''
words = djtext.split()
emails = ''
i = 0  

      
for word in words:
        if '@' in word and '.' in word:
            if word.count('@') ==1 and word.count('.') >=1:
                i+=1
                email = word.strip('.,?!:;"\'()[]{}')
                # emails.append(email
                    
                emails +=(f'{i}:{email} \n') 
print(emails)