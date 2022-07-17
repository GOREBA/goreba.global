from ckeditor.fields import RichTextField
from django.db import models


class Setting(models.Model):
    # Choices
    STORE_STATUS = (
        ('OPEN', 'OPEN'),
        ('CLOSE', 'CLOSE'),
        ('MAINTENANCE', 'MAINTENANCE'),
    )

    # Store metadata
    store_title = models.CharField(
        max_length=100,
        default='Beautifully Crafted Gifts for loved ones or yourself'
    )
    store_name = models.CharField(max_length=20, default='Goreba')
    company = models.CharField(max_length=20, default='Goreba')
    keywords = models.CharField(
        blank=True,
        max_length=500,
        default=''
    )
    short_description = models.CharField(
        blank=True,
        max_length=50,
        default=''
    )
    story_headline = models.CharField(
        blank=True, max_length=20, default='Goreba ~ Prologue')
    story = RichTextField(blank=True)
    store_phone = models.CharField(
        blank=True, max_length=20, default='+1 (514) 258 7260')
    store_address = models.CharField(
        blank=True, max_length=50, default='153 Cresthaven Dr. Nepean, ON, K2G 6T2 Canada')
    store_email = models.CharField(
        blank=True, max_length=20, default='goreba99@gmail.com')
    store_status = models.CharField(max_length=15, choices=STORE_STATUS)

    # Logo and images
    store_icon = models.ImageField(blank=True, upload_to='images/goreba/')
    store_photo = models.ImageField(blank=True, upload_to='images/goreba/')
    order_receipt_banner = models.ImageField(blank=True, upload_to='images/goreba')

    # Socials
    store_link_facebook = models.CharField(
        max_length=50, default='https://www.facebook.com/goreba.canada/')
    store_link_instagram = models.CharField(
        max_length=50, default='https://www.instagram.com/goreba.canada/')
    store_link_twitter = models.CharField(
        max_length=50, default='https://twitter.com/goreba_canada/')
    store_link_youtube = models.CharField(
        max_length=75, default='https://www.youtube.com/channel/UCJQTNsK5_sPUic7gO0tGovw')
    store_link_pinterest = models.CharField(
        max_length=50, default='https://www.pinterest.ca/goreba_canada/')
    store_link_linkedin = models.CharField(
        max_length=50, default='https://www.linkedin.com/company/goreba/')

    # Email servers
    smtp_server = models.CharField(blank=True, max_length=50)
    smtp_email = models.CharField(blank=True, max_length=50)
    smtp_password = models.CharField(blank=True, max_length=10)
    smtp_port = models.CharField(blank=True, max_length=5)

    # Store policies
    return_policy = RichTextField(blank=True)
    privacy_policy = RichTextField(blank=True)
    cookie_policy = RichTextField(blank=True)

    # Announcements
    store_announcements = RichTextField(blank=True)
    message_to_buyers = RichTextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name
