import imaplib
import email

# Đăng nhập vào tài khoản Gmail của bạn
imap_server = imaplib.IMAP4_SSL('imap.gmail.com')
imap_server.login('tanthuyhoang0220@gmail.com', 'wifgthdllmhwggas')

# Chọn hộp thư đến
imap_server.select('inbox')

# Lấy danh sách các email trong hộp thư đến
status, messages = imap_server.search(None, 'ALL')
messages = messages[0].split()[::-1]

# Đọc các email
for message in messages:
    status, data = imap_server.fetch(message, "(RFC822)")
    msg = email.message_from_bytes(data[0][1])

    # In ra tiêu đề và người gửi của email
    # print(f'Tiêu đề: {msg["Subject"]}')
    # print(str(msg.get_payload(1)).split('Content-Transfer-Encoding'))
    # print(msg['From'])
    for ele in msg.walk():
        if ele.get_content_type() == 'text/html':
            print(ele.get_payload())


# Đóng kết nối với máy chủ IMAP
imap_server.close()
imap_server.logout()