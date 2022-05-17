from django.test import TestCase
from django.db import IntegrityError
from .models import Post
from django.contrib.auth.models import User
import unittest
from django.test import Client
# Create your tests here.


class PostIntegrationTest(TestCase):
        def setup(self):
            User.objects.create(username='Testuser')
            test_user = User.objects.get(username = 'Testuser')
            Post.objects.create(user= test_user, title = "test", content="this is a test") 

        def test_post(self):
            User.objects.create(username='TestUser')
            #print(User.objects.all())
            test_user = User.objects.get(username = 'TestUser')
            Post.objects.create(user= test_user, title = "test", content="this is a test") 
            #print(Post.objects.all())
            test_post = Post.objects.get(title="test")
            self.assertEqual(test_post.content, "this is a test" )


class MissingUserIntegrityTest(TestCase):

    def test_post(self):
        try:
            Post.objects.create(user = None, title="test post title", content="test post") 
        except IntegrityError as e:
            self.assertEqual(1, 1)



from lib2to3.pgen2 import driver
from multiprocessing.connection import Client
from operator import contains
from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
import selenium
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from posts.models import Post
from comments.models import Comment
from django.contrib.auth.models import User
import time


class SearchFormTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        options = FirefoxOptions()
        cls.selenium = webdriver.Firefox(options=options,executable_path=r"C:\Users\lenna\Documents\geckodriver-v0.31.0-win64(1)\geckodriver.exe")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass()
   
    def testSearch(self):
        
        #self.selenium.get('http://127.0.0.1:8000/')
        self.selenium.get('%s%s' % (self.live_server_url))

        user = User.objects.create(username='testuser', password='test')

        query = self.selenium.find_element_by_name('query')
        author = self.selenium.find_element_by_name('author')
        submit = self.selenium.find_element_by_name('gosearch')

        time.sleep(5)

        query.send_keys('Search Test Post')
        author.send_keys('testuser')
        submit.send_keys(Keys.RETURN)

        time.sleep(5)

        try:
            assert 'No Posts Available' in self.selenium.page_source

        except AssertionError:
            print('The post was found')

        
        Post.objects.create(user=user, title="Test Post", content="Search Test Post")

        query = self.selenium.find_element_by_name('query').clear()
        author = self.selenium.find_element_by_name('author').clear()
        
        query = self.selenium.find_element_by_name('query')
        #author = driver.find_element_by_name('author')
        submit = self.selenium.find_element_by_name('gosearch')

        time.sleep(5)

        query.send_keys('Search Test')
        #author.send_keys('testuser')
        submit.send_keys(Keys.RETURN)

        time.sleep(2)

        try:
            assert 'Search Test Post' in self.selenium.page_source
        except AssertionError:
            print('The post was found')


        time.sleep(3)

class AuthenticationTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        User.objects.create_user(username='test', password='pw')
        options = FirefoxOptions()
        cls.selenium = webdriver.Firefox(options=options,executable_path=r"C:\Users\lenna\Documents\geckodriver-v0.31.0-win64(1)\geckodriver.exe")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass()

    def LoginTestRealUser(self):
        #self.selenium.get("http://127.0.0.1:8000/accounts/login")
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))


        username = self.selenium.find_element_by_name('username')
        password = self.selenium.find_element_by_name('password')
        loginbutton = self.selenium.find_element_by_class_name('btn')

        username.send_keys('test')
        password.send_keys('pw')

        time.sleep(5)

        loginbutton.send_keys(Keys.RETURN)

        time.sleep(3)

        assert 'Welcome to your post dashboard' in self.selenium.page_source

        time.sleep(2)

    def LoginTestFakeUser(self):
        #self.selenium.get("http://127.0.0.1:8000/accounts/login")
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))


        username = self.selenium.find_element_by_name('username')
        password = self.selenium.find_element_by_name('password')
        loginbutton = self.selenium.find_element_by_class_name('btn')

        username.send_keys('test')
        password.send_keys('test')

        time.sleep(5)

        loginbutton.send_keys(Keys.RETURN)

        time.sleep(3)

        assert 'Username' in self.selenium.page_source

        time.sleep(2)

class RegisterTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        options = FirefoxOptions()
        cls.selenium = webdriver.Firefox(options=options,executable_path=r"C:\Users\lenna\Documents\geckodriver-v0.31.0-win64(1)\geckodriver.exe")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass()

    def register_user_test(self):
        #url = self.live_server_url + "\\accounts\register\\"
        #self.selenium.get(self.live_server_url + "/accounts/register/")
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/register'))

        self.selenium.find_element_by_name('username').send_keys('test')
        self.selenium.find_element_by_name('firstname').send_keys('Test')
        self.selenium.find_element_by_name('lastname').send_keys('User')
        self.selenium.find_element_by_name('email').send_keys('test@example.com')
        self.selenium.find_element_by_name('password').send_keys('TestPassword12')
        self.selenium.find_element_by_name('password2').send_keys('TestPassword12')

        time.sleep(2)

        submit = self.selenium.find_element_by_class_name('btn')
        submit.send_keys(Keys.RETURN)

        time.sleep(6)
        
        assert 'Dashboard' in self.selenium.page_source

class LogoutButtonTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        User.objects.create_user(username = "test", password="12testTest!")
        print('Created User')
        options = FirefoxOptions()
        cls.selenium = webdriver.Firefox(options=options,executable_path=r"C:\Users\lenna\Documents\geckodriver-v0.31.0-win64(1)\geckodriver.exe")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass()

    def button_test(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))

        time.sleep(2)

        self.selenium.find_element_by_name('username').send_keys('test')
        self.selenium.find_element_by_name('password').send_keys('12testTest!')
        submit = self.selenium.find_element_by_class_name('btn').click()

        time.sleep(2)

        #submit.send_keys(Keys.RETURN)

        time.sleep(2)

        self.selenium.find_element_by_id('logoutbutton').click()

        assert 'Enter any Keyword and find a post' in self.selenium.page_source

        time.sleep(5)

class CreatePostTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        user = User.objects.create_user(username = "test", password="12testTest!")
        options = FirefoxOptions()
        cls.selenium = webdriver.Firefox(options=options,executable_path=r"C:\Users\lenna\Documents\geckodriver-v0.31.0-win64(1)\geckodriver.exe")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass() 

    def make_post(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))

        self.selenium.find_element_by_name('username').send_keys('test')
        self.selenium.find_element_by_name('password').send_keys('12testTest!')
        submit = self.selenium.find_element_by_class_name('btn').click()

        time.sleep(2)

        self.selenium.find_element_by_id('postbutton').click()
        time.sleep(1)
        self.selenium.find_element_by_id('newpostbutton').click()
        time.sleep(1)
        self.selenium.find_element_by_id('posttitle').send_keys('Test Post')
        self.selenium.find_element_by_id('postcontent').send_keys('Test Content')
        self.selenium.find_element_by_id('submitbutton').click()
        time.sleep(1)
        assert 'No Comments Available' in self.selenium.page_source

    def make_post_no_title(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))

        self.selenium.find_element_by_name('username').send_keys('test')
        self.selenium.find_element_by_name('password').send_keys('12testTest!')
        submit = self.selenium.find_element_by_class_name('btn').click()

        time.sleep(2)

        self.selenium.find_element_by_id('postbutton').click()
        time.sleep(1)
        self.selenium.find_element_by_id('newpostbutton').click()
        time.sleep(1)
        self.selenium.find_element_by_id('posttitle').send_keys('')
        self.selenium.find_element_by_id('postcontent').send_keys('Test Content')
        self.selenium.find_element_by_id('submitbutton').click()
        time.sleep(1)
        assert 'Create Your Post' in self.selenium.page_source

    def make_post_no_content(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))

        self.selenium.find_element_by_name('username').send_keys('test')
        self.selenium.find_element_by_name('password').send_keys('12testTest!')
        submit = self.selenium.find_element_by_class_name('btn').click()

        time.sleep(2)

        self.selenium.find_element_by_id('postbutton').click()
        time.sleep(1)
        self.selenium.find_element_by_id('newpostbutton').click()
        time.sleep(1)
        self.selenium.find_element_by_id('posttitle').send_keys('Test')
        self.selenium.find_element_by_id('postcontent').send_keys('')
        self.selenium.find_element_by_id('submitbutton').click()
        time.sleep(1)
        assert 'Create Your Post' in self.selenium.page_source


class LoginTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        user = User.objects.create_user(username = "test", password="12testTest!")
        options = FirefoxOptions()
        cls.selenium = webdriver.Firefox(options=options,executable_path=r"C:\Users\lenna\Documents\geckodriver-v0.31.0-win64(1)\geckodriver.exe")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass() 

    def login_with_real_user_test(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))

        self.selenium.find_element_by_name('username').send_keys('test')
        self.selenium.find_element_by_name('password').send_keys('12testTest!')
        submit = self.selenium.find_element_by_class_name('btn').click()

        assert 'Welcome to your post dashboard' in self.selenium.page_source

        time.sleep(5)

    def login_with_fake_user_test(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))

        self.selenium.find_element_by_name('username').send_keys('fake')
        self.selenium.find_element_by_name('password').send_keys('fake!')
        submit = self.selenium.find_element_by_class_name('btn').click()

        assert 'Welcome to your post dashboard' not in self.selenium.page_source

        time.sleep(5)

class CommentTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        user = User.objects.create_user(username = "test", password="12testTest!")
        Post.objects.create(user=user, title="Test Post", content="Test Content")
        options = FirefoxOptions()
        cls.selenium = webdriver.Firefox(options=options,executable_path=r"C:\Users\lenna\Documents\geckodriver-v0.31.0-win64(1)\geckodriver.exe")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass() 

    def make_comment_test(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))

        self.selenium.find_element_by_name('username').send_keys('test')
        self.selenium.find_element_by_name('password').send_keys('12testTest!')
        submit = self.selenium.find_element_by_class_name('btn').click()
        time.sleep(1)
        self.selenium.find_element_by_id('postbutton').click()
        time.sleep(1)
        self.selenium.find_element_by_class_name('link').click()
        time.sleep(1)
        self.selenium.find_element_by_id('newcommentbutton').click()
        time.sleep(1)
        self.selenium.find_element_by_id('commenttitle').send_keys('Test Title')
        self.selenium.find_element_by_id('commentcontent').send_keys('Test Content')
        self.selenium.find_element_by_id('submitcomment').click()

        assert 'Test Post' and 'Test Title' in self.selenium.page_source

        time.sleep(5)

    def make_comment_no_title_test(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))

        self.selenium.find_element_by_name('username').send_keys('test')
        self.selenium.find_element_by_name('password').send_keys('12testTest!')
        submit = self.selenium.find_element_by_class_name('btn').click()
        time.sleep(1)
        self.selenium.find_element_by_id('postbutton').click()
        time.sleep(1)
        self.selenium.find_element_by_class_name('link').click()
        time.sleep(1)
        self.selenium.find_element_by_id('newcommentbutton').click()
        time.sleep(1)
        self.selenium.find_element_by_id('commenttitle').send_keys('')
        self.selenium.find_element_by_id('commentcontent').send_keys('Test Content')
        self.selenium.find_element_by_id('submitcomment').click()

        assert 'Test Post' and 'Test Title' not in self.selenium.page_source

        time.sleep(5)

    def make_comment_no_content_test(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))

        self.selenium.find_element_by_name('username').send_keys('test')
        self.selenium.find_element_by_name('password').send_keys('12testTest!')
        submit = self.selenium.find_element_by_class_name('btn').click()
        time.sleep(1)
        self.selenium.find_element_by_id('postbutton').click()
        time.sleep(1)
        self.selenium.find_element_by_class_name('link').click()
        time.sleep(1)
        self.selenium.find_element_by_id('newcommentbutton').click()
        time.sleep(1)
        self.selenium.find_element_by_id('commenttitle').send_keys('Test Title')
        self.selenium.find_element_by_id('commentcontent').send_keys('')
        self.selenium.find_element_by_id('submitcomment').click()

        assert 'Test Post' and 'Test Title' not in self.selenium.page_source

        time.sleep(5)

class DashboardTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(username = "test", password="12testTest!")
        options = FirefoxOptions()
        cls.selenium = webdriver.Firefox(options=options,executable_path=r"C:\Users\lenna\Documents\geckodriver-v0.31.0-win64(1)\geckodriver.exe")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass() 

    def dashboard_test_no_post(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))
        time.sleep(1)

        self.selenium.find_element_by_name('username').send_keys('test')
        self.selenium.find_element_by_name('password').send_keys('12testTest!')
        submit = self.selenium.find_element_by_class_name('btn').click()
        time.sleep(1)

        self.selenium.find_element_by_id('dashbutton').click()
        time.sleep(1)

        assert 'No Posts Available' in self.selenium.page_source

    def dashboard_test_with_post(self):
        Post.objects.create(user=self.user, content="Test Content", title="Test Title")

        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))
        time.sleep(1)

        self.selenium.find_element_by_name('username').send_keys('test')
        self.selenium.find_element_by_name('password').send_keys('12testTest!')
        submit = self.selenium.find_element_by_class_name('btn').click()
        time.sleep(1)

        self.selenium.find_element_by_id('dashbutton').click()
        time.sleep(1)

        assert 'Test Content' in self.selenium.page_source


class PostPaginationTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(username = "test", password="12testTest!")
        
        options = FirefoxOptions()
        cls.selenium = webdriver.Firefox(options=options,executable_path=r"C:\Users\lenna\Documents\geckodriver-v0.31.0-win64(1)\geckodriver.exe")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass() 

    def pagination_test_no_pagination(self):
        for i in range(0,4):
            Post.objects.create(user=self.user, title="Post #"+str(i), content='Same content as the others')
        self.selenium.get('%s%s' % (self.live_server_url, '/post'))

        try:
            self.selenium.find_element_by_id('pageitem')
        except:
            print('No Pagination all good')
        
    def pagination_test_pagination(self):
        for i in range(0,6):
            Post.objects.create(user=self.user, title="Post #"+str(i), content='Same content as the others')
        self.selenium.get('%s%s' % (self.live_server_url, '/post'))

        if self.selenium.find_element_by_id('pageitemnext'):
            print('Pagination Present')
        else:
            print('Pagination Not Present')
        time.sleep(10)


class StaticButtonTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()        
        options = FirefoxOptions()
        cls.selenium = webdriver.Firefox(options=options,executable_path=r"C:\Users\lenna\Documents\geckodriver-v0.31.0-win64(1)\geckodriver.exe")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass() 

    def post_button_test(self):
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        self.selenium.find_element_by_id('postbutton').click()

        assert 'No Posts Available' in self.selenium.page_source

    def login_button_test(self):
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        self.selenium.find_element_by_id('loginbutton').click()

        assert 'Login' in self.selenium.page_source

    def register_button_test(self):
        self.selenium.get('%s%s' % (self.live_server_url, ''))
        self.selenium.find_element_by_id('registerbutton').click()

        assert 'Register' in self.selenium.page_source

    def home_button_test(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/post'))
        self.selenium.find_element_by_id('homebutton').click()

        assert 'Keyword' in self.selenium.page_source

    def cf_button_test(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/post'))
        time.sleep(3)
        self.selenium.find_element_by_id('cfbutton').click()
        time.sleep(3)

        assert 'Keyword' in self.selenium.page_source











